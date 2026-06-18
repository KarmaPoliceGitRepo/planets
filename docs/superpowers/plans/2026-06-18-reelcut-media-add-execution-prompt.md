# ReelCut media-add + mobile — sequential execution prompt (guard)

> Status: approved guard prompt (working artifact). The authoritative design lives
> in `reelcut/mbse/` (single source of truth — N-18). This file is the execution
> checklist's controlling prompt, refined via a `/grilling` session on 2026-06-18.
> Decisions captured as needs N-10…N-19 (see `reelcut/mbse/01-requirements-model.md`).

```text
## Objective
Evolve ReelCut (local-first editor under reelcut/) so audio and video are demuxed into
independent tracks that can be replaced/added/levelled, plus add image clips — simplest UX —
and run a mobile-port FEASIBILITY survey. NEEDS-FIRST: lock & MBSE-trace user needs before any
solution design; no implementation until the MBSE cascade is approved.

## Context (carry forward — established, do not re-derive)
- ReelCut: local-first (127.0.0.1), Python-stdlib backend (app/server.py) + vanilla-JS wizard
  (app/static/) + pipeline app/pipeline/{probe,segment,render,captions,master}.py. Render is
  TWO-STAGE; transitions xfade/acrossfade with overlap-adjusted offsets; captions re-timed;
  master = two-pass loudnorm -16 LUFS. Segments & captions derive FROM the source audio.
- MBSE is the SINGLE SOURCE OF TRUTH: reelcut/mbse/ (00 overview, 01 reqs STK-/N-/FR-/PR-/IR-/CR-,
  02 UC-, 03 blocks B-, 04 behaviour A-, 05 traceability->tests T-). Skill outputs (brainstorming
  spec, writing-plans) are TRANSIENT drafts distilled into MBSE; only a lightweight implementation
  checklist persists under docs/superpowers/plans/, keyed to MBSE IDs.
- Approved needs from grilling (N-10…N-19): needs-approved-before-design (N-10); demux to
  independent A/V tracks (N-11); first-class extensible track/clip model (N-12); independent
  manipulation MoP threshold=constrained (spoken sub-sections A/V-locked) / objective=fully
  independent timelines (N-13); replace audio invalidates/flags captions, offer re-transcribe
  (N-14); add audio = mix + level/mute + optional duck-under-speech (N-15); image clips = stills,
  4s default, Ken-Burns off-by-default, no intrinsic audio, existing reorder UX (N-16); preserve
  -16 LUFS + two-stage invariants (N-17); MBSE single source of truth (N-18); mobile availability
  Android/iOS (N-19, feasibility-first).
- Skills: brainstorming, writing-plans, graphify, using-superpowers, grill-me.

## Execute IN ORDER. Do NOT cross a gate without my explicit "approved".

PHASE 0 — Orient (no changes)
- Read KNOWLEDGE.md, reelcut/README.md, reelcut/mbse/*, and segment/render/captions/master + UI.
- Output a 5-line map of where demux / tracks / replace-audio / add-audio / images touch the
  current architecture. Continue.

PHASE 1 — Lock the NEEDS (intent only, not solution)  [GATE 1]
- Confirm/refine user needs N-10…N-19 (purpose, constraints, MoPs) — NOT implementation detail.
  IN PARALLEL: a SUBAGENT produces a short MOBILE FEASIBILITY brief (native / Flutter-RN /
  PWA-wrapper; where FFmpeg runs on-device; what breaks vs desktop) to surface constraints that
  should shape the needs. (No formal mobile plan yet.)
- Distill agreed needs into reelcut/mbse/01-requirements (+ stakeholders/use-cases as needed).
- STOP. Present the MBSE needs diff + feasibility brief; wait for "approved".

PHASE 2 — MBSE cascade + solution design (design only)  [GATE 2]
- From approved needs, cascade in reelcut/mbse/: requirements (FR-/PR-/IR-/CR-), use-cases (UC-),
  structure (B-: track/clip model, image-clip synthesiser, audio-mix/duck, demux), behaviour (A-),
  traceability (req->block->behaviour->test). Keep IDs + Mermaid consistent.
- writing-plans -> implementation CHECKLIST at docs/superpowers/plans/, keyed to MBSE IDs, sliced
  into the increments below. Defer the formal mobile plan (feasibility-only for now).
- STOP. Present MBSE diff + checklist; wait for "approved".

PHASE 3 — Implement MEDIA FEATURE in ordered increments  [after GATE 2]
Ship each independently; verify with real FFmpeg; extend reelcut/tests/ (test_reelcut.py +
run_e2e.sh); trace to MBSE IDs; preserve two-stage render, -16 LUFS, caption rules. Do NOT
implement the mobile port.
  1. Demux / track-clip data model — done when: input splits into A/V tracks AND all existing
     tests still pass.
  2. Replace audio — done when: swapping the audio track renders + masters to -16 LUFS AND captions
     are invalidated/flagged (re-transcribe offered).
  3. Add audio (mix + optional duck) — done when: a 2nd track mixes with per-track level/mute,
     optional duck works, final mix = -16 LUFS.
  4. Image clips — done when: a still inserts as an orderable item with editable duration + optional
     Ken-Burns and renders correctly in sequence.

## Scope
- Work only in: reelcut/, docs/superpowers/, KNOWLEDGE.md.
- Do NOT touch: podcast-the-missing-link/, .claude/skills/, anything outside the above.

## Constraints
- Local-first, dependency-light (Python stdlib + FFmpeg); no new runtime dependency without asking.
- Preserve two-stage render, -16 LUFS master, caption re-timing. Keep MoP-objective reachable
  (first-class tracks) but build only the threshold now.
- Only what each phase/increment requires; no extra features/files. Record each crossed gate via graphify.

## Acceptance Criteria (binary)
- [ ] Needs N-10…N-19 captured + approved in reelcut/mbse (GATE 1).
- [ ] Full MBSE cascade consistent + traced, plan checklist keyed to IDs, approved (GATE 2).
- [ ] Increments 1–4 each meet their "done when" with passing FFmpeg-verified tests.
- [ ] -16 LUFS, two-stage render, and caption-handling invariants hold throughout.

## Stop Conditions — stop and ask before:
- Crossing GATE 1 or GATE 2 without my "approved".
- Writing ANY implementation code before Phase 3.
- Implementing the mobile port (feasibility/plan only).
- Adding a dependency, deleting a file, or touching anything outside Scope.

## Progress
After each step: [what was done] — [file(s)] — [phase/increment + next gate].
```
