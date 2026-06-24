#!/usr/bin/env python3
"""video_ops.py — reframe to a platform aspect (SR-4.2) and burn-in open
captions (SR-4.9). Both are single FFmpeg passes.
"""
from __future__ import annotations

import subprocess

# aspect -> (w, h) ratio
ASPECTS = {"16:9": (16, 9), "9:16": (9, 16), "1:1": (1, 1)}


def target_size(aspect: str, height: int) -> tuple[int, int]:
    rw, rh = ASPECTS[aspect]
    w = int(round(height * rw / rh))
    w -= w % 2  # keep even dimensions for yuv420p
    h = height - (height % 2)
    return w, h


def reframe(src: str, out_path: str, aspect: str = "9:16", height: int = 1280) -> str:
    """Letterbox/pad ``src`` into the target aspect+resolution without cropping (SR-4.2)."""
    w, h = target_size(aspect, height)
    vf = (f"scale={w}:{h}:force_original_aspect_ratio=decrease,"
          f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,setsar=1")
    subprocess.run(["ffmpeg", "-y", "-i", src, "-vf", vf, "-pix_fmt", "yuv420p",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                    "-c:a", "aac", "-b:a", "192k", out_path],
                   capture_output=True, check=True)
    return out_path


def burn_captions(video: str, srt: str, out_path: str) -> str:
    """Burn an .srt into the video as open captions for sound-off playback (SR-4.9)."""
    safe = srt.replace("\\", "/").replace(":", "\\:").replace("'", "\\'")
    subprocess.run(["ffmpeg", "-y", "-i", video, "-vf", f"subtitles='{safe}'",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                    "-c:a", "copy", out_path],
                   capture_output=True, check=True)
    return out_path


def highlight_clip(src: str, start: float, end: float, out_path: str) -> str:
    """Export a sub-range as a standalone highlight clip (SR-4.6).

    Uses input ``-ss`` for a fast seek plus output ``-t`` for an accurate duration
    (``end-start``); ``-to`` before ``-i`` would be measured from the post-seek
    origin and could yield the wrong length (CR-M1)."""
    dur = max(0.0, end - start)
    subprocess.run(["ffmpeg", "-y", "-ss", f"{start}", "-i", src, "-t", f"{dur}",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                    "-c:a", "aac", "-b:a", "192k", out_path],
                   capture_output=True, check=True)
    return out_path


def cover_frame(src: str, t: float, out_png: str) -> str:
    """Grab a single frame at time ``t`` as the cover image (SR-4.6)."""
    subprocess.run(["ffmpeg", "-y", "-ss", f"{t}", "-i", src, "-frames:v", "1", out_png],
                   capture_output=True, check=True)
    return out_png
