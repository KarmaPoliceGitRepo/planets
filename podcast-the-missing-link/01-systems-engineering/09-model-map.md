# 9 · Model Map (diagrams)

> One-picture views of the whole model. Source of truth = the Mermaid blocks below;
> rendered SVGs live in [`../diagrams/`](../diagrams/) (run `../diagrams/render.sh`).
> Diagrams are illustrative; the authoritative text is in `00`–`08`.

## 9.1 Lifecycle through-line (concept → implementation)

```mermaid
flowchart TD
  subgraph CONCEPT["Conceptual layer"]
    M["Mission"] --> MOE["MoE-1..6"]
    MOE --> N["Needs N-01..N-33 (+ collective CN-G1..6)"]
  end
  subgraph SYSTEM["System layer (problem domain)"]
    N --> R["Requirements FR / PR / UR / IR / CR"]
    R --> CO["ConOps modes M1..M5"]
    R --> F["Functions F1..F10"]
  end
  subgraph PHYS["Physical / solution layer"]
    F --> TS["Trade study: variants V1..V4"]
    TS --> SEL["Select V3 Integrated Studio"]
    SEL --> C["Components C1..C10 (+C4b/C5b)"]
  end
  subgraph IMPL["Implementation layer"]
    SEL --> RC["reelcut/mbse: Studio editor subsystem"]
    C --> SCR["scripts/ + studio/"]
  end
  C --> VV["V&V: verify reqs + validate MoE"]
  VV -.->|validates| MOE
```

## 9.2 Traceability spine (no orphans, bidirectional)

```mermaid
flowchart LR
  MOE["MoE"] --> N["Need"] --> REQ["Requirement"] --> FN["Function"] --> CMP["Component"] --> VER["Verify"]
  VER -.->|validates| MOE
```

## 9.3 Stakeholder groups -> collective needs (many-to-many)

```mermaid
flowchart LR
  S8["S8 Platforms"] --> G4["G4 Financial"]
  S8 --> G5["G5 Technical"]
  S8 --> G6["G6 Regulatory"]
  S5["S5 Guests"] --> G2["G2 Originators"]
  S5 --> G3["G3 Subjects"]
  S2["S2 Listeners"] --> G1["G1 Audience"]
  G1 --> CN1["CN-G1 find/play/follow"]
  G2 --> CN2["CN-G2 produce at zero cost"]
  G3 --> CN3["CN-G3 fair representation"]
  G4 --> CN4["CN-G4 verifiable reach"]
  G5 --> CN5["CN-G5 compatible, no lock-in"]
  G6 --> CN6["CN-G6 lawful + shareable"]
```

## 9.4 Solution trade study (physical layer)

```mermaid
flowchart TD
  SC["Solution class: Local-first podcast toolchain"]
  SC --> V1["V1 GUI"]
  SC --> V2["V2 CLI scripts"]
  SC --> V3["V3 Integrated Studio"]
  SC --> V4["V4 Paid all-in-one"]
  V4 -->|fails K1 cost gate| X["eliminated"]
  V1 --> SCORE["score vs K1..K6"]
  V2 --> SCORE
  V3 --> SCORE
  SCORE --> PICK["V3 selected (score 12)"]
  PICK --> RC["realised by reelcut/mbse"]
```

## 9.5 Cross-layer bridge (podcast requirement -> reelcut)

```mermaid
flowchart LR
  subgraph POD["Podcast SoI (system)"]
    FR3["FR-3 edit"]
    PR1["PR-1 loudness"]
    FR6["FR-6 transcript"]
    CR6["CR-6 no lock-in"]
  end
  subgraph RC["reelcut SoI (implementation)"]
    SR11["SR-1.1 segment"]
    SR15["SR-1.5 -16 LUFS"]
    SR43["SR-4.3 captions"]
    SR22["SR-2.2 portable doc"]
  end
  FR3 --> SR11
  PR1 --> SR15
  FR6 --> SR43
  CR6 --> SR22
```

➡️ Back to the spine: [`08-traceability-matrix.md`](08-traceability-matrix.md).
