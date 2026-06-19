# ReelCut — MBSE Model (00 · Overview & Framework)

> **Position in the bigger model — read first.** ReelCut is **not** a standalone
> system. It is the **implementation-layer System-of-Interest** selected by the
> **podcast** system's physical-layer trade study (variant **V3 — Integrated local
> Studio**; see
> [`../../podcast-the-missing-link/01-systems-engineering/06-physical-architecture.md`](../../podcast-the-missing-link/01-systems-engineering/06-physical-architecture.md)
> §6.0). The real System-of-Interest is the **Missing Link Podcast Production &
> Distribution System**; ReelCut realises its local **Studio editor** subsystem
> (components C4b DSP-clean + C5b Segmenter + C10 Studio UI). This model details
> that subsystem. The cross-layer requirement bridge is in §00.1 below.

> **Method:** OMG **SysML** organised by the **MagicGrid** framework, applied per
> **NASA/MSFC "NASA MBSE Implementation"** (Plattsmier, 2019, NTRS 20190032390) and
> aligned to **NPR 7123.1** System Design processes. This model is the **single
> source of truth** (skill outputs are distilled into it).

## 00.1 Cross-layer bridge — podcast requirements → ReelCut needs/requirements

The podcast system allocates the editing/mastering/captioning functions (F4, F4b,
F4c, F5, F6, F7) to the Studio solution; the requirements behind those functions are
the **parent** requirements this ReelCut model refines:

| Podcast requirement (parent) | Realised by ReelCut |
|---|---|
| FR-3 non-destructive edit (cut/trim/re-order/denoise) | SN-1, SN-2.1/2.2, SN-9, SN-13; SR-1.1/1.2, SR-4.1/4.5 |
| PR-1 loudness −16 LUFS / −1 dBTP · PR-2 noise floor | SN-2.4, SN-16; SR-1.5, SR-4.8 |
| FR-5 export MP3 + MP4 · IR-3 H.264/AAC | SN-1; SR-1.8 |
| FR-6 transcript + `.srt` captions | SN-2.3, SN-11, SN-21; SR-1.4, SR-4.3, SR-5.1 |
| UR-1/UR-4 beginner, single-action local UI | SN-1, SN-12; SR-1.7 (127.0.0.1 HMI), SR-4.4 |
| CR-6 no lock-in / portable project | SN-9; SR-2.2 |

These podcast requirements are the upward trace target; everything below in this
model traces back to them (and through them to the podcast needs N-xx).

## The MagicGrid (pillars × layers of abstraction)

Columns = SysML pillars; rows = layer of abstraction. Workflow follows the arrows
(left→right across a layer, then down).

| Layer ↓ / Pillar → | **Requirements** | **Behavior** | **Structure** | **Parametrics** |
|---|---|---|---|---|
| **Enterprise / SoS** (*Mission Analysis*) | Mission UCs → Capabilities → derived Needs `0-enterprise-sos/3` | SoS activities & perspectives `…/4` | **SoS Context BDD + IBD** `…/1`,`…/2` | (mission effectiveness → MoE) |
| **Conceptual** (Black Box / *Stakeholder Needs Definition*) | Stakeholder Needs `1-problem-domain/black-box/1` | Use Cases `…/2` | **System Context (IBD)** `…/3` | Measurements of Effectiveness `…/4` |
| **Logical** (White Box / *Architecture Definition*) | System Requirements `…/white-box/1` | Functional Analysis `…/2` + **Behaviour Catalogue `…/5` + Interaction `…/6` + State Model `…/7`** (+ dynamics `…/4`) | Logical Subsystems Communication `…/3` | (MoE/MoP) |
| **Physical** (Solution / *Design Definition*) | Component Requirements (SW + HW) `2-solution-domain/1` | Component Behavior `…/2` | Component Structure `…/3` | Component Parameters (MoP) `…/4` |

> **Enterprise/SoS layer (top):** the SoI is first a **black-box node** inside the
> **System of Systems** — surrounded by external/environment nodes (incl. iPhone &
> Android). Mission vignettes → mission use cases → **capabilities** → **derive the
> stakeholder needs** bottom-up, validating the Conceptual baseline below.

- **Conceptual:** stakeholder needs → … → **system requirements**.
- **Logical:** system requirements → … → **system-element (component) requirements**.
- **Physical:** component requirements → **hardware + software requirements**; the
  **scripts** under `reelcut/app/` are the physical realisation and the means of
  **verifying the software requirements**; **hardware requirements are constraints**
  (e.g. *runs on Android ≥ Galaxy S23 / iPhone 11*).

## Package structure (mirrors NTRS 20190032390 p.10)
```
reelcut/mbse/
├── 00-model-overview.md
├── 0-enterprise-sos/  1-sos-context-and-bdd · 2-sos-ibd-exchanges · 3-mission-use-cases-to-needs · 4-actors-perspectives-activities
├── 1-problem-domain/
│   ├── black-box/   1-stakeholder-needs · 2-use-cases · 3-system-context(IBD) · 4-measures-of-effectiveness
│   └── white-box/   1-system-requirements · 2-functional-analysis · 3-logical-subsystems · 4-system-behavior-dynamics(seq+state)
├── 2-solution-domain/
│   └── 1-component-requirements · 2-component-behavior · 3-component-structure · 4-component-parameters
├── 3-system-configuration.md      (top-level system: structural + behavioural features)
├── 4-implementation-domain.md     (scripts ↔ software-requirement verification; HW constraints)
├── 5-traceability.md
└── diagrams/                      (rendered SVGs, mirroring the cells)
```

## Relationships (SysML, applied per your rules)
| Relation | Rule used here |
|---|---|
| **«deriveReqt»** | **requirement → requirement only.** User needs →(ConOps/mission analysis)→ Stakeholder Needs (SN) → System Requirements (SR) → Component Requirements (CR/HW). |
| **«refine»** | a **behaviour/use-case/function refines a requirement or need** (SR are *written from* functions). |
| **«satisfy»** | a **white-box structural element satisfies a requirement**. |
| **«verify»** | a requirement is **verified by behaviour or structure** of system components (logical subsystems) — realised as tests / analysis. |
| **«allocate»** | a **behaviour is allocated to a structure in the same abstraction layer**; a structure allocates to a structure. Allocation implies *complete inheritance of scope* — decompose a behaviour until a part can be allocated **in its entirety** to one structure. |
| **«value binding»** | a parametric value binds to a structural value property (MoE/MoP). |

## ID scheme (NASA-style: prefix = layer, stereotype = type)
- **MV-** Mission Vignette · **MUC-** Mission Use Case · **CAP-** Capability *(Enterprise/SoS)*
- **SN-** Stakeholder Need · **UC-** Use Case · **F-** Function · **MOE-** Measure of Effectiveness
- **SR-** System Requirement, stereotyped «functionalRequirement» / «interfaceRequirement» / «performanceRequirement» / «physicalRequirement»
- **LS-** Logical Subsystem · **I-** Interface Block · **MOP-** Measure of Performance
- **C-** Component (physical) · **CR-** Component (software) Requirement · **HC-** Hardware Constraint · **T-** Test (software-requirement verification)
- Requirement attributes (per p.15 «extendedRequirement»): `id · text · stereotype · status{Built|Planned} · verifyMethod{I|A|D|T} · risk · derivedFrom · refinedBy · satisfiedBy · priority(MoSCoW) · rationale`.

> **Migration note:** supersedes the earlier flat `01–06` model (which lacked the
> logical layer and function-derived requirements). Old → new: N-→SN-, FR/PR/IR/CR-
> (as *types*) → SR- with stereotypes; new logical + physical layers added.

Every modeled element has a one-line description in **`6-element-dictionary.md`**
(the data dictionary) and its **full property set, value types and signals** in
**`7-properties-and-types.md`** (with compartment diagrams). Every MagicGrid cell —
across all four pillars and all four layers — has a rendered diagram in `diagrams/`
(32 SVGs, incl. property compartments under `diagrams/types/` and the full
**behaviour model** — end-to-end activity, per-use-case interaction/sequences, and
the orthogonal end-to-end state machine — under `diagrams/logical/`).

> **Behaviour-model rule (CLAUDE.md):** behaviour scope is enriched/completed via
> the `brainstorming` skill. The behaviour catalogue (`white-box/5`) enumerates all
> Nominal/Alternate/Exception/Edge flows per stage and consolidates them into
> reusable behaviours (CB-1…CB-7).

Read **00 → 7** (white-box `1 → 7`).
