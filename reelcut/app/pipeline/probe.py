#!/usr/bin/env python3
"""probe.py — read basic facts about a media file with ffprobe."""
from __future__ import annotations

import json
import subprocess
from typing import Optional


def probe(path: str) -> dict:
    """Return {duration,width,height,fps,has_video,has_audio}. Robust to missing streams."""
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-print_format", "json",
             "-show_format", "-show_streams", path],
            capture_output=True, text=True, check=True).stdout
        data = json.loads(out)
    except Exception:
        return {"duration": 0.0, "width": 1280, "height": 720, "fps": 30,
                "has_video": False, "has_audio": False}
    info = {"duration": float(data.get("format", {}).get("duration", 0.0) or 0.0),
            "width": 1280, "height": 720, "fps": 30,
            "has_video": False, "has_audio": False}
    for s in data.get("streams", []):
        if s.get("codec_type") == "video" and not info["has_video"]:
            info["has_video"] = True
            info["width"] = int(s.get("width", 1280) or 1280)
            info["height"] = int(s.get("height", 720) or 720)
            r = s.get("avg_frame_rate") or s.get("r_frame_rate") or "30/1"
            try:
                n, d = r.split("/")
                info["fps"] = max(1, round(float(n) / float(d))) if float(d) else 30
            except Exception:
                info["fps"] = 30
        elif s.get("codec_type") == "audio":
            info["has_audio"] = True
    return info
