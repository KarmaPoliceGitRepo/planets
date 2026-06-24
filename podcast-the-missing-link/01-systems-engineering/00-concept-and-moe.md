# 0 · Concept, Mission & Measures of Effectiveness

> **SE step (concept layer):** before stakeholders and needs, state *why the
> system exists* — the mission and the **Measures of Effectiveness (MoE)** that
> define success. MoE are **solution-independent** value measures: they say what
> "good" looks like for the mission, and every later requirement target traces up
> to one. This is the head of the model; the lifecycle runs concept → needs →
> requirements → ConOps → functional → physical/solution → implementation → V&V,
> all bound by the traceability matrix ([`08`](08-traceability-matrix.md)).

## 0.1 Mission statement

Enable a single beginner, at zero cost on their own laptop, to **produce and
distribute a professional bilingual podcast & vlog** — *The Missing Link* — that
tells the story of Nepali migration, village economics, energy and tourism, and
that builds an audience for a future village **Tourism Guide Platform**.

## 0.2 Vision / end state

A repeatable weekly show, published to the platforms people already use
(Spotify/Apple via RSS, YouTube), accessible (captions + transcripts, bilingual),
lawful and rights-clean, produced in ≤ 3 hours per episode by a non-expert — with
all work backed up and portable (no lock-in).

## 0.3 Operating context (not part of the SoI)

- **Enabling systems:** the creator's laptop, free software, internet, host platforms.
- **External / future system:** the **Tourism Guide Platform** (licensing + Uber-like
  app) — the *subject* the show promotes; out of scope to build here.

## 0.4 Measures of Effectiveness (MoE)

Solution-independent. Each MoE is realised later by a measurable requirement
target (Measure of Performance, MoP) and traces down to needs.

| ID | Measure of Effectiveness | What it captures | Realised by (MoP / requirement) | From needs |
|---|---|---|---|---|
| **MoE-1** | **Reach** | The show is on the platforms the audience already uses, and is discoverable. | FR-7, FR-8, IR-2; metadata/discovery | N-06, N-10, N-25 |
| **MoE-2** | **Accessibility** | Anyone can follow it — captions, transcripts, bilingual, small files on weak data. | FR-6, PR-5, PR-3, PR-4 | N-11, N-12, N-13, N-21 |
| **MoE-3** | **Sustainability (cost & effort)** | A beginner can keep a weekly cadence at $0. | UR-2, UR-1, UR-3, UR-4, PR-6 | N-04, N-05, N-07 |
| **MoE-4** | **Production quality** | Audio is clear and consistently loud; video is platform-valid. | PR-1, PR-2, IR-3 | N-01, N-02, N-18 |
| **MoE-5** | **Integrity & impact** | Content is lawful, rights-clean, consented, culturally respectful, and advances the village/tourism agenda via a clear CTA. | CR-1…CR-5, FR-9 | N-09, N-16, N-17, N-19, N-20, N-33 |
| **MoE-6** | **Portability (no lock-in)** | Episodes and the RSS feed move to another host freely. | CR-6 | N-04 |

## 0.5 MoE → MoP linkage (how success is measured)

| MoE | Hard target that proves it (MoP) |
|---|---|
| MoE-1 Reach | Live on Spotify/Apple (RSS) **and** YouTube; episode carries title/chapter metadata. |
| MoE-2 Accessibility | `.srt` + `.txt` present; transcript ≥ 90 % accuracy (PR-5); MP3 ≥ 128 kbps, ≤ 40 MB / 30 min (PR-3/4). |
| MoE-3 Sustainability | One episode produced in ≤ 3 h (PR-6) at **$0** (UR-2), via single-command tasks (UR-4). |
| MoE-4 Quality | −16 LUFS ±1, TP ≤ −1 dBTP (PR-1); noise floor ≤ −50 dBFS (PR-2); H.264/AAC MP4 (IR-3). |
| MoE-5 Integrity | Licence log present (CR-1); consent/release on file (CR-4); CTA in every episode (FR-9). |
| MoE-6 Portability | RSS feed exportable to another host (CR-6). |

➡️ Next: who cares and what they need — [`01-stakeholders.md`](01-stakeholders.md)
and [`02-stakeholder-needs.md`](02-stakeholder-needs.md).


## Cross-layer like-to-like links (ADR-013)

> Mirrors this file's rows from the cross-layer spine (`10-cross-layer-traceability.md`).
> `▽` = within-layer decomposition · `⇒` = across-layer realization (routed via a Configuration item).

| Link | Type | From | To |
|------|------|------|----|
| MoE-4 ▽ {loudness, caption accuracy} | ▽ constraint decomposition | MoE-4 Quality | sub-measures |
| MoE-4.x ⇒ PR-1 / PR-5 | ⇒ refine | Measure of Effectiveness | performance requirement |
