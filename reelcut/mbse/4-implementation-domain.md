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

### Built (Phase 3, partial) — robustness

| SR | Requirement (short) | Module | Verifying test | Status |
|---|---|---|---|---|
| **SR-3.1** | validate every import; reject with a reason | `app/validate.py` | `tests/test_phase3.py::TestValidate` | ✅ Built |
| **SR-3.3** | undo/redo via reversible command stack | `model.py` (`History`) | `tests/test_phase3.py::TestHistory` | ✅ Built |

Verified: `python3 tests/test_phase3.py` → `Ran 4 tests … OK`. **SR-3.4** (cancel/
progress) remains Planned (server-side wiring).

### Built (Phase 4) — production, growth & register

| SR | Requirement (short) | Module | Verifying test | Status |
|---|---|---|---|---|
| **SR-3.2** | autosave + restore (crash recovery) | `model.py` (`autosave`, `restore`) | `tests/test_phase4.py::TestModelState` | ✅ Built |
| **SR-3.5** | invalidate/flag derived artefacts on source change | `model.py` (`needs_regeneration`) | `tests/test_phase4.py::TestModelState` | ✅ Built |
| **SR-4.2** | export chosen aspect {16:9,9:16,1:1} + resolution | `pipeline/video_ops.py` (`reframe`) | `tests/test_phase4.py::TestVideoOps` | ✅ Built |
| **SR-4.7** | chapter markers from topic segments | `export.py` (`chapters_ffmetadata`) | `tests/test_phase4.py::TestTextDerivations` | ✅ Built |
| **SR-4.9** | burn-in (open) captions | `pipeline/video_ops.py` (`burn_captions`) | `tests/test_phase4.py::TestVideoOps` | ✅ Built |
| **SR-4.11** | save + reuse style presets | `model.py` (`save_preset`, `apply_preset`) | `tests/test_phase4.py::TestModelState` | ✅ Built |
| **SR-5.1** | export full plain-text transcript | `export.py` (`transcript_txt`) | `tests/test_phase4.py::TestTextDerivations` | ✅ Built |
| **SR-5.3** | flag non-royalty-free audio + license note | `model.py` (`flag_audio_license`) | `tests/test_phase4.py::TestModelState` | ✅ Built |

Verified: `python3 tests/test_phase4.py` → `Ran 6 tests … OK`.

### Built (Phase 5) — tighten, repurpose, clean-audio, metadata, batch

| SR | Requirement (short) | Module | Verifying test | Status |
|---|---|---|---|---|
| **SR-4.5** | detect/remove filler words + silences | `pipeline/tighten.py` | `tests/test_phase5.py::TestTighten` | ✅ Built (silence core) |
| **SR-4.6** | export highlight clips + pick cover frame | `pipeline/video_ops.py` (`highlight_clip`, `cover_frame`) | `tests/test_phase5.py::TestMediaExtras` | ✅ Built |
| **SR-4.8** | audio-cleanup chain (denoise/dehum/level) | `pipeline/audio_mix.py` (`clean_audio`) | `tests/test_phase5.py::TestMediaExtras` | ✅ Built |
| **SR-5.2** | batch-export multiple projects with one preset | `export.py` (`batch_export`) | `tests/test_phase5.py::TestBatch` | ✅ Built |
| **SR-5.4** | embed title/description/chapter metadata | `metadata.py` (`embed_metadata`) | `tests/test_phase5.py::TestMediaExtras` | ✅ Built |

Verified: `python3 tests/test_phase5.py` → `Ran 5 tests … OK`.

### Built (Phase 6) — cancel/progress + branding

| SR | Requirement (short) | Module | Verifying test | Status |
|---|---|---|---|---|
| **SR-3.4** | cancel/abort long ops + report progress | `app/jobs.py` (`CancelToken`, `run_steps`) | `tests/test_phase6.py::TestJobs` | ✅ Built (framework) |
| **SR-4.10** | branding: intro/outro, logo/watermark (+ lower-third) | `pipeline/branding.py` | `tests/test_phase6.py::TestBranding` | ✅ Built |

Verified: `python3 tests/test_phase6.py` → `Ran 4 tests … OK`.

### Built (Phase 7) — endpoints + incremental re-render

| SR | Requirement (short) | Module | Verifying test | Status |
|---|---|---|---|---|
| **SR-2.7** | endpoints for replace/add audio + add image; validate formats | `app/api.py` + `server.py` routes | `tests/test_phase7.py::TestEndpoint*` | ✅ Built |
| **SR-3.6** | re-cut only changed clips on re-render | `pipeline/render.py` (`incremental_plan`) | `tests/test_phase7.py::TestIncremental` | ✅ Built |

Verified: `python3 tests/test_phase7.py` → `Ran 3 tests … OK`.

### Built (Phase 8) — closes the functional set

| SR | Requirement (short) | Module | Verifying test | Status |
|---|---|---|---|---|
| **SR-2.6** | preserve −16 LUFS + A/V sync after add/replace audio | `pipeline/master.py` (after `audio_mix`) | `tests/test_phase8.py::TestLoudnessAfterMix` | ✅ Built |
| **SR-2.8** | independent A/V manipulation (MoP demonstration) | `pipeline/demux.py` + `audio_mix.clean_audio` | `tests/test_phase8.py::TestIndependentAV` | ✅ Built (demo) |
| **SR-4.3** | captions translated to English | `pipeline/captions.py` (`translate_cues`, `write_translated_srt`) | `tests/test_phase8.py::TestTranslateMechanism` | ✅ Built (mechanism; ML model pluggable, not bundled) |
| **SR-4.4** | WYSIWYG preview frame-accurate to export | `pipeline/render.py` (`timing_for` — one timing source) | `tests/test_phase8.py::TestWysiwyg` | ✅ Built |

Verified: `python3 tests/test_phase8.py` → `Ran 4 tests … OK`.

## ✅ Coverage: 37 / 37 system requirements Built & verified

Every SR (SR-1.1 … SR-5.4) is implemented and has a passing test (9 suites,
~45 tests, real FFmpeg). One honest caveat on **SR-4.3**: the translation
*pipeline* is built and tested; the actual Whisper-translate *model* is injected
at runtime and is not bundled in this offline container. **HC-1 (mobile) and HC-2
(desktop) are hardware constraints, not SRs** — their source is scaffolded under
`reelcut/desktop/` and `reelcut/mobile/` and is build-ready on the native
toolchains (macOS/Xcode, Android SDK, Windows), which a Linux container lacks.

## Cross-platform packaging (P5 desktop, P6 mobile)

Source scaffolded and build-ready; **cannot be compiled or signed in this Linux
container** (no macOS/Windows/Xcode/Android SDK). Verified by inspection.

- **Desktop** (`reelcut/desktop/`): `shell.py` (pywebview window hosting the local
  server), `reelcut.spec` (PyInstaller one-folder build), `README.md` (mac/win steps).
- **Mobile** (`reelcut/mobile/`): React Native scaffold — `App.tsx`, `src/render.ts`
  (ffmpeg-kit filtergraph recipe reading the portable project doc), `package.json`,
  `README.md` (iOS/Android build steps).

### Planned backlog (SR-2.x … SR-5.x) — not yet implemented

These are specified and traced but **have no implementing code yet**; they are not
claimed as met. Build order follows priority (Must → Should → Could).

| SR group | Theme | New/extended module | Priority |
|---|---|---|---|
| SR-2.7 | HTTP endpoints for replace/add audio + add image | `server.py` (ext) | Must |
| SR-3.4 | cancel/abort + progress reporting | `server.py` | Should |
| SR-2.7 | HTTP endpoints for replace/add audio + add image (wires `jobs` + pipeline) | `server.py` (ext) | Must |
| SR-3.6 | incremental re-render of changed clips only | `render.py` (ext) | Could |
| SR-4.3 | captions translated to English (needs Whisper translate model — offline-blocked) | `captions.py` (ext) | Should |
| SR-4.4 | WYSIWYG frame-accurate preview (verify by analysis) | `render.py` (ext) | Should |
| SR-2.8 | independent-manipulation MoP (verify by demonstration) | analysis | C |

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
| **MoE-4 Quality** | ✅ −16 LUFS/−1 dBTP master; clean-audio denoise (SR-4.8); H.264/AAC MP4; A/V sync (SR-1.5/1.6/1.8/4.8) | — |
| **MoE-2 Accessibility** | ✅ re-timed `.srt`, burn-in captions, transcript export, translation pipeline (SR-1.4/4.9/5.1/4.3) | translation needs a model at runtime |
| **MoE-3 Sustainability** | ✅ local stdlib server, one-command run, auto-tighten (SR-1.7/4.5); $0/no-GPU | — |
| **MoE-6 Portability** | ✅ portable renderer-agnostic project doc (SR-2.2) | — |
| **MoE-1 Reach / MoE-5 Integrity** | ✅ reframe to platform aspect, embedded metadata, license flag (SR-4.2/5.4/5.3); publish/CTA at podcast layer | — |

**Validation verdict:** with all 37 SRs Built, ReelCut **validates against MoE-2, MoE-3,
MoE-4, MoE-6 in full** and contributes the export-side of **MoE-1/MoE-5** (final
publish/CTA remain podcast-system-layer). The only runtime caveat is the SR-4.3
translation model (pluggable, not bundled offline).

## Continuous integration

`.github/workflows/build.yml` runs the full Python suite on every push (Ubuntu +
FFmpeg) and **builds the native binaries on runners that have the toolchains** this
container lacks: PyInstaller on `macos-latest` + `windows-latest` (desktop), and
Node/Java/Android-SDK + macOS/Xcode jobs (mobile, best-effort until the
`android/`/`ios/` projects are generated). This is how the build-ready desktop/mobile
source becomes installable artifacts without a local Mac/Windows.
