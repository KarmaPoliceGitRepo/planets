# 8 · Requirements Traceability Matrix (RTM)

> **SE step:** *Traceability.* The RTM is the spine of systems engineering. It
> proves **nothing is orphaned**: every stakeholder need leads to a requirement,
> every requirement is realised by a function and a real component, and every
> requirement is verified. Read a row left-to-right and you can answer
> *"why does this exist, and how do we know it works?"*

## 8.1 Master trace: Need → Requirement → Function → Component → Verify

| Need | Requirement(s) | Function | Component | Verify (method) |
|---|---|---|---|---|
| **N-01** clear audio | FR-1, PR-1, PR-2 | F2, F5 | C1 OBS, C2 Audacity, C4 FFmpeg | T/A loudness+noise |
| **N-02** video | FR-2, FR-5, IR-3 | F2, F6 | C1 OBS, C4 FFmpeg | D/I MP4 codec |
| **N-03** edit mistakes | FR-3 | F4 | C2 Audacity | D |
| **N-04** free | UR-2, CR-6 | all | all (free tier) | I cost review |
| **N-05** simple | UR-1, UR-3, UR-4 | all | scripts, quickstart | D novice run |
| **N-06** right platforms | FR-7, FR-8 | F9 | C7 Spotify4Creators, C9 YouTube | D live |
| **N-07** repeatable | PR-6, UR-4, FR-9 | F1, F3, F5 | scripts | T timed run |
| **N-08** safe work | FR-11 | F3 | C8 cloud backup | I copies exist |
| **N-09** call-to-action | FR-4, FR-9 | F8 | show-notes template, C6 | I notes |
| **N-10** on my apps | FR-7, FR-8, PR-3 | F9 | C7, C9 | D live |
| **N-11** small files | PR-3, PR-4 | F6 | C4 FFmpeg | T size |
| **N-12** bilingual | FR-6 | F7 | C5 Whisper | A translation present |
| **N-13** notes/chapters | FR-9, FR-6 | F8 | template, C7 | I |
| **N-14** remote guest | FR-10, IR-4 | F2 | C3 call tool | D call |
| **N-15** weak signal | FR-10 (double-ender) | F2 | C3 + phone | D two tracks |
| **N-16** credit guides | FR-9 | F8 | show-notes template | I credits/links |
| **N-17** fair/consent | CR-3, CR-4 | F1, F8 | editorial + release form | I review |
| **N-18** platform rules | IR-2, IR-3, PR-1, PR-3, CR-2 | F6, F9 | C4, C7, C9 | T/I |
| **N-19** rights | CR-1, FR-4 | F4, F8 | royalty-free libraries | I licence log |
| **N-20** lawful/respectful | CR-2, CR-3 | F1 | editorial review | I |
| **N-21** captions | FR-6, PR-5 | F7 | C5 Whisper | T/A |
| **N-22** helper-friendly | UR-1 | all | quickstart | D |
| **N-23** minor safety | CR-5 | F9 | adult-owned accounts | I |
| **N-24** sponsor-ready | FR-9 | F10 | C7/C9 analytics | I dashboard |
| **N-25** discoverability | FR-9, IR-2 | F8, F9 | C6, C7, C9 (metadata/tags) | I metadata present |
| **N-26** offline/download | FR-5, PR-3, PR-4 | F6, F9 | C4 FFmpeg, C7 host | D download + play |
| **N-27** advertiser reach | FR-9 | F10 | C7/C9 analytics | I impressions/brand-safe |
| **N-29** device formats | IR-3, PR-3 | F6 | C4 FFmpeg | D codec/bitrate |
| **N-30** in-field weak signal | FR-10, PR-4 | F2, F3 | C3 + phone, C8 cloud | D local capture |
| **N-31** Trust&Safety/age | CR-2, CR-5 | F1, F9 | editorial review, adult accounts | I policy/age |
| **N-32** social clips/embeds | FR-9 | F8, F10 | C6 Canva (clips) | I clip + preview |
| **N-33** CTA / community link | FR-9 | F8 | show-notes template | I CTA present |

> **Collective needs:** every `N-xx` above also rolls up to one group **collective
> need CN-G1…CN-G6** ([`01-stakeholders.md`](01-stakeholders.md) §1.4,
> [`02-stakeholder-needs.md`](02-stakeholder-needs.md) §2.0). The roll-up is the
> upward parent of these rows.

## 8.2 Coverage check (no gaps, no orphans)

- ✅ **Every need N-01…N-33** maps to ≥ 1 requirement.
- ✅ **Every requirement** (FR-1…11, PR-1…6, UR-1…4, IR-1…4, CR-1…6) maps to ≥ 1 function **and** has a verification method in [`07`](07-verification-validation.md).
- ✅ **Every function F1…F10** is allocated to ≥ 1 component in [`06`](06-physical-architecture.md).
- ✅ **Every component C1…C10 (+ C4b/C5b)** traces up to ≥ 1 function it serves.
- ✅ **Every MoE-1…MoE-6** ([`00`](00-concept-and-moe.md)) is realised by ≥ 1 requirement target.

## 8.4a Solution-selection & cross-layer trace

| From | To | Link |
|---|---|---|
| Requirements UR-2, CR-1, CR-6, UR-1/3, UR-4, PR-6, N-15, PR-1, IR-3 | Trade study | criteria K1–K6 ([`06`](06-physical-architecture.md) §6.0.3) |
| Trade study | **V3 Integrated local Studio** | selected (score 12; V4 eliminated on cost gate) §6.0.5 |
| V3 selected solution | `reelcut/mbse` model | realises Studio subsystem (C4b/C5b/C10); bridge in `reelcut/mbse/00-model-overview.md` §00.1 |
| Podcast FR-3/PR-1/PR-2/FR-5/FR-6/IR-3/UR-1/CR-6 | ReelCut SN/SR | parent→child trace table, `…/00-model-overview.md` §00.1 |

## 8.3 Bidirectional spot-checks

- *Backward (component → need):* **C8 cloud backup** → F3 Ingest/Backup → FR-11 → **N-08 "keep work safe."** ✔
- *Forward (need → verify):* **N-21 captions** → FR-6/PR-5 → F7 Transcribe → C5 Whisper → **T/A ≥90% accuracy test.** ✔

## 8.4 Open items / future systems (tracked, not built)

| Item | Status | Where it lives |
|---|---|---|
| Tourism **Guide Platform** (licensing + Uber-like app) | Context/future system — *subject of the show* | concept in [`../03-content/research-pack.md`](../03-content/research-pack.md) |
| Full **bilingual dubbing** | Deferred (Could) | revisit after audience grows |
| **Sponsorship** integration | Deferred (Could) | enabled by F10 analytics |

This matrix is the single source of truth — update it whenever a need,
requirement, function, or tool changes.

> **Two complementary spines.** This file is the **cross-pillar** RTM
> (need→requirement→function→component→verify, *across* pillars at a level). The
> **like-to-like** threads that run *down the layers within one pillar*
> (requirement→requirement, structure→structure, behaviour→behaviour,
> parametric→parametric), with decomposition, recursion, and the configuration join to
> the ReelCut sub-model, are in
> [`10-cross-layer-traceability.md`](10-cross-layer-traceability.md) (DECISIONS ADR-013).

➡️ Build it for real: [`../02-implementation/`](../02-implementation/).
