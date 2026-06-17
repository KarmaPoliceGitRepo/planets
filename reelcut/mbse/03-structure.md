# ReelCut — MBSE Model (03 · Structure)

## Block Definition Diagram (BDD) — what the system is made of

```mermaid
classDiagram
  class B1_WebUI {
    +wizard (5 steps)
    +drag/swap/renumber
    +transition pickers
    realised: app/static/*
  }
  class B2_LocalServer {
    +HTTP on 127.0.0.1:8770
    +REST API + job runner
    realised: app/server.py
  }
  class B3_EditModel {
    +project.json
    +move() swap() reorder_by_permutation()
    +set_keep() set_transition()
    realised: app/model.py
  }
  class B4_Probe {
    +duration,res,fps,streams
    realised: pipeline/probe.py
  }
  class B5_Segmenter {
    +whisper | silence engine
    +tag + group
    realised: pipeline/segment.py
  }
  class B6_RenderEngine {
    +build_plan / timing_map
    +two-stage cut+join
    +xfade/acrossfade/concat
    realised: pipeline/render.py
  }
  class B7_CaptionRetimer {
    +remap to new order
    realised: pipeline/captions.py
  }
  class B8_Master {
    +two-pass loudnorm -16 LUFS
    +export mp3/mp4
    realised: pipeline/master.py
  }
  class B9_FFmpeg {
    <<external>>
    +ffmpeg / ffprobe
  }

  B1_WebUI --> B2_LocalServer : HTTP/JSON
  B2_LocalServer --> B3_EditModel
  B2_LocalServer --> B4_Probe
  B2_LocalServer --> B5_Segmenter
  B2_LocalServer --> B6_RenderEngine
  B2_LocalServer --> B7_CaptionRetimer
  B2_LocalServer --> B8_Master
  B4_Probe ..> B9_FFmpeg
  B5_Segmenter ..> B9_FFmpeg
  B6_RenderEngine ..> B9_FFmpeg
  B8_Master ..> B9_FFmpeg
```

## Internal Block Diagram (IBD) — how data flows between blocks

```mermaid
flowchart TD
  U[Creator's browser] -- "upload bytes" --> S[B-2 Local Server]
  S -- "raw/upload.mp4" --> PR[B-4 Probe]
  PR -- "w,h,fps,dur" --> S
  S -- "media" --> SEG[B-5 Segmenter]
  SEG -- "segments[] + tags" --> MDL[(B-3 project.json)]
  U -- "keep / order / transition" --> S --> MDL
  MDL -- "plan" --> RND[B-6 Render Engine]
  RND -- "edit.mp4 + timing_map" --> CAP[B-7 Caption Re-timer]
  RND -- "edit.mp4" --> MAS[B-8 Master]
  CAP -- "episode.srt" --> EXP[(exports/)]
  MAS -- "episode.mp4 / .mp3" --> EXP
  EXP -- "download" --> U
```

## Key interface (ports) — the REST API of B-2

| Port (endpoint) | Dir | Payload | Block served |
|---|---|---|---|
| `POST /api/upload` | in | raw body + `X-Filename` | B-4 |
| `POST /api/segment` | in | `{id,model,language}` | B-5 |
| `POST /api/keep` | in | `{id,item,keep}` | B-3 |
| `POST /api/reorder` | in | `{id,method,…}` | B-3 |
| `POST /api/transition` | in | `{id,to,type,duration}` | B-3 |
| `GET /api/sequence` | out | ordered items + boundaries | B-3/B-6 |
| `POST /api/render` | in | `{id}` | B-6/B-7/B-8 |
| `GET /api/file` | out | exported media | exports/ |

## Deployment view
A single Python process serves the UI and runs all blocks in-process; **B-9
FFmpeg** is the only external dependency. Everything binds to `127.0.0.1`
(satisfies **CR-1** privacy / local-only).
