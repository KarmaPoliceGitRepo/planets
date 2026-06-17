#!/usr/bin/env python3
"""master.py — finish the rendered edit to podcast loudness (-16 LUFS).

Two-pass FFmpeg loudnorm on the rendered video's audio, then:
  • write exports/episode.mp3 (44.1 kHz / 128 kbps)
  • re-mux the normalised audio back into the video → exports/episode.mp4
Prints/returns a PASS/FAIL on integrated loudness and true peak.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

TARGET_I, TARGET_TP, TARGET_LRA = -16.0, -1.0, 11.0


def _measure(path: str) -> dict:
    out = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", path,
         "-af", f"loudnorm=I={TARGET_I}:TP={TARGET_TP}:LRA={TARGET_LRA}:print_format=json",
         "-f", "null", "-"], capture_output=True, text=True).stderr
    m = {}
    for key in ("input_i", "input_tp", "input_lra", "input_thresh", "target_offset"):
        g = re.search(rf'"{key}"\s*:\s*"?(-?[0-9.]+|inf)"?', out)
        if g:
            m[key] = g.group(1)
    return m


def master(in_video: str, out_dir: str, has_video: bool = True, progress=None) -> dict:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    def log(m):
        if progress:
            progress(m)

    log("[master] pass 1/2 measuring loudness…")
    m = _measure(in_video)
    if m.get("input_i"):
        af = (f"loudnorm=I={TARGET_I}:TP={TARGET_TP}:LRA={TARGET_LRA}:"
              f"measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
              f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
              f"offset={m['target_offset']}:linear=true")
    else:
        af = f"loudnorm=I={TARGET_I}:TP={TARGET_TP}:LRA={TARGET_LRA}"

    mp3 = out / "episode.mp3"
    log("[master] pass 2/2 exporting MP3…")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                    "-i", in_video, "-af", af, "-ar", "44100",
                    "-codec:a", "libmp3lame", "-b:a", "128k", str(mp3)], check=False)

    result = {"ok": True, "mp3": str(mp3)}
    if has_video:
        mp4 = out / "episode.mp4"
        log("[master] muxing mastered audio into video…")
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                        "-i", in_video, "-af", af, "-c:v", "copy",
                        "-c:a", "aac", "-b:a", "192k", str(mp4)], check=False)
        result["mp4"] = str(mp4)

    v = _measure(str(mp3))
    fi = float(v.get("input_i", "0") or 0)
    ftp = float(v.get("input_tp", "0") or 0)
    result["loudness"] = fi
    result["true_peak"] = ftp
    result["pass"] = (-17.0 <= fi <= -15.0) and (ftp <= TARGET_TP + 0.5)
    log(f"[master] {'PASS ✅' if result['pass'] else 'CHECK ⚠️'} "
        f"loudness={fi} LUFS, true_peak={ftp} dBTP")
    return result
