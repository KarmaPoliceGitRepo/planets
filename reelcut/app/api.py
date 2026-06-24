#!/usr/bin/env python3
"""api.py — endpoint logic for replace/add audio and add image (SR-2.7).

Kept as plain functions (separate from the HTTP layer) so they are unit-testable
without a running server. The server delegates its routes here. Every entry
validates the incoming artifact's format and rejects with a reason (SR-3.1).
"""
from __future__ import annotations

import os

if __package__:  # 'app' in package context (tests); '' when server runs it flat
    from app import validate
    from app.pipeline import audio_mix
else:  # server context (APP dir on sys.path) — detect explicitly, never swallow a real ImportError (CR-L9/TD-1)
    import validate
    from pipeline import audio_mix


def check_upload(filename: str) -> tuple[bool, str]:
    return validate.validate_import(filename)


def replace_audio(workdir: str, video: str, new_audio: str) -> str:
    ok, reason = validate.validate_path(new_audio)
    if not ok:
        raise ValueError(reason)
    return audio_mix.replace_audio(video, new_audio, os.path.join(workdir, "replaced.mp4"))


def add_audio(workdir: str, video: str, extra: str,
              level_db: float = 0.0, duck: bool = False) -> str:
    ok, reason = validate.validate_path(extra)
    if not ok:
        raise ValueError(reason)
    return audio_mix.add_audio(video, extra, os.path.join(workdir, "mixed.mp4"),
                               level_db=level_db, duck=duck)


def add_image(workdir: str, image: str, duration: float = 4.0) -> str:
    ok, reason = validate.validate_path(image)
    if not ok:
        raise ValueError(reason)
    return audio_mix.image_clip(image, os.path.join(workdir, "image_clip.mp4"),
                                duration=duration)
