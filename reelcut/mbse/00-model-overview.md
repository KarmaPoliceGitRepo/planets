# ReelCut — MBSE Model (00 · Overview & Framework)

> **Method:** OMG **SysML** (language) organised by the **MagicGrid** framework
> (Dassault Systèmes / Morkevicius). **Single source of truth (G-2):** this
> `reelcut/mbse/` model. Skill outputs (brainstorming spec, writing-plans) are
> transient drafts distilled into here.

## Conformance statement (read this first)
This model **conforms to MagicGrid's structure** (four SysML pillars ×
Problem/Solution domains) and uses **SysML semantics** for relations
(`satisfy`, `derive`, `refine`, `allocate`). Because the repo has no SysML
authoring tool, notation is **hybrid (decision Q5-c)**:
- **Authoritative**, rigor-critical elements — requirements, ports/interfaces,
  and the Parameters pillar (parametric/constraint blocks) — are written in
  **SysML v2 textual notation** (```sysml fenced blocks).
- **Illustrative** views — context, use-case, state, sequence, BDD/IBD — are
  **Mermaid renderings** and are *non-normative*; the tables are normative.

## MagicGrid index — every cell has a home

| Pillar → / Domain ↓ | **Requirements** | **Behavior** | **Structure** | **Parameters** |
|---|---|---|---|---|
| **Black box (Problem)** | **B1** Stakeholder Needs → `01 §B1` | **B2** Use Cases → `02` | **B3** System Context → `03 §B3` | **B4** MoE → `06 §B4` |
| **White box (Solution)** | **W1** System Requirements → `01 §W1` | **W2** System Behaviour → `04` | **W3** System Structure → `03 §W3` | **W4** System Parameters / MoP → `06 §W4` |
| **Implementation** | code under `reelcut/app/` (allocated via W3) | — | — | — |

**Traceability** (closes the loop need→req→function→block→parameter→verification)
→ `05`. Verification tests → `reelcut/tests/`.

## ID scheme & attributes
- **STK-** stakeholder · **N-** stakeholder need (B1) · **UC-** use case (B2) ·
  **MOE-** measure of effectiveness (B4) · **FR/PR/IR/CR-** system requirement (W1) ·
  **A-** activity/state (W2) · **B-** block (W3) · **MOP-** measure of performance (W4) ·
  **T-** test. (N-5…N-9 are **reserved**; IDs are stable by decision Q2-a.)
- **Every W1 requirement carries:** Text · Cell · **Status** {Built \| Planned} ·
  **Verify** {I=Inspection, A=Analysis, D=Demonstration, T=Test} · **From** (derived-from) ·
  **Alloc** (allocated-to block) · **Pri** (MoSCoW: M/S/C/W) · Rationale.

## Block → code map (W3 allocation)
```
B-1 Web UI            → app/static/        B-8  Master            → app/pipeline/master.py
B-2 Local Server      → app/server.py      B-9  FFmpeg (external) → system binary
B-3 Edit Model        → app/model.py       B-10 Track/Clip Model  → app/model.py (extended)   [Planned]
B-4 Probe             → app/pipeline/probe.py   B-11 Image-clip Synth → app/pipeline/render.py (ext) [Planned]
B-5 Segmenter         → app/pipeline/segment.py B-12 Audio Mixer/Ducker → app/pipeline/audio_mix.py  [Planned]
B-6 Render Engine     → app/pipeline/render.py  B-13 Demux/Ingest     → app/pipeline/probe.py (ext)  [Planned]
B-7 Caption Re-timer  → app/pipeline/captions.py
```

## Status legend
**Built** = implemented & tested today. **Planned** = designed here (media-tracks v2:
needs N-11…N-19), not yet implemented; gated behind GATE 2 approval.

Read in order **00 → 06**. Start the product with `../run.sh`.
