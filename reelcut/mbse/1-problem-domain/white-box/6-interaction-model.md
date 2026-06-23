# Logical · White Box · Behavior — Interaction (Sequence) Model

> The **interaction model** shows the **interaction between the entities involved**
> (your definition). One sequence per significant use case / behaviour group, drawn
> from `5-behaviour-catalogue.md` — including the **alternate / exception** fragments
> (`alt` / `opt` / `loop`). The export sequence (UC-6 nominal) lives in `4`; this
> file covers the remaining interactions end-to-end.

## Ingest + validate (UC-1; B-IN.*)

```mermaid
sequenceDiagram
  actor CR as Creator
  participant BR as Browser
  participant RC as ReelCut
  participant FF as ffprobe
  participant FS as Filesystem
  CR->>BR: choose file
  BR->>RC: POST /upload (X-Filename, raw body)
  RC->>FF: probe(mediaFile)
  alt valid A/V
    FF-->>RC: streams + duration
    RC->>RC: F-2 demux into A/V tracks
    RC->>FS: store tracks
    RC-->>BR: 200 {accepted, tracks}
  else invalid / corrupt (B-IN.4)
    FF-->>RC: error
    RC-->>BR: 422 {rejected, reason}
  end
```

## Segment with fallback (UC-2; B-SG.*)

```mermaid
sequenceDiagram
  participant RC as ReelCut
  participant WH as Whisper
  participant FF as FFmpeg
  RC->>WH: transcribe(audio)
  alt Whisper present & speech found
    WH-->>RC: timedText
    RC->>RC: F-4 segment & tag by topic
  else no Whisper / no speech (B-SG.2)
    RC->>FF: silencedetect(audio)
    FF-->>RC: silence ranges
    RC->>RC: F-4 segment by silence
  end
  RC-->>RC: SegmentModel (segments + subs + tags)
```

## Curate + reorder with undo (UC-3/4; B-CU.*, B-SQ.*)

```mermaid
sequenceDiagram
  actor CR as Creator
  participant BR as Browser
  participant MD as EditModel
  CR->>BR: keep/drop, drag/swap/renumber
  BR->>MD: setKeep / reorder(permutation)
  MD-->>BR: updated order (+ jarring-jump flags B-SQ.3)
  opt undo (B-CU.3 / B-SQ.2)
    CR->>BR: undo
    BR->>MD: F-17 pop command stack
    MD-->>BR: restored state
  end
```

## Replace audio → invalidate captions (UC-7; B-RA.*, CB-4)

```mermaid
sequenceDiagram
  actor CR as Creator
  participant BR as Browser
  participant MD as EditModel
  participant CP as Caption
  CR->>BR: replace audio (file)
  BR->>MD: replaceAudio(audioFile)
  alt unsupported format (B-RA.5)
    MD-->>BR: 422 rejected (CB-1)
  else accepted
    MD->>MD: fit length (pad/trim B-RA.3/4)
    MD->>CP: CB-4 invalidate cues+segments from old audio
    CP-->>BR: captions flagged stale → offer re-transcribe
  end
```

## Add audio + duck (UC-8; B-AA.*)

```mermaid
sequenceDiagram
  participant BR as Browser
  participant MD as EditModel
  participant AM as AudioMix
  participant MS as Master
  BR->>MD: addTrack(audio, level, mute)
  opt duck-under-speech (B-AA.2)
    alt speech track exists
      MD->>AM: mix + sidechain duck
    else no speech track (B-AA.3)
      AM-->>BR: warn: duck disabled (CB-2)
    end
  end
  AM->>MS: mixed audio
  MS->>MS: re-check -16 LUFS (B-AA.5)
  MS-->>BR: mixed, in-spec
```

## Render with retry / cancel (UC-6; B-RN.*, CB-3/CB-5)

```mermaid
sequenceDiagram
  actor CR as Creator
  participant BR as Browser
  participant RN as Render
  participant FF as FFmpeg
  BR->>RN: render(plan)
  loop each changed clip (CB-5 incremental)
    RN->>FF: cut+normalise clip
    alt ffmpeg error (B-RN.2)
      FF-->>RN: error
      RN->>FF: retry once
    else ok
      FF-->>RN: clip
    end
    RN-->>BR: progress % (F-18)
  end
  opt cancel (B-RN.3 / F-19)
    CR->>BR: cancel
    BR->>RN: abort → cleanup + log
  end
  RN->>FF: join clips (xfade/acrossfade)
  FF-->>RN: edit
```

## Autosave / restore (B-SE.1/2; CB-7)

```mermaid
sequenceDiagram
  participant MD as EditModel
  participant SV as Server
  participant FS as Filesystem
  participant BR as Browser
  loop on every edit / timer
    MD->>SV: state changed
    SV->>FS: write projectDoc (autosave)
  end
  note over BR,FS: close / crash
  BR->>SV: reopen session
  SV->>FS: read last projectDoc
  FS-->>SV: projectDoc
  SV-->>BR: restore edit (B-SE.2)
```
</content>
</invoke>
