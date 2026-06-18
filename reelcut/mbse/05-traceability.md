# ReelCut — MBSE Model (05 · Traceability)

End-to-end allocation: every requirement is realised by a **block** and a
**behaviour**, and verified by a **test** in `../tests/`.

| Req | Realised by block(s) | Behaviour | Verified by test |
|---|---|---|---|
| FR-1 Upload | B-2 Server, B-4 Probe | A-1 | T-7 |
| FR-2 Segment+tag | B-5 Segmenter | A-2 | T-5, T-7 |
| FR-3 Keep/drop | B-3 Edit Model | A-3 | T-2 |
| FR-4 Re-order (3 ways) | B-3 Edit Model | A-4 | **T-1** |
| FR-5 Transitions + gap flag | B-3, B-6 | A-5 | T-3, T-6 |
| FR-6 Render order+transitions | B-6 Render | A-6 | T-3, **T-4** |
| FR-7 Re-time captions | B-7 Captions | A-7 | **T-6** |
| FR-8 Export mp4/mp3/srt | B-6, B-8 | A-6, A-8 | T-7 |
| PR-1 −16 LUFS | B-8 Master | A-8 | T-7 |
| PR-2 A/V sync (overlap math) | B-6 Render | A-6 | T-3, T-4 |
| IR-1 local HTTP UI | B-1, B-2 | — | T-7 |
| IR-2 H.264/AAC/SRT | B-6, B-8 | A-6, A-8 | T-7 |
| CR-1 local-only | B-2 (binds 127.0.0.1) | — | design review |
| CR-2 stdlib+FFmpeg | all | — | design review |

## Test catalogue (`../tests/`)

| ID | Test | Kind | File |
|---|---|---|---|
| **T-1** | reorder: move / swap / permutation + bad-permutation rejected | unit | `test_reelcut.py::TestReorder` |
| **T-2** | keep/drop + auto-renumber | unit | `test_reelcut.py::TestKeep` |
| **T-3** | timing-map math (cut & overlap) + gap auto-detection | unit | `test_reelcut.py::TestTiming` |
| **T-4** | real FFmpeg render → A/V present, exact duration | integration | `test_reelcut.py::TestRenderFFmpeg` |
| **T-5** | segmentation grouping into segments/sub-sections | unit | `test_reelcut.py::TestSegment` |
| **T-6** | caption remap onto re-ordered timeline | unit | `test_reelcut.py::TestCaptions` |
| **T-7** | server end-to-end upload→segment→reorder→transition→export | integration | `run_e2e.sh` |

Run them:

```bash
python3 tests/test_reelcut.py      # unit + ffmpeg integration (T-1..T-6)
bash    tests/run_e2e.sh           # full server E2E (T-7)
```

## Coverage statement
All functional (FR-1..8) and performance (PR-1..2) requirements have at least one
automated test. Constraints CR-1/CR-2 are satisfied by construction (server binds
`127.0.0.1`; core imports are stdlib + subprocess to FFmpeg) and confirmed by
design review rather than a runtime test.

---

# v2 — Traceability for media tracks (PLANNED)

| Req | Realised by block(s) | Behaviour | Verified by test |
|---|---|---|---|
| FR-9 Demux A/V tracks | B-13 Demux, B-10 Track/Clip | A-9 | **T-8** |
| FR-10 First-class portable doc | B-10 Track/Clip | A-9 | **T-8** |
| FR-11 Replace audio | B-10, B-7 Captions | A-10 | **T-9** |
| FR-12 Add audio (mix/duck) | B-12 Mixer/Ducker, B-8 Master | A-11 | **T-10** |
| FR-13 Add image clip | B-11 Image synth, B-10 | A-12 | **T-11** |
| PR-3 Independent-manip MoP | B-10 | A-4/A-11/A-12 | T-8…T-11 |
| PR-4 −16 LUFS on final mix | B-12, B-8 | A-11, A-8 | T-9, T-10 |
| IR-3 Media endpoints | B-2, B-10/B-11/B-12 | A-10/A-11/A-12 | T-7 (extended) |
| IR-4 Image/audio inputs | B-2, B-13 | A-9/A-11/A-12 | T-9…T-11 |
| CR-3 Portable project doc | B-10 | — | design review |
| CR-4 Needs-before-design | — (governance) | — | design review |
| CR-5 MBSE single source | — (governance) | — | design review |

## v2 test catalogue (PLANNED — added during Phase 3)

| ID | Test | Kind | Increment |
|---|---|---|---|
| **T-8** | Demux + first-class track/clip model; existing T-1..T-7 still pass | unit + integration | 1 |
| **T-9** | Replace audio → render + master −16 LUFS; captions invalidated/flagged | integration | 2 |
| **T-10** | Add audio → per-track level/mute + optional duck; final mix −16 LUFS | integration | 3 |
| **T-11** | Add image clip → orderable still, editable duration, renders in sequence | integration | 4 |

## Implementation increments → MBSE map (Phase 3)

| # | Increment | Requirements | Blocks | Behaviour | Test | Done when |
|---|---|---|---|---|---|---|
| 1 | Demux / track-clip model | FR-9, FR-10, CR-3, PR-3 | B-13, B-10 | A-9 | T-8 | input splits into A/V tracks **and** all existing tests pass |
| 2 | Replace audio | FR-11, PR-4 | B-10, B-7 | A-10 | T-9 | swap renders + masters −16 LUFS **and** captions invalidated/flagged |
| 3 | Add audio (mix + duck) | FR-12, PR-4 | B-12, B-8 | A-11 | T-10 | 2nd track mixes w/ level/mute, duck works, final mix −16 LUFS |
| 4 | Image clips | FR-13 | B-11, B-10 | A-12 | T-11 | still inserts as orderable item w/ duration + optional Ken-Burns, renders |

## Mobile (N-19) — traceability deferred
No requirement/block/test yet. The feasibility brief
(`docs/superpowers/plans/2026-06-18-reelcut-mobile-port-feasibility.md`) recommends a
cross-platform client offloading renders to the desktop engine; **CR-3** (portable project
doc) is the only thing adopted now to keep that path open. Formal mobile requirements/plan
follow once approved.
