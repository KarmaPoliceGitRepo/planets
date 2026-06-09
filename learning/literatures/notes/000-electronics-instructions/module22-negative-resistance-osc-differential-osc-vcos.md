# Module 22 – Negative Resistance Oscillators, Differential Oscillators, and VCOs

- **Source:** module22 - Negative Resistance Osc, Differential Osc, and.pdf
- **Drive link:** https://drive.google.com/file/d/1BKf1usqlu2UhmheKwL_f-JFFx5Abb4Yv/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (31 pages) covering the negative resistance perspective on oscillation, cross-coupled differential oscillators, voltage-controlled oscillators (VCOs) using PN junction varactors, MOS varactors, and switched capacitor banks, and the phase-locked loop (PLL) as a frequency synthesizer.

## Unique contribution
Provides a complete VCO design treatment — from the negative resistance analysis (Gx = −gm/n for transformer feedback, Rx = −gm/(ω²C1C2) for Clapp) through varactor physics (Cj formula with doping-dependent exponent n) to switched-capacitor tuning for coarse + fine frequency control — covering the full design space in a single module.

## Key concepts
- Negative resistance oscillator
- Cross-coupled differential pair
- Differential oscillator
- Voltage-controlled oscillator (VCO)
- Phase-locked loop (PLL)
- PN junction varactor
- MOS varactor (accumulation mode)
- Switched capacitor tuning
- VCO tuning range
- Virtual ground in differential circuits
- Crystal oscillator (Pierce, MOS)

## Methods / results / takeaways
- Negative conductance of transformer-feedback oscillator: Gx = −gm/n; oscillation starts when gm/n > GT = 1/RT (equivalent to loop gain > 1).
- Colpitts negative conductance: Gx = −gm/n + jω·C1C2'/(C1+C2'); reactive part can be absorbed into tank.
- Clapp oscillator negative resistance: Rx = −gm/(ω²C1C2); condition gm > Rs·ω²C1C2 for oscillation start-up.
- Cross-coupled pair: Gx = −gm/2 per side; provides negative conductance without a transformer; standard CMOS LC oscillator topology.
- Differential oscillator with center-tapped inductor: saves area vs. two separate inductors due to mutual inductance M; virtual ground at center tap.
- VCO tuning range: TR = 2·(fmax−fmin)/(fmax+fmin); typical 20–30% to cover process/temperature corners.
- PN junction varactor: Cj = Cj0/(1 − Vj/ψ0)^n; n = 1/2 (abrupt), 1/3 (linear grade), 2 (hyperabrupt → linear f vs. Vc).
- MOS varactor: capacitance varies from Cmin (depletion) to Cox (accumulation); accumulation-mode (n+ in n-well) preferred for high Q.
- Switched capacitor bank: MOSFET switches for discrete (coarse) tuning; on-resistance must be minimized to maintain Q; optimal W/L balances Ron vs. parasitic Cdd.
- PLL block diagram: VCO + divider ÷N + phase detector + loop filter; fout = N·fref; used for frequency synthesis locked to crystal reference.
- Crystal oscillator (MOS Pierce): quartz resonator acts as inductive element between series and parallel resonances; Q ~ 10⁵ ppm-level stability.
