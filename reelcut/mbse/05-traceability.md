# ReelCut — MBSE Model (05 · Traceability)

> Closes the MagicGrid loop: **Need (B1) → Requirement (W1) → Function (W2) →
> Block (W3) → Parameter (B4/W4) → Verification**. Verification method per W1:
> **I**nspection / **A**nalysis / **D**emonstration / **T**est.

## Master traceability matrix

| Need | Req | Func | Block | Param | Verify (method · test) | Status |
|---|---|---|---|---|---|---|
| N-1 | FR-1 | A-1 | B-2,B-4 | — | T · T-7 | Built |
| N-1 | FR-2 | A-2 | B-5 | — | T · T-5,T-7 | Built |
| N-1 | FR-3 | A-3 | B-3 | — | T · T-2 | Built |
| N-1 | FR-4 | A-4 | B-3 | — | T · T-1 | Built |
| N-2 | FR-5 | A-5 | B-3,B-6 | — | T · T-3,T-6 | Built |
| N-1 | FR-6 | A-6 | B-6 | MOP-2 | T · T-3,T-4 | Built |
| N-2 | FR-7 | A-7 | B-7 | MOP-6 | T · T-6 | Built |
| N-1 | FR-8 | A-6,A-8 | B-6,B-8 | — | T · T-7 | Built |
| N-2 | PR-1 | A-8 | B-8 | MOP-1 | T · T-7 | Built |
| N-2 | PR-2 | A-6 | B-6 | MOP-2 | A/T · T-3,T-4 | Built |
| N-3 | IR-1 | — | B-1,B-2 | MOP-8 | I · T-7 | Built |
| N-2 | IR-2 | A-6,A-8 | B-6,B-8 | — | T · T-7 | Built |
| N-3 | CR-1 | — | B-2 | MOP-8 | I/A · design review | Built |
| N-4 | CR-2 | — | all | MOP-9 | I · design review | Built |
| N-11 | FR-9 | A-9 | B-13,B-10 | — | T · **T-8** | Planned |
| N-12 | FR-10 | A-9 | B-10 | — | I/T · **T-8** | Planned |
| N-14 | FR-11 | A-10 | B-10,B-7 | MOP-6 | T · **T-9** | Planned |
| N-15 | FR-12 | A-11 | B-12,B-8 | MOP-5 | T · **T-10** | Planned |
| N-16 | FR-13 | A-12 | B-11,B-10 | MOP-4 | T · **T-11** | Planned |
| N-13 | PR-3 | A-4,A-11,A-12 | B-10 | MOP-3 | D · T-8…T-11 | Planned |
| N-17 | PR-4 | A-11,A-8 | B-12,B-8 | MOP-1 | T · T-9,T-10 | Planned |
| N-14/15/16 | IR-3 | A-10/11/12 | B-2 | — | T · T-7(ext) | Planned |
| N-15/16 | IR-4 | A-9/11/12 | B-13 | — | T · T-9…T-11 | Planned |
| N-12/19 | CR-3 | — | B-10 | — | I/A · design review | Planned |

**Effectiveness roll-up (B4):** MOE-2←MOP-8 · MOE-3←MOP-1,MOP-2 · MOE-6←MOP-6 ·
MOE-5←MOP-3 · MOE-1←MOP-4 · MOE-4←MOP-9/CR-3.

## Test catalogue (`../tests/`)

| ID | Test | Kind | Status |
|---|---|---|---|
| **T-1** | reorder move/swap/permutation + bad-permutation rejected | unit | Built |
| **T-2** | keep/drop + auto-renumber | unit | Built |
| **T-3** | timing-map math (cut & overlap) + gap detection | unit | Built |
| **T-4** | real FFmpeg render → A/V present, exact duration | integration | Built |
| **T-5** | segmentation grouping | unit | Built |
| **T-6** | caption remap onto re-ordered timeline | unit | Built |
| **T-7** | server E2E upload→…→export | integration | Built |
| **T-8** | demux + first-class track/clip model; T-1..T-7 still pass | unit+integ | Planned |
| **T-9** | replace audio → −16 LUFS; captions invalidated (MOP-6=0) | integration | Planned |
| **T-10** | add audio → level/mute + duck; final mix −16 LUFS | integration | Planned |
| **T-11** | image clip → orderable still, duration, renders | integration | Planned |

## Implementation increments → MBSE (Phase 3)

| # | Increment | Reqs | Blocks | Func | Test | Done when |
|---|---|---|---|---|---|---|
| 1 | Demux / track-clip model | FR-9,FR-10,CR-3,PR-3 | B-13,B-10 | A-9 | T-8 | input splits to A/V tracks **and** all existing tests pass |
| 2 | Replace audio | FR-11,PR-4 | B-10,B-7 | A-10 | T-9 | swap renders+masters −16 LUFS **and** captions flagged (MOP-6=0) |
| 3 | Add audio (mix+duck) | FR-12,PR-4 | B-12,B-8 | A-11 | T-10 | 2nd track mixes w/ level/mute, duck works, final mix −16 LUFS |
| 4 | Image clips | FR-13 | B-11,B-10 | A-12 | T-11 | still inserts as orderable item w/ duration + Ken-Burns, renders |

## Coverage & conformance
- **Coverage:** every W1 requirement traces up to a need and down to a verification.
  Built reqs FR-1..8/PR-1..2/IR-1..2/CR-1..2 are test- or inspection-verified today; Planned reqs
  carry their target tests T-8..11.
- **MagicGrid conformance:** all 8 cells populated — B1 `01` · B2 `02` · B3 `03` · B4 `06` ·
  W1 `01` · W2 `04` · W3 `03` · W4 `06`; this matrix is the cross-cell trace.
- **Mobile (N-19):** requirements/blocks/tests deferred; only **CR-3** adopted now (portable doc).
  Feasibility: `docs/superpowers/plans/2026-06-18-reelcut-mobile-port-feasibility.md`.
