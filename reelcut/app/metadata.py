#!/usr/bin/env python3
"""metadata.py — embed title/description/chapter metadata into the export (SR-5.4).

Discoverability and chapter navigation once the file is published depend on
embedded metadata. ``chapters_file`` is an FFMETADATA file (see
``export.chapters_ffmetadata``).
"""
from __future__ import annotations

import subprocess
from typing import Optional


def embed_metadata(in_media: str, out_path: str, title: Optional[str] = None,
                   description: Optional[str] = None,
                   chapters_file: Optional[str] = None) -> str:
    def _clean(v: str) -> str:
        # Values go to FFmpeg via argv (no shell), so the only corruption risk is
        # embedded newlines breaking the metadata stream — flatten them (CR-H12).
        return v.replace("\n", " ").replace("\r", " ")

    cmd = ["ffmpeg", "-y", "-i", in_media]
    if chapters_file:
        cmd += ["-i", chapters_file, "-map_metadata", "1"]
    if title is not None:
        cmd += ["-metadata", f"title={_clean(title)}"]
    if description is not None:
        d = _clean(description)
        cmd += ["-metadata", f"description={d}", "-metadata", f"comment={d}"]
    cmd += ["-c", "copy", out_path]
    subprocess.run(cmd, capture_output=True, check=True)
    return out_path
