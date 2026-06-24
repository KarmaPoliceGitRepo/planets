# 12 · Formal Behaviour — Use Cases, Activity, State Machine & Sequences

> **SE step:** formalise the behaviour pillar. Functions `F1–F10` (`05`) and modes `M1–M5`
> (`04`) become a **use-case model**, a **control-flow activity** with object flows and
> exception branches, a **state machine** (modes-as-states + episode lifecycle with recovery),
> and a **sequence** for the hardest scenario. Behaviour was enumerated for completeness —
> **nominal / alternate / exception / edge** — per the repo's MBSE behaviour rule (brainstorming
> discipline). Counterpart of `reelcut/mbse/1-problem-domain/white-box/{2,4,6,7}`.

## 12.1 Actors and use cases

| Actor | Description | Use cases (associations) |
|---|---|---|
| **Host** (primary) | The creator operating the system | UC-P1 Plan, UC-P2 Capture, UC-P3 Produce, UC-P5 Engage |
| **Guest** | Remote interviewee | UC-P2 Capture (remote, M2) |
| **Listener/Viewer** | The audience | UC-P4 Consume (via published episode + captions) |
| **Platform** | Spotify/Apple host + YouTube | UC-P3 Produce → Publish (receives RSS/MP4) |
| **Cloud backup** | Off-device store | UC-P2/UC-P3 backup |

Each use case `«refine»`s the functions that realise it: UC-P1→F1; UC-P2→F2/F3; UC-P3→F4–F9;
UC-P4→(F6/F7 outputs consumed); UC-P5→F10.

```mermaid
flowchart LR
  HOST([Host]):::a
  GUEST([Guest]):::a
  AUD([Listener/Viewer]):::a
  PLAT([Platform]):::a
  subgraph SYS["PodcastSystem"]
    U1(("UC-P1 Plan"))
    U2(("UC-P2 Capture"))
    U3(("UC-P3 Produce & Publish"))
    U4(("UC-P4 Consume"))
    U5(("UC-P5 Engage & Grow"))
  end
  HOST --- U1 & U2 & U3 & U5
  GUEST --- U2
  AUD --- U4
  U3 --- PLAT
  U2 -. "«include» backup" .-> U3
  classDef a fill:#eef;
```

## 12.2 Production activity (object flow + exception branches)

Nominal flow plus the alternate capture modes and the master-loudness exception loop.

```mermaid
flowchart TB
  start([●]) --> F1["F1 Plan"]
  F1 -->|script, assets| CAP{capture mode?}
  CAP -->|M1 solo| F2a["F2 Capture solo (C1)"]
  CAP -->|M2 remote| F2b["F2 Capture remote (C1+C3)"]
  CAP -->|M3 field| F2c["F2 Capture field (C1)"]
  F2a & F2b & F2c -->|rawAudio, rawVideo| F3["F3 Ingest & Backup (C8)"]
  F3 -->|episodeFolder| F4["F4 Edit / F4b clean / F4c segment"]
  F4 -->|roughMaster| F5["F5 Master loudnorm (C4)"]
  F5 --> CHK{loudness PASS?\n−16 LUFS ±1}
  CHK -->|FAIL| F4
  CHK -->|PASS| F6["F6 Export MP3+MP4"]
  F6 --> F7["F7 Transcribe (C5)"]
  F6 --> F8["F8 Package art/notes (C6)"]
  F7 & F8 --> NET{internet?}
  NET -->|no field| DEFER[/defer publish — N-15/]
  NET -->|yes| F9["F9 Publish RSS + YouTube"]
  DEFER -.-> F9
  F9 --> F10["F10 Engage & Measure"]
  F10 -->|next-topic ideas| F1
  F10 --> done([◉])
```

## 12.3 State machine — operating modes + episode lifecycle (with recovery)

Modes `M1–M5` are formalised as **states**; the do-activity of each is the function set the
ConOps assigns it (`04` §4.1), which links every mode to its requirements.

```mermaid
stateDiagram-v2
  [*] --> Planning : M5→M1 new episode
  Planning : M1/M5 do F1 Plan
  Capturing : M1/M2/M3 do F2,F3
  Producing : M4 do F4..F9
  Growing : M5 do F10

  Planning --> Capturing : script ready
  Capturing --> Producing : footage ingested+backed up
  Producing --> Growing : episode live
  Growing --> Planning : next topic chosen

  state Capturing {
    [*] --> Recording
    Recording --> CallDropped : M2 guest link lost
    CallDropped --> Recording : resume (double-ender local backup, N-15)
    Recording --> [*] : stop & save
  }
  state Producing {
    [*] --> Mastering
    Mastering --> Mastering : loudness FAIL → re-edit
    Mastering --> Publishing : PASS −16 LUFS
    Publishing --> [*]
  }
```

## 12.4 Sequence — M2 Remote interview (the hardest scenario, with alt/break)

```mermaid
sequenceDiagram
  actor Host
  actor Guest
  participant C3 as C3 Caller
  participant C1 as C1 OBS
  participant C8 as C8 Backup
  Host->>C3: connect(guest)
  Guest->>C3: join (per-speaker tracks, IR-4)
  Host->>C1: record() local A/V
  loop interview
    Guest-->>C1: speech (guestTrack)
    Host-->>C1: speech
  end
  alt call drops (exception, N-15)
    C3--xHost: link lost
    Host->>C1: keep local double-ender recording
    Host->>C3: reconnect()
  end
  Host->>C1: stopAndSave()
  C1->>C8: sync(raw + per-speaker tracks)
```

## 12.5 Behaviour-completeness register (nominal / alternate / exception / edge)

| Class | Behaviour | Where handled |
|---|---|---|
| Nominal | Plan→Capture→Ingest→Edit→Master(PASS)→Export→Transcribe→Package→Publish→Engage | §12.2 |
| Alternate | Solo (M1) / Remote (M2) / Field (M3) capture; Studio (C10) vs Audacity edit path | §12.2 CAP branch |
| Alternate | Defer publish when offline in the field, sync later | §12.2 NET branch (N-15) |
| Exception | Master loudness FAIL → re-edit loop until −16 LUFS ±1 | §12.2 CHK / §12.3 Mastering |
| Exception | Remote call drops → double-ender local backup, reconnect | §12.3 CallDropped / §12.4 alt |
| Edge | Guest no-show → fall back to solo (M1) monologue | mode transition Capturing→Planning |
| Edge | Corrupted/over-noisy recording → re-capture (PR-2 gate fails at edit) | re-enter Capturing |

*Created 2026-06-24. Companion to `04-concept-of-operations.md` (modes), `05-functional-architecture.md`
(functions), and `11-formal-structure.md` (the components that perform these behaviours). Every use
case, function, mode and state here is linked (association / «refine» / do-activity / transition).*
