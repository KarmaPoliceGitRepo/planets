#!/usr/bin/env python3
"""segment_episode.py — split an episode into context-based SEGMENTS and
SUB-SECTIONS, each auto-TAGGED, so you can later choose what to keep.

Function F4c in the architecture (sits between cleaning and mastering).

What it produces
----------------
  <episode>/working/segments.json   ← the editable plan (segments → subsections)
  <episode>/captions/episode.txt     ← full transcript  (same as transcribe.py)
  <episode>/captions/episode.srt     ← subtitles
  <episode>/working/whisper.json      ← cached transcription (so re-runs are fast)

How the split works (no paid API, all local)
---------------------------------------------
1. Whisper transcribes the audio into many short timed "lines".
2. Lines are grouped into **sub-sections** at natural pauses (silence gaps) and
   sentence endings, capped to a comfortable length.
3. Sub-sections are grouped into **segments** (topics) using BOTH long pauses and
   a simple lexical-cohesion test: when the vocabulary of the next sub-section
   stops overlapping the current topic, a new segment begins.
4. Every segment and sub-section gets a short **tag/title** from its top keywords.

Each item has a "keep": true flag you can flip in the Studio UI (studio.py) or by
hand, then rebuild with render_selection.py.

Usage:
    python3 scripts/segment_episode.py episodes/01-the-missing-link
    python3 scripts/segment_episode.py episodes/01-the-missing-link --model small --language ne
    python3 scripts/segment_episode.py episodes/01-the-missing-link --reuse   # skip re-transcribing

If Whisper isn't installed it prints how to install it and exits politely.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

AUDIO_EXTS = (".mp3", ".wav", ".m4a", ".mp4", ".mov", ".mkv", ".aac", ".flac")
VIDEO_EXTS = (".mp4", ".mov", ".mkv")

# Tuning knobs for grouping (seconds) — chosen for natural speech.
GAP_SUB = 0.55     # a pause longer than this can end a sub-section
MAX_SUB = 45.0     # never let a sub-section grow past this
MIN_SUB = 6.0      # don't end a sub-section before this (avoid tiny slivers)
GAP_SEG = 1.4      # a pause longer than this can end a segment (topic)
MIN_SEG = 50.0     # don't end a segment before this
MAX_SEG = 300.0    # force a new segment past this (5 min)
COHESION_MIN = 0.07  # if keyword overlap drops below this, start a new segment

STOPWORDS = set("""
a an the and or but if then so because as of to in on at for with from by about into over after
before under above is are was were be been being am do does did doing have has had having i you he
she it we they me him her us them my your his its our their this that these those there here what
which who whom whose when where why how all any both each few more most other some such no nor not
only own same than too very can will just dont don't im i'm youre you're its it's were we're theyre
they're thats that's gonna wanna kind really actually basically like yeah okay ok um uh you know
""".split())


def maybe_reexec_in_venv() -> None:
    """If setup.sh made a local .venv with Whisper, re-run inside it."""
    if os.environ.get("MISSING_LINK_REEXEC"):
        return
    repo_root = Path(__file__).resolve().parent.parent
    here = Path(sys.executable).resolve()
    for cand in (repo_root / ".venv" / "bin" / "python",
                 repo_root / ".venv" / "Scripts" / "python.exe"):
        if cand.exists() and cand.resolve() != here:
            os.environ["MISSING_LINK_REEXEC"] = "1"
            os.execv(str(cand), [str(cand), os.path.abspath(__file__), *sys.argv[1:]])


def find_audio(ep: Path) -> Optional[Path]:
    """The edit source, in priority order: cleaned → premaster → newest raw."""
    for cand in (ep / "working" / "episode_clean.wav",
                 ep / "working" / "episode_premaster.wav"):
        if cand.exists():
            return cand
    raw = ep / "raw"
    if raw.is_dir():
        files = [p for p in raw.iterdir() if p.suffix.lower() in AUDIO_EXTS]
        if files:
            return max(files, key=lambda p: p.stat().st_mtime)
    return None


def find_video(ep: Path) -> Optional[Path]:
    raw = ep / "raw"
    if raw.is_dir():
        vids = [p for p in raw.iterdir() if p.suffix.lower() in VIDEO_EXTS]
        if vids:
            return max(vids, key=lambda p: p.stat().st_mtime)
    return None


def fmt_ts(seconds: float) -> str:
    if seconds < 0:
        seconds = 0
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def write_srt(lines: List[dict], path: Path) -> None:
    out = []
    for i, seg in enumerate(lines, start=1):
        out.append(str(i))
        out.append(f"{fmt_ts(seg['start'])} --> {fmt_ts(seg['end'])}")
        out.append(seg["text"].strip())
        out.append("")
    path.write_text("\n".join(out), encoding="utf-8")


def keywords(text: str, k: int = 6) -> List[str]:
    words = re.findall(r"[A-Za-z']+", text.lower())
    counts: Dict[str, int] = {}
    for w in words:
        if len(w) < 3 or w in STOPWORDS:
            continue
        counts[w] = counts.get(w, 0) + 1
    ranked = sorted(counts, key=lambda w: (-counts[w], w))
    return ranked[:k]


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def title_from(text: str) -> str:
    kw = keywords(text, 4)
    if kw:
        return " · ".join(kw[:3])
    snippet = text.strip().split(".")[0]
    return (snippet[:40] + "…") if len(snippet) > 40 else snippet or "section"


def group_subsections(lines: List[dict]) -> List[dict]:
    """Group fine Whisper lines into sub-sections at pauses / sentence ends."""
    subs: List[dict] = []
    cur: List[dict] = []

    def flush():
        if not cur:
            return
        text = " ".join(l["text"].strip() for l in cur).strip()
        subs.append({
            "start": round(cur[0]["start"], 2),
            "end": round(cur[-1]["end"], 2),
            "text": text,
            "tag": title_from(text),
            "keep": True,
        })

    for i, line in enumerate(lines):
        cur.append(line)
        dur = cur[-1]["end"] - cur[0]["start"]
        nxt_gap = (lines[i + 1]["start"] - line["end"]) if i + 1 < len(lines) else 99.0
        ends_sentence = line["text"].strip().endswith((".", "?", "!", "।"))
        if dur >= MAX_SUB:
            flush(); cur = []
        elif dur >= MIN_SUB and (nxt_gap >= GAP_SUB or ends_sentence):
            flush(); cur = []
    flush()
    return subs


def group_segments(subs: List[dict]) -> List[dict]:
    """Group sub-sections into context segments (topics)."""
    segments: List[dict] = []
    cur: List[dict] = []
    cur_kw: set = set()

    def flush():
        if not cur:
            return
        text = " ".join(s["text"] for s in cur)
        segments.append({
            "id": f"seg-{len(segments) + 1}",
            "title": title_from(text),
            "tag": (keywords(text, 3) or ["topic"])[0],
            "start": cur[0]["start"],
            "end": cur[-1]["end"],
            "keep": True,
            "subsections": [
                {**s, "id": f"seg-{len(segments) + 1}-{j + 1}"}
                for j, s in enumerate(cur)
            ],
        })

    for i, sub in enumerate(subs):
        sub_kw = set(keywords(sub["text"], 8))
        if cur:
            dur = sub["end"] - cur[0]["start"]
            gap = sub["start"] - cur[-1]["end"]
            cohesion = jaccard(cur_kw, sub_kw)
            topic_shift = (gap >= GAP_SEG or cohesion < COHESION_MIN)
            if dur >= MAX_SEG or (dur >= MIN_SEG and topic_shift):
                flush(); cur = []; cur_kw = set()
        cur.append(sub)
        cur_kw |= sub_kw
    flush()
    return segments


def main() -> int:
    ap = argparse.ArgumentParser(description="Split an episode into tagged segments & sub-sections.")
    ap.add_argument("episode", help="path to the episode folder, e.g. episodes/01-the-missing-link")
    ap.add_argument("--model", default="base", help="whisper model: tiny|base|small|medium|large")
    ap.add_argument("--language", default=None, help="force a language e.g. 'en' or 'ne' (default: auto)")
    ap.add_argument("--reuse", action="store_true",
                    help="reuse working/whisper.json if present (skip re-transcribing)")
    args = ap.parse_args()

    ep = Path(args.episode)
    if not ep.is_dir():
        print(f"❌ No such episode folder: {ep}", file=sys.stderr)
        return 1

    src = find_audio(ep)
    if src is None:
        print(f"❌ Found no audio in {ep}/working or {ep}/raw.", file=sys.stderr)
        print("   Clean or record something first.", file=sys.stderr)
        return 1

    (ep / "working").mkdir(parents=True, exist_ok=True)
    (ep / "captions").mkdir(parents=True, exist_ok=True)
    cache = ep / "working" / "whisper.json"

    result: Optional[dict] = None
    if args.reuse and cache.exists():
        print(f"[segment] reusing cached transcription: {cache}")
        result = json.loads(cache.read_text(encoding="utf-8"))

    if result is None:
        try:
            import whisper  # type: ignore
        except ImportError:
            maybe_reexec_in_venv()
            print("ℹ️  Whisper isn't installed yet. Install it (one time) with:\n")
            print("    python3 -m pip install -r scripts/requirements.txt\n")
            print("   (or:  python3 -m pip install openai-whisper)")
            print("   Tip: scripts/setup.sh can do this for you in a virtual env.")
            return 2

        print(f"[segment] input : {src}")
        print(f"[segment] model : {args.model}  (first run downloads it once)")
        print("[segment] transcribing... this can take a few minutes.")
        model = whisper.load_model(args.model)
        result = model.transcribe(str(src), language=args.language, verbose=False)
        cache.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")

    lines = [
        {"start": float(s["start"]), "end": float(s["end"]), "text": s["text"]}
        for s in result.get("segments", []) if s.get("text", "").strip()
    ]
    if not lines:
        print("❌ Whisper returned no speech segments — is there talking in the file?", file=sys.stderr)
        return 1

    # captions (parity with transcribe.py)
    (ep / "captions" / "episode.txt").write_text(
        result.get("text", "").strip() + "\n", encoding="utf-8")
    write_srt(lines, ep / "captions" / "episode.srt")

    subs = group_subsections(lines)
    segments = group_segments(subs)
    video = find_video(ep)

    plan = {
        "episode": str(ep),
        "source": str(src),
        "video": str(video) if video else None,
        "language": result.get("language", args.language or "auto"),
        "duration": round(lines[-1]["end"], 2),
        "generated": _dt.datetime.now().isoformat(timespec="seconds"),
        "segments": segments,
    }
    out = ep / "working" / "segments.json"
    out.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")

    kept = sum(1 for s in segments)
    print(f"✅ Segments  : {len(segments)} topics, {len(subs)} sub-sections")
    print(f"✅ Plan saved: {out}")
    print(f"✅ Captions  : {ep/'captions'/'episode.txt'} + episode.srt")
    print("\nNext:")
    print("  • Open the Studio UI to choose what to keep:")
    print("        python3 scripts/studio.py")
    print("  • Then rebuild the premaster from your choices:")
    print(f"        python3 scripts/render_selection.py {ep}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
