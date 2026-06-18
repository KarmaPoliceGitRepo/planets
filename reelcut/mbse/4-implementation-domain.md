# Implementation Domain

> NTRS p.10 "Implementation Domain" + "Code Engineering Sets". The **scripts** under
> `reelcut/app/` implement the physical components and are the means of **verifying
> the software requirements**; **hardware requirements remain constraints**.

## Software requirement → script → verification (Code Engineering Set)
| Component req | Implementing script | Verifying test | Status |
|---|---|---|---|
| CR-1 render fold | `app/pipeline/render.py` | `tests/test_reelcut.py::TestRenderFFmpeg` (T-4) | Built |
| CR-2 loudness | `app/pipeline/master.py` | `tests/run_e2e.sh` (T-7) | Built |
| CR-3 caption re-time | `app/pipeline/captions.py` | `TestCaptions` (T-6) | Built |
| CR-4 portable model | `app/model.py` (ext) | T-8 | Planned |
| CR-5 demux | `app/pipeline/` (new) | T-8 | Planned |
| CR-6 replace-audio caption invalidation | `app/model.py`/`captions.py` | T-9 | Planned |
| CR-7 audio mix/duck | `app/pipeline/audio_mix.py` (new) | T-10 | Planned |
| CR-8 image clip synth | `app/pipeline/render.py` (ext) | T-11 | Planned |

## Hardware constraints (not implemented — verified by analysis)
- **HC-1** mobile: Android ≥ Galaxy S23 / iPhone 11 (future client) — analysis against the
  mobile feasibility brief (`docs/superpowers/plans/2026-06-18-reelcut-mobile-port-feasibility.md`).
- **HC-2** desktop: Python 3 + FFmpeg, no GPU — inspection.

## Build sequence (physical-layer increments)
1. **C-Demux + C-Model** (CR-4, CR-5) → T-8.
2. **replace-audio** (CR-6) → T-9.
3. **C-AudioMix** (CR-7) → T-10.
4. **C-ImageSynth** (CR-8) → T-11.

Each increment closes only when its test passes with real FFmpeg and the
**−16 LUFS / A/V-sync / caption-integrity** parametric constraints still hold.
