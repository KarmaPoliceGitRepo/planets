# 10 · Cross-Layer Traceability (four pillars, like-to-like, with decomposition, recursion, and a configuration join)

> **SE step:** make the System-of-Interest's traceability *formal and same-kind across
> every layer*, matching the framework already used in the ReelCut sub-model
> (`reelcut/mbse/8-cross-layer-traceability.md`, DECISIONS ADR-013). Until now this model
> carried a prose requirements-traceability matrix (`08-traceability-matrix.md`) that links
> *across* pillars (need→requirement→function→component→verify). This file adds the missing
> **like-to-like** threads that run *down the layers* within a single pillar —
> **requirement→requirement**, **structure→structure**, **behaviour→behaviour**,
> **parametric→parametric** — each with **within-layer decomposition `▽`**,
> **across-layer realization `⇒`**, applied **recursively**, and routed through a
> **Configuration** join. `08` stays the cross-pillar spine; `10` is the down-the-pillar spine.

## 10.0 Layers and the recursion rule

| # | Layer | Pillar homes |
|---|-------|--------------|
| L0 | **Enterprise / mission** | `00-concept-and-moe.md` (mission, MoE), `01-stakeholders.md` |
| L1 | **Conceptual** | `02-stakeholder-needs.md` (N-01…33, CN-G1…6) |
| L2 | **Logical / system** | `03-requirements.md` (FR/PR/UR/IR/CR), `05-functional-architecture.md` (F1…F10, M1…M5) |
| L3 | **Physical / solution** | `06-physical-architecture.md` (V1…V4 → V3; C0…C10) |
| L4 | **Implementation** | `reelcut/` (Studio subsystem) + repo `scripts/` |
| — | **Configuration (join)** | the selected variant **V3** binds the four threads across each hop (§10.6) |

**Recursion rule (every pillar, every level):** each element carries a *within-layer
decomposition* `▽` (parent → children of the same pillar/layer) and an *across-layer
realization* `⇒` (same-pillar element one layer down, routed via a Configuration item).
Applying `▽` then `⇒` from L0 to L4 yields a self-similar tree, traversable up (`⇐ trace`)
and down (`⇒ derive`) at any depth.

| Pillar | within-layer `▽` | across-layer `⇒` |
|--------|------------------|------------------|
| Requirements | `«containment»` (collective need ⊃ need; req ⊃ sub-req) | `«deriveReqt»` / `«trace»` |
| Structure | `«composition»` (system ⊃ component ⊃ part) | `«allocate»` / `«realize»` |
| Behaviour | `«decompose»` (function ⊃ sub-function) | `«refine»` |
| Parametric | constraint decomposition (MoE ⊃ sub-measure) | `«refine»` value binding |

---

## 10.1 Thread R — Requirement ⇄ Requirement

The collective (group) needs give this model a **real** within-layer requirement
decomposition that `08` did not make explicit: each collective need `CN-Gk` contains the
individual needs of its stakeholder group, which derive into the typed requirements.

```mermaid
flowchart TB
  subgraph L0[Mission]
    MOE1["MoE-1 Reach"]:::m
    MOE4["MoE-4 Quality"]:::m
  end
  subgraph L1[Conceptual needs — containment ▽]
    CNG2["CN-G2 Listeners (collective)"] --> N01["N-01 clear audio"]
    CNG2 --> N21["N-21 captions"]
    CNG1["CN-G1 Host (collective)"] --> N07["N-07 plan series"]
  end
  subgraph L2[System requirements — containment ▽]
    FR1["FR-1 capture clean audio"]
    PR1["PR-1 −16 LUFS / −1 dBTP"]
    FR6["FR-6 transcript + captions"]
    PR5["PR-5 ≥90% transcript accuracy"]
    FR1 -.->|prerequisite ▽| PR1
    FR6 -.->|prerequisite ▽| PR5
  end
  subgraph L3[Component allocation]
    PR1 ==>|deriveReqt ⇒ via V3| C4["C4 FFmpeg −16 LUFS"]
    PR5 ==>|deriveReqt ⇒ via V3| C5["C5 Whisper"]
  end
  MOE1 ==>|⇒| N01
  MOE4 ==>|⇒| N01
  N01 ==>|deriveReqt ⇒| FR1
  N01 ==>|deriveReqt ⇒| PR1
  N21 ==>|deriveReqt ⇒| FR6
  classDef m fill:#eef;
```

**Decomposition added:** `CN-G2 ▽ {N-01, N-21, …}` and `CN-G1 ▽ {N-07, …}` (collective→individual
need), plus the **requirement prerequisite** links `FR-1 ▽→ PR-1`, `FR-6 ▽→ PR-5` (you cannot
normalise loudness without captured audio; you cannot hit transcript accuracy without a transcript).

---

## 10.2 Thread S — Structure ⇄ Structure

```mermaid
flowchart TB
  SOI["L1  Podcast Production & Distribution System (SoI)"]
  SOI ==>|realize ⇒ V3| STUDIO["L3  V3 Integrated local Studio"]
  subgraph L3[Components — composition ▽]
    STUDIO --> C0["C0 Laptop (hub)"]
    STUDIO --> C1["C1 OBS (capture)"]
    STUDIO --> C2["C2 Audacity (edit)"]
    STUDIO --> C4["C4 FFmpeg (master/export)"]
    STUDIO --> C5["C5 Whisper (transcribe)"]
    STUDIO --> C7["C7 Spotify for Creators (host/RSS)"]
    STUDIO --> C9["C9 YouTube (video)"]
    STUDIO --> C10["C10 Studio UI (local web app)"]
  end
  subgraph L4[Implementation — composition ▽]
    C10 --> C4b["C4b DSP cleaner"]
    C10 --> C5b["C5b Segmenter"]
    C10 ==>|realize ⇒| REEL["reelcut/ Studio editor sub-model"]
  end
```

**Composition added:** `SoI ⇒ V3 ▽ {C0,C1,C2,C4,C5,C7,C9,C10}`; and the **Studio subsystem**
`C10 ▽ {C4b, C5b}` realized by `reelcut/` — the cross-model structural hand-off (the SoI's
component tree continues into the ReelCut structure thread, `reelcut/mbse §8.2`).

---

## 10.3 Thread B — Behaviour ⇄ Behaviour

```mermaid
flowchart TB
  subgraph L2[Functions — decomposition ▽]
    F4["F4 Edit (parent)"] --> F4b["F4b clean audio (DSP)"]
    F4 --> F4c["F4c segment + select"]
    F2["F2 Capture"]:::f
    F5["F5 Master"]:::f
  end
  subgraph L2m[Operating modes — behaviour context]
    M4["M4 Produce"]
  end
  F4 -. runs in .-> M4
  F5 -. runs in .-> M4
  subgraph L3[Component operations]
    F4b ==>|allocate ⇒| OP1["C4b: highpass→afftdn→compress"]
    F4c ==>|allocate ⇒| OP2["C5b: silencedetect→group→select"]
    F5 ==>|allocate ⇒| OP3["C4: loudnorm −16 LUFS"]
  end
  subgraph L4[Implementation behaviour]
    OP1 ==>|refine ⇒| S1["reelcut audio_mix.clean_audio()"]
    OP2 ==>|refine ⇒| S2["reelcut segment.segment()"]
    OP3 ==>|refine ⇒| S3["reelcut master.master()"]
  end
  classDef f fill:#efe;
```

**Decomposition added:** `F4 Edit ▽ {F4b clean, F4c segment}` (the §6.6 automation made these
real sub-functions), realized down to the ReelCut behaviour thread (`reelcut/mbse §8.3`).

---

## 10.4 Thread P — Parametric ⇄ Parametric

```mermaid
flowchart TB
  subgraph L0[MoE — constraint blocks]
    MOE4["MoE-4 Quality (parent)"] --> Q1["loudness conformance"]
    MOE4 --> Q2["caption accuracy"]
    MOE6["MoE-6 Portability"] --> P6a["no lock-in / RSS portable"]
  end
  subgraph L2[Performance requirements — refined constraints]
    Q1 ==>|refine ⇒| PR1["PR-1 = −16 LUFS, ≤ −1 dBTP"]
    Q2 ==>|refine ⇒| PR5["PR-5 ≥ 90% transcript accuracy"]
    P6a ==>|refine ⇒| CR6["CR-6 portable RSS / open formats"]
  end
  subgraph L3[Component capability — binding]
    PR1 -->|bind| B1["C4 FFmpeg loudnorm I=-16:TP=-1"]
    PR5 -->|bind| B2["C5 Whisper model accuracy"]
    CR6 -->|bind| B3["C7 RSS feed export"]
  end
  subgraph L4[Verified]
    B1 ==>|verify ⇒| V1["process_episode.sh PASS gate (−16 ±1)"]
    B2 ==>|verify ⇒| V2["transcript spot-check"]
  end
```

**Decomposition added:** `MoE-4 Quality ▽ {loudness, caption-accuracy}` → `{PR-1, PR-5}`; the
binding equation (`loudness == loudnorm(I=-16)`) is the constraint carried across the `⇒` hop,
identical to the parameter that the ReelCut parametric thread verifies (`reelcut/mbse §8.4`) —
i.e. the loudness MoP has **one definition** shared across both models.

---

## 10.5 Layers × Pillars closure

| Pillar | L0⇒L1 | L1 ▽ | L1⇒L2 | L2 ▽ | L2⇒L3 | L3 ▽ | L3⇒L4 |
|--------|------|------|------|------|------|------|------|
| Requirements | MoE⇒N | CN-G▽N ✅new | N⇒FR/PR | FR▽PR prereq ✅new | req⇒component | — | ⇒reelcut SR |
| Structure | SoI⇒V3 | — | V3▽C | C10▽C4b/C5b ✅new | C⇒parts | C10▽reelcut ✅new | ⇒reelcut C |
| Behaviour | — | — | F⇒op | F4▽F4b/F4c ✅new | op⇒script | — | ⇒reelcut op |
| Parametric | MoE▽ ✅new | — | MoE⇒PR | MoE▽sub ✅new | PR⇒capability | — | ⇒reelcut MoP |

✅new = like-to-like decomposition formalised by this file (was prose/implicit in `08`).

---

## 10.6 Configuration model — the join (and the cross-model recursion)

The trade study (§6.0) selected **V3 Integrated local Studio**. In configuration terms V3 is the
**root Configuration Item** of the SoI, binding the 4-tuple `⟨R, S, B, P⟩`:

```
CFG-Podcast(V3) = ⟨ R: FR/PR/UR/IR/CR satisfied at $0 with no lock-in,
                    S: components C0…C10,
                    B: functions F1…F10 across modes M1…M5,
                    P: −16 LUFS, ≥90% transcript, RSS-portable ⟩
```

It **decomposes** into per-stage configuration items (Capture, Edit, Master, Publish) mirroring the
component tree, and its **Edit/Studio** sub-configuration is realized by the ReelCut root
configuration — i.e. the recursion crosses the model boundary:

```mermaid
flowchart TB
  CFG["CFG-Podcast (V3 selected)"]
  CFG --> CAP["CFG-Capture (C1/C3)"]
  CFG --> EDIT["CFG-Edit/Studio (C10)"]
  CFG --> MAST["CFG-Master (C4)"]
  CFG --> PUB["CFG-Publish (C7/C9)"]
  EDIT ==>|realized by| RC["reelcut CFG-ReelCut (its own ⟨R,S,B,P⟩ join)"]
  RC -.->|variants| DESK["CFG-Desktop"]
  RC -.->|variants| MOB["CFG-Mobile"]
```

This makes the **system→implementation bridge** a configuration relationship, not a loose pointer:
the SoI's selected configuration `CFG-Podcast(V3)` contains, at its Edit/Studio node, the ReelCut
configuration `CFG-ReelCut` (`reelcut/mbse §8.6`), which itself decomposes into the Desktop/Mobile
variants. The four like-to-like threads therefore run **continuously from the podcast mission down
into the ReelCut implementation** through one chain of configuration joins.

---

## 10.7 Closure

- The cross-model loudness parameter (−16 LUFS / −1 dBTP) and transcript-accuracy target have a
  **single definition** shared by both models' parametric threads — change it in one place.
- `08-traceability-matrix.md` remains the cross-pillar RTM; this file is the down-the-pillar spine.
- A thread is **complete** when every L4 leaf traces `⇐` through one configuration per hop back to an
  L0 MoE/capability in the *same pillar*, and `⇒` back down, with no gap.

*Created 2026-06-24. Companion to `08-traceability-matrix.md` and to
`reelcut/mbse/8-cross-layer-traceability.md` (the realizing sub-model). Keep IDs consistent with
`03-requirements.md`, `05-functional-architecture.md`, and `06-physical-architecture.md`.*
