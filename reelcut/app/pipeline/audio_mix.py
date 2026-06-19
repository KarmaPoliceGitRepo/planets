#!/usr/bin/env python3
"""audio_mix.py — replace/add audio and synth image clips (SR-2.3, SR-2.4, SR-2.5).

All operations are FFmpeg-based and keep the video stream copied where possible
(lossless, fast). Loudness is re-normalised separately by ``master.py`` so the
final mix still meets −16 LUFS (SR-2.6).
"""
from __future__ import annotations

import os
import subprocess


def replace_audio(video: str, new_audio: str, out_path: str) -> str:
    """Swap the video's audio for ``new_audio`` (SR-2.3). Video stream copied."""
    subprocess.run(["ffmpeg", "-y", "-i", video, "-i", new_audio,
                    "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", out_path],
                   capture_output=True, check=True)
    return out_path


def add_audio(video: str, extra_audio: str, out_path: str,
              level_db: float = 0.0, duck: bool = False) -> str:
    """Mix ``extra_audio`` under the existing audio (SR-2.4).

    ``level_db`` adjusts the added track; ``duck`` ducks it under speech using
    sidechain compression keyed by the original (speech) track.
    """
    if duck:
        fc = (f"[1:a]volume={level_db}dB[m];"
              f"[m][0:a]sidechaincompress=threshold=0.03:ratio=8:attack=5:release=250[dk];"
              f"[0:a][dk]amix=inputs=2:duration=first:dropout_transition=0[a]")
    else:
        fc = (f"[1:a]volume={level_db}dB[m];"
              f"[0:a][m]amix=inputs=2:duration=first:dropout_transition=0[a]")
    subprocess.run(["ffmpeg", "-y", "-i", video, "-i", extra_audio,
                    "-filter_complex", fc, "-map", "0:v:0", "-map", "[a]",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", out_path],
                   capture_output=True, check=True)
    return out_path


def image_clip(image: str, out_path: str, duration: float = 4.0,
               width: int = 1280, height: int = 720) -> str:
    """Synthesise a still video clip from an image (SR-2.5): fixed duration,
    no Ken-Burns motion, no intrinsic audio."""
    vf = f"scale={width}:{height}:force_original_aspect_ratio=decrease," \
         f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1"
    subprocess.run(["ffmpeg", "-y", "-loop", "1", "-i", image, "-t", f"{duration}",
                    "-vf", vf, "-r", "30", "-pix_fmt", "yuv420p",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                    "-an", out_path],
                   capture_output=True, check=True)
    return out_path
