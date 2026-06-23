# ReelCut MBSE — Stakeholder-Register Expansion (design)

**Date:** 2026-06-18 · **Skill:** brainstorming → cascade · **Scope:** stakeholder register +
needs (SN-20…SN-30) + 4 system requirements. No product code (HARD-GATE honoured).

## Problem
A comprehensive INCOSE-style stakeholder map was supplied for the YouTube/Spotify podcast &
vlog ecosystem (operational, content-originator, financial, technical-enabler, regulatory).
ReelCut's System-of-Interest, however, is a **local, offline, single-user editor** (no upload,
no network, no accounts — SN-3 privacy, SN-4 dependency-light). Most of the supplied map belongs
to the **streaming-platform** system, not ReelCut.

## Decision
Keep the ReelCut SoI. Apply the INCOSE rule: **register every stakeholder, derive needs only
inside the SoI boundary.** Each in-scope stakeholder's need is phrased as an obligation **on
ReelCut** (a local edit / export / metadata behaviour). Platform-only stakeholders are registered
and **Parked/Rejected** with rationale — never faked as features.

## In-SoI register additions (STK-8…STK-18) and needs (SN-20…SN-30)
- SN-20.1/.2 audio engineer — set export loudness / bitrate target (→ SR-1.5 / SR-4.2)
- SN-21 accessibility user — export a full plain-text transcript (→ **SR-5.1**, F-32)
- SN-22 offline listener — export audio-only MP3 (→ SR-1.8, already Built)
- SN-23 guest/SME — on-screen name attribution (→ SR-4.10 lower-thirds)
- SN-24 enterprise creator — batch-export with one preset (→ **SR-5.2**, F-33)
- SN-25 advertiser — mark mid-roll ad-insertion points (→ SR-4.7 chapters / SR-5.4)
- SN-26 hardware/gear — ingest recorder WAV/MP4 (→ SR-3.1 validate-input)
- SN-27 social platform — export a cover thumbnail (→ SR-4.6 cover frame)
- SN-28 copyright body — flag non-royalty-free audio + license note (→ **SR-5.3**, F-34)
- SN-29 regulator — collect zero personal data (→ SR-1.7 local-only, already Built)
- SN-30 active consumer — embed title/chapter metadata in export (→ **SR-5.4**, F-35)

Only four new system requirements (SR-5.1…SR-5.4) and functions (F-32…F-35); the rest reuse
existing requirements.

## Parked / Rejected (STK-P1…STK-P6) — out of SoI
Shareholders (platform ROI); ML/recommendation engineer (**conflicts SN-3**, zero telemetry —
Rejected); CDN provider; trust & safety/moderation; enterprise team-access/bulk API (deferred);
premium billing/DRM (Rejected). Registered for completeness; revisit only on SoI re-baseline.

## Cascade
Functions F-32…F-35; requirements SR-5.1…SR-5.4 (+ risk/rationale); tests T-28…T-31;
traceability rows; element dictionary. Drift-check green; no mermaid diagrams changed.

## Self-review
Placeholders: none. Consistency: every SN-20…30 resolves to a defined SR; every SR-5.x
derives from a defined need and is refined by a defined function (drift-check enforces).
Scope: explicit SoI boundary; platform features parked, not implemented. Ambiguity:
SR-5.3 "flag" (not enforce) — ReelCut has no Content-ID DB; stated explicitly.
