#!/usr/bin/env python3
"""metadata.py — embed title/description/chapter metadata into the export (SR-5.4).

Discoverability and chapter navigation once the file is published depend on
embedded metadata. ``chapters_file`` is an FFMETADATA file (see
``export.chapters_ffmetadata``).
"""
from __future__ import annotations

from typing import Optional

if __package__:  # 'app' in package context; '' when run flat by the server (CR-L9 / TD-1)
    from app.pipeline import _ff
else:
    from pipeline import _ff


def embed_metadata(in_media: str, out_path: str, title: Optional[str] = None,
                   description: Optional[str] = None,
                   chapters_file: Optional[str] = None) -> str:
    def _clean(v: str) -> str:
        # Values go to FFmpeg via argv (no shell), so the only corruption risk is
        # embedded newlines breaking the metadata stream — flatten them (CR-H12).
        return v.replace("\n", " ").replace("\r", " ")

    cmd = ["ffmpeg", "-y", "-i", in_media]
    if chapters_file:
        # Keep the source's own global metadata and import ONLY chapters from the
        # FFMETADATA file, rather than replacing all metadata with it (CR-L6).
        cmd += ["-i", chapters_file, "-map_metadata", "0", "-map_chapters", "1"]
    if title is not None:
        cmd += ["-metadata", f"title={_clean(title)}"]
    if description is not None:
        d = _clean(description)
        cmd += ["-metadata", f"description={d}", "-metadata", f"comment={d}"]
    cmd += ["-c", "copy", out_path]
    _ff.run(cmd)
    return out_path
