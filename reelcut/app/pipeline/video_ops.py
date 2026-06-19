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
