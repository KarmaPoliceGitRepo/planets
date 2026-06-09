# Module 12 – MOSFET LNA Design

- **Source:** module12 - MOSFET LNA Design.pdf
- **Drive link:** https://drive.google.com/file/d/1vtqRleRVVDeYyHenW6Jep-hVh_9SkGJh/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (29 pages) applying two-port noise theory to CMOS LNA design. Covers the inductive source degeneration technique for simultaneous noise and power matching, cascode topology for improved isolation, differential LNA variants, and packaging parasitics.

## Unique contribution
Derives the specific condition ωT·Ls = Rs that enables simultaneous noise and input power matching in an inductively degenerated CMOS LNA — a key design insight showing that the same inductance satisfies both constraints when the FET is biased at a specific gm.

## Key concepts
- Inductive source degeneration
- Cascode LNA
- Simultaneous noise and power match
- fT (transit frequency)
- Bond wire inductance Ls
- Gate inductor Lg
- MOSFET Fmin
- Differential LNA
- Multi-finger FET layout
- Input matching network

## Methods / results / takeaways
- MOSFET Fmin = 1 + 2(f/fT)·√(gm·Rg·γ/α); scales with f/fT, so high fT is critical for low NF at RF.
- Inductive source degeneration (Ls): adds real part to input impedance (ωT·Ls) without adding noise → perfect for noise-lossless input matching.
- Matching condition: ωT·Ls = Rs (50 Ω); combined with gate inductor Lg to resonate out input capacitance Cgs at operating frequency.
- When the simultaneous match condition is met, NF ≈ Fmin — the design is as good as the device permits.
- Cascode LNA (common-source + common-gate stack): reduces Miller effect on Cgd, improves reverse isolation (S12), adds near-zero noise from cascode transistor at low gain.
- Differential LNA: rejects common-mode interference; each half-circuit analyzed independently; requires balun at input.
- Bond wire inductance (~1 nH/mm) used as Ls — turns packaging parasite into a design element.
- Key trade-off: larger W (wider FET) → lower Rn but larger Cgs → need larger Lg; optimal width for minimum NF exists.
