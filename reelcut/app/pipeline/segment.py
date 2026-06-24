#!/usr/bin/env python3
"""segment.py — split a clip into tagged SEGMENTS and SUB-SECTIONS.

Two engines, chosen automatically:

  • Whisper (if installed): real transcript → topic tags via keyword cohesion.
    Best quality; produces meaningful titles like "mahendra · villages · roads".
  • Silence fallback (always available): ffmpeg `silencedetect` carves speech
    into chunks at pauses, so ReelCut is usable even with no Whisper install.
    Sub-sections are time-labelled ("part 3 · 02:14"); group by larger gaps.

Both paths emit the same structure that render.py / the UI consume.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

GAP_SUB, MAX_SUB, MIN_SUB = 0.55, 45.0, 6.0
GAP_SEG, MIN_SEG, MAX_SEG, COHESION_MIN = 1.4, 50.0, 300.0, 0.07

STOP = set("a an the and or but if then so as of to in on at for with from by about into over "
           "is are was were be been being i you he she it we they me him her us them my your this "
           "that these those there what which who when where why how not no do does did have has "
           "had will can just like really actually um uh yeah okay ok you know".split())


def _kw(text: str, k: int = 6) -> List[str]:
    counts: Dict[str, int] = {}
    for w in re.findall(r"[A-Za-z']+", text.lower()):
        if len(w) >= 3 and w not in STOP:
            counts[w] = counts.get(w, 0) + 1
    return sorted(counts, key=lambda w: (-counts[w], w))[:k]


def _jac(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a and b else 0.0


def _title(text: str) -> str:
    kw = _kw(text, 3)
    return " · ".join(kw) if kw else (text.strip()[:36] or "section")


def _mmss(t: float) -> str:
    t = int(max(0, t))
    return f"{t//60:02d}:{t%60:02d}"


# ---- engine 1: Whisper -------------------------------------------------------
def _whisper_lines(src: Path, model: str, language: Optional[str], cache: Path) -> Optional[List[dict]]:
    if cache.exists():
        res = json.loads(cache.read_text(encoding="utf-8"))
    else:
        try:
            import whisper  # type: ignore
        except ImportError:
            return None
        m = whisper.load_model(model)
        res = m.transcribe(str(src), language=language, verbose=False)
        cache.write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
    return [{"start": float(s["start"]), "end": float(s["end"]), "text": s["text"]}
            for s in res.get("segments", []) if s.get("text", "").strip()]


# ---- engine 2: silence ------------------------------------------------------
def _silence_lines(src: Path, duration: float) -> List[dict]:
    """Carve speech into chunks using ffmpeg silencedetect (no transcript)."""
    out = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(src),
         "-af", "silencedetect=noise=-30dB:d=0.4", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    # Speech = complement of the detected silences (shared robust parser).
    from .silences import speech_ranges   # sibling import works in both contexts (CR-L9)
    speech = speech_ranges(out, duration, min_gap=0.4)
    if not speech:
        speech = [[0.0, duration]]
    lines = []
    for i, (s, e) in enumerate(speech, 1):
        lines.append({"start": round(s, 2), "end": round(e, 2),
                      "text": f"part {i} · {_mmss(s)}"})
    return lines


# ---- grouping (shared) ------------------------------------------------------
def _group_subs(lines: List[dict]) -> List[dict]:
    subs, cur = [], []

    def flush():
        if not cur:
            return
        text = " ".join(l["text"].strip() for l in cur).strip()
        subs.append({"start": round(cur[0]["start"], 2), "end": round(cur[-1]["end"], 2),
                     "text": text, "tag": _title(text), "keep": True})
    for i, line in enumerate(lines):
        cur.append(line)
        dur = cur[-1]["end"] - cur[0]["start"]
        nxt = (lines[i + 1]["start"] - line["end"]) if i + 1 < len(lines) else 99.0
        ends = line["text"].strip().endswith((".", "?", "!", "।"))
        if dur >= MAX_SUB or (dur >= MIN_SUB and (nxt >= GAP_SUB or ends)):
            flush(); cur = []
    flush()
    return subs


def _group_segs(subs: List[dict]) -> List[dict]:
    segs, cur, ckw = [], [], set()

    def flush():
        if not cur:
            return
        text = " ".join(s["text"] for s in cur)
        n = len(segs) + 1
        segs.append({"id": f"seg-{n}", "title": _title(text),
                     "tag": (_kw(text, 1) or ["topic"])[0],
                     "start": cur[0]["start"], "end": cur[-1]["end"], "keep": True,
                     "subsections": [{**s, "id": f"seg-{n}-{j+1}", "order": 0}
                                     for j, s in enumerate(cur)]})
    for sub in subs:
        skw = set(_kw(sub["text"], 8))
        if cur:
            dur = sub["end"] - cur[0]["start"]
            gap = sub["start"] - cur[-1]["end"]
            if dur >= MAX_SEG or (dur >= MIN_SEG and (gap >= GAP_SEG or _jac(ckw, skw) < COHESION_MIN)):
                flush(); cur, ckw = [], set()
        cur.append(sub); ckw |= skw
    flush()
    return segs


def segment(src: str, duration: float, model: str = "base",
            language: Optional[str] = None, cache: Optional[str] = None) -> dict:
    """Return a project-shaped dict: {engine, segments:[...]} with global order set."""
    srcp = Path(src)
    cachep = Path(cache) if cache else srcp.with_suffix(".whisper.json")
    lines = _whisper_lines(srcp, model, language, cachep)
    engine = "whisper"
    if lines is None:
        engine = "silence"
        lines = _silence_lines(srcp, duration)
    segs = _group_segs(_group_subs(lines))
    # assign a global default output order (chronological) across all sub-sections
    order = 1
    for seg in segs:
        for sub in seg["subsections"]:
            sub["order"] = order
            order += 1
    return {"engine": engine, "segments": segs}
