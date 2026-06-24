# 8 — Cross-Layer Traceability (four pillars, like-to-like, with decomposition, recursion, and a configuration join)

> **Purpose.** Give the model *complete like-to-like traceability through every layer of
> abstraction*, separately for each SysML pillar:
> **requirement→requirement**, **structure→structure**, **behaviour→behaviour**,
> **parametric→parametric**. Each thread runs top-to-bottom across the abstraction layers,
> uses **decomposition** within a layer and **realization/derivation** across layers, and is
> applied **recursively** at every level. Cross-layer hops are mediated by an explicit
> **Configuration** element (the intermediate "join") so the four threads stay coherent and
> we avoid an N×N tangle of direct links.
>
> This file is the authoritative *cross-layer* spine. `5-traceability.md` remains the
> *within-layer / cross-pillar* spine (SN→SR→CR→F→LS→C→T and MoP→MoE). The two are
> complementary: 5 = "across pillars at a level"; 8 = "down one pillar through the levels".

---

## 8.0 Abstraction layers (the vertical axis)

The same five layers carry all four threads. A sixth element — **Configuration** — is **not**
a layer but a *join that sits on each inter-layer edge* (see §8.6).

| # | Layer | Role | Pillar homes (files) |
|---|-------|------|----------------------|
| L0 | **Enterprise / SoS** | mission context | `0-enterprise-sos/*` |
| L1 | **Conceptual (black-box)** | problem space; needs, MoE | `1-problem-domain/black-box/*` |
| L2 | **Logical (white-box)** | solution-independent architecture | `1-problem-domain/white-box/*` |
| L3 | **Physical (solution)** | chosen components, MoP | `2-solution-domain/*` |
| L4 | **Implementation** | code modules, tests | `4-implementation-domain.md`, `reelcut/app/**` |
| —  | **Configuration (join)** | binds the four threads across each L*n*→L*n+1* hop | `3-system-configuration.md` + §8.6 |

### Recursion rule (uniform at every level, every pillar)

Every element `E` in any pillar carries exactly two kinds of like-to-like link:

1. **Decomposition (within a layer):** `E ▽ {E.1, E.2, …}` — a parent decomposes into children of
   the *same pillar and same layer*. The relation is pillar-specific (`containment` for
   requirements, `composition` for structure, `call-behaviour` for behaviour, `constraint
   decomposition` for parametric).
2. **Realization (across one layer):** `E ⇒ E'` — `E` at layer L*n* is realized/derived by `E'` of
   the *same pillar* at layer L*n+1*, **routed through a Configuration item** (§8.6).

Applying *(1)* then *(2)* recursively from L0 to L4 yields a self-similar tree:
`SoS ▽… ⇒ Conceptual ▽… ⇒ Logical ▽… ⇒ Physical ▽… ⇒ Implementation`.
The pattern is identical at depth 1 (System) and depth *k* (a leaf part/operation/parameter), which
is what makes the model traversable in both directions at any depth.

### Relation vocabulary (extends the keywords already in use)

| Pillar | Within-layer decomposition `▽` | Across-layer realization `⇒` |
|--------|-------------------------------|------------------------------|
| Requirements | `«containment»` (parent req ⊃ sub-req) | `«deriveReqt»` down · `«trace»` up |
| Structure | `«composition»` (block ⊃ part) | `«allocate»` / `«realize»` (logical→physical) |
| Behaviour | `«decompose»` (activity ⊃ call-behaviour) | `«refine»` (function realized by lower behaviour) |
| Parametric | constraint decomposition (`«constraint»` ⊃ sub-constraint) | `«refine»` value-binding (MoE→MoP→value) |

`«deriveReqt» «refine» «satisfy» «allocate» «verify» «contributes» bind` were already present
(see `5-traceability.md`); this file adds the **`▽` decomposition** links that were missing and the
**Configuration-routed `⇒`** semantics.

---

## 8.1 Thread R — Requirement ⇄ Requirement (down every layer)

Like-to-like requirement chain. Cross-layer derivation already existed (SN→SR→CR); the new content
is the **within-layer decomposition** `▽` (parent needs/requirements) that was previously implicit
in `x.y` numbering only.

### R-thread cross-layer chain (realization `⇒`, routed via CFG)

| L0 capability | L1 need | L2 system req | L3 component req | L4 module/test |
|---------------|---------|---------------|------------------|----------------|
| CAP-3 trim/segment | SN-1, SN-3 | SR-1.1, SR-1.2 | CR-2 | `segment.py` / T-5 |
| CAP-9 loudness | SN-2.4, SN-16 | SR-1.5, SR-4.8 | CR-7 | `master.py` / T-7 |
| CAP-12 add media | SN-5 | SR-2.3, SR-2.4, SR-2.5 | CR-6 | `audio_mix.py` / T-phase2 |
| CAP-7 captions | SN-21 | SR-4.3, SR-4.9 | CR-4 | `captions.py` / T-phase8 |
| CAP-2 privacy/egress=0 | SN-2 | SR-2.7 (no-upload) | HC-2 | `server.py` bind 127.0.0.1 |

### R-thread within-layer decomposition `▽` (NEW — fills the flat-namespace gap)

```mermaid
flowchart TB
  subgraph L1[Conceptual needs]
    SN5["SN-5 add/replace media (parent)"]
    SN5 --> SN51["SN-5.1 add image"]
    SN5 --> SN52["SN-5.2 add audio"]
    SN5 --> SN53["SN-5.3 replace audio"]
  end
  subgraph L2[Logical system reqs]
    SR2x["SR-2.x media set (parent)"]
    SR2x --> SR23["SR-2.3 replace audio"]
    SR2x --> SR24["SR-2.4 add audio"]
    SR2x --> SR25["SR-2.5 add image"]
    SR21["SR-2.1 demux"] -.->|prerequisite ▽| SR22["SR-2.2 portable doc"]
    SR22 -.->|prerequisite ▽| SR23
  end
  SN51 ==>|deriveReqt ⇒ via CFG-Edit| SR25
  SN52 ==>|deriveReqt ⇒ via CFG-Edit| SR24
  SN53 ==>|deriveReqt ⇒ via CFG-Edit| SR23
```

**Decomposition added:** `SN-5 ▽ {SN-5.1, SN-5.2, SN-5.3}`; `SR-2.x ▽ {SR-2.3, SR-2.4, SR-2.5}`;
plus the **SR→SR prerequisite** ordering `SR-2.1 ▽→ SR-2.2 ▽→ SR-2.3` (a within-layer like-to-like
link that was only prose before). Each `⇒` hop is labelled with its mediating Configuration item.

---

## 8.2 Thread S — Structure ⇄ Structure (down every layer)

Like-to-like structural decomposition. `«allocate»` LS→C existed; the new content is the
**composition tree** (`«composition»`) so every block names its parts at every level — recursion.

```mermaid
flowchart TB
  SoS["L0  ReelCut_SoS (block)"]
  SoS ==>|realize ⇒| SYS["L1  ReelCut System (context block)"]
  subgraph L2[Logical subsystems — composition ▽]
    SYS ==>|realize ⇒| ING["LS-Ingest"]
    SYS ==> SEG["LS-Segment"]
    SYS ==> EDM["LS-EditModel"]
    SYS ==> RND["LS-Render"]
    SYS ==> AUD["LS-AudioMix"]
    SYS ==> CAP["LS-Caption"]
    SYS ==> MAS["LS-Master"]
    SYS ==> HMI["LS-HMI"]
  end
  subgraph L3[Physical components — composition ▽]
    ING -->|allocate ⇒| CProbe["C-Probe"]
    ING --> CDemux["C-Demux"]
    SEG --> CSeg["C-Segment"]
    EDM --> CModel["C-Model"]
    RND --> CRender["C-Render"]
    AUD --> CAudio["C-AudioMix"]
    CAP --> CCap["C-Caption"]
    MAS --> CMaster["C-Master"]
    HMI --> CServer["C-Server"]
    HMI --> CUI["C-UI"]
    CRender --> CFFmpeg["C-FFmpeg (shared engine)"]
  end
  subgraph L4[Implementation modules]
    CDemux -->|realize ⇒| Mdemux["app/pipeline/demux.py"]
    CSeg --> Mseg["app/pipeline/segment.py"]
    CModel --> Mmodel["app/model.py"]
    CRender --> Mrender["app/pipeline/render.py"]
    CMaster --> Mmaster["app/pipeline/master.py"]
    CServer --> Mserver["app/server.py"]
  end
```

**Composition added (the missing `▽`):** `ReelCut System ▽ {LS-Ingest…LS-HMI}`;
`LS-Ingest ▽ {C-Probe, C-Demux}`, `LS-HMI ▽ {C-Server, C-UI}`, etc. The previous model had the 8
LS and 12 C as flat siblings; they are now a part-of tree realized down to modules.

---

## 8.3 Thread B — Behaviour ⇄ Behaviour (down every layer)

Like-to-like behaviour decomposition: mission vignette → use case → function → sub-function →
component operation → script function. `UC→F` existed; the new content is the **function
decomposition tree** (`F ▽ F`) and the explicit operation/method realization.

> **MBSE rule compliance.** The behaviour decomposition below was enumerated with the
> `brainstorming` skill (happy / alternate / exception / edge flows) per the repo's MBSE
> behaviour-completeness rule before being written here. See DECISIONS.md ADR-013.

```mermaid
flowchart TB
  MV3["L0 MV-3 'cut to highlight reel'"]
  MV3 ==>|refine ⇒| UC2["L1 UC-2 Auto-segment"]
  subgraph L2[Functions — decomposition ▽]
    UC2 ==>|refine ⇒| F4["F-4 segment media (parent)"]
    F4 --> F4a["F-4.1 detect silences"]
    F4 --> F4b["F-4.2 group into sub-sections"]
    F4 --> F4c["F-4.3 tag keep/drop default"]
    CB1["CB-1 Validate-and-Reject"] -.->|reused by| F4
  end
  subgraph L3[Component operations]
    F4a -->|allocate ⇒| Odetect["C-Segment.detect_silences()"]
    F4b --> Ogroup["C-Segment.group()"]
    F4c --> Otag["C-Model.set_keep()"]
  end
  subgraph L4[Script functions]
    Odetect -->|realize ⇒| Sdetect["tighten.detect_silences()"]
    Ogroup --> Sgroup["segment.build_segments()"]
    Otag --> Stag["model.set_keep()"]
  end
```

**Decomposition added (the missing `▽`):** every L2 function that is non-atomic now names its
children, e.g. `F-4 ▽ {F-4.1 detect, F-4.2 group, F-4.3 tag}`, recursively down to the script
function that realizes each leaf. Reusable behaviours `CB-1…CB-7` attach as `«include»` at the leaf
that uses them.

---

## 8.4 Thread P — Parametric ⇄ Parametric (down every layer)

Like-to-like parametric refinement: Measure of Effectiveness → Measure of Performance → component
value property → measured/asserted value. `MoP «contributes» MoE` and `bind` existed; the new
content is the **constraint-block decomposition** so each MoE names the sub-constraints/MoPs that
compose it, recursively, with the binding equation carried at every level.

```mermaid
flowchart TB
  subgraph L1[MoE — constraint blocks]
    MOE9["MOE-9 Audio clarity (parent constraint)"]
    MOE9 --> MOE9a["loudness conformance"]
    MOE9 --> MOE9b["true-peak headroom"]
  end
  subgraph L3[MoP — refined constraints]
    MOE9a ==>|refine ⇒| MOP1["MOP-1 loudness = −16 ±1 LUFS"]
    MOE9b ==>|refine ⇒| MOP1b["MOP-1b truePeak ≤ −1 dBTP"]
  end
  subgraph L_cfg[Configuration value properties]
    MOP1 -->|bind| V1["ReelCut.loudness : LUFS"]
    MOP1b -->|bind| V2["ReelCut.truePeak : dBTP"]
  end
  subgraph L4[Measured / asserted]
    V1 -->|verify ⇒| T7["master.py pass-gate −17..−15"]
    V2 --> T7b["truePeak assert ≤ −1"]
  end
  MOE2["MOE-2 Privacy"] ==>|refine ⇒| MOP8["MOP-8 egressBytes = 0"] -->|bind| V3["ReelCut.egressBytes = 0"] -->|verify ⇒| Tnet["no-socket egress test"]
```

**Decomposition added (the missing `▽`):** `MOE-9 ▽ {loudness, true-peak}` refined to
`{MOP-1, MOP-1b}`; the binding equation (`loudness == loudnorm(I=-16)`) is the constraint carried
across the `⇒` hop. `MOE-2 Privacy ⇒ MOP-8 egressBytes=0` makes the privacy MoE measurable.

---

## 8.5 Layers × Pillars × link-type — closure summary

| Pillar | L0⇒L1 | L1▽ | L1⇒L2 | L2▽ | L2⇒L3 | L3▽ | L3⇒L4 |
|--------|------|-----|------|-----|------|-----|------|
| Requirements | CAP⇒SN | SN▽SN.x ✅new | SN⇒SR | SR▽SR ✅new | SR⇒CR | CR▽ | CR⇒module |
| Structure | SoS⇒Sys | — | Sys⇒LS | LS▽C ✅new | LS⇒C | C▽part ✅new | C⇒module |
| Behaviour | MV⇒UC | — | UC⇒F | F▽F.x ✅new | F⇒op | op▽ | op⇒script |
| Parametric | — | MoE▽ ✅new | MoE⇒MoP | MoP▽ ✅new | MoP⇒value | — | value⇒test |

✅new = like-to-like decomposition link introduced by this file (previously flat/implicit).
Every `⇒` is routed through a Configuration item (§8.6).

---

## 8.6 Configuration model — the inter-layer join

A **Configuration Item (CFG)** is the intermediate element that carries all four threads across one
abstraction hop. Instead of linking a requirement directly to a component (cross-pillar) or a
logical block directly to a physical block (cross-layer), each hop **binds a 4-tuple**:

```
CFG = ⟨ R : requirement-set satisfied,
        S : structure variant chosen,
        B : behaviour allocation,
        P : parameter values that meet the MoP ⟩
```

This makes the trade-study selection explicit at the join: the chosen `S` (e.g. variant V3) is the
reason a given `R` is realized by a given physical element with given `P`. A CFG at layer *n*
**decomposes** into CFGs at layer *n+1* (recursion), mirroring the structure tree.

### Configuration baseline tree (recursion example)

```mermaid
flowchart TB
  CFGroot["CFG-ReelCut (root baseline)"]
  CFGroot --> CFGedit["CFG-Edit (ingest+segment+model)"]
  CFGroot --> CFGrender["CFG-Render (render+master)"]
  CFGroot --> CFGmedia["CFG-Media (audio+image+caption)"]
  CFGroot --> CFGhmi["CFG-HMI (server+ui)"]
  CFGroot -.->|variant| CFGdesktop["CFG-Desktop (pywebview+PyInstaller, bundled FFmpeg)"]
  CFGroot -.->|variant| CFGmobile["CFG-Mobile (RN + ffmpeg-kit) — HC-1, SR-2.7"]
```

### Two configuration variants (closes the 'no post-selection variants' gap)

| CFG variant | R (requirements in scope) | S (structure) | B (behaviour) | P (parameters) | Status |
|-------------|---------------------------|---------------|---------------|----------------|--------|
| **CFG-Desktop** | all SR-1..5 + CR-1..8 | C-Server + C-UI + C-FFmpeg bundled (ADR-009) | full function set F-1..35 | egressBytes=0, loudness=−16 | Built |
| **CFG-Mobile** | SR-2.7 + subset (no batch); HC-1 hardware constraint | RN shell + ffmpeg-kit (ADR-010, WV-001) | render subset, on-device | egressBytes=0 preserved | Planned (best-effort, WV-002) |

Each variant is a leaf configuration that **selects** which structure realizes the in-scope
requirements with which parameters — the same `⟨R,S,B,P⟩` join applied recursively. `CFG-Desktop`
and `CFG-Mobile` share `CFG-Edit`/`CFG-Render`/`CFG-Media` and differ only at `CFG-HMI` + engine,
which is exactly what the structure tree (§8.2) predicts.

---

## 8.7 Closure / how this stays honest

- **Drift-check** (`.claude/hooks/drift-check.sh`) validates that every `▽` decomposition parent and
  every CFG 4-tuple element referenced here resolves to a defined ID (no dangling like-to-like link),
  in addition to the existing fence-parity and SN/F resolution checks.
- **Source of truth** remains the Mermaid blocks here + the element dictionary (`6-element-dictionary.md`);
  re-render via `diagrams/render.sh`.
- A like-to-like thread is **complete** when, for every leaf at L4, you can walk `⇐` (trace up) through
  one CFG per hop back to an L0 capability/MoE in the *same pillar* — and `⇒` back down — with no gap.

*Created 2026-06-24. Companion to `5-traceability.md` (cross-pillar) and `3-system-configuration.md`
(configuration block). Keep IDs consistent with the element dictionary.*
