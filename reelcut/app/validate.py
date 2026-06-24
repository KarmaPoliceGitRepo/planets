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
    """Return (ok, reason) by EXTENSION only. ok=True with reason="" when accepted.

    Use this for a filename that does not exist on disk yet (e.g. an upload name).
    For an artifact that must already exist, use ``validate_path`` (CR-M10)."""
    ext = os.path.splitext(path)[1].lower()
    if not ext:
        return False, "file has no extension; cannot determine its type"
    if ext not in ACCEPTED:
        accepted = ", ".join(sorted(ACCEPTED))
        return False, f"unsupported format '{ext}'. Accepted: {accepted}"
    return True, ""


def validate_path(path: str) -> tuple[bool, str]:
    """Like ``validate_import`` but also require the path to be an existing file
    (CR-M10) — a renamed/missing file is rejected with a reason rather than
    surfacing as a confusing FFmpeg failure."""
    ok, reason = validate_import(path)
    if not ok:
        return ok, reason
    if not os.path.isfile(path):
        return False, f"file not found: {path}"
    return True, ""
