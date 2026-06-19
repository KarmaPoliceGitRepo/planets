#!/usr/bin/env python3
"""validate.py — accept/reject imported artifacts by format (SR-3.1).

Rejecting bad input early, with a human reason, prevents confusing downstream
FFmpeg failures for a non-expert user.
"""
from __future__ import annotations

import os

VIDEO = {".mp4", ".mov", ".mkv", ".webm", ".m4v"}
AUDIO = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"}
IMAGE = {".png", ".jpg", ".jpeg", ".webp"}
ACCEPTED = VIDEO | AUDIO | IMAGE


def kind(path: str) -> str | None:
    ext = os.path.splitext(path)[1].lower()
    if ext in VIDEO:
        return "video"
    if ext in AUDIO:
        return "audio"
    if ext in IMAGE:
        return "image"
    return None


def validate_import(path: str) -> tuple[bool, str]:
    """Return (ok, reason). ok=True with reason="" when accepted."""
    ext = os.path.splitext(path)[1].lower()
    if not ext:
        return False, "file has no extension; cannot determine its type"
    if ext not in ACCEPTED:
        accepted = ", ".join(sorted(ACCEPTED))
        return False, f"unsupported format '{ext}'. Accepted: {accepted}"
    return True, ""
