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
