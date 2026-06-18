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

## Stakeholder Needs (SN-)
| ID | Stakeholder | Need (shall) | Pri | Status | Derives |
|---|---|---|---|---|---|
| **SN-1** | STK-1 | Produce a clean, watchable video from a raw recording **without editing skill**. | M | Built | SR-1.x |
| **SN-2** | STK-2 | Get a **tight, well-ordered** video with **readable captions**. | M | Built | SR-1.x |
| **SN-3** | STK-3 | Keep all media **on the local machine** (nothing uploaded). | M | Built | SR (IR) |
| **SN-4** | STK-4 | **Free & dependency-light**, runs anywhere. | M | Built | SR (CR) |
| **SN-5** | STK-1 | **Add photos & audio, or replace the audio**, with the simplest possible UX. | M | Planned | SR-2.x |
| **SN-6** | STK-1 | **Manipulate audio and video independently** (MoP: *threshold* = constrained, *objective* = fully independent timelines). | M/C | Planned | SR-2.x |
| **SN-7** | STK-5 | Edit on **Android / iOS**. | C | Planned | HC-1 |
| **SN-8** | STK-6 | **Never lose work**: autosave & restore (incl. crash recovery), **undo/redo** edits, and **cancel/abort** any long operation with clear error feedback. | S | Planned | SR-3.x |
| **SN-9** | STK-1/STK-3 | Keep the **original recording untouched** — all edits non-destructive and reversible. | M | Planned | SR-4.1 |
| **SN-10** | STK-7 | Export in the **right shape for the platform** — aspect ratio {16:9, 9:16, 1:1} + resolution preset. | S | Planned | SR-4.2 |
| **SN-11** | STK-2 | Get captions in the **spoken language**, with optional **English translation**. | S | Planned | SR-4.3 |
| **SN-12** | STK-1 | **Trust the preview** — what is previewed is exactly what exports (WYSIWYG). | S | Planned | SR-4.4 |
| **SN-13** | STK-1 | **One-tap tighten** — auto-remove filler words ("um/uh") and long silences. | S | Planned | SR-4.5 |
| **SN-14** | STK-7 | **Repurpose** — pull short highlight clips (and choose a cover frame) from one long recording. | S | Planned | SR-4.6 |
| **SN-15** | STK-1/STK-2 | **Chapters** — auto timestamps from the topic segments for easy navigation. | C | Planned | SR-4.7 |
| **SN-16** | STK-1/STK-2 | **Clean audio** — reduce background noise/hum and even out speech. | S | Planned | SR-4.8 |
| **SN-17** | STK-2 | **Follow with sound off** — optional burned-in (open) captions for muted autoplay. | S | Planned | SR-4.9 |
| **SN-18** | STK-7 | **On-brand** — optional intro/outro, title card, lower-thirds, logo/watermark. | C | Planned | SR-4.10 |
| **SN-19** | STK-7 | **Consistency** — save & reuse a style preset across episodes. | C | Planned | SR-4.11 |

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
