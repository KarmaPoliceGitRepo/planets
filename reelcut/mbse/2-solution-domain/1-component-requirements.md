# Physical · Solution · Requirements — Component Requirements (SW + HW)

> MagicGrid cell **Requirements / Physical**. Component (system-element)
> requirements **derive** from system requirements (`«deriveReqt»`). Per your #1
> they split into **software requirements** — *verified by the scripts/tests* — and
> **hardware requirements expressed as constraints**.

## Software Component Requirements (CR-) — verified by scripts (tests T-)
| ID | Shall (software) | derivedFrom | Component | verify (test) | St |
|---|---|---|---|---|---|
| **CR-1** | `render` shall fold clips with concat/xfade+acrossfade at `offset=running−t`. | SR-1.3, SR-1.6 | C-Render | T-3, T-4 | Built |
| **CR-2** | `master` shall two-pass loudnorm to −16 LUFS and report PASS/FAIL. | SR-1.5 | C-Master | T-7 | Built |
| **CR-3** | `captions.remap` shall re-time cues to the new order. | SR-1.4 | C-Caption | T-6 | Built |
| **CR-4** | `model` shall hold first-class tracks/clips; media by stable handle; **no abs paths / FFmpeg strings**. | SR-2.2 | C-Model | T-8 | Planned |
| **CR-5** | `demux` shall split input into independent A/V tracks. | SR-2.1 | C-Demux | T-8 | Planned |
| **CR-6** | `model/captions` shall, on audio replace, invalidate/flag captions. | SR-2.3 | C-Model,C-Caption | T-9 | Planned |
| **CR-7** | `audio_mix` shall mix per-track level/mute + optional sidechain duck. | SR-2.4 | C-AudioMix | T-10 | Planned |
| **CR-8** | `render` shall synthesise image clips (loop + optional zoompan). | SR-2.5 | C-ImageSynth | T-11 | Planned |

> **Software-requirement verification = the scripts:** each CR is verified by a
> test in `reelcut/tests/` (T-*); the implementation scripts both **realise** and
> **verify** these requirements (your #1).

### Full attributes (risk + rationale)
| ID | risk | rationale |
|---|---|---|
| CR-1 | Med | The two-stage fold is what avoids the acrossfade audio-drop bug. |
| CR-2 | Low | Two-pass loudnorm + PASS/FAIL makes loudness verifiable in CI. |
| CR-3 | Med | Cue re-timing keeps captions aligned after reorder. |
| CR-4 | High | Stable media handles / no abs paths make the project portable for mobile. |
| CR-5 | Med | Demux yields the independent tracks the media feature needs. |
| CR-6 | Med | Invalidating captions on replace prevents stale, wrong subtitles. |
| CR-7 | Med | Per-track level/mute + sidechain duck is the add-audio core. |
| CR-8 | Low | Image-clip synth (loop + optional zoompan) reuses the render path. |

## Hardware Requirements as Constraints (HC-)
| ID | Hardware constraint | derivedFrom | Applies to | Verify |
|---|---|---|---|---|
| **HC-1** | The mobile client **shall run on Android ≥ Samsung Galaxy S23, or iPhone 11 or newer**. | SN-7 | C-Mobile (future) | Analysis |
| **HC-2** | Desktop **shall run on any machine with Python 3 + FFmpeg** (no GPU required). | SN-4 | C-Server | Inspection |

```sysml
constraint def MobileHardwareFloor {        // HC-1 as a constraint (your #1)
    require { androidTier >= GalaxyS23 or iosModel >= iPhone11 }
}
deriveReqt CR_4_PortableModel from SR_2_2;
verify CR_2_Loudness by Test_T7;            // SW requirement verified by the script/test
```
