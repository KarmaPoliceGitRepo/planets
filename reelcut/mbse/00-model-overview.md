# ReelCut — MBSE Model (00 · Overview & Framework)

> **Method:** OMG **SysML** organised by the **MagicGrid** framework, applied per
> **NASA/MSFC "NASA MBSE Implementation"** (Plattsmier, 2019, NTRS 20190032390) and
> aligned to **NPR 7123.1** System Design processes. This model is the **single
> source of truth** (skill outputs are distilled into it).

## The MagicGrid (pillars × layers of abstraction)

Columns = SysML pillars; rows = layer of abstraction. Workflow follows the arrows
(left→right across a layer, then down).

| Layer ↓ / Pillar → | **Requirements** | **Behavior** | **Structure** | **Parametrics** |
|---|---|---|---|---|
| **Conceptual** (Black Box / *Stakeholder Needs Definition*) | Stakeholder Needs `1-problem-domain/black-box/1` | Use Cases `…/2` | **System Context (IBD)** `…/3` | Measurements of Effectiveness `…/4` |
| **Logical** (White Box / *Architecture Definition*) | System Requirements `…/white-box/1` | Functional Analysis `…/2` | Logical Subsystems Communication `…/3` | (MoE/MoP) |
| **Physical** (Solution / *Design Definition*) | Component Requirements (SW + HW) `2-solution-domain/1` | Component Behavior `…/2` | Component Structure `…/3` | Component Parameters (MoP) `…/4` |

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
├── 1-problem-domain/
│   ├── black-box/   1-stakeholder-needs · 2-use-cases · 3-system-context(IBD) · 4-measures-of-effectiveness
│   └── white-box/   1-system-requirements · 2-functional-analysis · 3-logical-subsystems
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
- **SN-** Stakeholder Need · **UC-** Use Case · **F-** Function · **MOE-** Measure of Effectiveness
- **SR-** System Requirement, stereotyped «functionalRequirement» / «interfaceRequirement» / «performanceRequirement» / «physicalRequirement»
- **LS-** Logical Subsystem · **I-** Interface Block · **MOP-** Measure of Performance
- **C-** Component (physical) · **CR-** Component (software) Requirement · **HC-** Hardware Constraint · **T-** Test (software-requirement verification)
- Requirement attributes (per p.15 «extendedRequirement»): `id · text · stereotype · status{Built|Planned} · verifyMethod{I|A|D|T} · risk · derivedFrom · refinedBy · satisfiedBy · priority(MoSCoW) · rationale`.

> **Migration note:** supersedes the earlier flat `01–06` model (which lacked the
> logical layer and function-derived requirements). Old → new: N-→SN-, FR/PR/IR/CR-
> (as *types*) → SR- with stereotypes; new logical + physical layers added.

Read **00 → 5**.
