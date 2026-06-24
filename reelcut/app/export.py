#!/usr/bin/env python3
"""export.py — derive text artefacts from the edit project.

Transcript export (SR-5.1) and chapter metadata (SR-4.7) are pure-Python
derivations of the segment model — no FFmpeg needed.
"""
from __future__ import annotations


def _kept_subs_in_order(project: dict) -> list:
    subs = []
    for seg in project.get("segments", []):
        if seg.get("keep", True) is False:
            continue
        for sub in seg.get("subsections", []):
            if sub.get("keep", True):
                subs.append(sub)
    subs.sort(key=lambda s: s.get("order", 0))
    return subs


def transcript_txt(project: dict) -> str:
    """Full plain-text transcript of the kept content, in output order (SR-5.1)."""
    return "\n".join(s.get("text", "").strip() for s in _kept_subs_in_order(project)).strip() + "\n"


def chapters_ffmetadata(project: dict, timing_map: list = None) -> str:
    """FFMETADATA chapter list derived from the kept segments (SR-4.7).

    Output is feedable to ``ffmpeg -i in -i chapters.txt -map_chapters 1``.

    When ``timing_map`` (from ``render.timing_map``) is provided, chapter times come
    from the actual rendered output positions, so they stay correct under reorder /
    transition overlap (CR-M6). Without it, they fall back to the cumulative sum of
    kept sub-section source durations (correct only when nothing is re-timed)."""
    pos = {c["id"]: c for c in (timing_map or [])}
    lines = [";FFMETADATA1"]
    t = 0.0
    for seg in project.get("segments", []):
        if seg.get("keep", True) is False:
            continue
        subs = [s for s in seg.get("subsections", []) if s.get("keep", True)]
        if not subs:
            continue
        if pos:  # use real rendered timeline
            kept = [pos[s["id"]] for s in subs if s["id"] in pos]
            if not kept:
                continue
            start_s = min(c["new_start"] for c in kept)
            end_s = max(c["new_start"] + (c["src_end"] - c["src_start"]) for c in kept)
        else:    # fall back to cumulative source durations
            seg_dur = sum(max(0.0, s.get("end", 0) - s.get("start", 0)) for s in subs)
            start_s, end_s = t, t + seg_dur
            t += seg_dur
        title = seg.get("title", "Chapter").replace("\n", " ")
        lines += ["[CHAPTER]", "TIMEBASE=1/1000",
                  f"START={int(round(start_s * 1000))}", f"END={int(round(end_s * 1000))}",
                  f"title={title}"]
    return "\n".join(lines) + "\n"


def batch_export(projects: list, preset: dict) -> list:
    """Apply one shared preset to many projects for batch export (SR-5.2).

    Returns the list of preset-applied project dicts (the render of each then
    follows the normal single-project path)."""
    from . import model  # local import avoids a cycle at module load
    out = []
    for p in projects:
        q = dict(p)
        model.apply_preset(q, preset)
        out.append(q)
    return out
