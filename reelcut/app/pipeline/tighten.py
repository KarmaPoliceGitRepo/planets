#!/usr/bin/env python3
"""tighten.py — detect silences and compute keep-ranges to auto-tighten an edit
(SR-4.5). Filler-word removal reuses the same keep-range machinery once word
timestamps are available from the transcript; silence removal is the
deterministic core implemented here.
"""
from __future__ import annotations

import subprocess
from typing import List, Tuple

from .silences import silent_spans   # sibling in the same package — works as app.pipeline or pipeline (CR-L9)


def detect_silences(src: str, noise: str = "-30dB", min_d: float = 0.3) -> List[Tuple[float, float]]:
    """Return [(start, end), …] of silent spans using FFmpeg silencedetect."""
    p = subprocess.run(
        ["ffmpeg", "-i", src, "-af", f"silencedetect=noise={noise}:d={min_d}", "-f", "null", "-"],
        capture_output=True, text=True)
    return silent_spans(p.stderr)


def keep_ranges(duration: float, silences: List[Tuple[float, float]],
                min_keep: float = 0.1) -> List[Tuple[float, float]]:
    """Invert silent spans into the speech ranges to keep (SR-4.5)."""
    ranges, t = [], 0.0
    for s, e in silences:
        if s - t > min_keep:
            ranges.append((t, s))
        t = max(t, e)
    if duration - t > min_keep:
        ranges.append((t, duration))
    return ranges
