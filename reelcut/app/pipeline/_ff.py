#!/usr/bin/env python3
"""_ff.py — one consistent way to invoke FFmpeg/ffprobe (CR-L4 / TD reduction).

Every pipeline pass previously called ``subprocess.run(..., check=True)``, which
raises a bare ``CalledProcessError`` whose message hides ffmpeg's own stderr — the
one thing you need to debug a failed encode. ``run`` here always captures output
and, on a non-zero exit, raises :class:`FFmpegError` carrying the tail of stderr.
"""
from __future__ import annotations

import subprocess


class FFmpegError(RuntimeError):
    """An ffmpeg/ffprobe invocation exited non-zero; message includes stderr tail."""


def run(cmd, tail: int = 800) -> subprocess.CompletedProcess:
    """Run ``cmd`` capturing output; raise :class:`FFmpegError` with the stderr tail
    on failure. Returns the CompletedProcess on success."""
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise FFmpegError(f"{cmd[0]} failed (exit {p.returncode}):\n{(p.stderr or '')[-tail:]}")
    return p
