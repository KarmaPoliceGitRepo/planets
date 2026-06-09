# Module 15 – Effect of Feedback on Distortion

- **Source:** module15 - Effect of Feedback on Distortion.pdf
- **Drive link:** https://drive.google.com/file/d/1jkW70V5wzw84EgtBfZKaYNM6zm1Le/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (29 pages) analyzing how negative feedback modifies distortion in RF amplifiers. Derives how each power series coefficient transforms under feedback, identifies conditions where feedback reduces or (counterintuitively) increases specific distortion products, and discusses BJT emitter degeneration as a practical example.

## Unique contribution
Shows that third-order distortion b3 under feedback contains a second-order interaction term 2a2²f that can partially cancel a3, enabling a distortion null at a specific emitter resistance RE = 1/(2gm) for the BJT — a non-obvious design technique for improving IIP3 without sacrificing gain.

## Key concepts
- Negative feedback and distortion reduction
- Power series under feedback
- Loop gain T
- Second-order interaction in HD3
- BJT emitter degeneration
- Distortion null
- Multi-tone distortion analysis
- Multinomial expansion
- Feedback factor f
- IIP3 improvement

## Methods / results / takeaways
- Under negative feedback with loop gain T = a1·f, the closed-loop coefficients transform as: b1 = a1/(1+T), b2 = a2/(1+T)³, b3 = [a3 − 2a2²f/(1+T)]/(1+T)⁵.
- b2 is reduced by (1+T)³ → feedback strongly suppresses second-order distortion.
- b3 has two terms: the a3 term (reduced by feedback) minus a second-order interaction 2a2²f term; these can cancel.
- For BJT with emitter degeneration RE: gm_eff = gm/(1+gm·RE); second-order interaction can be engineered so that b3 ≈ 0.
- Distortion null at RE ≈ 1/(2gm) gives a high IIP3 at that bias point; moving away from this RE restores distortion.
- Feedback also increases the input impedance and reduces output impedance (series-series topology), useful for LNA broadband matching.
- Multinomial analysis for multi-tone signals is used to rigorously track all intermodulation products under feedback; single-tone Taylor series is insufficient for multi-carrier systems.
