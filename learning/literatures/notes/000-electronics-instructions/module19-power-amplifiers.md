# Module 19 – Power Amplifiers

- **Source:** module19 - Power Amplifiers.pdf
- **Drive link:** https://drive.google.com/file/d/1wp2AG52qDVn57BZsMejiC5Sv1cFj48vI/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (27 pages) introducing Class A power amplifier design. Covers efficiency analysis for emitter follower, common-emitter with resistive and inductive loads, optimum load calculation, and the impact of package parasitics on RF PA performance.

## Unique contribution
Provides a rigorous efficiency comparison across three Class A topologies (emitter follower ≤20%, resistive CE ≤25%, inductive CE approaching 50%) and identifies bond wire inductance as the critical packaging limitation — motivating flip-chip and down-bond packaging strategies.

## Key concepts
- Class A power amplifier
- Power added efficiency (PAE)
- Drain/collector efficiency ηc
- Optimum load resistance Ropt
- Emitter follower PA efficiency
- Inductive load PA
- Load line analysis
- Bond wire inductance
- Flip-chip packaging
- Package parasitics

## Methods / results / takeaways
- PAE = (Pout − Pin)/PDC; drain efficiency ηd = Pout/PDC; PAE ≈ ηd·(1 − 1/Gp) for high Gp.
- Emitter follower (source follower): output voltage swing limited to VCC/2 by the bias current; efficiency ≤ VCC²/(8·R·PDC) → max ~20% at 3 V supply.
- Common-emitter with resistive load: quiescent current wastes DC power; efficiency ≤ 25%.
- Common-emitter with inductive load: inductor allows collector voltage to swing up to 2·VCC; efficiency ≤ 50% (limited by current swing).
- Optimum load: Ropt = VCC/IP where IP is peak output current; for BJT, Ropt = VCC²/(2·Pout).
- Package parasitics: bond wire inductance (LE ≈ 1 nH/mm) at emitter/source limits voltage swing and reduces efficiency; critical in GHz-range PAs.
- Flip-chip bonding: solder bumps replace bond wires → LE < 0.1 nH, allowing full swing at higher frequencies; required for >10 GHz PA designs.
- Down-bond (bonding directly to ground plane): minimizes ground inductance, another approach to reducing LE.
