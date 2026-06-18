# ReelCut — MBSE Model (06 · Parameters pillar)

> MagicGrid cells **B4** (Measurements of Effectiveness, black box) and **W4**
> (System Parameters / Measurements of Performance, white box). MoP **contribute
> to** MoE; the SysML `constraint` blocks below make those bindings explicit.
> Hard targets are firm now; soft targets are **TBD** (decision Q3-a).

## §B4 — Measures of Effectiveness (problem-level, solution-independent)

| ID | Effectiveness measure | From need | Target | Contributing MoP |
|---|---|---|---|---|
| **MOE-1** | **Simplicity** — a non-expert completes raw→export unaided. | N-1 | 0 docs read; ≤ **TBD** min | MOP-4 |
| **MOE-2** | **Privacy** — fraction of media leaving the device. | N-3 | **0** (firm) | MOP-8 |
| **MOE-3** | **Output watchability** — consistent loudness + correct sync. | N-2 | no desync; loudness on spec | MOP-1, MOP-2 |
| **MOE-4** | **Cost/portability** — free on commodity HW; portable to mobile. | N-4, N-19 | $0; portable doc | MOP-9 |
| **MOE-5** | **Creative control** — keep/reorder/replace/add media to realise intent. | N-13/14/15/16 | all ops available (threshold) | MOP-3 |
| **MOE-6** | **Accessibility** — captions present, correct, readable. | N-2 (STK-2) | SRT always; **0** mismatches | MOP-6 |

## §W4 — Measures of Performance (solution-level, measurable)

| ID | Parameter | Value / unit | St | Verify | Satisfies |
|---|---|---|---|---|---|
| **MOP-1** | Integrated loudness / true peak | **−16 LUFS ±1**, TP ≤ **−1 dBTP** (firm) | Built | T | PR-1 |
| **MOP-2** | A/V sync error across cuts/transitions | overlap-adjusted; ≤ **1 frame** | Built | A/T | PR-2 |
| **MOP-3** | Independent-manipulation level | **threshold** = constrained / **objective** = full | Planned | D | PR-3 |
| **MOP-4** | Image clip default duration / motion | **4 s** (editable); Ken-Burns **off** by default | Planned | T | FR-13 |
| **MOP-5** | Duck attenuation under speech | **TBD** dB (e.g. −9…−12) | Planned | T | FR-12 |
| **MOP-6** | Caption integrity on audio replace | **0** mismatched cues (firm) | Planned | T | FR-11 |
| **MOP-7** | Render time per minute of footage | **TBD** (commodity laptop) | Planned | A | FR-6 |
| **MOP-8** | Bytes of media egressing the device | **0** (firm) | Built | I/A | CR-1 |
| **MOP-9** | Runtime dependencies beyond stdlib+FFmpeg | **0** (Whisper optional) | Built | I | CR-2 |

## SysML v2 — parametric / constraint blocks (authoritative)
```sysml
// W4 performance constraints, bound to B4 effectiveness
constraint def LoudnessBudget {            // MOP-1
    in I_LUFS; in TP_dBTP;
    require { I_LUFS >= -17 and I_LUFS <= -15 and TP_dBTP <= -1 }
}
constraint def AVSyncBudget {              // MOP-2
    in syncError_ms; require { abs(syncError_ms) <= frameDuration_ms }
}
constraint def CaptionIntegrity {          // MOP-6 -> MOE-6
    in mismatchedCues; require { mismatchedCues == 0 }
}
constraint def PrivacyBudget {             // MOP-8 -> MOE-2
    in egressBytes; require { egressBytes == 0 }
}

// MoP --contributes to--> MoE  (effectiveness realised by performance)
binding MOP_1_Loudness   -> MOE_3_Watchability;
binding MOP_2_AVSync     -> MOE_3_Watchability;
binding MOP_6_Captions   -> MOE_6_Accessibility;
binding MOP_8_Egress     -> MOE_2_Privacy;
binding MOP_3_Independence-> MOE_5_CreativeControl;
binding MOP_4_ImageDur   -> MOE_1_Simplicity;
```

## Verification of parameters
Firm MoPs are verified by **Test** against the running pipeline (loudness via
`ffmpeg loudnorm` measurement; caption integrity via the re-time check; privacy/
dependencies by **Inspection/Analysis** of imports and network use). TBD targets
are set during Phase-3 design and then frozen here before their increment closes.
