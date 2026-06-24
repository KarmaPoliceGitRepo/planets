# Conceptual · Black Box · Requirements — Stakeholder Needs

> MagicGrid cell **Requirements / Conceptual**. Per NPR 7123.1 *Stakeholder
> Expectations Definition*: user expectations are turned into **stakeholder needs**
> via a ConOps / mission-analysis step, then baselined here. Needs are **refined by**
> use cases and **derive** system requirements (`«deriveReqt»`, p.27 trace).

## Stakeholders
| ID | Stakeholder | Concern |
|---|---|---|
| STK-1 | Creator | make a clean, watchable video without editing skill |
| STK-2 | Viewer | tight, well-ordered video with readable captions |
| STK-3 | Privacy-conscious user | media never leaves the machine |
| STK-4 | Maintainer / distributor | free, dependency-light, runs anywhere |
| STK-5 | Mobile creator | edit on Android / iOS |
| STK-6 | Returning / interrupted creator | never lose work; undo mistakes; resume after closing or a crash |
| STK-7 | Growth-focused creator (vlogger / podcaster) | reach more audience: repurpose to shorts, captions for sound-off, on-brand & professional |
| STK-8 | Active consumer | find and play published content; navigate by metadata |
| STK-9 | Offline / background listener | listen audio-only, offline, in the background |
| STK-10 | Accessibility user | transcripts and screen-reader-friendly text, not just captions |
| STK-11 | Audio engineer / production team | meet platform technical specs (loudness, bitrate) |
| STK-12 | Enterprise / network creator | process episodes in bulk with a shared house style |
| STK-13 | Guest / subject-matter expert | be correctly attributed on screen |
| STK-14 | Advertiser / sponsor | have ad slots placed and labelled in the content |
| STK-15 | Hardware / gear ecosystem (Rode, Shure, Sony, Apple…) | have recorder file formats ingested and run on common OS |
| STK-16 | Copyright / licensing body | avoid unlicensed audio in published output |
| STK-17 | Government regulator (GDPR / CCPA / accessibility) | no personal-data collection; accessible output |
| STK-18 | Social / interfacing platform (X, Instagram, TikTok) | receive shareable, correctly-shaped exports with a cover image |

### Parked / out-of-SoI stakeholders (registered for completeness; no buildable ReelCut need)

> INCOSE: identify all stakeholders, but derive needs only inside the System-of-Interest
> boundary. ReelCut's SoI is a **local, offline, single-user editor**. The stakeholders
> below belong to the **streaming-platform** system, not ReelCut; each is registered with
> the reason no need is derived. Revisit only if the SoI is ever re-baselined to a platform.

| ID | Stakeholder | Why no ReelCut need (Parked / Rejected) |
|---|---|---|
| STK-P1 | Shareholders / corporate leadership | Platform ROI/growth; ReelCut's product owner is STK-4. **Parked.** |
| STK-P2 | ML / recommendation engineer | Needs behavioural/telemetry data — **directly conflicts SN-3** (zero egress). ReelCut emits no telemetry. **Rejected.** |
| STK-P3 | Cloud / CDN provider | Local tool; no streaming/delivery infrastructure. **Parked.** |
| STK-P4 | Trust & safety / moderation | ReelCut does not host or distribute content. **Parked.** |
| STK-P5 | Enterprise team-access / bulk-upload API | Single-user local app; multi-tenant API is a different system. **Parked (deferred).** |
| STK-P6 | Premium billing (ad-free / DRM) | No accounts, payments, or DRM in a local tool. **Rejected.** |

## Stakeholder Needs (SN-)

> **Atomic form (one action · one object · one capability per need).** Each need
> reads *"The ‹stakeholder› needs to ‹single action› ‹single object›."* Compound
> expectations are split into sub-needs (`SN-‹n›.‹m›`); the parent number is the
> *need group* a system requirement derives from, the sub-need is the atomic unit.

| ID | Stakeholder | Need — *"The ‹actor› needs to …"* | Pri | Status | Derives |
|---|---|---|---|---|---|
| **SN-1** | Creator | The creator needs to produce a finished video from a raw recording. | M | Built | SR-1.1 |
| **SN-2.1** | Viewer | The viewer needs to have dead air trimmed from the video. | M | Built | SR-1.2 |
| **SN-2.2** | Viewer | The viewer needs to have the sub-sections arranged in a chosen order. | M | Built | SR-1.2 |
| **SN-2.3** | Viewer | The viewer needs to read captions on the video. | M | Built | SR-1.4 |
| **SN-2.4** | Viewer | The viewer needs to hear the audio at a consistent loudness. | M | Built | SR-1.5 |
| **SN-2.5** | Viewer | The viewer needs to have the audio kept in sync with the video. | M | Built | SR-1.6 |
| **SN-3** | Privacy-conscious user | The privacy-conscious user needs to keep all media on the local machine. | M | Built | SR-1.7 |
| **SN-4.1** | Maintainer | The maintainer needs to use the tool free of cost. | M | Built | SR (CR) |
| **SN-4.2** | Maintainer | The maintainer needs to run the tool with minimal dependencies. | M | Built | SR (CR) |
| **SN-4.3** | Maintainer | The maintainer needs to run the tool on any common OS. | M | Built | HC-2 |
| **SN-5.1** | Creator | The creator needs to add an image clip to the edit. | M | Planned | SR-2.5 |
| **SN-5.2** | Creator | The creator needs to add an audio track to the edit. | M | Planned | SR-2.4 |
| **SN-5.3** | Creator | The creator needs to replace the audio of the edit. | M | Planned | SR-2.3 |
| **SN-6** | Creator | The creator needs to manipulate the audio track independently of the video track. | M/C | Planned | SR-2.1 |
| **SN-7** | Mobile creator | The mobile creator needs to edit on a mobile device. | C | Planned | HC-1 |
| **SN-8.1** | Returning creator | The returning creator needs to have the project autosaved and restored. | S | Planned | SR-3.2 |
| **SN-8.2** | Returning creator | The returning creator needs to undo and redo an edit. | S | Planned | SR-3.3 |
| **SN-8.3** | Returning creator | The returning creator needs to cancel a running operation. | S | Planned | SR-3.4 |
| **SN-9** | Creator | The creator needs to keep the original recording unmodified. | M | Planned | SR-4.1 |
| **SN-10.1** | Growth-focused creator | The growth-focused creator needs to export the video in a target aspect ratio. | S | Planned | SR-4.2 |
| **SN-10.2** | Growth-focused creator | The growth-focused creator needs to export the video at a target resolution preset. | S | Planned | SR-4.2 |
| **SN-11.1** | Viewer | The viewer needs to read captions in the spoken language. | S | Planned | SR-4.3 |
| **SN-11.2** | Viewer | The viewer needs to read captions translated into English. | S | Planned | SR-4.3 |
| **SN-12** | Creator | The creator needs to see a preview that matches the export. | S | Planned | SR-4.4 |
| **SN-13.1** | Creator | The creator needs to remove filler words from the audio. | S | Planned | SR-4.5 |
| **SN-13.2** | Creator | The creator needs to remove long silences from the timeline. | S | Planned | SR-4.5 |
| **SN-14.1** | Growth-focused creator | The growth-focused creator needs to extract a highlight clip from the recording. | S | Planned | SR-4.6 |
| **SN-14.2** | Growth-focused creator | The growth-focused creator needs to choose a cover frame for the video. | S | Planned | SR-4.6 |
| **SN-15** | Viewer | The viewer needs to navigate the video by chapter markers. | C | Planned | SR-4.7 |
| **SN-16.1** | Viewer | The viewer needs to have background noise reduced in the audio. | S | Planned | SR-4.8 |
| **SN-16.2** | Viewer | The viewer needs to hear speech levelled to a consistent volume. | S | Planned | SR-4.8 |
| **SN-17** | Viewer | The viewer needs to read captions burned into the video. | S | Planned | SR-4.9 |
| **SN-18.1** | Growth-focused creator | The growth-focused creator needs to add an intro/outro to the video. | C | Planned | SR-4.10 |
| **SN-18.2** | Growth-focused creator | The growth-focused creator needs to add a title card to the video. | C | Planned | SR-4.10 |
| **SN-18.3** | Growth-focused creator | The growth-focused creator needs to add lower-thirds to the video. | C | Planned | SR-4.10 |
| **SN-18.4** | Growth-focused creator | The growth-focused creator needs to add a logo/watermark to the video. | C | Planned | SR-4.10 |
| **SN-19.1** | Growth-focused creator | The growth-focused creator needs to save a style preset. | C | Planned | SR-4.11 |
| **SN-19.2** | Growth-focused creator | The growth-focused creator needs to apply a saved preset to a new project. | C | Planned | SR-4.11 |
| **SN-20.1** | Audio engineer | The audio engineer needs to set the export's target loudness. | S | Planned | SR-1.5 |
| **SN-20.2** | Audio engineer | The audio engineer needs to set the export's target bitrate. | C | Planned | SR-4.2 |
| **SN-21** | Accessibility user | The accessibility user needs to export a full transcript file. | S | Planned | SR-5.1 |
| **SN-22** | Offline / background listener | The offline listener needs to export an audio-only MP3. | S | Built | SR-1.8 |
| **SN-23** | Guest / SME | The guest needs to be credited by an on-screen name attribution. | C | Planned | SR-4.10 |
| **SN-24** | Enterprise / network creator | The enterprise creator needs to batch-export multiple episodes with one preset. | C | Planned | SR-5.2 |
| **SN-25** | Advertiser / sponsor | The advertiser needs to mark mid-roll ad-insertion points in the timeline. | C | Planned | SR-4.7 |
| **SN-26** | Hardware / gear ecosystem | The gear maker needs ReelCut to ingest its recorder's WAV/MP4 files. | M | Planned | SR-3.1 |
| **SN-27** | Social / interfacing platform | The social platform needs ReelCut to export a cover thumbnail image. | C | Planned | SR-4.6 |
| **SN-28** | Copyright / licensing body | The licensing body needs ReelCut to flag audio not marked royalty-free. | C | Planned | SR-5.3 |
| **SN-29** | Government regulator | The regulator needs ReelCut to collect zero personal data. | M | Built | SR-1.7 |
| **SN-30** | Active consumer | The active consumer needs ReelCut to embed title and chapter metadata in the export. | C | Planned | SR-5.4 |

## ConOps (one line)
A creator records on a phone/camera, opens ReelCut locally, and goes
**upload → auto-segment → keep/order → add or replace media → export** to a
finished MP4/MP3/SRT — never leaving their machine. Mobile (SN-7) is a future
client over the same portable project document.

```sysml
requirement def SN_5_AddOrReplaceMedia {
    doc /* simplest-UX media add/replace */
    attribute status = "Planned"; attribute priority = "Must";
}
// needs are refined by use cases and derive system requirements
refine UC_7_ReplaceAudio    -> SN_5_AddOrReplaceMedia;
deriveReqt SR_2_1_Demux from SN_6_IndependentManipulation;
```


## Cross-layer like-to-like links (ADR-013)

> Mirrors this file's rows from the cross-layer spine (`../../../8-cross-layer-traceability.md`).
> `▽` = within-layer decomposition · `⇒` = across-layer realization (routed via a Configuration item).

| Link | Type | From | To |
|------|------|------|----|
| SN-5 ▽ {SN-5.1, SN-5.2, SN-5.3} | ▽ containment | SN-5 add/replace media | SN-5.1 add image · SN-5.2 add audio · SN-5.3 replace audio |
| SN-5.x ⇒ SR-2.x | ⇒ deriveReqt (via CFG-Edit) | conceptual need | logical system requirement |
