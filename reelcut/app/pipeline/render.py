#!/usr/bin/env python3
"""render.py — ReelCut's reorder-aware render engine (two-stage).

Turns an edit plan (kept clips in a chosen ORDER, with per-boundary TRANSITIONS)
into one finished video.

Why two stages? Feeding ONE input into many ``atrim`` branches starves
``acrossfade`` (the audio silently drops while video survives — FFmpeg emits no
error). So we:

  Stage 1 — cut & normalise each clip to its OWN file (independent streams).
  Stage 2 — join those separate files with ``xfade`` + ``acrossfade`` (video) or
            ``concat`` (hard cuts). Separate inputs = no shared-input buffering.

Both xfade and acrossfade OVERLAP clips by the transition duration, so each
subsequent offset is computed from the running, overlap-adjusted duration. A
timing map (original time → new output time) is produced so captions can be
re-timed for the re-sequenced edit.
"""
from __future__ import annotations

import json
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Tuple

# UI transition name  →  ffmpeg xfade transition name
XFADE_MAP: Dict[str, str] = {
    "crossfade": "fade",
    "dissolve": "dissolve",
    "fade-black": "fadeblack",
    "fade-white": "fadewhite",
    "wipe-left": "wipeleft",
    "wipe-right": "wiperight",
    "wipe-up": "wipeup",
    "wipe-down": "wipedown",
    "slide-left": "slideleft",
    "slide-right": "slideright",
    "slide-up": "slideup",
    "slide-down": "slidedown",
    "circle-open": "circleopen",
    "circle-close": "circleclose",
    "radial": "radial",
    "smooth-right": "smoothright",
}
TRANSITION_NAMES = ["cut"] + list(XFADE_MAP.keys())


@dataclass
class Clip:
    id: str
    start: float
    end: float
    order: int

    @property
    def dur(self) -> float:
        return max(0.0, self.end - self.start)


@dataclass
class Boundary:
    type: str = "cut"
    duration: float = 0.5
    auto_gap: bool = False


@dataclass
class Plan:
    source: str
    clips: List[Clip]
    boundaries: List[Boundary]
    width: int = 1280
    height: int = 720
    fps: int = 30
    timing_map: List[dict] = field(default_factory=list)


# --------------------------------------------------------------------------- #
# Plan building
# --------------------------------------------------------------------------- #
def kept_clips(project: dict) -> List[Clip]:
    clips: List[Clip] = []
    for seg in project.get("segments", []):
        if not seg.get("keep", True):
            continue
        for sub in seg.get("subsections", []):
            if sub.get("keep", True):
                s, e = float(sub["start"]), float(sub["end"])
                if e <= s:  # an inverted/zero range would emit an empty -t 0 clip (CR-L10)
                    raise ValueError(f"sub-section {sub['id']!r} has end ({e}) <= start ({s})")
                clips.append(Clip(sub["id"], s, e, int(sub.get("order", 10_000))))
    clips.sort(key=lambda c: (c.order, c.start))
    for i, c in enumerate(clips, 1):
        c.order = i
    return clips


def _original_index(project: dict) -> Dict[str, int]:
    order, idx = {}, 0
    for seg in project.get("segments", []):
        for sub in seg.get("subsections", []):
            order[sub["id"]] = idx
            idx += 1
    return order


def build_plan(project: dict) -> Plan:
    clips = kept_clips(project)
    if not clips:
        raise ValueError("Nothing kept — every segment/sub-section is switched off.")
    trans = project.get("transitions", {})
    orig = _original_index(project)
    boundaries: List[Boundary] = []
    for a, b in zip(clips, clips[1:]):
        # Adjacency is purely "were these consecutive in the original?" — a time
        # proximity heuristic wrongly classified reordered clips that happened to have
        # near-equal times (CR-M9).
        was_adjacent = orig.get(b.id, -99) == orig.get(a.id, -1) + 1
        cfg = trans.get(b.id, {})
        boundaries.append(Boundary(
            type=cfg.get("type", "cut" if was_adjacent else "crossfade"),
            duration=float(cfg.get("duration", 0.5)),
            auto_gap=not was_adjacent))
    return Plan(project["source"], clips, boundaries,
                int(project.get("width", 1280)), int(project.get("height", 720)),
                int(project.get("fps", 30)))


def timing_map(plan: Plan) -> List[dict]:
    """Compute each clip's new output start time (overlap-adjusted)."""
    tm = [{"id": plan.clips[0].id, "src_start": plan.clips[0].start,
           "src_end": plan.clips[0].end, "new_start": 0.0}]
    running = plan.clips[0].dur
    for i in range(1, len(plan.clips)):
        b, c = plan.boundaries[i - 1], plan.clips[i]
        if b.type == "cut" or b.duration <= 0:
            new_start = running
            running += c.dur
        else:
            t = min(b.duration, plan.clips[i - 1].dur, c.dur, running)
            new_start = max(0.0, running - t)
            running += c.dur - t
        tm.append({"id": c.id, "src_start": c.start, "src_end": c.end,
                   "new_start": round(new_start, 3)})
    return tm


# --------------------------------------------------------------------------- #
# Stage 1 — cut & normalise each clip to its own file
# --------------------------------------------------------------------------- #
def _extract(plan: Plan, workdir: Path, has_video: bool, progress) -> List[Path]:
    files: List[Path] = []
    for i, c in enumerate(plan.clips):
        out = workdir / (f"clip_{i:03d}.mp4" if has_video else f"clip_{i:03d}.m4a")
        cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
               "-ss", f"{c.start:.3f}", "-i", plan.source, "-t", f"{c.dur:.3f}"]
        if has_video:
            cmd += ["-vf", (f"scale={plan.width}:{plan.height}:force_original_aspect_ratio=decrease,"
                            f"pad={plan.width}:{plan.height}:(ow-iw)/2:(oh-ih)/2,setsar=1,"
                            f"fps={plan.fps},format=yuv420p"),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20"]
        cmd += ["-af", "aformat=sample_rates=44100:channel_layouts=stereo",
                "-c:a", "aac", "-b:a", "192k", str(out)]
        if progress:
            progress(f"[render] cut clip {i + 1}/{len(plan.clips)} ({c.dur:.1f}s)")
        rc = subprocess.run(cmd, capture_output=True, text=True)
        if rc.returncode != 0:
            raise RuntimeError(f"clip {i} extract failed:\n{rc.stderr[-600:]}")
        files.append(out)
    return files


# --------------------------------------------------------------------------- #
# Stage 2 — join the separate files
# --------------------------------------------------------------------------- #
def _build_join(plan: Plan, n: int, has_video: bool) -> Tuple[str, str, str]:
    parts: List[str] = []
    # label each input's streams cleanly
    for i in range(n):
        if has_video:
            parts.append(f"[{i}:v]setpts=PTS-STARTPTS[v{i}]")
        parts.append(f"[{i}:a]asetpts=PTS-STARTPTS[a{i}]")
    vacc = "v0" if has_video else ""
    aacc = "a0"
    running = plan.clips[0].dur
    for i in range(1, n):
        b, c = plan.boundaries[i - 1], plan.clips[i]
        if b.type == "cut" or b.duration <= 0:
            if has_video:
                parts.append(f"[{vacc}][v{i}]concat=n=2:v=1:a=0[vc{i}]"); vacc = f"vc{i}"
            parts.append(f"[{aacc}][a{i}]concat=n=2:v=0:a=1[ac{i}]"); aacc = f"ac{i}"
            running += c.dur
        else:
            t = min(b.duration, plan.clips[i - 1].dur, c.dur, running)
            offset = max(0.0, running - t)
            xf = XFADE_MAP.get(b.type, "fade")
            if has_video:
                parts.append(f"[{vacc}][v{i}]xfade=transition={xf}:duration={t:.3f}:"
                             f"offset={offset:.3f}[vx{i}]"); vacc = f"vx{i}"
            parts.append(f"[{aacc}][a{i}]acrossfade=d={t:.3f}[ax{i}]"); aacc = f"ax{i}"
            running += c.dur - t
    return ";".join(parts), vacc, aacc


def render(project: dict, out_path: str, has_video: bool = True, progress=None) -> dict:
    plan = build_plan(project)
    tm = timing_map(plan)
    plan.timing_map = tm
    workdir = Path(tempfile.mkdtemp(prefix="reelcut_"))
    try:
        if len(plan.clips) == 1:
            # single clip: just cut it, no join needed
            files = _extract(plan, workdir, has_video, progress)
            rc = subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                                 "-i", str(files[0]), "-c", "copy", out_path],
                                capture_output=True, text=True)
            if rc.returncode != 0 or not Path(out_path).exists():   # CR-M2
                return {"ok": False, "error": rc.stderr[-1500:], "timing_map": tm}
        else:
            files = _extract(plan, workdir, has_video, progress)
            fg, vlab, alab = _build_join(plan, len(files), has_video)
            cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
            for f in files:
                cmd += ["-i", str(f)]
            cmd += ["-filter_complex", fg]
            if has_video:
                cmd += ["-map", f"[{vlab}]", "-c:v", "libx264", "-preset", "veryfast",
                        "-crf", "20", "-pix_fmt", "yuv420p"]
            cmd += ["-map", f"[{alab}]", "-c:a", "aac", "-b:a", "192k", out_path]
            if progress:
                progress("[render] joining clips with transitions…")
            rc = subprocess.run(cmd, capture_output=True, text=True)
            if rc.returncode != 0:
                return {"ok": False, "error": rc.stderr[-1500:], "timing_map": tm}
        total = tm[-1]["new_start"] + plan.clips[-1].dur
        return {"ok": True, "timing_map": tm, "duration": round(total, 2)}
    finally:
        for f in workdir.glob("*"):
            try:
                f.unlink()
            except OSError:
                pass
        try:
            workdir.rmdir()
        except OSError:
            pass


def build_filtergraph(plan: Plan, has_video: bool = True):
    """Back-compat shim for tests: returns (join_filter, vlab, alab, timing_map)."""
    tm = timing_map(plan)
    plan.timing_map = tm
    fg, v, a = _build_join(plan, len(plan.clips), has_video)
    return fg, v, a, tm


def _kept_index(project: dict) -> Dict[str, tuple]:
    out: Dict[str, tuple] = {}
    for seg in project.get("segments", []):
        if seg.get("keep", True) is False:
            continue
        for s in seg.get("subsections", []):
            if s.get("keep", True):
                out[s["id"]] = (round(s.get("start", 0.0), 3),
                                round(s.get("end", 0.0), 3),
                                s.get("order", 0))
    return out


def incremental_plan(old_project: dict, new_project: dict) -> dict:
    """Compare two project states and report which kept clips can be reused versus
    re-cut, so a re-render only touches changed clips (SR-3.6). A clip is reusable
    when its id, source in/out and output order are all unchanged."""
    old, new = _kept_index(old_project), _kept_index(new_project)
    reuse = [i for i in new if i in old and old[i] == new[i]]
    recut = [i for i in new if i not in old or old[i] != new[i]]
    return {"reuse": reuse, "recut": recut}


def timing_for(project: dict) -> List[dict]:
    """The output timing map for a project. Preview and final export both derive
    their clip boundaries from THIS one function, so the preview is frame-accurate
    to the export by construction (SR-4.4 / WYSIWYG)."""
    return timing_map(build_plan(project))


if __name__ == "__main__":
    import sys
    proj = json.loads(Path(sys.argv[1]).read_text())
    out = sys.argv[2] if len(sys.argv) > 2 else "out.mp4"
    print(json.dumps(render(proj, out, progress=print), indent=2))
