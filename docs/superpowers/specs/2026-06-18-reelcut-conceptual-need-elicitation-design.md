# ReelCut MBSE — Conceptual-Layer Need Elicitation (design)

**Date:** 2026-06-18 · **Skill:** brainstorming → using-superpowers (cascade) ·
**Scope:** conceptual-layer needs + system-requirement rewrite. No product code (GATE-2 gated).

## Goal
From the conceptual layer (stakeholders, mission vignettes, MoE, system-context
actors), **elicit additional user needs** the model was missing — going wide into
vlogger/podcaster and audience psychology and SoI improvement levers — add them,
cascade, and **rewrite the system requirements in canonical "‹actor› shall …" form**.

## Elicited needs (added)
Approved seeds: SN-9 non-destructive, SN-10 platform-ready output, SN-11 multilingual
captions, SN-12 WYSIWYG. Wide brainstorm added:
- **SN-13 Auto-tighten** (filler words + silence) — biggest pacing win for talk content.
- **SN-14 Repurpose** (highlight clips + cover frame) — main audience-growth lever.
- **SN-15 Chapters** — reuses existing topic segments; long-form navigation.
- **SN-16 Clean audio** (denoise/dehum/level) — intelligibility gate (from DSP work).
- **SN-17 Sound-off captions** (burned-in/open) — most social video watched muted.
- **SN-18 Branding** (intro/outro, title, lower-thirds, logo) — recognition/consistency.
- **SN-19 Style presets** — per-episode effort down, channel consistency up.
New stakeholder **STK-7** (growth-focused creator). Folded (not needs): publish-fast →
MOE-1 + MOP-7; authenticity → constraint.

## Cascade
- Capabilities **CAP-12…CAP-21**; mission vignettes **MV-7 Grow/Repurpose**, **MV-8
  Polish/Brand**; coverage matrix shows every CAP owned by ≥1 need (SN-1…SN-19 complete).
- Measures **MOE-7 Reach / MOE-8 Engagement / MOE-9 Audio-clarity** with **MOP-10/11/12**.
- Functions **F-21…F-31**; system requirements **SR-4.1…SR-4.11** (all "ReelCut shall …",
  with risk + rationale); tests **T-17…T-27**; traceability, dictionary, diagrams updated.

## Requirement-form rewrite
All system requirements (SR-1.x / SR-2.x / SR-3.x / SR-4.x) rewritten into
**"ReelCut shall …"** (or "ReelCut shall let the creator …" where creator-initiated).
Scope per decision: **system requirements only** — CR-/HC- untouched.

## Out of scope / YAGNI
No product code. SR-4.x are Planned, mostly Should/Could priority. Branding (SN-18) and
presets (SN-19) kept explicitly optional to protect authenticity. Behaviour-model
detailing of SR-4.x deferred (would re-trigger the behaviour brainstorm at build time).

## Self-review
Placeholders: none (MOP-5/12 noise-floor targets marked TBD by design). Consistency:
SN-9…19 ↔ CAP-12…21 ↔ MOE-7/8/9 ↔ F-21…31 ↔ SR-4.x ↔ T-17…27 cross-checked in
traceability. Ambiguity: "platform preset" exact list is a GATE-2 design choice — noted.
</content>
</invoke>
