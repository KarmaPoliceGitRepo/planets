# ReelCut Cross-Platform Build — Implementation Plan (Roadmap + Phase 1)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete the ReelCut software (the podcast system's implementation-layer SoI) from its verified SR-1.x baseline through the full SR-2…SR-5 backlog, and package it for **desktop (macOS, Windows)** and **mobile (iOS, Android)**.

**Architecture:** Keep the proven core — a stdlib-only local HTTP server (`app/server.py`) driving an FFmpeg pipeline (`app/pipeline/*`) with a browser UI — and grow it in test-gated increments. Desktop = wrap the same server + UI in a native window (pywebview) with a bundled FFmpeg, packaged per-OS (PyInstaller). Mobile = a thin native client that reads the **portable, renderer-agnostic project document** (SR-2.2) and renders via mobile FFmpeg (ffmpeg-kit). The portable project doc is the keystone that makes one model serve all platforms.

**Tech Stack:** Python 3.11 (stdlib `http.server`), FFmpeg/ffprobe, Whisper (optional), vanilla HTML/CSS/JS UI; desktop: pywebview + PyInstaller + static FFmpeg; mobile: React Native (or Flutter) + ffmpeg-kit.

## Global Constraints (verbatim from the model)

- Audio output **−16 LUFS ±1, true-peak ≤ −1 dBTP** (SR-1.5 / podcast PR-1).
- A/V stay in sync across cuts and transitions (SR-1.6).
- HMI binds **127.0.0.1**; media is **never uploaded** (SR-1.7 / SN-3).
- Outputs: **H.264/AAC MP4, MP3 44.1 kHz, SubRip** (SR-1.8).
- **$0 / no paid software**, runs on Python 3 + FFmpeg, **no GPU** (podcast UR-2, HC-2).
- Project document is **portable and renderer-agnostic**: stable media handles, **no absolute paths, no embedded FFmpeg strings** (SR-2.2).
- Original recording is **read-only**; all edits non-destructive and reversible (SR-4.1).
- Every increment closes only when its test passes **with real FFmpeg** and the loudness / A/V-sync / caption-integrity constraints still hold.

## Skill inventory (using-superpowers result)

| Need | Skill (installed) |
|---|---|
| Plan / spec | `writing-plans`, `brainstorming` |
| Terse chat / review / commits | `caveman`, `caveman-review`, `caveman-commit` |
| Durable memory across sessions | `graphify` (the "mem") |
| Manual verification | `verify` (bundled), `code-review`, `simplify` |

**Gap:** no desktop (Electron/Tauri) or mobile (React Native/Flutter) framework skill exists on disk or in the marketplace (searched). Phases 5–6 therefore rely on engineering knowledge, not a skill. If such a skill is published later, install via `find-skills`.

## Decomposition (each phase = its own working, testable deliverable)

| Phase | Scope | SRs | Status |
|---|---|---|---|
| **P0** | Baseline editor (segment→reorder→render→caption→master→serve) | SR-1.1…1.8 | ✅ Built & verified (12 tests) |
| **P1** | **Portable doc + non-destructive + demux** (this plan, detailed below) | SR-2.2, SR-4.1, SR-2.1 | ▶ Next |
| **P2** | Media ops: replace/add audio (+duck), image clips, preserve −16 LUFS | SR-2.3…2.7, SR-2.6 | Planned |
| **P3** | Robustness: validate, autosave/restore, undo/redo, cancel/progress | SR-3.1…3.5 | Planned |
| **P4** | Production/growth + register: aspect/preset, translation, WYSIWYG, tighten, highlights, clean-audio, burn-in, branding, presets, transcript, batch, license, metadata | SR-4.x, SR-5.x | Planned |
| **P5** | **Desktop packaging** (macOS + Windows) | HC-2 | Planned |
| **P6** | **Mobile client** (iOS + Android) | HC-1 | Planned |

> P2–P6 each get their own `writing-plans` document when reached (a single bite-sized
> plan for all six phases would be tens of thousands of lines and force placeholders —
> a plan failure). This document fully details **P1** and fixes the **P5/P6 architecture**
> so later plans inherit the decisions.

## Desktop architecture (P5) — decided

- **Wrap, don't rewrite.** A native window via **pywebview** loads `http://127.0.0.1:<port>`
  served by the existing `app/server.py` started as a child thread. Zero UI rewrite.
- **Bundle FFmpeg**: ship a static `ffmpeg`/`ffprobe` per-OS under `app/bin/<os>/`; the
  pipeline resolves the bundled binary first, falling back to PATH.
- **Package**: PyInstaller one-folder build per OS → `ReelCut.app` (macOS, signed/notarized
  later) and `ReelCut.exe` (Windows). `run.sh`/`run.bat` remain the dev entry points.
- **Why not Electron/Tauri:** both add a second runtime/toolchain and a JS/Rust rewrite of
  the host; pywebview reuses 100 % of the Python core and keeps the $0/no-GPU constraint.

## Mobile architecture (P6) — decided

- **Keystone = SR-2.2 portable project doc.** The mobile app reads the *same* JSON project
  document; rendering is re-implemented natively (the Python server does not run on mobile).
- **Client**: React Native (TypeScript) — one codebase for iOS + Android; **render** via
  `ffmpeg-kit-react-native` (bundled mobile FFmpeg), reusing the documented filtergraph
  recipe from `app/pipeline/render.py` re-expressed against the portable doc.
- **Scope first**: read-only playback + reorder + render of an existing project doc, then
  capture. Tracked against the mobile feasibility brief
  (`docs/superpowers/plans/2026-06-18-reelcut-mobile-port-feasibility.md`).

---

## Phase 1 — Portable doc + non-destructive + demux

Files in play:
- Modify: `reelcut/app/model.py` (portable handles, read-only guard)
- Create: `reelcut/app/pipeline/demux.py`
- Modify: `reelcut/app/pipeline/probe.py` (track inventory)
- Test: `reelcut/tests/test_phase1.py` (new), run with `python3 tests/test_phase1.py`

### Task 1: Non-destructive source guard (SR-4.1)

**Files:**
- Modify: `reelcut/app/model.py`
- Test: `reelcut/tests/test_phase1.py`

**Interfaces:**
- Produces: `model.source_digest(project: dict) -> str` (sha256 of the source file);
  `model.assert_source_unchanged(project: dict) -> None` (raises `SourceMutated` if the
  source file's digest differs from the one recorded at import).

- [ ] **Step 1: Write the failing test**

```python
# reelcut/tests/test_phase1.py
import hashlib, os, tempfile, unittest, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import model

class TestNonDestructive(unittest.TestCase):
    def test_source_digest_detects_mutation(self):
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d) / "raw.wav"
            src.write_bytes(b"original-bytes")
            project = {"source": str(src)}
            dig = model.source_digest(project)
            project["source_sha256"] = dig
            model.assert_source_unchanged(project)          # no raise
            src.write_bytes(b"tampered")                    # simulate mutation
            with self.assertRaises(model.SourceMutated):
                model.assert_source_unchanged(project)

if __name__ == "__main__":
    unittest.main(verbosity=2)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd reelcut && python3 tests/test_phase1.py TestNonDestructive -v`
Expected: FAIL — `AttributeError: module 'app.model' has no attribute 'source_digest'`.

- [ ] **Step 3: Write minimal implementation**

```python
# add to reelcut/app/model.py
import hashlib

class SourceMutated(Exception):
    """Raised when an imported source file has changed since import (SR-4.1)."""

def source_digest(project: dict) -> str:
    with open(project["source"], "rb") as f:
        h = hashlib.sha256()
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def assert_source_unchanged(project: dict) -> None:
    recorded = project.get("source_sha256")
    if recorded is not None and source_digest(project) != recorded:
        raise SourceMutated(project["source"])
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd reelcut && python3 tests/test_phase1.py TestNonDestructive -v`
Expected: PASS (2 assertions).

- [ ] **Step 5: Commit**

```bash
git add reelcut/app/model.py reelcut/tests/test_phase1.py
git commit -m "feat(model): non-destructive source guard (SR-4.1)"
```

### Task 2: Portable, renderer-agnostic project doc (SR-2.2)

**Files:**
- Modify: `reelcut/app/model.py`
- Test: `reelcut/tests/test_phase1.py`

**Interfaces:**
- Produces: `model.to_portable(project: dict, project_dir: str) -> dict` (rewrites the
  `source` to a path **relative** to `project_dir`, strips any absolute paths / keys
  starting with `ffmpeg_`); `model.from_portable(doc: dict, project_dir: str) -> dict`
  (resolves the relative handle back to an absolute path for the current machine).

- [ ] **Step 1: Write the failing test**

```python
# append to reelcut/tests/test_phase1.py
class TestPortableDoc(unittest.TestCase):
    def test_roundtrip_survives_dir_move(self):
        with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
            media = pathlib.Path(d1) / "media" / "raw.wav"
            media.parent.mkdir(); media.write_bytes(b"x")
            project = {"source": str(media), "ffmpeg_cmd": "ffmpeg -i ...", "segments": []}
            doc = model.to_portable(project, d1)
            self.assertFalse(os.path.isabs(doc["source"]))          # relative handle
            self.assertNotIn("ffmpeg_cmd", doc)                     # no renderer strings
            # simulate moving the whole project folder d1 -> d2
            import shutil; shutil.copytree(d1, d2, dirs_exist_ok=True)
            restored = model.from_portable(doc, d2)
            self.assertTrue(os.path.exists(restored["source"]))     # resolves on new machine
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd reelcut && python3 tests/test_phase1.py TestPortableDoc -v`
Expected: FAIL — `AttributeError: ... 'to_portable'`.

- [ ] **Step 3: Write minimal implementation**

```python
# add to reelcut/app/model.py
import os

def to_portable(project: dict, project_dir: str) -> dict:
    doc = {k: v for k, v in project.items() if not k.startswith("ffmpeg_")}
    src = project.get("source")
    if src and os.path.isabs(src):
        doc["source"] = os.path.relpath(src, project_dir)
    return doc

def from_portable(doc: dict, project_dir: str) -> dict:
    project = dict(doc)
    src = doc.get("source")
    if src and not os.path.isabs(src):
        project["source"] = os.path.normpath(os.path.join(project_dir, src))
    return project
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd reelcut && python3 tests/test_phase1.py TestPortableDoc -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add reelcut/app/model.py reelcut/tests/test_phase1.py
git commit -m "feat(model): portable renderer-agnostic project doc (SR-2.2)"
```

### Task 3: Demux into independent A/V tracks (SR-2.1)

**Files:**
- Create: `reelcut/app/pipeline/demux.py`
- Test: `reelcut/tests/test_phase1.py`

**Interfaces:**
- Consumes: `probe.probe(path) -> {has_video, has_audio, duration, ...}` (existing).
- Produces: `demux.demux(src: str, out_dir: str) -> dict` returning
  `{"video": <path|None>, "audio": <path|None>}` — stream-copied tracks (`-c copy`),
  no re-encode, so it is lossless and fast.

- [ ] **Step 1: Write the failing test**

```python
# append to reelcut/tests/test_phase1.py
import subprocess
def _ffmpeg_ok():
    try: subprocess.run(["ffmpeg","-version"], capture_output=True, check=True); return True
    except Exception: return False

@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestDemux(unittest.TestCase):
    def test_splits_av(self):
        from app.pipeline import demux, probe
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d) / "in.mp4"
            subprocess.run(["ffmpeg","-y","-f","lavfi","-i","testsrc=d=1:s=160x120",
                            "-f","lavfi","-i","sine=d=1","-shortest",str(src)],
                           capture_output=True, check=True)
            out = demux.demux(str(src), d)
            self.assertTrue(out["video"] and os.path.exists(out["video"]))
            self.assertTrue(out["audio"] and os.path.exists(out["audio"]))
            self.assertFalse(probe.probe(out["audio"]).get("has_video"))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd reelcut && python3 tests/test_phase1.py TestDemux -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'app.pipeline.demux'`.

- [ ] **Step 3: Write minimal implementation**

```python
# reelcut/app/pipeline/demux.py
"""demux.py — split a media file into independent A/V track files (SR-2.1).
Stream-copy only (-c copy): lossless, fast, no re-encode. Precondition for
independent A/V manipulation (SN-6)."""
import os, subprocess
from . import probe

def demux(src: str, out_dir: str) -> dict:
    p = probe.probe(src)
    os.makedirs(out_dir, exist_ok=True)
    result = {"video": None, "audio": None}
    if p.get("has_video"):
        v = os.path.join(out_dir, "track_video.mp4")
        subprocess.run(["ffmpeg","-y","-i",src,"-map","0:v:0","-c","copy","-an",v],
                       capture_output=True, check=True); result["video"] = v
    if p.get("has_audio"):
        a = os.path.join(out_dir, "track_audio.m4a")
        subprocess.run(["ffmpeg","-y","-i",src,"-map","0:a:0","-c","copy","-vn",a],
                       capture_output=True, check=True); result["audio"] = a
    return result
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd reelcut && python3 tests/test_phase1.py TestDemux -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add reelcut/app/pipeline/demux.py reelcut/tests/test_phase1.py
git commit -m "feat(pipeline): demux into independent A/V tracks (SR-2.1)"
```

### Task 4: Wire Phase-1 into the model-domain doc + run full suite

- [ ] **Step 1:** Update `reelcut/mbse/4-implementation-domain.md` — move SR-2.1, SR-2.2,
  SR-4.1 rows from "Planned backlog" to a new "Built (Phase 1)" block, citing
  `tests/test_phase1.py`.
- [ ] **Step 2:** Run the whole suite: `cd reelcut && python3 tests/test_reelcut.py && python3 tests/test_phase1.py` — expected: all PASS.
- [ ] **Step 3:** Run `.claude/hooks/drift-check.sh` — expected `✅ OK`.
- [ ] **Step 4: Commit**

```bash
git add reelcut/mbse/4-implementation-domain.md
git commit -m "docs(mbse): mark SR-2.1/2.2/4.1 Built (Phase 1)"
```

## Self-Review

- **Spec coverage:** P1 implements SR-2.1, SR-2.2, SR-4.1 with a test each; SR-2.3…SR-5.4
  and packaging (P2–P6) are explicitly deferred to their own plans, with P5/P6 architecture
  fixed here so they inherit decisions. No silent gaps.
- **Placeholder scan:** none — every step has runnable test + implementation code.
- **Type consistency:** `source_digest`/`assert_source_unchanged`/`SourceMutated`,
  `to_portable`/`from_portable`, `demux.demux(...)->{"video","audio"}` are used identically
  in tests and impl.
- **Constraint check:** demux uses `-c copy` (lossless, no loudness/codec change); portable
  doc strips `ffmpeg_*` and absolutises only at load — both honour SR-2.2; source guard
  enforces SR-4.1.
