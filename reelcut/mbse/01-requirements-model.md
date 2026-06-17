# ReelCut — MBSE Model (01 · Requirements)

## Stakeholders & needs

| ID | Stakeholder | Need (ID) |
|---|---|---|
| STK-1 | **Creator** (podcaster/teacher/student) | N-1 turn a raw recording into a clean, watchable video without editing skills |
| STK-2 | **Viewer** | N-2 a tight, well-ordered video with readable captions |
| STK-3 | **Privacy-conscious user** | N-3 keep media on their own machine |
| STK-4 | **Maintainer / distributor** | N-4 a free, dependency-light app that runs anywhere |

## Requirements diagram

```mermaid
requirementDiagram
  requirement FR_1 { id: "FR-1" text: "Upload a single video/audio file" }
  requirement FR_2 { id: "FR-2" text: "Auto-split into tagged segments & sub-sections" }
  requirement FR_3 { id: "FR-3" text: "Keep/drop segments and sub-sections" }
  requirement FR_4 { id: "FR-4" text: "Re-order sub-sections (drag, swap, renumber)" }
  requirement FR_5 { id: "FR-5" text: "Choose transitions per boundary; flag gaps" }
  requirement FR_6 { id: "FR-6" text: "Render to one video in chosen order+transitions" }
  requirement FR_7 { id: "FR-7" text: "Re-time captions for the new sequence" }
  requirement FR_8 { id: "FR-8" text: "Master audio and export MP4+MP3+SRT" }
  requirement PR_1 { id: "PR-1" text: "Output loudness -16 LUFS +/-1, TP <= -1 dBTP" }
  requirement PR_2 { id: "PR-2" text: "A/V stay in sync across cuts & transitions" }
  requirement CR_1 { id: "CR-1" text: "Runs locally; media never uploaded" }
  requirement CR_2 { id: "CR-2" text: "Free; core needs only Python + FFmpeg" }

  element Viewer { type: "stakeholder" }
  FR_2 - derives -> FR_3
  FR_3 - derives -> FR_4
  FR_4 - derives -> FR_6
  FR_5 - derives -> FR_6
  FR_6 - derives -> FR_7
  FR_6 - derives -> FR_8
  PR_2 - refines -> FR_6
  PR_1 - refines -> FR_8
```

## Requirement table (the authoritative list)

| ID | Type | "Shall" statement | Verify |
|---|---|---|---|
| **FR-1** | Functional | The system **shall** accept one uploaded video or audio file and store it in a local project. | T-7 |
| **FR-2** | Functional | The system **shall** split the media into segments and sub-sections, each with a tag, using Whisper if available else a silence-based fallback. | T-5, T-7 |
| **FR-3** | Functional | The system **shall** let the user keep or drop any segment or sub-section. | T-2 |
| **FR-4** | Functional | The system **shall** let the user re-order kept sub-sections by (a) drag-and-drop, (b) swapping two positions, (c) entering a new order as a permutation. | T-1 |
| **FR-5** | Functional | The system **shall** present every output boundary, auto-flag gap/reorder-jump boundaries, and let the user set a transition (type + duration) on any boundary. | T-3, T-6 |
| **FR-6** | Functional | The system **shall** render the kept clips in the chosen order, applying the chosen transitions. | T-3, T-4 |
| **FR-7** | Functional | The system **shall** produce captions (.srt) re-timed to the new output sequence. | T-6 |
| **FR-8** | Functional | The system **shall** export `episode.mp4`, `episode.mp3`, and `episode.srt`. | T-7 |
| **PR-1** | Performance | Exported audio **shall** measure −16 LUFS ±1 with true peak ≤ −1 dBTP. | T-7 |
| **PR-2** | Performance | Audio and video **shall** remain in sync across all cuts and transitions (overlap-adjusted timing). | T-3, T-4 |
| **IR-1** | Interface | The UI **shall** be a browser app served over HTTP on `127.0.0.1`. | T-7 |
| **IR-2** | Interface | Output **shall** be H.264/AAC MP4, MP3 (44.1 kHz), and SubRip `.srt`. | T-7 |
| **CR-1** | Constraint | All processing **shall** run locally; media **shall not** be uploaded to any server. | design review |
| **CR-2** | Constraint | The core **shall** depend only on Python 3 stdlib + FFmpeg (Whisper optional). | design review |
