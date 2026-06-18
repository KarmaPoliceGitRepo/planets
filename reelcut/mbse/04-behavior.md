# ReelCut — MBSE Model (04 · Behaviour)

## Wizard state machine

```mermaid
stateDiagram-v2
  [*] --> Upload
  Upload --> Segments : file probed (A-1)
  Segments --> Segments : keep/drop (A-3)
  Segments --> Order : Next
  Order --> Order : drag / swap / renumber (A-4)
  Order --> Transitions : Next
  Transitions --> Transitions : set transition / apply-to-gaps (A-5)
  Transitions --> Export : Next
  Export --> Done : render+caption+master ok (A-6)
  Order --> Segments : Back
  Transitions --> Order : Back
  Done --> [*]
```

## A-6 Export — activity diagram (the critical flow)

```mermaid
flowchart TD
  start([Build my video]) --> plan[build_plan: kept clips sorted by order]
  plan --> tm[timing_map: overlap-adjusted new_start per clip]
  tm --> cut[Stage 1: cut+normalise each clip to its own file]
  cut --> dec{>1 clip?}
  dec -- no --> single[copy single clip]
  dec -- yes --> join[Stage 2: fold clips]
  join --> b{boundary type?}
  b -- cut --> concat[concat video+audio]
  b -- transition --> xf[xfade video + acrossfade audio at offset=running-t]
  concat --> nextv
  xf --> nextv[update running duration]
  nextv --> more{more clips?}
  more -- yes --> b
  more -- no --> enc[encode edit.mp4]
  single --> capn
  enc --> capn[A-7 re-time captions onto new_start]
  capn --> mas[A-8 two-pass loudnorm -16 LUFS -> mp3 + mp4]
  mas --> done([episode.mp4 / .mp3 / .srt])
```

## A-6 sequence diagram (blocks collaborating)

```mermaid
sequenceDiagram
  participant UI as B-1 UI
  participant SV as B-2 Server
  participant RN as B-6 Render
  participant CP as B-7 Captions
  participant MS as B-8 Master
  participant FF as B-9 FFmpeg
  UI->>SV: POST /api/render {id}
  SV->>RN: render(project)
  RN->>FF: cut clip_i (stage 1) ×N
  RN->>FF: xfade/acrossfade/concat join (stage 2)
  FF-->>RN: edit.mp4 + timing_map
  RN-->>SV: ok, timing_map
  SV->>CP: remap(project, timing_map)
  CP-->>SV: episode.srt
  SV->>MS: master(edit.mp4)
  MS->>FF: 2-pass loudnorm; export mp3+mp4
  MS-->>SV: PASS -16 LUFS
  SV-->>UI: result (poll /api/job)
```

## Behaviour catalogue

| ID | Activity | Realised by |
|---|---|---|
| **A-1** | Upload & probe | `server._upload` + `probe.probe` |
| **A-2** | Segment & tag | `segment.segment` |
| **A-3** | Keep/drop | `model.set_keep` + `renumber` |
| **A-4** | Re-order (3 methods) | `model.move/swap/reorder_by_permutation` |
| **A-5** | Set transition / flag gaps | `model.set_transition` + `render.build_plan` |
| **A-6** | Render (two-stage) | `render.render` |
| **A-7** | Caption re-time | `captions.remap` |
| **A-8** | Master | `master.master` |

## Critical behavioural property (PR-2)
Each transition **overlaps** clips by its duration, so the engine tracks a
*running, overlap-adjusted duration* and sets each `xfade`/`acrossfade`
`offset = running − t`. This keeps audio and video aligned for the whole
timeline — verified numerically in **T-3** and against real FFmpeg output in
**T-4**.

---

# v2 — Media-track behaviour (PLANNED)

## v2 wizard state machine (adds a Media step)

```mermaid
stateDiagram-v2
  [*] --> Upload
  Upload --> Segments : demux + probe (A-9)
  Segments --> Order : Next
  Order --> Media : Next
  Media --> Media : replace audio (A-10) / add audio (A-11) / add image (A-12) / level-mute
  Media --> Transitions : Next
  Transitions --> Export : Next
  Export --> Done : render+caption+master ok (A-6)
  Media --> Order : Back
  Done --> [*]
```

## A-10 Replace audio — activity

```mermaid
flowchart TD
  s([upload new audio]) --> setp[set as primary audio track]
  setp --> chk{captions/segments derived from old audio?}
  chk -- yes --> flag[mark stale + offer re-transcribe]
  chk -- no --> keep[no caption change]
  flag --> done([render+master -16 LUFS])
  keep --> done
```

## v2 behaviour catalogue

| ID | Activity | Realised by | Req |
|---|---|---|---|
| **A-9** | Demux input → A/V tracks (+ per-stream probe) | `probe` + ingest (extended) | FR-9 |
| **A-10** | Replace audio track (+ invalidate/flag captions) | `model` + `captions` (extended) | FR-11 |
| **A-11** | Add/mix audio + optional duck (sidechain) | `audio_mix` (new) + `master` | FR-12 |
| **A-12** | Synthesise image clip (loop + optional Ken-Burns `zoompan`) | `render` (extended) | FR-13 |

## v2 critical properties
- **PR-4 (loudness preserved):** A-11 mixes tracks with `amix`/`sidechaincompress`, but the **final
  mix** still goes through the existing two-pass `loudnorm` (A-8) → −16 LUFS, so adding/replacing
  audio never changes the loudness contract.
- **PR-3 (MoP):** the threshold keeps spoken sub-sections A/V-locked during reorder (A-4 unchanged);
  image clips and audio tracks are the only independently-placed items now. The objective
  (independent A/V timelines) is a future behaviour, enabled by the B-10 first-class model.
- **Caption integrity (N-14):** A-10 must never leave captions that no longer match the audible
  speech — it flags/clears them rather than silently shipping a mismatch.
