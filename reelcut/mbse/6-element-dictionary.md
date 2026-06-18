# Element Dictionary — every modeled element, with description

> Data dictionary for the whole model. **Every element** that appears in any
> diagram or table is listed here once with a one-line **description** (the SysML
> `doc` of that element) and its kind. This is the authoritative gloss; the cell
> files hold the relationships, this file holds the meanings.

## Enterprise / SoS — nodes (blocks)
| Element | Kind | Description |
|---|---|---|
| ReelCut | «system of interest» block | The local-first video editor; black-box node at SoS level — ingests a recording and produces a finished video/audio/captions entirely on-device. |
| Creator | «external» actor | The non-expert person who records footage and makes keep/order/media decisions. |
| Viewer / Audience | «external» block | Consumer of the finished video; reads captions on an arbitrary device. |
| Capture Device | «external» block | Phone camera or camera that records the raw A/V the creator imports. |
| Media Library | «external» block | The creator's local store of reusable photos and audio used for add/replace media. |
| Host Filesystem | «external» block (reference) | Local directories holding the upload source and render outputs; referenced, not owned. |
| Web Browser | «external» block | Renders the ReelCut HMI and runs the wizard JavaScript over a localhost origin. |
| FFmpeg / ffprobe | «external» block | CLI media engine: decode, filter-graph, two-pass loudnorm, and measurement/probe. |
| Whisper ASR | «external» block (optional) | Offline speech-to-timed-text engine; silence-detect fallback when absent. |
| Android Phone | «environment» block | Capture device and future mobile-client host; constrained to ≥ Galaxy S23 (HC-1). |
| iPhone | «environment» block | Capture device and future mobile-client host; constrained to ≥ iPhone 11 (HC-1). |
| Publishing Destination | «external» block (optional) | Off-device social/storage target; receives the finished video only on explicit user action. |

## Interface blocks & item flows (signals)
| Element | Kind | Description |
|---|---|---|
| I-HMI | interface block | Boundary between Browser and ReelCut: carries editDecision (in) and previewExports (out) as http/json on 127.0.0.1. |
| I-Media | interface block | Boundary between Filesystem and ReelCut: mediaFile (in), renderedFile (out). |
| I-Engine | interface block | Boundary between ReelCut and FFmpeg: filterGraph command (out), measurement (in). |
| I-Transcript | interface block | Boundary Whisper→ReelCut: timedText (in). |
| I-Project | interface block | Boundary ReelCut↔Mobile: portable projectDoc (bidirectional). |
| rawRecording | flow / signal | Raw A/V produced by the capture device. |
| mediaFile | flow / signal | A media file presented to ReelCut for ingest. |
| photo / extraAudio | flow / signal | Image / audio asset from the Media Library for add/replace media. |
| editDecision | flow / signal | Creator's keep/drop, order, transition and track choices. |
| filterGraph | flow / signal | FFmpeg command string ReelCut emits to render. |
| measurement | flow / signal | Loudness (LUFS/TP) and probe data FFmpeg returns. |
| timedText | flow / signal | Time-stamped transcript used for captions. |
| renderedFile | flow / signal | Output mp4/mp3/srt written back to the filesystem. |
| portableProjectDoc | flow / signal | Renderer-agnostic JSON project carrying the full edit for mobile resume. |

## Mission layer
| Element | Kind | Description |
|---|---|---|
| MV-1 | mission vignette | Turn a raw phone recording into a clean finished video unaided. |
| MV-2 | mission vignette | Cut dead air, re-order topics, add gap-aware transitions, caption it. |
| MV-3 | mission vignette | Replace audio, add a ducked music/VO track, drop in photos — independent of video. |
| MV-4 | mission vignette | Complete the whole job with nothing leaving the device unless explicitly published. |
| MV-5 | mission vignette | Resume the same edit on a phone via a portable project document. |
| MV-6 | mission vignette | Never lose work: autosave/restore (crash recovery), undo/redo, cancel/abort a long operation. |
| MV-7 | mission vignette | Grow/repurpose: tighten, platform-fit highlight clips with sound-off & translated captions + chapters. |
| MV-8 | mission vignette | Polish/brand: clean audio + consistent branding/presets, non-destructive, trustworthy preview. |
| CAP-1…CAP-11 | capability | Ingest, Comprehend, Curate, Bridge, Re-media, Balance, Render, Normalize, Caption, Keep-local/Port, **Sustain** (work preservation). |
| CAP-12…CAP-21 | capability | Tighten, Repurpose, Structure (chapters), Present (aspect/burned captions), Localise (translation), Enhance-audio, Brand, Reuse (presets), Protect (non-destructive), Trust (WYSIWYG) — production-quality & growth capabilities (see `0-enterprise-sos/3`). |

## Stakeholders & needs
| Element | Kind | Description |
|---|---|---|
| STK-1…STK-7 | stakeholder | Creator, Viewer, Privacy-conscious user, Maintainer/distributor, Mobile creator, Returning/interrupted creator, Growth-focused creator (vlogger/podcaster). |
| SN-1 | stakeholder need | Produce a clean watchable video from a raw recording without editing skill. |
| SN-2 | stakeholder need | Get a tight, well-ordered video with readable captions. |
| SN-3 | stakeholder need | Keep all media on the local machine (nothing uploaded). |
| SN-4 | stakeholder need | Free and dependency-light; runs anywhere. |
| SN-5 | stakeholder need | Add photos & audio, or replace the audio, with the simplest UX. |
| SN-6 | stakeholder need | Manipulate audio and video independently (threshold/objective MoP). |
| SN-7 | stakeholder need | Edit on Android / iOS. |
| SN-8 | stakeholder need | Never lose work — autosave/restore (incl. crash recovery), undo/redo, cancel/abort with clear errors. |
| SN-9 | stakeholder need | Keep the original recording untouched — non-destructive, reversible edits. |
| SN-10 | stakeholder need | Export in the right shape for the platform (aspect 16:9/9:16/1:1 + resolution preset). |
| SN-11 | stakeholder need | Captions in the spoken language + optional English translation. |
| SN-12 | stakeholder need | Trust the preview — WYSIWYG (preview = export). |
| SN-13 | stakeholder need | One-tap tighten — auto-remove filler words and long silences. |
| SN-14 | stakeholder need | Repurpose — extract short highlight clips + pick a cover frame. |
| SN-15 | stakeholder need | Chapters/timestamps auto-derived from topic segments. |
| SN-16 | stakeholder need | Clean audio — reduce noise/hum, even out speech. |
| SN-17 | stakeholder need | Follow with sound off — optional burned-in (open) captions. |
| SN-18 | stakeholder need | On-brand — optional intro/outro, title, lower-thirds, logo/watermark. |
| SN-19 | stakeholder need | Consistency — save/reuse a style preset across episodes. |

> Needs are stated **atomically** (one action · one object · one capability) as
> *"The ‹actor› needs to …"* in `1-problem-domain/black-box/1`; compound rows above
> are need *groups* split into sub-needs `SN-‹n›.‹m›` (e.g. SN-8 → SN-8.1 autosave,
> SN-8.2 undo/redo, SN-8.3 cancel). System requirements derive from the atomic sub-need.

## Use cases (black-box behavior)
| Element | Kind | Description |
|---|---|---|
| UC-1…UC-6 | use case | Upload, Auto-segment, Keep/drop, Re-order, Set transitions, Export. |
| UC-7…UC-10 | use case | Replace audio, Add audio, Add image clip, Level/mute tracks. |

## Measures of effectiveness (black-box parametrics)
| Element | Kind | Description |
|---|---|---|
| MOE-1 | «moe» | Simplicity — a non-expert completes raw→export unaided. |
| MOE-2 | «moe» | Privacy — bytes of media leaving the device (target 0, firm). |
| MOE-3 | «moe» | Watchability — consistent loudness and A/V sync. |
| MOE-4 | «moe» | Cost / portability — free, runs anywhere, portable document. |
| MOE-5 | «moe» | Creative control — keep/order/replace/add media. |
| MOE-6 | «moe» | Accessibility — captions present, correct, readable (0 mismatch, firm). |
| MOE-7 | «moe» | Reach — output fits target platforms & is followable sound-off / cross-language. |
| MOE-8 | «moe» | Engagement — tight pacing, strong hook, navigable (chapters). |
| MOE-9 | «moe» | Audio clarity — speech intelligible, low noise. |

## Functions (logical behavior)
| Element | Kind | Description |
|---|---|---|
| F-1…F-7 | function | Ingest, Demux, Transcribe, Segment&tag, Select, Sequence, Set-transition/flag-gaps. |
| F-8…F-14 | function | Render(cut+join), Re-time captions, Master loudnorm, Replace audio, Mix+duck, Synthesise image clip, Adjust track level/mute. |
| F-15…F-20 | function | Validate input, Manage session (autosave/restore), Undo/redo, Report progress/errors, Cancel/abort, Incremental re-render — surfaced by the behaviour brainstorm (`white-box/5`). |
| F-21…F-31 | function | Detect/trim filler+silence, Extract highlight+cover, Generate chapters, Clean audio, Reframe to aspect, Translate captions, Burn-in captions, Compose branding, Save/apply preset, Enforce non-destructive, WYSIWYG preview — surfaced by the conceptual-layer need elicitation (SN-9…SN-19). |

## System requirements (logical requirements)
| Element | Kind | Description |
|---|---|---|
| SR-1.1…SR-1.8 | system requirement | Built baseline: segment&tag, keep/order, render+transitions, re-time captions, loudness −16 LUFS, A/V sync, local-only HMI, output formats. |
| SR-2.1…SR-2.8 | system requirement | Media increment: demux, portable model, replace audio, add/mix audio, image clips, mix loudness, media endpoints, independent-manipulation MoP. |
| SR-3.1…SR-3.6 | system requirement | Robustness/session: validate-and-reject, autosave/restore, undo/redo, cancel+progress, invalidate-on-source-change, incremental re-render. |
| SR-4.1…SR-4.11 | system requirement | Production/growth ("ReelCut shall…"): non-destructive, aspect/preset, multilingual captions, WYSIWYG, auto-tighten, highlights+cover, chapters, clean audio, burned captions, branding, style presets. |

## Logical subsystems (logical structure)
| Element | Kind | Description |
|---|---|---|
| LS-Ingest | logical subsystem | Brings media in and demuxes into independent A/V tracks. |
| LS-Segment | logical subsystem | Runs ASR and segments/tags content by topic. |
| LS-EditModel | logical subsystem | Holds tracks/clips; applies keep/drop, order, transitions, track levels. |
| LS-Render | logical subsystem | Cuts and joins clips and synthesises image clips. |
| LS-AudioMix | logical subsystem | Mixes per-track audio and ducks under speech. |
| LS-Caption | logical subsystem | Re-times and invalidates captions. |
| LS-Master | logical subsystem | Two-pass loudness normalisation to −16 LUFS. |
| LS-HMI | logical subsystem | Local UI and API surface. |

## Physical components (physical structure)
| Element | Kind | Description |
|---|---|---|
| C-Probe / C-Demux / C-Segment | component | probe.py; demux (ext); segment.py — ingest & comprehension code. |
| C-Model | component | model.py — the editable track/clip model with portable handles. |
| C-Render / C-ImageSynth | component | render.py and its image-clip extension — composition code. |
| C-AudioMix | component | audio_mix.py — mixing/ducking code. |
| C-Caption / C-Master | component | captions.py and master.py — caption re-timing and loudness code. |
| C-Server / C-UI | component | server.py and static/ — the local HMI. |
| C-FFmpeg | external component | The FFmpeg/ffprobe binary invoked by the pipeline. |

## Component requirements & hardware constraints (physical requirements)
| Element | Kind | Description |
|---|---|---|
| CR-1…CR-8 | software requirement | Script-level shall-statements (render fold, loudness, caption remap, portable model, demux, caption invalidation, audio mix, image synth) — each verified by a test T-*. |
| HC-1 | hardware constraint | Mobile client runs on Android ≥ Galaxy S23 / iPhone 11+. |
| HC-2 | hardware constraint | Desktop runs on any machine with Python 3 + FFmpeg, no GPU. |

## Measures of performance (physical parametrics)
| Element | Kind | Description |
|---|---|---|
| MOP-1…MOP-3 | «constraint» / MoP | Loudness/true-peak, A/V-sync error, independent-manipulation level. |
| MOP-4…MOP-6 | «constraint» / MoP | Image default duration/motion, duck attenuation, caption integrity. |
| MOP-7…MOP-9 | «constraint» / MoP | Render time per minute, media egress bytes (0), runtime deps beyond stdlib+FFmpeg (0). |
| MOP-10…MOP-12 | «constraint» / MoP | Aspect/preset+caption availability (→MOE-7), filler-removed+chapters (→MOE-8), speech clarity/noise floor (→MOE-9). |

## Behaviours (logical behavior — see `white-box/5`)
| Element | Kind | Description |
|---|---|---|
| B-IN.* … B-SE.* | behaviour | Per-stage Nominal/Alternate/Exception/Edge flows for every stage (ingest, segment, curate, sequence, transition, re-media, mix, render, caption, master, deliver, session). |
| CB-1…CB-7 | reusable behaviour | Validate-and-Reject, Guard-Precondition, Retry-or-Abort, Invalidate-Derived-on-Source-Change, Incremental-Re-render, Undo/Redo, Autosave/Restore — the consolidated behavioural elements. |

## Verification (tests)
| Element | Kind | Description |
|---|---|---|
| T-1…T-7 | test | Built: reorder, keep/renumber, timing math, ffmpeg render, segment, caption remap, e2e/loudness. |
| T-8…T-11 | test | Planned (media): demux/portable-model, replace-audio, add-audio, image-clip. |
| T-12…T-16 | test | Planned (robustness): validate-input, autosave/restore, undo/redo, cancel/progress, incremental-render. |
| T-17…T-27 | test | Planned (production/growth): non-destructive, aspect/preset, multilingual-captions, WYSIWYG, auto-tighten, highlight-clip, chapters, clean-audio, burned-captions, branding, style-preset. |
</content>
</invoke>
