#!/usr/bin/env python3
"""demux.py — split a media file into independent A/V track files (SR-2.1).

Stream-copy only (``-c copy``): lossless, fast, no re-encode. This is the
precondition for independent audio/video manipulation (SN-6 / SR-2.8).
"""
from __future__ import annotations

import os

from . import probe
from . import _ff


def demux(src: str, out_dir: str) -> dict:
    """Return {"video": <path|None>, "audio": <path|None>} of stream-copied tracks."""
    p = probe.probe(src)
    os.makedirs(out_dir, exist_ok=True)
    result = {"video": None, "audio": None}
    if p.get("has_video"):
        v = os.path.join(out_dir, "track_video.mp4")
        _ff.run(["ffmpeg", "-y", "-i", src, "-map", "0:v:0", "-c", "copy", "-an", v])
        result["video"] = v
    if p.get("has_audio"):
        a = os.path.join(out_dir, "track_audio.m4a")
        _ff.run(["ffmpeg", "-y", "-i", src, "-map", "0:a:0", "-c", "copy", "-vn", a])
        result["audio"] = a
    return result
