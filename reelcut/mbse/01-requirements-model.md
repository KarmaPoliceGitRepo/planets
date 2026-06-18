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

---

# v2 — Media tracks, replace/add audio, image clips, mobile (PLANNED)

> Source: `/grilling` session 2026-06-18 + parallel mobile feasibility brief
> (`docs/superpowers/plans/2026-06-18-reelcut-mobile-port-feasibility.md`). Needs
> N-10…N-19 drive the requirements below. Everything here is **design only** until
> GATE 2 is approved; nothing is implemented yet.

## v2 stakeholders & needs

| ID | Stakeholder | Need (shall) | MoP / note |
|---|---|---|---|
| STK-1 | Creator | **N-10** Needs are approved **before** solution design; every design element traces to a need. | governance |
| STK-1 | Creator | **N-11** Demux input into **independent audio & video tracks**, each manipulable separately. | foundation |
| STK-1 | Creator | **N-12** The track/clip model is **first-class and portable/renderer-agnostic** (no absolute paths, no embedded FFmpeg strings, media by stable handles, edit-decisions separated from render recipe) so the objective MoP and a future mobile client are reachable without rework. | enabler |
| STK-1 | Creator | **N-13** Allow **independent manipulation of audio & video.** | **MoP threshold:** constrained — replace/add audio, add images, per-track level/mute; spoken sub-sections stay **A/V-locked** for reorder. **MoP objective:** fully independent A&V timelines. |
| STK-1 | Creator | **N-14** **Replace the whole audio track**; on replace, **invalidate/flag** captions & segments derived from the old audio and offer re-transcribe. | |
| STK-1 | Creator | **N-15** **Add an audio track** mixed with per-track level + mute and an **optional one-tap duck under speech** (requires a speech track present). | |
| STK-1 | Creator | **N-16** **Add image clips** to the video track: synthesised stills, editable duration (default 4 s), Ken-Burns **off by default** (toggle), no intrinsic audio (independent audio plays under), inserted via the existing reorder UX. | |
| STK-2/STK-3 | Viewer / Privacy | **N-17** All audio operations **preserve −16 LUFS** (master the final mix) and the two-stage-render / caption invariants. | constraint |
| STK-4 | Maintainer | **N-18** `reelcut/mbse/` is the **single source of truth**; skill outputs are transient drafts distilled into it. | governance |
| **STK-5** | **Mobile creator** | **N-19** ReelCut is available on **Android/iOS** (feasibility-first; approach decided after the brief). | deferred |

## v2 requirements

| ID | Type | "Shall" statement | From need | Verify |
|---|---|---|---|---|
| **FR-9** | Functional | The system **shall** demux an uploaded file into independent audio and video tracks. | N-11 | T-8 |
| **FR-10** | Functional | The system **shall** represent the edit as a first-class track/clip document where every clip references a track, media is referenced by stable handle, and no absolute paths or FFmpeg command strings are embedded. | N-12 | T-8 |
| **FR-11** | Functional | The system **shall** let the user replace the audio track, and on replace **shall** invalidate/flag captions & segments and offer re-transcribe. | N-14 | T-9 |
| **FR-12** | Functional | The system **shall** let the user add an audio track mixed with per-track level + mute and an optional duck-under-speech. | N-15 | T-10 |
| **FR-13** | Functional | The system **shall** let the user add image clips (still, editable duration default 4 s, optional Ken-Burns off by default, no intrinsic audio), orderable via the existing reorder UX. | N-16 | T-11 |
| **PR-3** | Performance | Independent manipulation **shall** meet **threshold** (constrained: A/V-locked spoken sub-sections + replace/add audio + images + per-track level/mute); **objective** = fully independent A & V timelines. | N-13 | T-8…T-11 |
| **PR-4** | Performance | Replacing or adding audio **shall** preserve −16 LUFS on the final mix and A/V sync. | N-17 | T-9, T-10 |
| **IR-3** | Interface | The API **shall** expose endpoints to replace audio, add an audio track (level/mute/duck), and add an image clip. | N-14/15/16 | T-7 |
| **IR-4** | Interface | The system **shall** accept image (PNG/JPG) and audio (MP3/WAV/M4A/AAC) inputs as track/clip media. | N-15/16 | T-9…T-11 |
| **CR-3** | Constraint | The project document **shall** stay portable & renderer-agnostic (no absolute paths / embedded FFmpeg strings; media by stable handles; edit-decisions separated from the render recipe) to keep the objective MoP and mobile reachable. | N-12/N-19 | design review |
| **CR-4** | Constraint | Needs **shall** be approved before solution design (governance). | N-10 | design review |
| **CR-5** | Constraint | `reelcut/mbse/` **shall** be the single source of truth for design. | N-18 | design review |

> **N-19 (mobile)** has **no FR yet** — requirements are deferred pending the feasibility brief.
> Brief recommendation: a **cross-platform client (Flutter/RN) that offloads heavy renders to the
> desktop/companion engine over the LAN**; full on-device rendering is not near-term (FFmpegKit
> retired 2025; H.264 encoder GPL/patent exposure). This is *why* **CR-3** (portable project doc)
> is adopted now — it is the cheap insurance that makes the future mobile client possible.

## v2 requirement diagram (additions)

```mermaid
requirementDiagram
  requirement N12 { id: "N-12" text: "First-class, portable, renderer-agnostic track/clip model" }
  requirement FR_9  { id: "FR-9"  text: "Demux into independent A/V tracks" }
  requirement FR_10 { id: "FR-10" text: "First-class portable track/clip document" }
  requirement FR_11 { id: "FR-11" text: "Replace audio (+ invalidate captions)" }
  requirement FR_12 { id: "FR-12" text: "Add audio (mix + level/mute + duck)" }
  requirement FR_13 { id: "FR-13" text: "Add image clips" }
  requirement PR_3  { id: "PR-3"  text: "Independent-manipulation MoP (threshold/objective)" }
  requirement PR_4  { id: "PR-4"  text: "Preserve -16 LUFS on final mix" }
  requirement CR_3  { id: "CR-3"  text: "Portable / renderer-agnostic project doc" }

  FR_9  - derives -> FR_10
  FR_10 - derives -> FR_11
  FR_10 - derives -> FR_12
  FR_10 - derives -> FR_13
  PR_3  - refines -> FR_10
  PR_4  - refines -> FR_11
  PR_4  - refines -> FR_12
  CR_3  - refines -> FR_10
  N12   - derives -> CR_3
```
