# ReelCut — MBSE Model (01 · Requirements pillar)

> MagicGrid cells **B1** (Stakeholder Needs, black box) and **W1** (System
> Requirements, white box). Conformance/notation: see `00`.

## Stakeholders
| ID | Stakeholder | Concern |
|---|---|---|
| **STK-1** | Creator (podcaster/teacher/student) | make a clean, watchable video without editing skill |
| **STK-2** | Viewer | a tight, well-ordered video with readable captions |
| **STK-3** | Privacy-conscious user | media stays on their own machine |
| **STK-4** | Maintainer / distributor | free, dependency-light, runs anywhere |
| **STK-5** | Mobile creator | edit on Android/iOS (feasibility-first) |

## §B1 — Stakeholder Needs (black box)

| ID | Stakeholder | Need | Pri | Status |
|---|---|---|---|---|
| **N-1** | STK-1 | Turn a raw recording into a clean, watchable video without editing skills. | M | Built |
| **N-2** | STK-2 | A tight, well-ordered video with readable captions. | M | Built |
| **N-3** | STK-3 | Keep media on their own machine. | M | Built |
| **N-4** | STK-4 | Free, dependency-light app that runs anywhere. | M | Built |
| *N-5…N-9* | — | *reserved* | — | — |
| **N-11** | STK-1 | Demux input into **independent audio & video tracks**, each manipulable separately. | M | Planned |
| **N-12** | STK-1 | Track/clip model is **first-class & portable/renderer-agnostic** (stable media handles; edit-decisions separated from render recipe) so the objective MoP and a mobile client are reachable without rework. | M | Planned |
| **N-13** | STK-1 | **Independent manipulation of audio & video** — graded MoP (see MOP-3). | M (threshold) / C (objective) | Planned |
| **N-14** | STK-1 | **Replace the audio track**; on replace, invalidate/flag captions & segments and offer re-transcribe. | M | Planned |
| **N-15** | STK-1 | **Add an audio track** mixed with per-track level + mute and optional duck-under-speech. | M | Planned |
| **N-16** | STK-1 | **Add image clips** (still, editable duration, optional Ken-Burns) via the existing reorder UX. | M | Planned |
| **N-17** | STK-2/3 | Audio operations **preserve −16 LUFS** and the two-stage-render / caption invariants. | M | Planned |
| **N-19** | STK-5 | ReelCut available on **Android/iOS** (feasibility-first; approach TBD). | C | Planned |

> **N-13 MoP**: *threshold* = constrained independence (replace/add audio, add images, per-track
> level/mute; spoken sub-sections stay A/V-locked for reorder); *objective* = fully independent A&V
> timelines. Formalised as **MOP-3** in `06`.

## Method & Governance (NOT stakeholder needs — Q2-a)
These govern the *process*, not the product, so they live outside the grid:
- **G-1** (was N-10) — Needs are approved before solution design; every design element traces to a need.
- **G-2** (was N-18) — `reelcut/mbse/` is the single source of truth; skill outputs are distilled into it.

## §W1 — System Requirements (white box)

Attributes: **Cell** always W1 · **St**atus {Built/Planned} · **V** {I/A/D/T} ·
**From** (need) · **Alloc** (block) · **Pri** (MoSCoW). Verified-by test in `05`.

| ID | "Shall" statement | St | V | From | Alloc | Pri | Rationale |
|---|---|---|---|---|---|---|---|
| **FR-1** | Accept one uploaded video/audio file into a local project. | Built | T | N-1 | B-2,B-4 | M | entry point |
| **FR-2** | Split media into tagged segments & sub-sections (Whisper, else silence). | Built | T | N-1 | B-5 | M | edit-by-meaning |
| **FR-3** | Keep/drop any segment or sub-section. | Built | T | N-1 | B-3 | M | core trim |
| **FR-4** | Re-order kept sub-sections (drag / swap / permutation). | Built | T | N-1 | B-3 | M | sequence control |
| **FR-5** | Present boundaries, auto-flag gaps, set transition (type+duration). | Built | T | N-2 | B-3,B-6 | S | smooth joins |
| **FR-6** | Render kept clips in chosen order with transitions. | Built | T | N-1 | B-6 | M | the output |
| **FR-7** | Produce captions (.srt) re-timed to the new sequence. | Built | T | N-2 | B-7 | M | accessibility |
| **FR-8** | Export episode.mp4, episode.mp3, episode.srt. | Built | T | N-1 | B-6,B-8 | M | deliverables |
| **PR-1** | Exported audio measures −16 LUFS ±1, TP ≤ −1 dBTP (→ MOP-1). | Built | T | N-2 | B-8 | M | loudness std |
| **PR-2** | A/V stay in sync across cuts & transitions (→ MOP-2). | Built | A/T | N-2 | B-6 | M | watchability |
| **IR-1** | UI is a browser app over HTTP on 127.0.0.1. | Built | I | N-3 | B-1,B-2 | M | local-only HMI |
| **IR-2** | Output is H.264/AAC MP4, MP3 44.1 kHz, SubRip .srt. | Built | T | N-2 | B-6,B-8 | M | portability |
| **CR-1** | All processing local; media not uploaded. | Built | I/A | N-3 | B-2 | M | privacy (→ MOE-2) |
| **CR-2** | Core depends only on Python stdlib + FFmpeg (Whisper optional). | Built | I | N-4 | all | M | dependency-light |
| **FR-9** | Demux input into independent audio & video tracks. | Planned | T | N-11 | B-13,B-10 | M | foundation |
| **FR-10** | Represent the edit as a first-class track/clip document: clips reference a track; media by stable handle; no absolute paths / embedded FFmpeg strings. | Planned | I/T | N-12 | B-10 | M | portability/mobile |
| **FR-11** | Replace the audio track; on replace, invalidate/flag captions & segments and offer re-transcribe. | Planned | T | N-14 | B-10,B-7 | M | no stale captions |
| **FR-12** | Add an audio track mixed with per-track level + mute and optional duck-under-speech. | Planned | T | N-15 | B-12 | M | music/VO |
| **FR-13** | Add image clips (still, editable duration default 4 s, Ken-Burns off by default, no intrinsic audio), orderable via existing UX. | Planned | T | N-16 | B-11,B-10 | M | photos |
| **PR-3** | Independent manipulation meets threshold (constrained) MoP; objective = full (→ MOP-3). | Planned | D | N-13 | B-10 | M (thr)/C (obj) | scoped complexity |
| **PR-4** | Replace/add audio preserves −16 LUFS on the final mix and A/V sync. | Planned | T | N-17 | B-12,B-8 | M | invariant |
| **IR-3** | Expose endpoints to replace audio, add audio (level/mute/duck), add image clip. | Planned | T | N-14/15/16 | B-2 | M | HMI |
| **IR-4** | Accept image (PNG/JPG) and audio (MP3/WAV/M4A/AAC) inputs. | Planned | T | N-15/16 | B-13 | M | media in |
| **CR-3** | Project document stays portable & renderer-agnostic (no abs paths / FFmpeg strings; stable handles; edit-decisions separated from render recipe). | Planned | I/A | N-12,N-19 | B-10 | M | mobile insurance |

> **PR-1/PR-2/PR-3/PR-4** are performance requirements *verified through* the parametric
> measures **MOP-1…MOP-3** in `06`; **CR-1** contributes to **MOE-2** (privacy).

## SysML v2 — authoritative requirement definitions (sample, rigor-critical)
```sysml
requirement def FR_10_PortableDocument {
    doc /* First-class, renderer-agnostic edit document */
    subject project : EditProject;
    attribute status : String = "Planned";
    attribute verifyBy : VerificationMethod = Inspection;  // + Test
    require constraint { project.usesAbsolutePaths == false }
    require constraint { project.embedsRenderStrings == false }
    require constraint { project.mediaReferencedBy == HandleKind::stable }
}
requirement def PR_1_Loudness {
    subject mix : FinalMix;
    attribute verifyBy : VerificationMethod = Test;
    require constraint LoudnessBudget;   // defined in 06 (Parameters)
}
satisfy FR_10_PortableDocument by TrackClipModel;   // B-10
satisfy PR_1_Loudness        by Master;             // B-8
derive  FR_9 from N_11;  derive FR_11 from N_14;  derive CR_3 from N_12;
```
