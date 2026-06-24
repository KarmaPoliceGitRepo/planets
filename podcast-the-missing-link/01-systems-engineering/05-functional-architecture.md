# 5 · Functional (Logical) Architecture

> **SE step:** *Functional architecture.* We describe **what the system must do**
> as a set of **functions**, and how data flows between them — **without yet
> naming any tool**. (Tools come next, in the physical architecture.) This keeps
> the design tool-independent: if Audacity vanished tomorrow, the *functions*
> stay the same and we just swap the box behind them.

## 5.1 Top-level functional flow (the production pipeline)

```
        ┌──────────┐
 inputs │ F1 PLAN  │  topic, script, guest, assets
        └────┬─────┘
             ▼
        ┌──────────┐   raw audio + video + room tone
 mic ──▶│ F2       │──────────────┐
 cam ──▶│ CAPTURE  │              │
        └──────────┘              ▼
                            ┌───────────┐
                            │ F3 INGEST │  organise + label files
                            │ & BACKUP  │──┐ (off-device copy)
                            └─────┬─────┘  │
                                  ▼        ▼
                            ┌───────────┐  archive
                            │ F4 EDIT   │  cut, arrange, level, music
                            └─────┬─────┘
                                  ▼
                            ┌───────────┐
                            │ F5 MASTER │  noise-clean, loudness-normalise
                            └─────┬─────┘
                       ┌──────────┼──────────┐
                       ▼          ▼          ▼
                 ┌─────────┐ ┌─────────┐ ┌──────────┐
                 │F6 EXPORT│ │F7 TRANS-│ │F8 PACKAGE│
                 │ MP3/MP4 │ │ CRIBE   │ │notes/art │
                 └────┬────┘ └────┬────┘ └────┬─────┘
                      └──────┬────┴───────────┘
                             ▼
                       ┌───────────┐   audio→RSS→Spotify/Apple
                       │ F9 PUBLISH│   video→YouTube
                       └─────┬─────┘
                             ▼
                       ┌───────────┐
                       │ F10 ENGAGE│  share, reply, measure
                       │ & MEASURE │──▶ feeds back into F1 PLAN
                       └───────────┘
```

## 5.2 Function dictionary

| Fn | Function | Inputs | Outputs | Key reqs |
|---|---|---|---|---|
| **F1** | **Plan episode** | series arc, research, guest availability | script, asset list, booking | N-07, FR-9 |
| **F2** | **Capture** | mic signal, camera signal | raw audio file, raw video file, room tone | FR-1, FR-2, IR-1 |
| **F3** | **Ingest & back up** | raw files | organised episode folder + off-device copy | FR-11, UR-4 |
| **F4** | **Edit** | raw audio/video, music assets | edited timeline / rough master | FR-3, FR-4 |
| **F5** | **Master** | edited audio | clean, loudness-normalised audio | PR-1, PR-2 |
| **F6** | **Export** | mastered audio, edited video | MP3 + MP4 (spec-compliant) | FR-5, PR-3, IR-3 |
| **F7** | **Transcribe** | mastered audio | `.txt` transcript + `.srt` captions | FR-6, PR-5 |
| **F8** | **Package** | episode metadata | show notes, chapters, CTA, cover art | FR-9, IR-2 |
| **F9** | **Publish & distribute** | MP3, MP4, metadata, art, captions | live episode on host→Spotify/Apple + YouTube | FR-7, FR-8, IR-2 |
| **F10** | **Engage & measure** | published episode, analytics, comments | clips, replies, metrics, next-topic ideas | N-24, N-09 |

## 5.3 Functional interfaces (data hand-offs)

| From → To | Data item | Format/contract |
|---|---|---|
| F2 → F3 | raw recordings | WAV/MOV/MP4, named `raw_*` |
| F3 → F4 | working files | same, inside `NN-episode/` folder |
| F4 → F5 | rough master | single WAV, full episode |
| F5 → F6 | clean master | WAV, −16 LUFS, ≤ −1 dBTP (PR-1) |
| F5 → F7 | clean master | WAV/MP3 input to transcriber |
| F6 → F9 | deliverables | `episode.mp3` (PR-3), `episode.mp4` (IR-3) |
| F7 → F9 | captions | `episode.srt`, `episode.txt` |
| F8 → F9 | metadata | title, description, chapters, `cover_1400.png` (IR-2) |
| F10 → F1 | feedback | metrics + idea backlog |

## 5.4 Function → mode mapping

| Function | M1 Solo | M2 Remote | M3 Field | M4 Produce | M5 Grow |
|---|:--:|:--:|:--:|:--:|:--:|
| F1 Plan | ● | ● | ● | | ● |
| F2 Capture | ● | ● | ● | | |
| F3 Ingest/Backup | ● | ● | ● | | |
| F4 Edit | | | | ● | |
| F5 Master | | | | ● | |
| F6 Export | | | | ● | |
| F7 Transcribe | | | | ● | |
| F8 Package | | | | ● | |
| F9 Publish | | | | ● | |
| F10 Engage | | | | | ● |

➡️ Now allocate each function to a real, free tool:
[`06-physical-architecture.md`](06-physical-architecture.md).


## Cross-layer like-to-like links (ADR-013)

> Mirrors this file's rows from the cross-layer spine (`10-cross-layer-traceability.md`).
> `▽` = within-layer decomposition · `⇒` = across-layer realization (routed via a Configuration item).

| Link | Type | From | To |
|------|------|------|----|
| F4 ▽ {F4b, F4c} | ▽ decompose | F4 Edit | F4b clean audio · F4c segment + select |
| F4b/F4c ⇒ component ops ⇒ reelcut/ | ⇒ refine | function | implementation behaviour |
