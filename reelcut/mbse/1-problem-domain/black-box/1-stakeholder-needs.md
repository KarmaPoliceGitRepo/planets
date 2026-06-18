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
