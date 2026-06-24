#!/usr/bin/env python3
"""captions.py — re-time captions for the RE-SEQUENCED edit.

After reordering, the original timestamps are meaningless. Given the render
timing map (each kept clip's src_start/src_end → new_start), we shift every
caption line that falls inside a kept clip onto its new output time and emit a
correct .srt for the finished video.

If a Whisper transcript exists we re-time line-by-line; otherwise we fall back to
one caption per clip using the sub-section text.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional


def _ts(seconds: float) -> str:
    if seconds < 0:
        seconds = 0
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _write_srt(cues: List[dict], path: Path) -> None:
    lines = []
    for i, c in enumerate(sorted(cues, key=lambda x: (x["start"], x["end"])), 1):
        lines += [str(i), f"{_ts(c['start'])} --> {_ts(c['end'])}", c["text"].strip(), ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def remap(project: dict, timing_map: List[dict], out_srt: str,
          whisper_cache: Optional[str] = None) -> dict:
    """Write a re-timed .srt for the finished edit. Returns {ok, cues}."""
    sub_text = {}
    for seg in project.get("segments", []):
        for sub in seg.get("subsections", []):
            sub_text[sub["id"]] = sub.get("text", "")

    wlines: List[dict] = []
    if whisper_cache and Path(whisper_cache).exists():
        res = json.loads(Path(whisper_cache).read_text(encoding="utf-8"))
        wlines = [{"start": float(s["start"]), "end": float(s["end"]), "text": s["text"]}
                  for s in res.get("segments", []) if s.get("text", "").strip()]

    cues: List[dict] = []
    for clip in timing_map:
        s0, e0, ns = clip["src_start"], clip["src_end"], clip["new_start"]
        delta = ns - s0
        # Any cue that OVERLAPS the clip is kept and clamped to the clip window, so a
        # caption straddling a cut boundary is neither dropped nor allowed to spill into
        # the next clip's captions (CR-M5).
        overlap = [w for w in wlines if w["end"] > s0 and w["start"] < e0]
        if overlap:
            for w in overlap:
                cs = max(w["start"], s0)
                ce = min(w["end"], e0)
                cues.append({"start": cs + delta, "end": ce + delta, "text": w["text"]})
        else:
            cues.append({"start": ns, "end": ns + (e0 - s0),
                         "text": sub_text.get(clip["id"], "")})
    _write_srt(cues, Path(out_srt))
    return {"ok": True, "cues": len(cues)}


# ---- SR-4.3: caption translation (mechanism; ML backend is pluggable) -------
def translate_cues(cues: List[dict], translator) -> List[dict]:
    """Return cues with text passed through ``translator`` (str -> str), keeping
    timings. ``translator`` is any callable — a Whisper-translate task, an offline
    dictionary, or a stub. The pipeline is built here; the model is injected."""
    return [{**c, "text": translator(c.get("text", ""))} for c in cues]


def write_translated_srt(cues: List[dict], translator, out_srt: str) -> dict:
    """Translate cues and write the English (or target) .srt (SR-4.3)."""
    tcues = translate_cues(cues, translator)
    _write_srt(tcues, Path(out_srt))
    return {"ok": True, "cues": len(tcues)}
