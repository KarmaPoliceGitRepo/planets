# ReelCut MBSE — Behaviour-Model Enrichment (design)

**Date:** 2026-06-18 · **Skill:** brainstorming (mandatory for behaviour scope) ·
**Scope:** the `reelcut/mbse/` behaviour models only — no product code (GATE-2 not crossed).

## Problem
The model's behaviour views were **happy-path only**: each use case, activity,
sequence and the state machine modelled the nominal flow. Concept definition lacked
**session** concerns (lose-work / resume). Behaviour completeness — the case where
brainstorming is mandatory — was not met.

## Decisions (from the brainstorming dialogue)
1. **Concept:** add the full session behaviour set — autosave/restore (incl. crash
   recovery), undo/redo, cancel/abort — as first-class concept (new **SN-8**,
   **MV-6**, **CAP-11 Sustain**).
2. **Depth:** model behaviours **end-to-end across all three behaviour views** —
   activity (behaviours + flow), interaction/sequence (entity interactions), and
   an overall-context state machine — with all alternate/exception/edge elements.
3. **Scope:** cover **Built + Planned** (SR-1.x and SR-2.x), plus the new SR-3.x.

## What was produced
- **`white-box/5-behaviour-catalogue.md`** — every stage's Nominal/Alternate/
  Exception/Edge behaviours (B-IN.* … B-SE.*), consolidated into **CB-1…CB-7**
  (Validate-and-Reject, Guard-Precondition, Retry-or-Abort,
  Invalidate-Derived-on-Source-Change, Incremental-Re-render, Undo/Redo,
  Autosave/Restore).
- **New functions F-15…F-20** (validate, manage-session, undo/redo, report
  progress/errors, cancel/abort, incremental re-render) and an **end-to-end
  activity diagram** with branches in `white-box/2`.
- **`white-box/6-interaction-model.md`** — 7 sequence diagrams with alt/opt/loop
  fragments (ingest+validate, segment+fallback, curate+undo, replace-audio+
  invalidate, add-audio+duck, render+retry/cancel, autosave/restore).
- **`white-box/7-state-model.md`** — overall end-to-end state machine (composite
  states + error/recovery) plus a **concurrent persistence/history region**
  (autosave + undo/redo) that runs throughout the session.
- **Requirements SR-3.1…SR-3.6** (validate, autosave/restore, undo/redo,
  cancel+progress, invalidate-on-source-change, incremental re-render) with risk +
  rationale, plus tests **T-12…T-16**.
- Traceability (SN-8 thread + SR-3.x cross-pillar rows), element dictionary, and
  overview updated. **32/32 diagrams render green.**

## Out of scope / YAGNI
- No product code — these are design artifacts; implementation stays gated.
- Speaker diarisation (B-SG.3) and manual caption editing (B-CP.3) are recorded as
  behaviours but flagged future; no requirements forced for them.

## Self-review
Placeholders: none. Consistency: SR-3.x ↔ F-15…F-20 ↔ CB-1…CB-7 ↔ tests T-12…T-16
cross-check in the traceability matrix. Scope: bounded to behaviour models.
Ambiguity: pad/trim policy for replace-audio length mismatch (B-RA.3/4) is left as a
design choice for GATE-2 — explicitly noted, not silently assumed.
</content>
</invoke>
