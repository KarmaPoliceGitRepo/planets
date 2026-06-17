#!/usr/bin/env python3
"""transcribe.py — make a transcript (.txt) and subtitles (.srt) for an episode.

Function F7 in the architecture. Satisfies FR-6 / PR-5 / N-21 (accessibility) and
helps bilingual listeners (N-12).

It uses OpenAI's open-source **Whisper**, which runs locally and free — your
audio never leaves your computer.

Usage:
    python3 scripts/transcribe.py episodes/01-the-missing-link
    python3 scripts/transcribe.py episodes/01-the-missing-link --model small --language ne

Input:  <episode>/exports/episode.mp3   (preferred)
        else the newest <episode>/raw/* audio/video file
Output: <episode>/captions/episode.txt
        <episode>/captions/episode.srt

If Whisper isn't installed yet, this script prints the exact command to install
it and exits politely — it never crashes with a wall of red.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import List, Optional

AUDIO_EXTS = (".mp3", ".wav", ".m4a", ".mp4", ".mov", ".mkv", ".aac", ".flac")


def maybe_reexec_in_venv() -> None:
    """If scripts/setup.sh created a local .venv (with Whisper) but we're not
    running inside it, re-run this script with the venv's Python. This makes
    `python3 scripts/transcribe.py ...` "just work" for beginners after setup.
    A guard env var prevents any chance of an infinite re-exec loop."""
    if os.environ.get("MISSING_LINK_REEXEC"):
        return
    repo_root = Path(__file__).resolve().parent.parent
    here = Path(sys.executable).resolve()
    for cand in (repo_root / ".venv" / "bin" / "python",
                 repo_root / ".venv" / "Scripts" / "python.exe"):
        if cand.exists() and cand.resolve() != here:
            os.environ["MISSING_LINK_REEXEC"] = "1"
            os.execv(str(cand), [str(cand), os.path.abspath(__file__), *sys.argv[1:]])


def find_input(ep: Path) -> Optional[Path]:
    """Prefer the finished export; fall back to the newest raw recording."""
    preferred = ep / "exports" / "episode.mp3"
    if preferred.exists():
        return preferred
    candidates: List[Path] = []
    for sub in ("exports", "working", "raw"):
        d = ep / sub
        if d.is_dir():
            candidates += [p for p in d.iterdir() if p.suffix.lower() in AUDIO_EXTS]
    if not candidates:
        return None
    return max(candidates, key=lambda p: p.stat().st_mtime)


def fmt_ts(seconds: float) -> str:
    """Seconds -> SRT timestamp HH:MM:SS,mmm."""
    if seconds < 0:
        seconds = 0
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def write_srt(segments, path: Path) -> None:
    lines = []
    for i, seg in enumerate(segments, start=1):
        lines.append(str(i))
        lines.append(f"{fmt_ts(seg['start'])} --> {fmt_ts(seg['end'])}")
        lines.append(seg["text"].strip())
        lines.append("")  # blank line between cues
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Transcribe an episode to .txt + .srt")
    ap.add_argument("episode", help="path to the episode folder, e.g. episodes/01-the-missing-link")
    ap.add_argument("--model", default="base",
                    help="whisper model: tiny|base|small|medium|large "
                         "(bigger = more accurate but slower; 'small' is a good balance)")
    ap.add_argument("--language", default=None,
                    help="force a language, e.g. 'en' or 'ne' (Nepali). Default: auto-detect.")
    args = ap.parse_args()

    ep = Path(args.episode)
    if not ep.is_dir():
        print(f"❌ No such episode folder: {ep}", file=sys.stderr)
        return 1

    src = find_input(ep)
    if src is None:
        print(f"❌ Found no audio/video in {ep}/exports, /working or /raw.", file=sys.stderr)
        print("   Record something first, or run process_episode.sh.", file=sys.stderr)
        return 1

    # Import whisper lazily so we can give a friendly message if it's missing.
    try:
        import whisper  # type: ignore
    except ImportError:
        # If a local .venv has Whisper, transparently re-run inside it.
        maybe_reexec_in_venv()
        print("ℹ️  Whisper isn't installed yet. Install it (one time) with:\n")
        print("    python3 -m pip install -r scripts/requirements.txt\n")
        print("   (or:  python3 -m pip install openai-whisper)")
        print("   Tip: scripts/setup.sh can do this for you in a virtual env.")
        return 2

    print(f"[transcribe] input : {src}")
    print(f"[transcribe] model : {args.model}  (first run downloads it once)")
    print("[transcribe] working... this can take a few minutes.")

    model = whisper.load_model(args.model)
    result = model.transcribe(str(src), language=args.language, verbose=False)

    out_dir = ep / "captions"
    out_dir.mkdir(parents=True, exist_ok=True)
    txt_path = out_dir / "episode.txt"
    srt_path = out_dir / "episode.srt"

    txt_path.write_text(result.get("text", "").strip() + "\n", encoding="utf-8")
    write_srt(result.get("segments", []), srt_path)

    detected = result.get("language", args.language or "auto")
    print(f"[transcribe] language detected: {detected}")
    print(f"✅ Transcript: {txt_path}")
    print(f"✅ Subtitles : {srt_path}")
    print("\nNext steps:")
    print("  • Skim the transcript and fix names (Mahendra, Gyanendra, Mustang,")
    print("    Manang, tato pani) — Whisper guesses spellings.")
    print("  • Upload episode.srt to YouTube as subtitles (accessibility, N-21).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
