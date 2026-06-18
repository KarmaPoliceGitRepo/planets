# ReelCut — MBSE Model (00 · Overview)

> **Model-Based Systems Engineering.** Instead of prose specs, ReelCut is
> described by a small set of inter-linked *models* — requirements, use cases,
> structure, and behaviour — each with diagrams that render on GitHub (Mermaid).
> Every model element carries an **ID** and every ID is traced to the **code**
> that realises it and the **test** that verifies it (see `05-traceability.md`).

## What ReelCut is
A **local-first** web app that turns a single uploaded talking-head video into a
finished, captioned, loudness-mastered video — by letting the user **pick**,
**re-order**, and **add transitions** between topic segments. It runs entirely on
the user's machine; the video never leaves it.

## The model viewpoints

| File | Viewpoint | SysML analogue | Renders |
|---|---|---|---|
| `01-requirements-model.md` | what it must do | Requirements diagram | needs → SR/FR/PR/CR IDs |
| `02-use-cases.md` | who uses it & how | Use-case diagram | actors, use cases UC-x |
| `03-structure.md` | what it's made of | BDD + IBD (blocks) | components B-x + ports |
| `04-behavior.md` | how it behaves | Activity / sequence / state | flows A-x, wizard states |
| `05-traceability.md` | proof it all connects | Allocation matrix | req → block → behaviour → test |

## ID scheme
- **STK-n** stakeholder · **N-n** need · **UC-n** use case
- **FR-n** functional · **PR-n** performance · **IR-n** interface · **CR-n** constraint
- **B-n** block (structural component) · **A-n** activity (behaviour)
- **T-n** test (in `../tests/`)

## How the model maps to the build
The blocks in `03-structure.md` are **one-to-one** with real modules:

```
B-1 Web UI            → app/static/ (index.html, app.js, styles.css)
B-2 Local Server      → app/server.py
B-3 Edit Model        → app/model.py
B-4 Probe             → app/pipeline/probe.py
B-5 Segmenter         → app/pipeline/segment.py
B-6 Render Engine     → app/pipeline/render.py
B-7 Caption Re-timer  → app/pipeline/captions.py
B-8 Master            → app/pipeline/master.py
B-9 FFmpeg (external) → system binary

# v2 (PLANNED — media tracks):
B-10 Track/Clip Model    → app/model.py (extended, first-class tracks/clips)
B-11 Image-clip Synth    → app/pipeline/render.py (extended)
B-12 Audio Mixer/Ducker  → app/pipeline/audio_mix.py (new) + master.py
B-13 Demux/Ingest        → app/pipeline/probe.py + ingest (extended)
```

> **v2 (PLANNED):** needs **N-10…N-19** add demuxed independent A/V tracks, replace/add
> audio, and image clips (from the 2026-06-18 `/grilling` session), plus a feasibility-first
> mobile path (N-19). `reelcut/mbse/` is the **single source of truth** (N-18). Nothing in the
> v2 sections is implemented until GATE 2 is approved.

Read in order 01 → 05. Start the product with `../run.sh`.
