# DECISIONS.md — Decision Log + RAID Register

> **Purpose.** Durable, committed memory for *why things are the way they are* and
> *what is still open*. This is the companion to `KNOWLEDGE.md`: `KNOWLEDGE.md` holds
> facts/architecture; **this file holds decisions, knowingly-accepted concessions, and
> open risks/issues** so nobody has to re-derive them or go digging through git history.
>
> **Industry terms used here:**
> - **Decision Log / ADR** (Architecture Decision Record) — a choice we made and why.
> - **Accepted Concession / Waiver / Deviation** — a gap against a requirement or an
>   ideal that we *knowingly* accept, with rationale and (where relevant) an expiry.
> - **RAID register** — running **R**isks, **A**ssumptions, **I**ssues, **D**ependencies.
> - **Technical-debt register** — shortcuts taken that we intend to pay back.
>
> **How to maintain.** When a durable decision is made, a concession is accepted, or a
> problem is found, add a row here in the same commit. Never delete entries — change
> their **Status** instead (history is the point). IDs are immutable once assigned.
>
> **Status legend:** `Accepted` · `Proposed` · `Superseded(by ID)` · `Open` · `Mitigated` · `Closed` · `Done`

---

## 1. Decision Log (ADRs)

Format: **ID · Date · Status · Decision** — *Rationale.* (Supersedes/Superseded links where relevant.)

| ID | Date | Status | Decision | Rationale |
|----|------|--------|----------|-----------|
| ADR-001 | 2026-06-18 | Accepted | `podcast-the-missing-link` is the **System-of-Interest**; **ReelCut is its implementation-layer SoI / allocated component** (the Studio editor), not a separate system. | The real system is the podcast production+distribution system; ReelCut is one solution component inside it. Locks the MBSE layering. |
| ADR-002 | (pre-session, commit 8c3690a) | Accepted | ReelCut is **local-first**: Python stdlib `http.server` binds `127.0.0.1`, serves a vanilla-JS wizard UI, **no upload**. | Privacy + zero-infra; the editor runs entirely on the creator's machine. |
| ADR-003 | 2026-06-18 | Accepted | ReelCut's **output is platform-bound** (YouTube / Spotify), **not** local-only. | "Local-first editing" ≠ "local-only output." The deliverable is published to external platforms the user does not own. |
| ADR-004 | 2026-06-18 | Accepted | Stakeholders are modelled **many-to-many** across groups **G1–G6**; collective needs established at group level. | One stakeholder (e.g. a platform) legitimately sits in several groups; per-group tables forced false 1:1 membership. |
| ADR-005 | 2026-06-18 | Accepted | **Stakeholder needs live only at the conceptual layer.** | MagicGrid discipline: needs are problem-space; they must not leak into logical/physical layers. |
| ADR-006 | 2026-06-19 | Accepted | Physical layer selects a solution via **trade study**: solution **class → variants V1–V4 → criteria K1–K6 → select V3 "Integrated Studio" (= ReelCut)**. Criteria derived from requirements, not invented. | A defensible, traceable selection rather than an assumed tool. |
| ADR-007 | 2026-06-17 | Accepted | MBSE framework = **NASA MagicGrid**, three layers (NTRS 20190032390); SysML notation; traceability spine Need→Requirement→Function→Component→Verify. | Standards-conformant, auditable model structure. |
| ADR-008 | 2026-06-19 | Accepted | Audio mastering uses **two-pass loudness normalization** (`loudnorm`, target **−16 LUFS / −1 dBTP**): measure, then apply measured values. | Single-pass loudnorm guesses; two-pass is accurate and meets PR-1. |
| ADR-009 | 2026-06-18 | Accepted | Desktop packaging = **pywebview + PyInstaller + bundled FFmpeg**; CI builds native binaries on macOS + Windows runners. | Single-binary, no-install distribution for non-technical creators. |
| ADR-010 | 2026-06-18 | Accepted | Mobile port = **React Native + ffmpeg-kit**, rendering on-device from the portable project doc. | Reuse the same portable project; keep the local-first guarantee on mobile. **See WV-001 / R-1 — ffmpeg-kit is retired.** |
| ADR-011 | 2026-06-19 | Accepted | Tests use **`unittest`**, run as `python3 tests/test_*.py` (pytest is not installed). | Zero extra deps; runs in any container. |
| ADR-012 | 2026-06-18 | Accepted | **Caveman chat mode** + **drift-check** persisted as committed hooks in `.claude/settings.json`; `KNOWLEDGE.md` auto-loaded each session. | User-mandated durable conventions, enforced by the harness rather than memory. |
| ADR-013 | 2026-06-24 | Accepted | **Four-pillar like-to-like cross-layer traceability** (requirement→requirement, structure→structure, behaviour→behaviour, parametric→parametric), each thread running through all abstraction layers with **within-layer decomposition `▽`** + **across-layer realization `⇒`**, applied **recursively**, and **routed through a Configuration item (`⟨R,S,B,P⟩` join)** as the inter-layer intermediate. Spine = `reelcut/mbse/8-cross-layer-traceability.md`; config join = `3-system-configuration.md`. **Extended 2026-06-24 to the podcast SoI model:** `podcast-the-missing-link/01-systems-engineering/10-cross-layer-traceability.md` formalises the same four threads (prose-RTM `08` was cross-pillar only), and the configuration join chains `CFG-Podcast(V3)` → `CFG-ReelCut` → Desktop/Mobile so the threads run continuously from podcast mission into ReelCut implementation. **Mirrored 2026-06-24:** each pillar's like-to-like rows are also reproduced as a "Cross-layer like-to-like links" table in that element's *home* source file (needs, system-requirements, functional-analysis, logical-subsystems, component-structure, MoE, component-parameters in ReelCut; needs, requirements, functional, physical, concept/MoE in podcast) — the central doc stays authoritative, the source files carry the mirror. | User requirement: complete same-kind traceability across every layer, with decomposition/recursion and a configuration model as the intermediate. Routing each hop through a CFG avoids an N×N link tangle and makes the trade-study selection explicit at the join. Closes the flat-namespace / no-config-variant gaps and the "podcast model is prose-RTM only" gap found by the model map. |

---

## 2. Accepted Concessions / Waivers / Deviations

Things we **knowingly** accept as gaps. Each has a reason and, where possible, the
condition under which it should be revisited.

| ID | Date | Status | Concession (what we accept) | Why accepted | Revisit when |
|----|------|--------|------------------------------|--------------|--------------|
| WV-001 | 2026-06-18 | Open | Mobile depends on **ffmpeg-kit, which Arthenica retired (binaries pulled 2025-04-01, repo archived 2025-06-23)**. | No drop-in maintained equivalent at decision time; mobile is secondary to desktop. | A maintained fork/alternative is validated — then supersede ADR-010. |
| WV-002 | 2026-06-19 | Open | **Mobile CI jobs are `continue-on-error`** (best-effort). Native `ios/`/`android/` projects are **not** generated in CI. | iOS tooling is macOS-only; cannot generate/sign on the Linux CI runner. Generated on a Mac via `setup-ios.sh`. | A macOS signing pipeline + secrets exist. |
| WV-003 | 2026-06-19 | Open | **Whisper transcription is optional** — graceful fallback if the model isn't installed. | Keeps the core pipeline dependency-light; transcription is value-add, not core. | Transcription becomes a hard requirement. |
| WV-004 | 2026-06-19 | Open | **SVG diagrams are committed**, but source of truth is the Mermaid in the `.md` files; `drift-check.sh` checks **fence parity only, not render fidelity**. | Rendering needs a toolchain the fast hook shouldn't require. | A render step is added to CI. (See TD-3 / R-3.) |
| WV-005 | 2026-06-19 | Open | **Mobile `tsconfig.json` is lenient** (`noImplicitAny:false`, `skipLibCheck:true`). | Untyped RN/JSX libs blocked CI typecheck; relaxed to ship the best-effort mobile path. | Mobile is promoted from best-effort to supported. |

---

## 3. RAID Register

### Risks (could hurt us; not yet happened)
| ID | Status | Risk | Impact | Mitigation / Owner |
|----|--------|------|--------|--------------------|
| R-1 | Open | ffmpeg-kit retirement (WV-001) — mobile render path may break with a new OS/toolchain. | Mobile renders stop working. | Migrate to a maintained fork; track upstream. Owner: TBD. |
| R-2 | Mitigated | **Ephemeral container loses uncommitted work** (the exact incident that prompted this file). | Hours of work vanish on container reclaim. | Commit early/often; persist findings to committed files (this log). |
| R-3 | Open | Mermaid→SVG drift: `render.sh` not enforced by any hook (WV-004). | Diagrams silently diverge from model text. | Add render to CI / pre-commit. |

### Assumptions (taken as true; revisit if they break)
| ID | Status | Assumption |
|----|--------|------------|
| A-1 | Accepted | Desktop users run on Mac/Windows with the **bundled** FFmpeg (no separate install). |
| A-2 | Accepted | YouTube/Spotify remain the distribution targets; ReelCut output stays platform-bound (ADR-003). |
| A-3 | Accepted | The repo is the single durable store; the container filesystem is disposable. |

### Issues (active problems; actionable now)
| ID | Status | Issue | Next action |
|----|--------|-------|-------------|
| I-1 | Open | Native `ios/`/`android/` projects not generated (needs a Mac). | Run `reelcut/mobile/setup-ios.sh` on macOS. |
| I-2 | Open | No automated verification that diagrams render. | Add a render check (R-3). |
| I-3 | Closed | **Defect-level code-review of the finished ReelCut modules** — now done (2026-06-24). Full prioritised backlog in [`reelcut/CODE-REVIEW-2026-06-24.md`](reelcut/CODE-REVIEW-2026-06-24.md): 12 HIGH (5 security, 7 correctness), 12 MED, 11 LOW. | Fixes tracked there + as I-5..I-7 below. |
| I-5 | Closed | **Security (HIGH):** all 5 fixed 2026-06-24 — path confinement (CR-H1/H3), `level_db` validation (CR-H2), Host-header guard (CR-H4), static resolve+symlink guard (CR-H5). Regression tests in `reelcut/tests/test_fixes.py`. | Done. |
| I-6 | Closed | **Correctness (HIGH): all resolved.** Fixed — source-digest baseline (CR-H6), atomic autosave (CR-H7), Event CancelToken (CR-H8), escaped drawtext/metadata (CR-H12), and shared strict silence parser `app/pipeline/silences.py` (CR-H11/M12/L3). Verified-correct via golden tests (`tests/test_golden.py`) — A/V crossfade sync (CR-H10) and audio ducking (CR-H9) were false positives; Won't-fix. **0 live HIGH findings remain.** | Done. |
| I-7 | Closed | **Quality/debt: entire MED+LOW backlog resolved** (2026-06-24). All 12 MED + 11 LOW fixed; CR-L2 (rational fps), CR-L4 (shared `_ff.run` error handling), CR-L9/TD-1 (explicit-context imports) closed in the final pass. Full review backlog now Fixed or verified-correct — **0 open findings.** | Done. |
| I-4 | Closed | Earlier "find gaps/errors" findings (Jun 17–19) were narrated **in chat only** and lost when the session compacted (transcript now starts at the 2026-06-23 01:03 summary). | The durable record of those gaps survives: the **requirement-conformance gaps** are in [`reelcut/mbse/4-implementation-domain.md`](reelcut/mbse/4-implementation-domain.md) (SR→module→test→status) and phase commits `310bafc`…`4e57a4c` (37/37 SRs closed). Root cause = no auto-log existed; fixed by this file + SessionStart/UserPromptSubmit hooks. |

### Dependencies (external things we rely on)
| ID | Status | Dependency |
|----|--------|------------|
| D-1 | Accepted | `ffmpeg` / `ffprobe` present at runtime (bundled on desktop). |
| D-2 | Accepted | Whisper model (optional) for transcription (WV-003). |
| D-3 | Accepted | macOS + Xcode + CocoaPods for any iOS build (WV-002). |

---

## 4. Technical-Debt Register

| ID | Status | Debt | Why it exists | Pay-back |
|----|--------|------|---------------|----------|
| TD-1 | Closed | `app/api.py` used **dual-context `try/except` imports** that swallowed real `ImportError`s. | Module must run both as a package and as a flat script (server vs tests). | **Done (2026-06-24):** context detected explicitly via `__package__` (api/metadata) and relative sibling imports (tighten/segment); no error swallowed. |
| TD-2 | Open | Mobile **type safety relaxed** (WV-005). | Untyped libs blocked CI. | Add type stubs; re-enable strict checks. |
| TD-3 | Open | `drift-check.sh` validates **fence parity + ID resolution only**, not diagram render. | Keep the Stop hook fast and dependency-free. | Move render verification to CI (R-3 / WV-004). |

---

*Created 2026-06-23. Keep current in the same commit as the change it describes.*
