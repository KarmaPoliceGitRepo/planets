# Logical · White Box · Requirements — System Requirements

> MagicGrid cell **Requirements / Logical**. Per your method: **functional**
> requirements are written **from the behaviour model** (the unique functions F-*,
> white-box `2`); **non-functional / performance** requirements come from **timing
> constraints of sequence diagrams and parametric models**; **interface** and
> **condition** requirements come from the **system context IBD / state machine**.
> SR **derive** from SN (`«deriveReqt»`) and are **refined by** functions (`«refine»`).

Stereotypes (p.16): «functionalRequirement» F · «interfaceRequirement» I ·
«performanceRequirement» P · «physicalRequirement» Ph. Attributes per p.15.

| ID | Stereo | Shall statement | refinedBy | derivedFrom | verify | St | Pri |
|---|---|---|---|---|---|---|---|
| **SR-1.1** | F | Split media into tagged segments & sub-sections. | F-4 | SN-1 | T | Built | M |
| **SR-1.2** | F | Keep/drop & re-order kept sub-sections. | F-5,F-6 | SN-1 | T | Built | M |
| **SR-1.3** | F | Render the chosen order with transitions. | F-8 | SN-1 | T | Built | M |
| **SR-1.4** | F | Re-time captions to the new sequence. | F-9 | SN-2 | T | Built | M |
| **SR-1.5** | P | Output audio = **−16 LUFS ±1, TP ≤ −1 dBTP**. | F-10 | SN-2 | T | Built | M |
| **SR-1.6** | P | A/V remain in sync across cuts & transitions. | F-8 | SN-2 | A/T | Built | M |
| **SR-1.7** | I | HMI over HTTP on **127.0.0.1**; media not uploaded. | — (ctx) | SN-3 | I | Built | M |
| **SR-1.8** | I | Output **H.264/AAC MP4, MP3 44.1 kHz, SubRip**. | F-8,F-10 | SN-2 | T | Built | M |
| **SR-2.1** | F | **Demux** input into independent A/V tracks. | F-2 | SN-6 | T | Planned | M |
| **SR-2.2** | F | First-class **portable, renderer-agnostic** project doc (stable media handles; no abs paths / FFmpeg strings). | F-2 | SN-6 | I/T | Planned | M |
| **SR-2.3** | F | **Replace audio**; invalidate/flag captions; offer re-transcribe. | F-11 | SN-5 | T | Planned | M |
| **SR-2.4** | F | **Add audio**: per-track level/mute + optional duck-under-speech. | F-12 | SN-5 | T | Planned | M |
| **SR-2.5** | F | **Add image clips** (still, editable dur 4 s, Ken-Burns off, no intrinsic audio). | F-13 | SN-5 | T | Planned | M |
| **SR-2.6** | P | Add/replace audio **preserves −16 LUFS** on the final mix & A/V sync. | F-10,F-12 | SN-2 | T | Planned | M |
| **SR-2.7** | I | Endpoints for replace/add audio & add image; accept PNG/JPG + MP3/WAV/M4A/AAC. | — (ctx) | SN-5 | T | Planned | M |
| **SR-2.8** | Ph | Independent-manipulation **MoP threshold/objective**. | F-6,F-14 | SN-6 | D | Planned | M/C |

```sysml
requirement def SR_1_5_Loudness {
    attribute stereotype = "performanceRequirement";
    attribute verifyMethod : VerificationMethodKind = Test;
    require constraint LoudnessBudget;          // parametric, solution-domain/4
}
refine F_10_Master    -> SR_1_5_Loudness;       // SR written FROM the function
deriveReqt SR_1_5_Loudness from SN_2_Watchable;
verify SR_1_5_Loudness by Test_T7;              // verified by behaviour/test
```
