# Project Knowledge (graphify store)

> Durable project memory maintained by the `graphify` skill. Agents read this for
> context and append durable facts here. Keep entries terse; date decisions.
> Never write secrets, tokens, or personal data here — this file is committed and shared.
>
> **Companion file:** `DECISIONS.md` at the repo root holds the **Decision Log (ADRs)**,
> **accepted concessions/waivers**, and the **RAID register**. `KNOWLEDGE.md` = facts &
> architecture; `DECISIONS.md` = *why* and *what is still open*. Both auto-load each session.

## Overview
`planets` (GitHub: `KarmaPoliceGitRepo/planets`) hosts two things: (1) reusable **Claude Code
skills** under `.claude/skills/`, and (2) a complete **MBSE model + working software** for a free,
beginner-friendly **podcast production & distribution system** ("The Missing Link").

- The **System-of-Interest** is the **Missing Link Podcast Production & Distribution System**
  (`podcast-the-missing-link/`).
- **ReelCut** (`reelcut/`) is its **implementation-layer Studio editor subsystem** — a local-first,
  distributable video editor with its own full SysML/MagicGrid model (`reelcut/mbse/`), a Python
  pipeline (`reelcut/app/`), and desktop (`reelcut/desktop/`) + mobile (`reelcut/mobile/`) shells.

## Architecture
- **Skills** live in `.claude/skills/<name>/SKILL.md` (YAML frontmatter + Markdown body),
  auto-discovered in this repo.
- **Durable memory**: `KNOWLEDGE.md` (facts) + `DECISIONS.md` (decisions/waivers/RAID), both
  auto-injected each session by a `SessionStart` hook in `.claude/settings.json`.
- **Harness rules** (`.claude/settings.json` hooks): `SessionStart` loads both memory files;
  `Stop` runs `.claude/hooks/drift-check.sh` and surfaces its status; `UserPromptSubmit` injects the
  persistent caveman + drift-check + maintain-`DECISIONS.md` rules every turn. Rules also documented
  in `CLAUDE.md`.
- **podcast-the-missing-link/** (the SoI): `01-systems-engineering/` (`00-concept-and-moe` … `08`
  RTM, `09-model-map`, **`10-cross-layer-traceability`**), `02-implementation/`, `03-content/`,
  `scripts/` (FFmpeg master, Whisper, studio UI), `diagrams/` (rendered SVGs).
- **reelcut/** (the implementation SoI): `mbse/` (`0-enterprise-sos/` … `4-implementation-domain`,
  `5-traceability`, `6-element-dictionary`, `7-properties-and-types`, **`8-cross-layer-traceability`**;
  `diagrams/` SVGs), `app/` (stdlib `server.py` on 127.0.0.1 + `pipeline/` modules), `desktop/`
  (pywebview + PyInstaller), `mobile/` (React Native + ffmpeg-kit), `tests/` (unittest).
- **Traceability — two complementary spines per model:** the **cross-pillar RTM**
  (need→requirement→function→component→verify; `podcast …/08`, `reelcut/mbse/5-traceability`) and the
  **down-the-pillar cross-layer** spine (requirement→requirement, structure→structure,
  behaviour→behaviour, parametric→parametric; `podcast …/10`, `reelcut/mbse/8-cross-layer-traceability`),
  with within-layer decomposition `▽`, across-layer realization `⇒`, recursion, and a **configuration
  join** `CFG-Podcast(V3) → CFG-ReelCut → {Desktop, Mobile}` (DECISIONS ADR-013).
- **CI**: `.github/workflows/build.yml` — unittest suite on Ubuntu+FFmpeg, plus desktop
  (macOS/Windows PyInstaller) and best-effort mobile binary builds.

## Decisions
- 2026-06-24 — **SysML model completed to the HARD-rule standard + completeness report (ADR-014).**
  Audited both models (every element must have named+described structural & behavioural features and
  ≥1 relationship; all diagrams render). **ReelCut** verified compliant (37 diagrams; every element
  described in its defining table — the `6-element-dictionary.md` is only a partial index). **Podcast
  SoI** was prose/RTM, not formal SysML, so added three files: `11-formal-structure.md` (component +
  SoI blocks with ports/operations/value-properties, interface blocks I-Mic…I-Backup, function I/O
  flows, value-type catalogue, component BDD + context IBD), `12-formal-behaviour.md` (use-case,
  activity, state-machine with modes M1–M5 as states, sequence; behaviours enumerated
  nominal/alt/exception/edge), `13-parametrics-and-requirements.md` (MoE as constraint blocks +
  parametric & requirements diagrams; orphans K1–K6/modes/CFG linked; N-28 numbering gap documented).
  18 podcast diagrams render (`render.sh` refactored). Both models now compliant; **55 SVGs total, 0
  failures.** Findings written to `MBSE-COMPLETENESS-REPORT.md` at the repo root. Pipeline followed:
  plan → review plan → execute → review → complete.
- 2026-06-24 — **Durable Decision Log + RAID register created and persisted (`DECISIONS.md`).** New
  root file = Decision Log (ADRs), accepted concessions/waivers/deviations, and the RAID register
  (Risks/Assumptions/Issues/Dependencies) + tech-debt register. Made persistent like the
  caveman/drift rules: `SessionStart` hook auto-loads it; `UserPromptSubmit` hook injects a
  maintain-it-same-commit rule; `CLAUDE.md` documents the rule (read first, never delete entries —
  change Status). Seeded with ADR-001…013, waivers WV-001…005, RAID, TD-1…3. Motivation: a
  multi-hour review's findings had lived only in chat and were lost to `/compact` + container
  reclaim — this file makes such findings durable. Commits `7ccc3c1`, `d970714`.
- 2026-06-24 — **Four-pillar like-to-like cross-layer traceability (ADR-013), both models.** Added
  the down-the-pillar spine to ReelCut (`reelcut/mbse/8-cross-layer-traceability.md`) and the podcast
  SoI (`podcast-the-missing-link/01-systems-engineering/10-cross-layer-traceability.md`). Each of the
  four SysML pillars is traced same-kind through every abstraction layer with within-layer
  decomposition `▽` + across-layer realization `⇒`, applied recursively, and **routed through a
  Configuration item binding `⟨R,S,B,P⟩`** (the inter-layer join). The configuration join chains
  `CFG-Podcast(V3) → CFG-ReelCut → {CFG-Desktop, CFG-Mobile}`, so the threads run continuously from
  the podcast mission into the ReelCut implementation. Closes the model-map gaps (flat namespaces, no
  config variants, podcast prose-RTM-only). `drift-check.sh` now also asserts the four threads + the
  config join are present; both `render.sh` scripts emit the new per-pillar diagrams (all green).
  Commits `73fedc7` (reelcut), `f77136f` (podcast).
- 2026-06-24 — **ReelCut defect-level code review completed and fully resolved**
  (`reelcut/CODE-REVIEW-2026-06-24.md`). Four parallel reviewers over `app/**` (~1,700 LOC) found
  ~50 issues; deduplicated to 12 HIGH / 12 MED / ~11 LOW. Final state: **0 open** — 10 HIGH fixed +
  2 verified-correct (CR-H9 ducking and CR-H10 A/V crossfade were false positives, proven correct by
  a golden test), 12 MED fixed, 11 LOW fixed. Highlights: security hardening in `server.py`
  (project-dir path confinement, Host-header guard vs DNS-rebinding, `/static/` resolve+symlink
  guard, upload cap) and `audio_mix.py` (`level_db` validated before the filtergraph); correctness
  (real source-sha256 baseline so the SR-4.1 guard fires; atomic autosave; `threading.Event`
  CancelToken; drawtext/metadata escaping); new shared helpers `app/pipeline/silences.py` (one strict
  silencedetect parser) and `app/pipeline/_ff.py` (uniform FFmpeg run + stderr-surfacing error);
  explicit-context imports (no swallowed `ImportError`). **41 new regression/golden tests** across
  `tests/test_fixes.py`, `tests/test_golden.py`, `tests/test_batch.py`; full suite **12/12 green**.
  RAID I-3…I-7 + TD-1 all Closed. Commits `ba6d8d9`, `7efed96`, `9c11473`, `d577460`, `bf8ef4c`.
- 2026-06-24 — **PR #5 merged to `main`** (merge commit `0c091aa`): the full podcast MBSE model +
  ReelCut implementation + desktop/mobile + SysML diagrams (231 files). Ongoing work continues on
  branch `claude/nepal-village-tourism-podcast-dp29gf` (ahead of `main`).
- 2026-06-19 — **Layering locked + podcast MBSE completed concept→implementation.** The real
  **System-of-Interest is the Missing Link Podcast Production & Distribution System**
  (`podcast-the-missing-link/01-systems-engineering/`). **reelcut/mbse is the implementation-layer
  SoI** — the local Studio editor subsystem (C4b/C5b/C10) selected by the podcast physical-layer
  trade study (variant **V3 Integrated local Studio**; V4 paid eliminated on the $0 gate). Platform
  ecosystem (YouTube/Spotify) = external solution classes, NOT context layers; **stakeholder needs
  belong to the conceptual layer only**. Added `00-concept-and-moe.md` (mission + MoE-1…6); `06`
  §6.0 solution class→variants→trade study→selection; cross-layer bridge in
  `reelcut/mbse/00-model-overview.md` §00.1; RTM `08` extended with N-25…N-33 + MoE. Spec:
  `docs/superpowers/specs/2026-06-19-podcast-mbse-end-to-end-completion-design.md`.
- 2026-06-19 — **ReelCut cross-platform build executed** (was the `/goal`). Implemented the full
  app to 37/37 system requirements across 8 phases (`reelcut/app/` pipeline modules + `tests/`),
  plus desktop packaging (`reelcut/desktop/` pywebview + PyInstaller spec) and a mobile RN project
  (`reelcut/mobile/`, iOS-convertible via `setup-ios.sh` on a Mac), and CI
  (`.github/workflows/build.yml`). Roadmap: `docs/superpowers/plans/2026-06-19-reelcut-cross-platform-build.md`.
- 2026-06-18 — **Stakeholder-register expansion (brainstorming → cascade).** INCOSE rule on a full
  YouTube/Spotify-style stakeholder map: register all, derive needs only inside the SoI. Added
  stakeholders + atomic needs SN-20…SN-30, 4 new system reqs SR-5.1…SR-5.4, functions F-32…F-35,
  tests T-28…T-31. Platform-only stakeholders STK-P1…P6 Parked/Rejected with rationale. Design doc
  `docs/superpowers/specs/2026-06-18-reelcut-stakeholder-register-expansion-design.md`.
- 2026-06-18 — **Persistent harness rules committed (caveman + drift-check).** Made conventions
  durable as project-committed config: (1) **Communication rule** in `CLAUDE.md` — caveman in chat,
  full English in durable artifacts ("talk caveman, write proper"); (2) **Drift-check**
  `.claude/hooks/drift-check.sh` (fence parity + SR `derivedFrom`/`refinedBy` ID resolution) wired as
  a `Stop` hook, plus a CLAUDE.md rule to run it + `render.sh` before committing.
- 2026-06-18 — **Conceptual-layer need elicitation + "shall" rewrite (brainstorming → cascade).**
  Added SN-9…SN-19 + cascade (CAP-12…21, MV-7/8, MOE-7/8/9, MOP-10/11/12, F-21…31, SR-4.1…4.11,
  T-17…27); all system requirements rewritten to canonical "ReelCut shall …". Design doc
  `docs/superpowers/specs/2026-06-18-reelcut-conceptual-need-elicitation-design.md`.
- 2026-06-18 — **Behaviour-model rule + behaviour enrichment (brainstorming).** New persistent
  CLAUDE.md rule: MBSE behaviour-model completeness MUST use `brainstorming` (enumerate
  Nominal/Alternate/Exception/Edge). Added behaviour catalogue CB-1…CB-7, three end-to-end behaviour
  views (activity/interaction/state), functions F-15…F-20, SR-3.1…3.6, T-12…16. Design doc
  `docs/superpowers/specs/2026-06-18-reelcut-behaviour-model-enrichment-design.md`.
- 2026-06-18 — Rebuilt ReelCut's MBSE model to **NASA MagicGrid** per **NTRS 20190032390**: package
  tree mirrors NASA containment (`1-problem-domain/{black-box,white-box}`, `2-solution-domain`,
  `3-system-configuration`, `4-implementation-domain`, `5-traceability`); three abstraction layers;
  system context as an IBD; system requirements written FROM functions; relationship rules
  («deriveReqt» req→req, «refine» function→req, «satisfy» structure→req, «verify», «allocate»).
- 2026-06-18 — **ReelCut MBSE model completed end-to-end.** Added Enterprise/SoS layer
  (`0-enterprise-sos/`, MV-1…/CAP-/derived SN), `6-element-dictionary.md`, `7-properties-and-types.md`
  (value-type + signal catalogues, per-block compartments), and the four cell diagrams. All four
  MagicGrid pillars across all four layers populated and visualised.
- 2026-06-18 — Adopted **OMG SysML + MagicGrid** for ReelCut (via `/grilling`), hybrid notation
  (SysML v2 textual + Mermaid), per-element Status {Built|Planned}.
- 2026-06-18 — `/grilling` locked ReelCut media-add needs N-10…N-19 (demux to independent A/V
  tracks; graded-MoP independent manipulation; replace-audio flags captions; add-audio mix/duck;
  image clips; MBSE = single source of truth; mobile feasibility-first).
- 2026-06-18 — Installed `grill-me` + `grilling` skills (vendored from `github.com/mattpocock/skills`,
  MIT).
- 2026-06-18 — Installed the **superpowers** skill bundle (`using-superpowers`, `brainstorming`,
  `writing-plans`; vendored byte-identical from `github.com/obra/superpowers`, MIT). Design-first,
  approval-gated workflow; user instructions + CLAUDE.md still take precedence.
- 2026-06-17 — Added `reelcut/`: a standalone, local-first, distributable video editor. Upload one
  video → auto-segment (Whisper or silence fallback) → keep/drop → reorder (3 methods) → per-boundary
  transitions (xfade+acrossfade) → export. Python **stdlib-only** backend (binds 127.0.0.1) + vanilla
  JS UI. KEY ENGINEERING: **two-stage render** (cut+normalise each clip to its own file, then join) to
  dodge a real FFmpeg bug where one input into many `atrim` branches starves `acrossfade`. Master =
  two-pass loudnorm −16 LUFS. Self-contained under `reelcut/` (own README/LICENSE/run scripts).
- 2026-06-17 — Extended `podcast-the-missing-link/` to full end-to-end tooling + a local studio UI
  (`scripts/clean_audio.sh`, `segment_episode.py`, `render_selection.py`, `studio.py`). All additive;
  loudness (−16 LUFS) defined in exactly one place (`process_episode.sh`). GOTCHA: LibreOffice is
  broken in the container, so the committed how-to PDF is the reportlab fallback.
- 2026-06-14 — Added `podcast-the-missing-link/`: a free, beginner-friendly podcast production
  system built with SE methodology (stakeholders→needs→requirements→ConOps→functional→physical→V&V→
  traceability) + implementation guides, content, and FFmpeg/Whisper automation. $0, 12-year-old
  usable (OBS, Audacity, FFmpeg, Whisper, Canva, Spotify for Creators, YouTube).
- 2026-06-06/07 — First skills (`image-to-pptx`, `task-history-review`) merged via PR #1; added
  `graphify` (root `KNOWLEDGE.md` memory) + the `SessionStart` auto-load hook. Skills are versioned
  in-repo (project scope) so all agents share them.

## Conventions
- One skill per directory under `.claude/skills/`; keep `description` trigger-rich.
- Keep shell snippets in skill docs copy-pasteable.
- Commit knowledge updates with messages prefixed `graphify:`.
- **Caveman in chat, full English in artifacts.** Convert to normal prose for any durable artifact
  (model/code/commits/docs) or when precision matters.
- **After editing `reelcut/mbse` or `podcast-the-missing-link`,** run `.claude/hooks/drift-check.sh`
  and keep it green; re-run the relevant `diagrams/render.sh` when Mermaid changes.
- **Maintain `DECISIONS.md` in the same commit** as any durable decision / accepted concession /
  found problem. Never delete entries — change their Status.
- ReelCut tests run via `python3 tests/test_*.py` (no pytest); keep the full suite green before
  committing app changes.

## Entities & Relationships
- **Missing Link Podcast System** (`podcast-the-missing-link/`) —is→ **the System-of-Interest**.
- **ReelCut** (`reelcut/`) —is the **implementation-layer SoI**→ realises the SoI's Studio editor
  subsystem (C4b/C5b/C10); selected by the podcast trade study as variant **V3**.
- **`KNOWLEDGE.md`** —pairs with→ **`DECISIONS.md`** : facts vs decisions/RAID; both auto-loaded.
- **`drift-check.sh`** —guards→ both MBSE models : fence parity, SN/F resolution, 4-pillar threads +
  config join present.
- **Configuration join** `CFG-Podcast(V3)` —contains→ `CFG-ReelCut` —specialises into→ Desktop/Mobile.
- **`app/pipeline/_ff.py`** —standardises→ all FFmpeg calls : capture + stderr-surfacing error.
- **`app/pipeline/silences.py`** —is the single→ silencedetect parser : used by `segment` + `tighten`.
- **graphify skill** —writes/reads→ **KNOWLEDGE.md** : the persistent memory store.
- **using-superpowers** —gates→ all responses; **brainstorming** —precedes→ **writing-plans**.

## Glossary
- **SoI** — System-of-Interest (the podcast production & distribution system).
- **Like-to-like cross-layer trace** — same-pillar links down the abstraction layers (req→req,
  structure→structure, behaviour→behaviour, parametric→parametric); `▽` = within-layer decomposition,
  `⇒` = across-layer realization (routed through a Configuration item).
- **Configuration item (CFG)** — the inter-layer join binding `⟨Requirements, Structure, Behaviour,
  Parameters⟩` for one baseline (e.g. `CFG-Podcast(V3)`, `CFG-ReelCut`, `CFG-Desktop`/`CFG-Mobile`).
- **Decision Log / RAID register** — `DECISIONS.md`: ADRs, accepted concessions/waivers, and
  Risks/Assumptions/Issues/Dependencies + tech-debt.

## Gotchas
- The remote execution environment is an **ephemeral container**, NOT the user's machine: anything
  not committed/pushed is lost on reclaim, and `~/.claude/skills/` here does not sync to the user's
  real setup. (A multi-hour review once lived only in chat and was lost to `/compact` + reclaim —
  hence `DECISIONS.md`. Persist findings to committed files.)
- CI now exists (`.github/workflows/build.yml`): tests on Ubuntu+FFmpeg + desktop binaries on
  macOS/Windows; mobile jobs are **best-effort** (`continue-on-error`) — the native `ios/`/`android/`
  projects are generated on a Mac via `reelcut/mobile/setup-ios.sh` (iOS tooling is macOS-only; see
  DECISIONS WV-002).
- `ffmpeg-kit` (the mobile render dependency) was **retired by Arthenica in 2025** (binaries pulled,
  repo archived) — accepted technical risk WV-001/R-1; migrate to a maintained fork when one exists.
- `drift-check.sh` validates fence parity + ID resolution + 4-pillar-thread presence, but does **not**
  render Mermaid — run `diagrams/render.sh` yourself after changing diagrams (WV-004).
- `api.github.com` is rate-limited (HTTP 403, unauthenticated) from this container; the GitHub MCP
  token is scoped to `karmapolicegitrepo/planets` and cannot create new repos.
- LibreOffice is broken in the container (committed how-to PDF is the reportlab fallback).

## Open Questions
- What is the intended longer-term purpose of `planets` beyond hosting skills + the podcast/ReelCut
  system?
- Mobile: validate a maintained ffmpeg-kit replacement and stand up a macOS signing pipeline so the
  iOS/Android builds move from best-effort to supported (WV-001/WV-002).
- Whether to add a CI render-verification step so diagram SVGs can't silently drift from the Mermaid
  source (WV-004 / R-3).
