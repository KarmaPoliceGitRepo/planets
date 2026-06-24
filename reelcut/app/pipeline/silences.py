#!/usr/bin/env python3
"""silences.py — one robust parser for FFmpeg ``silencedetect`` output.

Both the silence-split segmenter (``segment.py``) and the auto-tighten path
(``tighten.py``) previously re-implemented this parsing with slightly different
logic (a ``zip`` vs a state machine). That duplication was the real defect behind
review items CR-L3 / CR-M12 / CR-H11: two parsers can disagree on edge cases
(audio ending in silence, duplicated ``silence_start``). This module is the single
source of truth, written as a strict state machine.
"""
from __future__ import annotations

import re
from typing import List, Optional, Tuple

_START = re.compile(r"silence_start: ([-\d.]+)")
_END = re.compile(r"silence_end: ([-\d.]+)")


def silent_spans(stderr: str) -> List[Tuple[float, float]]:
    """Closed silent spans ``[(start, end), …]`` parsed from silencedetect stderr.

    A ``silence_start`` with no matching ``silence_end`` (audio ends in silence) is
    NOT returned as a closed span — use :func:`speech_ranges` if you need to treat
    that trailing silence as running to EOF. A duplicated ``silence_start`` keeps
    the latest (the detector never nests silences)."""
    spans: List[Tuple[float, float]] = []
    start: Optional[float] = None
    for line in stderr.splitlines():
        m = _START.search(line)
        if m:
            start = float(m.group(1))
            continue
        m = _END.search(line)
        if m and start is not None:
            spans.append((start, float(m.group(1))))
            start = None
    return spans


def _trailing_open_silence(stderr: str) -> Optional[float]:
    """The time of a final ``silence_start`` that never closed (silence to EOF),
    or None if the audio does not end in silence."""
    start: Optional[float] = None
    for line in stderr.splitlines():
        m = _START.search(line)
        if m:
            start = float(m.group(1))
            continue
        if _END.search(line) and start is not None:
            start = None
    return start


def speech_ranges(stderr: str, duration: float, min_gap: float = 0.4) -> List[List[float]]:
    """Complement of the silences: the speech ranges ``[[start, end], …]``.

    Correct for every edge case the two old parsers split on:
    - audio ends in silence → the trailing open ``silence_start`` bounds speech (not ``duration``);
    - audio ends in speech → speech runs to ``duration``;
    - no silences at all → a single ``[0, duration]`` range;
    - gaps shorter than ``min_gap`` are not emitted as speech."""
    spans = silent_spans(stderr)
    end_of_speech = _trailing_open_silence(stderr)
    if end_of_speech is None:
        end_of_speech = duration
    speech: List[List[float]] = []
    cursor = 0.0
    for s, e in spans:
        if s - cursor > min_gap:
            speech.append([cursor, s])
        cursor = max(cursor, e)
    if end_of_speech - cursor > min_gap:
        speech.append([cursor, end_of_speech])
    return speech
