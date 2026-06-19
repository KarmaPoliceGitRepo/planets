#!/usr/bin/env python3
"""branding.py — optional branding overlays and intro/outro (SR-4.10).

Logo/watermark overlay and intro/outro concatenation are reliable, font-free
FFmpeg passes. Title cards / lower-thirds via drawtext are also provided but
depend on a system font being available.
"""
from __future__ import annotations

import os
import subprocess


def add_logo(video: str, logo: str, out_path: str, margin: int = 10) -> str:
    """Overlay a logo/watermark in the top-right corner (SR-4.10)."""
    subprocess.run(["ffmpeg", "-y", "-i", video, "-i", logo,
                    "-filter_complex", f"overlay=W-w-{margin}:{margin}",
                    "-c:a", "copy", out_path],
                   capture_output=True, check=True)
    return out_path


def concat_clips(clips: list, out_path: str, width: int = 1280, height: int = 720) -> str:
    """Concatenate intro + main + outro into one video (SR-4.10). Each clip is
    normalised to the same size/codec first so concatenation is safe."""
    work = os.path.dirname(out_path) or "."
    norm = []
    for i, c in enumerate(clips):
        n = os.path.join(work, f"_norm_{i}.mp4")
        vf = (f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
              f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1")
        subprocess.run(["ffmpeg", "-y", "-i", c, "-vf", vf, "-r", "30",
                        "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "veryfast",
                        "-crf", "20", "-c:a", "aac", "-b:a", "192k", n],
                       capture_output=True, check=True)
        norm.append(n)
    listf = os.path.join(work, "_concat.txt")
    with open(listf, "w", encoding="utf-8") as f:
        for n in norm:
            f.write(f"file '{os.path.abspath(n)}'\n")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listf,
                    "-c", "copy", out_path], capture_output=True, check=True)
    return out_path


def lower_third(video: str, text: str, out_path: str, fontfile: str = "") -> str:
    """Draw a lower-third name strip (SR-4.10). Requires a usable font."""
    font = f":fontfile='{fontfile}'" if fontfile else ""
    vf = (f"drawtext=text='{text}'{font}:fontcolor=white:fontsize=28:"
          f"box=1:boxcolor=black@0.5:x=40:y=h-80")
    subprocess.run(["ffmpeg", "-y", "-i", video, "-vf", vf, "-c:a", "copy", out_path],
                   capture_output=True, check=True)
    return out_path
