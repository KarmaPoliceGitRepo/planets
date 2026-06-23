#!/usr/bin/env python3
"""render_selection.py — rebuild the episode from ONLY the parts you kept.

Reads <episode>/working/segments.json (made by segment_episode.py and edited in
the Studio UI), collects every kept sub-section inside every kept segment, and
uses FFmpeg to trim + concatenate those pieces back into:

  <episode>/working/episode_premaster.wav   ← feeds process_episode.sh as usual
  <episode>/working/episode_cut.mp4          ← (only if the source had video)

A sub-section is kept only if BOTH it and its parent segment have "keep": true.
The original full clean/premaster is preserved (we read from segments.json's
"source"), so nothing is lost — re-render any time after changing your choices.

Usage:
    python3 scripts/render_selection.py episodes/01-the-missing-link
    python3 scripts/render_selection.py episodes/01-the-missing-link --no-video
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple

PAD = 0.04  # small pad (s) around each cut so words aren't clipped


def kept_intervals(plan: dict) -> List[Tuple[float, float]]:
    ivals: List[Tuple[float, float]] = []
    for seg in plan.get("segments", []):
        if not seg.get("keep", True):
            continue
        subs = seg.get("subsections") or []
        if not subs:
            ivals.append((float(seg["start"]), float(seg["end"])))
            continue
        for sub in subs:
            if sub.get("keep", True):
                ivals.append((float(sub["start"]), float(sub["end"])))
    # sort + merge touching/overlapping pieces (pad-aware)
    ivals.sort()
    merged: List[Tuple[float, float]] = []
    for s, e in ivals:
        s = max(0.0, s - PAD)
        e = e + PAD
        if merged and s <= merged[-1][1] + 0.01:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append((s, e))
    return merged


def build_filter(ivals: List[Tuple[float, float]], video: bool) -> str:
    parts = []
    labels_a = []
    labels_v = []
    for i, (s, e) in enumerate(ivals):
        parts.append(f"[0:a]atrim=start={s:.3f}:end={e:.3f},asetpts=PTS-STARTPTS[a{i}]")
        labels_a.append(f"[a{i}]")
        if video:
            parts.append(f"[0:v]trim=start={s:.3f}:end={e:.3f},setpts=PTS-STARTPTS[v{i}]")
            labels_v.append(f"[v{i}]")
    n = len(ivals)
    if video:
        inter = "".join(f"{v}{a}" for v, a in zip(labels_v, labels_a))
        parts.append(f"{inter}concat=n={n}:v=1:a=1[vout][aout]")
    else:
        parts.append(f"{''.join(labels_a)}concat=n={n}:v=0:a=1[aout]")
    return ";".join(parts)


def run(cmd: List[str]) -> int:
    print("[render] " + " ".join(cmd[:6]) + (" ..." if len(cmd) > 6 else ""))
    return subprocess.run(cmd).returncode


def main() -> int:
    ap = argparse.ArgumentParser(description="Rebuild premaster from kept segments/sub-sections.")
    ap.add_argument("episode", help="path to the episode folder")
    ap.add_argument("--no-video", action="store_true", help="audio only, even if video exists")
    args = ap.parse_args()

    ep = Path(args.episode)
    plan_path = ep / "working" / "segments.json"
    if not plan_path.exists():
        print(f"❌ No plan found: {plan_path}", file=sys.stderr)
        print("   Run: python3 scripts/segment_episode.py " + str(ep), file=sys.stderr)
        return 1
    if not shutil.which("ffmpeg"):
        print("❌ FFmpeg not found. Run: bash scripts/setup.sh", file=sys.stderr)
        return 1

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    audio_src = Path(plan.get("source", ""))
    if not audio_src.exists():
        print(f"❌ Source audio missing: {audio_src}", file=sys.stderr)
        return 1

    ivals = kept_intervals(plan)
    if not ivals:
        print("❌ Nothing is kept — every segment/sub-section is switched off.", file=sys.stderr)
        print("   Turn at least one back on in the Studio UI, then re-render.", file=sys.stderr)
        return 1

    total = sum(e - s for s, e in ivals)
    print(f"[render] keeping {len(ivals)} piece(s), ~{total/60:.1f} min total.")

    work = ep / "working"
    work.mkdir(parents=True, exist_ok=True)
    out_wav = work / "episode_premaster.wav"

    # Back up any hand-made premaster once, so we never clobber it silently.
    if out_wav.exists() and not (work / "episode_premaster.orig.wav").exists():
        if out_wav.resolve() != audio_src.resolve():
            shutil.copy2(out_wav, work / "episode_premaster.orig.wav")

    # --- audio ---
    af = build_filter(ivals, video=False)
    rc = run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
              "-i", str(audio_src),
              "-filter_complex", af, "-map", "[aout]",
              "-ar", "44100", str(out_wav)])
    if rc != 0:
        print("❌ Audio render failed.", file=sys.stderr)
        return 2
    print(f"✅ Audio rebuilt: {out_wav}")

    # --- video (optional) ---
    video_src: Optional[str] = plan.get("video")
    if video_src and not args.no_video and Path(video_src).exists():
        out_mp4 = work / "episode_cut.mp4"
        vf = build_filter(ivals, video=True)
        rc = run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                  "-i", str(video_src),
                  "-filter_complex", vf, "-map", "[vout]", "-map", "[aout]",
                  "-c:v", "libx264", "-preset", "veryfast", "-crf", "22",
                  "-c:a", "aac", "-b:a", "192k", str(out_mp4)])
        if rc == 0:
            print(f"✅ Video rebuilt: {out_mp4}")
            print("   (process_episode.sh will use this cut automatically.)")
        else:
            print("⚠️  Video render failed — audio premaster is still good.", file=sys.stderr)

    print("\nNext: master it →")
    print(f"      bash scripts/process_episode.sh {ep}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
