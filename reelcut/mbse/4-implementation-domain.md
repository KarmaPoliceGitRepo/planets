# Implementation Domain

> NTRS p.10 "Implementation Domain" + "Code Engineering Sets". The **modules** under
> `reelcut/app/` implement the physical components and are the means of **verifying
> the software requirements**; **hardware requirements remain constraints**. This page
> maps every **system requirement (SR)** to the module that implements it and the test
> that verifies it, and states the **true Built/Planned status** (no requirement is
> marked met unless a test demonstrates it).

## Modules (the "classifiers") and their responsibility

| Module | Responsibility |
|---|---|
| `app/pipeline/probe.py` | Read media facts (duration, A/V presence) via ffprobe — input to segment/render. |
| `app/pipeline/segment.py` | Split a clip into tagged **segments + sub-sections** (Whisper, or ffmpeg silencedetect fallback). |
| `app/model.py` | The edit project: keep/drop, reorder (move/swap/permutation), transitions, JSON load/save. |
| `app/pipeline/render.py` | Reorder-aware two-stage render: extract kept clips, join with gap-aware transitions, A/V sync; emits the timing map. |
| `app/pipeline/captions.py` | Re-time captions (`.srt`) onto the new sequence from the timing map. |
| `app/pipeline/master.py` | Two-pass loudness normalise to −16 LUFS / −1 dBTP; export `episode.mp3` (44.1 kHz) and `episode.mp4`. |
| `app/server.py` | Local HMI: binds `127.0.0.1:8770`, upload/segment/reorder/render endpoints; media never leaves the machine. |

## SR → module → test → status (Code Engineering Set)

### Built and verified (SR-1.x) — 12 unit tests + e2e, all green

| SR | Requirement (short) | Module | Verifying test | Status |
|---|---|---|---|---|
| **SR-1.1** | split into tagged segments/sub-sections | `segment.py` | `TestSegment.test_grouping_shapes` | ✅ Built |
| **SR-1.2** | keep/drop + reorder kept sub-sections | `model.py` | `TestReorder` (move/swap/permutation), `TestKeep` | ✅ Built |
| **SR-1.3** | render chosen order with transitions | `render.py` | `TestRenderFFmpeg.test_render_has_av_and_duration` | ✅ Built |
| **SR-1.4** | re-time captions to the new sequence | `captions.py` | `TestCaptions.test_remap_to_new_order` | ✅ Built |
| **SR-1.5** | audio −16 LUFS ±1, TP ≤ −1 dBTP | `master.py` | `tests/run_e2e.sh` + in-code pass-gate (−17..−15) | ✅ Built |
| **SR-1.6** | A/V stay in sync across cuts/transitions | `render.py` | `TestTiming` (cut offsets / crossfade / gap) | ✅ Built |
| **SR-1.7** | HMI on 127.0.0.1; no media upload | `server.py` | Inspection: binds `127.0.0.1`, no network egress | ✅ Built |
| **SR-1.8** | output H.264/AAC MP4, MP3 44.1 kHz, SubRip | `render.py` + `master.py` + `captions.py` | `TestRenderFFmpeg` (codecs), `run_e2e.sh` | ✅ Built |

All eight **Must** requirements of the baseline are implemented and pass with real
FFmpeg (`python3 tests/test_reelcut.py` → `Ran 12 tests … OK`).

### Built (Phase 1) — portable doc + non-destructive + demux

| SR | Requirement (short) | Module | Verifying test | Status |
|---|---|---|---|---|
| **SR-4.1** | original read-only; edits non-destructive | `model.py` (`source_digest`, `assert_source_unchanged`) | `tests/test_phase1.py::TestNonDestructive` | ✅ Built |
| **SR-2.2** | portable, renderer-agnostic project doc | `model.py` (`to_portable`, `from_portable`) | `tests/test_phase1.py::TestPortableDoc` | ✅ Built |
| **SR-2.1** | demux into independent A/V tracks | `pipeline/demux.py` | `tests/test_phase1.py::TestDemux` | ✅ Built |

Verified: `python3 tests/test_phase1.py` → `Ran 3 tests … OK`. Plan:
`docs/superpowers/plans/2026-06-19-reelcut-cross-platform-build.md`.

### Built (Phase 2) — media operations

| SR | Requirement (short) | Module | Verifying test | Status |
|---|---|---|---|---|
| **SR-2.3** | replace audio; flag captions stale; offer re-transcribe | `pipeline/audio_mix.py` (`replace_audio`), `model.py` (`mark_captions_stale`) | `tests/test_phase2.py::TestMedia::test_replace_audio`, `::TestCaptionsStale` | ✅ Built |
| **SR-2.4** | add audio with level/mute + optional duck-under-speech | `pipeline/audio_mix.py` (`add_audio`) | `tests/test_phase2.py::TestMedia::test_add_audio_mix` | ✅ Built |
| **SR-2.5** | add image clips (still, editable duration, no intrinsic audio) | `pipeline/audio_mix.py` (`image_clip`) | `tests/test_phase2.py::TestMedia::test_image_clip` | ✅ Built |

Verified: `python3 tests/test_phase2.py` → `Ran 4 tests … OK`. **SR-2.6** (preserve
−16 LUFS after mix) is met by re-running `master.py` on the mixed output (existing
SR-1.5 path); **SR-2.7** (HTTP endpoints for these ops) remains Planned.

### Planned backlog (SR-2.x … SR-5.x) — not yet implemented

These are specified and traced but **have no implementing code yet**; they are not
claimed as met. Build order follows priority (Must → Should → Could).

| SR group | Theme | New/extended module | Priority |
|---|---|---|---|
| SR-2.7 | HTTP endpoints for replace/add audio + add image | `server.py` (ext) | Must |
| SR-3.1–3.5 | validate input; autosave/restore; undo/redo; cancel+progress; invalidate-on-source-change | `server.py`, `model.py` (command stack) | Should |
| SR-4.2–4.9 | aspect/preset export; translation; WYSIWYG preview; tighten (filler/silence); highlights+cover; clean audio; burn-in captions | `render.py`, `captions.py`, `segment.py` (ext) | Should |
| SR-3.6, SR-4.10/4.11, SR-2.8 | incremental re-render; branding; presets; independent-manip MoP | various (ext) | Could |
| SR-5.1–5.4 | transcript export; batch export; license flag; embedded metadata | `captions.py`, `server.py`, `master.py` (ext) | S/C |

## Build sequence (physical-layer increments)

1. **Demux + portable model** (SR-2.1, SR-2.2, SR-4.1) → new T-8; unlocks everything else.
2. **Replace/add audio + image clips** (SR-2.3–2.7) preserving −16 LUFS (SR-2.6) → T-9/T-10/T-11.
3. **Robustness** (SR-3.1–3.5: validate, autosave, undo/redo, cancel) → T-12…T-15.
4. **Production/growth** (SR-4.x) and **register** (SR-5.x) per priority → T-17…T-31.

Each increment closes only when its test passes with real FFmpeg and the
**−16 LUFS / A/V-sync / caption-integrity** parametric constraints still hold.

## Hardware constraints (not implemented — verified by analysis)

- **HC-1** mobile: Android ≥ Galaxy S23 / iPhone 11 (future client) — analysis against the
  mobile feasibility brief (`docs/superpowers/plans/2026-06-18-reelcut-mobile-port-feasibility.md`).
- **HC-2** desktop: Python 3 + FFmpeg, no GPU — inspection (`run.sh`, stdlib-only server).

## Validation against the podcast system's MoE

ReelCut is the implementation-layer SoI; its job is to make the podcast system's
**Measures of Effectiveness** ([`../../podcast-the-missing-link/01-systems-engineering/00-concept-and-moe.md`](../../podcast-the-missing-link/01-systems-engineering/00-concept-and-moe.md))
achievable. Current contribution of the **Built** scope:

| Podcast MoE | ReelCut contribution (Built) | Gap (Planned) |
|---|---|---|
| **MoE-4 Quality** | ✅ −16 LUFS/−1 dBTP master; H.264/AAC MP4; A/V sync (SR-1.5/1.6/1.8) | denoise/clarity SR-4.8 |
| **MoE-2 Accessibility** | ✅ re-timed `.srt` captions on the edit (SR-1.4/1.8) | transcript SR-5.1, translation SR-4.3, burn-in SR-4.9 |
| **MoE-3 Sustainability** | ✅ local stdlib server, one-command `run.sh`, FFmpeg-only — $0 (SR-1.7) | tighten/effort SR-4.5 |
| **MoE-6 Portability** | ◐ JSON project doc saved by `model.py` (partial SR-2.2) | fully renderer-agnostic doc SR-2.2 |
| **MoE-1 Reach / MoE-5 Integrity** | (podcast-system level — publish/licence; ReelCut feeds exports) | metadata SR-5.4, license flag SR-5.3 |

**Validation verdict:** the Built ReelCut baseline **validates against MoE-3 and MoE-4
in full** and **MoE-2/MoE-6 in part**; MoE-1/MoE-5 are realised above ReelCut at the
podcast-system layer. Remaining MoE coverage is bounded by the Planned backlog above.
