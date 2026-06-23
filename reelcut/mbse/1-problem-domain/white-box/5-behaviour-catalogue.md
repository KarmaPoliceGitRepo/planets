# Logical · White Box · Behavior — Behaviour Catalogue (all flows)

> Produced with the **`brainstorming`** skill (mandatory for behaviour-model scope
> — see CLAUDE.md rule). For **every stage** the catalogue enumerates **all
> possible behaviours**: **Nominal**, **Alternate**, **Exception**, **Edge**. These
> are the source for the activity model (`2`), the interaction model (`6`) and the
> state model (`7`). Like behaviours are then **consolidated** into reusable
> behavioural elements (**CB-**), which is itself a brainstormed step.

## Per-stage behaviours (B-<stage>.<n>)

### Ingest (F-1, F-2)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-IN.1 | Nominal | Accept media, probe, demux into independent A/V tracks. | F-1,F-2 |
| B-IN.2 | Alternate | Audio-only input → no video track → require image/background (podcast mode). | CB-2 |
| B-IN.3 | Alternate | Video-only (no audio) → skip ASR; no captions. | F-3 |
| B-IN.4 | Exception | Unsupported / corrupt media → reject with reason. | CB-1 |
| B-IN.5 | Exception | Probe fails / times out → reject, surface error. | CB-1, CB-3 |
| B-IN.6 | Edge | Very large / long file → chunked handling; resource warning. | — |
| B-IN.7 | Alternate | Re-upload / replace source → invalidate downstream artifacts. | CB-4 |

### Segment & tag (F-3, F-4)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-SG.1 | Nominal | ASR transcribe → segment & tag by topic. | F-3,F-4 |
| B-SG.2 | Alternate | No Whisper / no speech → silence-detect fallback segmentation. | F-4 |
| B-SG.3 | Alternate | Multi-speaker → speaker-aware boundaries (flagged). | — |
| B-SG.4 | Alternate | Manual split / merge of a segment. | F-4 |
| B-SG.5 | Exception | ASR error → fallback + flag. | CB-3 |
| B-SG.6 | Edge | Single long monologue → time-based sub-section split. | F-4 |
| B-SG.7 | Alternate | Re-segment after source/audio change. | CB-4 |

### Curate — keep / drop (F-5)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-CU.1 | Nominal | Toggle keep/drop per sub-section. | F-5 |
| B-CU.2 | Alternate | Preview a sub-section before deciding. | — |
| B-CU.3 | Alternate | Undo a drop. | CB-6 |
| B-CU.4 | Exception | Keep-none → block export (precondition guard). | CB-2 |
| B-CU.5 | Edge | Keep-all (no trimming). | — |

### Sequence — order (F-6)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-SQ.1 | Nominal | Reorder via drag / swap / renumber-permutation. | F-6 |
| B-SQ.2 | Alternate | Revert to original order. | CB-6 |
| B-SQ.3 | Alternate | Reorder creates a jarring jump → auto-flag boundary for a transition. | F-7 |
| B-SQ.4 | Edge | Single kept clip → ordering is a no-op. | — |

### Transition (F-7)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-TR.1 | Nominal | Gap / jump detected → suggest & set per-boundary transition. | F-7 |
| B-TR.2 | Alternate | Adjacent clips, no gap → straight cut (no transition). | — |
| B-TR.3 | Exception | Transition longer than the shorter clip → clamp duration. | — |
| B-TR.4 | Edge | First / last boundary → fade-in / fade-out option. | — |

### Re-media — replace audio (F-11)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-RA.1 | Nominal | Replace whole-edit audio. | F-11 |
| B-RA.2 | Consequence | Invalidate captions + segments derived from old audio; offer re-transcribe. | CB-4 |
| B-RA.3 | Alternate | New audio shorter than video → pad / hold policy. | — |
| B-RA.4 | Alternate | New audio longer → trim / extend last clip. | — |
| B-RA.5 | Exception | Unsupported audio format → reject. | CB-1 |

### Re-media — add audio / mix (F-12)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-AA.1 | Nominal | Add track; per-track level / mute. | F-12 |
| B-AA.2 | Alternate | One-tap duck-under-speech. | F-12 |
| B-AA.3 | Exception | Duck requested but no speech track → warn / disable. | CB-2 |
| B-AA.4 | Alternate | Add multiple tracks. | F-12 |
| B-AA.5 | Edge | Mix would clip → auto-attenuate to preserve −16 LUFS. | MOP-1 |
| B-AA.6 | Alternate | Remove an added track. | CB-6 |

### Re-media — add image (F-13)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-IM.1 | Nominal | Add still as an orderable clip, default 4 s. | F-13 |
| B-IM.2 | Alternate | Edit duration; toggle Ken-Burns. | — |
| B-IM.3 | Alternate | Image plays over independent audio (no intrinsic audio). | — |
| B-IM.4 | Exception | Unsupported image format → reject. | CB-1 |
| B-IM.5 | Edge | Image inserted during a gap vs as its own clip. | — |
| B-IM.6 | Alternate | Remove image clip. | CB-6 |

### Render (F-8)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-RN.1 | Nominal | Two-stage cut + join with transitions. | F-8 |
| B-RN.2 | Exception | FFmpeg error → retry once, else abort with log. | CB-3 |
| B-RN.3 | Alternate | Cancel / abort mid-render. | CB-3 |
| B-RN.4 | Alternate | Re-render after an edit → incremental (only changed clips). | CB-5 |
| B-RN.5 | Behaviour | Progress reporting to the HMI. | F-18 |
| B-RN.6 | Edge | Single clip → passthrough (no join). | — |

### Caption (F-9)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-CP.1 | Nominal | Re-time cues to the new order. | F-9 |
| B-CP.2 | Alternate | No transcript → skip captions. | — |
| B-CP.3 | Alternate | Manually edit caption text / timing. | — |
| B-CP.4 | Consequence | Invalidate on audio replace → re-transcribe. | CB-4 |
| B-CP.5 | Edge | Dropped sub-section → drop its cues. | F-9 |

### Master (F-10)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-MS.1 | Nominal | Two-pass loudnorm −16 LUFS; report PASS/FAIL. | F-10, MOP-1 |
| B-MS.2 | Exception | Out-of-spec → re-pass / flag. | CB-3 |
| B-MS.3 | Alternate | Export subset (mp3-only / srt-only). | — |
| B-MS.4 | Edge | Very quiet / loud source → gain limits. | — |

### Deliver (HMI + filesystem)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-DL.1 | Nominal | Write mp4/mp3/srt to the local render dir. | SR-1.8 |
| B-DL.2 | Alternate | Choose save location / open folder. | — |
| B-DL.3 | Guard | Never auto-publish; egress only on explicit action. | MOE-2 |
| B-DL.4 | Exception | Disk full / write error → report. | CB-3 |

### Session — cross-cutting (SN-8)
| ID | Class | Behaviour | Ties |
|---|---|---|---|
| B-SE.1 | Nominal | Autosave the project doc periodically and on each edit. | CB-7 |
| B-SE.2 | Recovery | Restore / resume after close or crash. | CB-7 |
| B-SE.3 | Nominal | Undo / redo across edit operations. | CB-6 |
| B-SE.4 | Nominal | Cancel / abort any long operation. | CB-3 |
| B-SE.5 | Nominal | Surface every error to the HMI with reason + recovery action. | F-18 |
| B-SE.6 | Alternate | Export / import portable doc for mobile resume. | I-Project |

## Consolidated reusable behaviours (CB-) — the brainstormed consolidation

| CB | Reusable behaviour | Absorbs | New function | Derives requirement |
|---|---|---|---|---|
| **CB-1** | **Validate-and-Reject** — validate any imported artifact against accepted formats; reject with a reason. | B-IN.4/5, B-RA.5, B-IM.4 | **F-15** Validate input | SR-3.1 |
| **CB-2** | **Guard-Precondition** — block an action whose precondition fails (keep ≥ 1; speech track for duck; image for audio-only). | B-CU.4, B-AA.3, B-IN.2 | (in F-5/F-12) | SR-1.2, SR-2.4 |
| **CB-3** | **Retry-or-Abort** — long ops retry once on transient error, support user cancel, always log. | B-RN.2/3, B-MS.2, B-DL.4, B-SE.4 | **F-19** Cancel/abort op | SR-3.4 |
| **CB-4** | **Invalidate-Derived-on-Source-Change** — when a source changes, invalidate/flag derived artifacts and offer regeneration. | B-IN.7, B-SG.7, B-RA.2, B-CP.4 | (in F-11/F-4) | SR-2.3, SR-3.5 |
| **CB-5** | **Incremental-Re-render** — on edit after a render, re-cut only changed clips; reuse cached clips. | B-RN.4 | **F-20** Incremental render | SR-3.6 |
| **CB-6** | **Undo/Redo** — every edit operation is reversible via a command stack. | B-CU.3, B-SQ.2, B-AA.6, B-IM.6, B-SE.3 | **F-17** Undo/redo | SR-3.3 |
| **CB-7** | **Autosave/Restore** — persist the project doc continuously; restore on resume/crash. | B-SE.1/2 | **F-16** Manage session | SR-3.2 |

> The new functions **F-15…F-20** and requirements **SR-3.1…SR-3.6** introduced by
> this brainstorm are recorded in `2-functional-analysis.md` and
> `1-system-requirements.md`; the flows are visualised in `6-interaction-model.md`
> (sequences) and `7-state-model.md` (end-to-end state machine).
</content>
</invoke>
