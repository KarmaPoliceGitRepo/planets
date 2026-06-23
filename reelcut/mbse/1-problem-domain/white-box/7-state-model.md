# Logical · White Box · Behavior — State Model (overall context, end-to-end)

> The **state model** is the **overall context** (your definition): the complete
> lifecycle of a ReelCut session including **every** alternate, exception and
> recovery state from `5-behaviour-catalogue.md`, plus a **concurrent persistence
> region** (autosave / undo) that runs alongside the main flow. Guards in `[...]`
> are the **conditions** that source conditional requirements.

## End-to-end session state machine (with error/recovery)

```mermaid
stateDiagram-v2
  [*] --> Idle
  Idle --> Validating: upload(media)
  Validating --> Idle: reject [invalid/corrupt] / show reason
  Validating --> Ingesting: accept [valid A/V]
  Ingesting --> Segmenting: demuxed
  state Segmenting {
    [*] --> Transcribing
    Transcribing --> Tagging: timedText
    Transcribing --> SilenceFallback: no speech / no Whisper
    SilenceFallback --> Tagging
    Tagging --> [*]
  }
  Segmenting --> Editing: segments ready
  state Editing {
    [*] --> Curating
    Curating --> Ordering: keep set
    Ordering --> Transitioning: jumps flagged
    Transitioning --> ReMedia: optional
    ReMedia --> Curating: source changed / re-segment
    ReMedia --> Ready: edit settled
    Ordering --> Ready
  }
  Editing --> Idle: discard
  Ready --> Rendering: export [>=1 kept]
  state Rendering {
    [*] --> Cutting
    Cutting --> Cutting: next clip (incremental)
    Cutting --> RetryCut: ffmpeg error
    RetryCut --> Cutting: retry ok
    RetryCut --> Aborted: retry failed / cancel
    Cutting --> Joining: all clips ready
    Joining --> [*]
  }
  Rendering --> Editing: aborted / error [revise]
  Rendering --> Captioning: render ok
  Captioning --> Mastering: cues re-timed
  Captioning --> Mastering: no transcript [skip]
  Mastering --> Mastering: out of spec [re-pass]
  Mastering --> Delivered: in spec [-16 LUFS, TP<=-1]
  Delivered --> Editing: revise
  Delivered --> [*]: done [files on local disk]
  Aborted --> Editing
```

## Concurrent persistence & history region (runs throughout)

```mermaid
stateDiagram-v2
  state Session {
    direction LR
    state Persistence {
      [*] --> Clean
      Clean --> Dirty: edit
      Dirty --> Autosaving: timer / edit
      Autosaving --> Clean: projectDoc written
      Clean --> Restoring: reopen after close/crash
      Restoring --> Clean: projectDoc loaded
    }
    --
    state History {
      [*] --> Empty
      Empty --> Undoable: edit pushed
      Undoable --> Undoable: edit pushed
      Undoable --> Redoable: undo
      Redoable --> Undoable: redo / new edit
      Undoable --> Empty: cleared
    }
  }
```

## Guard → conditional-requirement catalogue (extends `4`)

| Guard | Sources |
|---|---|
| `[invalid/corrupt]` (Validating) | SR-3.1 validate-and-reject |
| `[no speech / no Whisper]` (Segmenting) | SR-1.1 fallback segmentation |
| `[>=1 kept]` (Ready→Rendering) | SR-1.2 precondition |
| `ffmpeg error → retry/abort` (Rendering) | SR-3.4 cancel/abort, CR-1 robustness |
| `next clip (incremental)` | SR-3.6 incremental re-render |
| `out of spec → re-pass` (Mastering) | SR-1.5 loudness |
| `reopen after close/crash → Restoring` | SR-3.2 autosave/restore |
| `undo / redo` (History) | SR-3.3 undo/redo |
| `done [files on local disk]` | SR-1.7 local-only (MOE-2) |

> The two regions are **orthogonal**: the main lifecycle and the
> persistence/history region are active **simultaneously** for the whole session —
> that is what makes autosave, crash-recovery and undo/redo cross-cutting rather
> than steps in the pipeline.
</content>
</invoke>
