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


def chapters_ffmetadata(project: dict) -> str:
    """FFMETADATA chapter list derived from the kept segments (SR-4.7).

    Output is feedable to ``ffmpeg -i in -i chapters.txt -map_metadata 1``.
    Chapter times are the cumulative output timeline of the kept sub-sections.
    """
    lines = [";FFMETADATA1"]
    t = 0.0
    for seg in project.get("segments", []):
        if seg.get("keep", True) is False:
            continue
        subs = [s for s in seg.get("subsections", []) if s.get("keep", True)]
        if not subs:
            continue
        seg_dur = sum(max(0.0, s.get("end", 0) - s.get("start", 0)) for s in subs)
        start_ms = int(round(t * 1000))
        end_ms = int(round((t + seg_dur) * 1000))
        title = seg.get("title", "Chapter").replace("\n", " ")
        lines += ["[CHAPTER]", "TIMEBASE=1/1000",
                  f"START={start_ms}", f"END={end_ms}", f"title={title}"]
        t += seg_dur
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
