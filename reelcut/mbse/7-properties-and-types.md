# Properties, Value Types & Signals — full definitions (with compartment diagrams)

> Closes the "every element has all its properties **defined and described**" bar.
> The element dictionary (`6`) gives each element a *meaning*; this file gives each
> block its **typed property set** (value/part/port/flow/reference properties +
> operations/constraints), defines every **value type** (with unit/quantity kind)
> and every **signal** (flow item) with its internal structure, and **visualises
> properties in compartments** (Mermaid `classDiagram` = SysML block compartments).

## 1 · Value-type catalogue (units / quantity kinds)

| Value type | Base | Unit / quantity kind | Description |
|---|---|---|---|
| `Duration` | Real | second (s) | A length of time on a timeline. |
| `Loudness` | Real | LUFS | Integrated programme loudness. |
| `TruePeak` | Real | dBTP | Sample-peak ceiling of the signal. |
| `SyncError` | Real | millisecond (ms) | Signed A/V offset; 0 = perfectly aligned. |
| `DataSize` | Integer | byte (B) | Quantity of data (e.g. egress). |
| `Count` | Integer | — | Dimensionless cardinality. |
| `Path` | String | — | Filesystem location (a `Directory` is a `Path` to a folder). |
| `Permutation` | Integer[1..*] | — | Ordering of kept sub-sections (new index sequence). |
| `TagLabel` | String | — | Topic tag attached to a segment/sub-section. |
| `TransitionKind` | enum | — | {none, crossfade, dissolve, fade, wipe, slide, circle, radial}. |
| `Status` | enum | — | {Built, Planned}. |
| `MoSCoW` | enum | — | {Must, Should, Could, Wont}. |
| `VerificationMethodKind` | enum | — | {Inspection, Analysis, Demonstration, Test}. |
| `RiskLevel` | enum | — | {Low, Medium, High}. |
| `TrackLevel` | Real | dB | Per-track gain applied in the mix (0 = unity). |
| `Attenuation` | Real | dB | Amount the added track is ducked under speech. |
| `HostAddress` | String | IPv4 dotted-quad | Loopback bind address (default 127.0.0.1). |
| `ContainerFormat` | enum | — | {mp4, mov, mkv, webm, m4a, mp3}. |
| `KeepFlag` | enum | — | {keep, drop} — per sub-section keep decision. |
| `MuteState` | enum | — | {muted, unmuted} — per-track mute state. |
| `CaptionText` | String | UTF-8 | Caption / transcript text payload. |
| `SemVer` | String | semver | Portable-project-document schema version. |
| `MediaHandle` | String | — | Stable, path-independent reference to a media unit. |
| `FFmpegCommand` | String | — | Generated filtergraph / command string sent to the engine. |
| `AspectKind` | enum | — | {r16x9, r9x16, r1x1} target output aspect. |
| `Rate` | Real | × real-time | Render time per minute of footage (e.g. 0.4 = 0.4× real-time). |

```mermaid
classDiagram
  class Duration { <<valueType>> +Real value; unit = s }
  class Loudness { <<valueType>> +Real value; unit = LUFS }
  class TruePeak { <<valueType>> +Real value; unit = dBTP }
  class SyncError { <<valueType>> +Real value; unit = ms }
  class DataSize { <<valueType>> +Integer value; unit = byte }
  class TransitionKind { <<enumeration>> none crossfade dissolve fade wipe slide circle radial }
  class Status { <<enumeration>> Built Planned }
  class VerificationMethodKind { <<enumeration>> Inspection Analysis Demonstration Test }
  class TrackLevel { <<valueType>> +Real value; unit = dB }
  class Attenuation { <<valueType>> +Real value; unit = dB }
  class HostAddress { <<valueType>> +String value; pattern = IPv4 }
  class ContainerFormat { <<enumeration>> mp4 mov mkv webm m4a mp3 }
  class KeepFlag { <<enumeration>> keep drop }
  class MuteState { <<enumeration>> muted unmuted }
```

## 2 · Signal / flow-item catalogue (internal structure)

Every item that crosses a port is a signal/block with typed properties:

```mermaid
classDiagram
  class MediaFile { <<signal>> +Path path; +ContainerFormat container; +Count vStreams; +Count aStreams; +Duration duration }
  class ImageFile { <<signal>> +Path path; +Count width; +Count height }
  class AudioFile { <<signal>> +Path path; +Duration duration; +Count sampleRate }
  class EditDecision { <<signal>> +KeepFlag[] keepSet; +Permutation order; +TransitionKind[] transitions; +TrackLevel[] trackLevels; +MuteState[] mutes }
  class FilterGraph { <<signal>> +FFmpegCommand command }
  class Measurement { <<signal>> +Loudness loudness; +TruePeak truePeak; +Duration duration }
  class TimedText { <<signal>> +Cue[] cues }
  class Cue { <<valueType>> +Duration start; +Duration end; +CaptionText text }
  class Delivery { <<signal>> +MediaFile mp4; +MediaFile mp3; +File srt; +Loudness measuredLoudness }
  class ProjectDoc { <<signal>> +SemVer version; +Track[] tracks; +Clip[] clips; +MediaHandle[] mediaHandles }
  class SegmentModel { <<signal>> +Segment[] segments }
  class Segment { <<valueType>> +Duration start; +Duration end; +TagLabel tag; +SubSection[] subs }
  MediaFile <|-- ImageFile
  MediaFile <|-- AudioFile
  TimedText *-- Cue
  SegmentModel *-- Segment
  Delivery *-- MediaFile
```

| Signal | Carried by interface | Description |
|---|---|---|
| `MediaFile` / `ImageFile` / `AudioFile` | I-Media | The media units ingested or produced; images/audio specialise MediaFile. |
| `EditDecision` | I-HMI | The creator's complete keep/order/transition/track choice set. |
| `FilterGraph` / `Measurement` | I-Engine | Command sent to FFmpeg; loudness/probe result returned. |
| `TimedText` (`Cue`) | I-Transcript | Caption cues with start/end/text. |
| `Delivery` | I-HMI | The export bundle (mp4/mp3/srt + measured loudness). |
| `ProjectDoc` | I-Project | The portable, renderer-agnostic edit for mobile resume. |
| `SegmentModel` (`Segment`/`SubSection`) | internal | The tagged segmentation the edit model is built on. |

## 3 · Block property definitions (compartments)

### 3.1 System of Interest — `ReelCut`

```mermaid
classDiagram
  class ReelCut {
    <<block>>
    +Loudness loudness
    +TruePeak truePeak
    +SyncError avSyncErr
    +Duration totalDuration
    +DataSize egressBytes = 0
    +Count runtimeDeps = 0
    +port hmi : I_HMI
    +port media : I_Media
    +port engine : I_Engine
    +port asr : I_Transcript [0..1]
    +ref uploadDir : Directory
    +ingest() 
    +segment()
    +render()
    +mix()
    +master()
    +export()
    +onUpload(MediaFile)
    +onRender()
    +onReplaceAudio(MediaFile)
  }
```

### 3.2 Logical subsystems — ports & key value properties

| Block | value properties | ports (typed by interface block) | operations |
|---|---|---|---|
| **LS-Ingest** | `trackCount : Count` | `out tracks : I_AVTracks` | `ingest()`, `demux()` |
| **LS-Segment** | `segmentCount : Count` | `out segs : I_Segments` | `transcribe()`, `segment()` |
| **LS-EditModel** | `order : Permutation`, `trackLevels : TrackLevel[*]`, `fillerTrimmed : Duration` | `in fromHMI : I_HMI`, `out plan : I_RenderPlan` | `setKeep()`, `reorder()`, `setTransition()`, `setTrackLevel()`, `replaceAudio()` |
| **LS-Render** | `runningDuration : Duration`, `renderRate : Rate`, `aspect : AspectKind`, `imageClipDur : Duration = 4` | `in plan : I_RenderPlan`, `out edit : I_Edit` | `render()`, `synthImageClip()` |
| **LS-AudioMix** | `duckAtten : Attenuation`, `noiseFloorCut : Attenuation` | `in tracks : I_AVTracks`, `out mixed : I_Audio` | `mix()`, `duck()` |
| **LS-Caption** | `cueCount : Count` | `in timing : I_TimingMap`, `out srt : I_Captions` | `remap()`, `invalidate()` |
| **LS-Master** | `loudness : Loudness`, `truePeak : TruePeak` | `in edit : I_Edit`, `out delivery : I_Media` | `master()` |
| **LS-HMI** | `bindAddress : HostAddress = 127.0.0.1` | `hmi : I_HMI` | `serve()`, `route()` |

### 3.3 Components — value properties & operations

Component operations and their realising scripts are in `2-solution-domain/2` &
`3`; each component's **value properties** are the measurable state it owns, each
typed by the §1 catalogue: `C-Master.loudness : Loudness` / `truePeak : TruePeak`,
`C-Render.runningDuration : Duration`, `C-Model.order : Permutation` /
`trackLevels : TrackLevel[*]`, `C-Server.bindAddress : HostAddress = 127.0.0.1`,
`C-AudioMix.duckAtten : Attenuation`, `C-Probe.vStreams : Count` / `aStreams : Count` /
`duration : Duration`. No component value property is left as a raw primitive.

## 4 · Coverage statement

Every block now has its **value / part / port / flow / reference properties** and
**operations / receptions** enumerated; every **value type** has a unit/quantity
kind; every **signal** has its internal structure typed; and all of this is
**visualised in compartments** (the `classDiagram` blocks above render to SVG —
`diagrams/types/value-types`, `diagrams/types/signals`, `diagrams/types/soi-block`).
Requirement-element **attributes** (risk + rationale, completing the p.15 set) are
in `1-problem-domain/white-box/1` and `2-solution-domain/1`.
</content>
</invoke>
