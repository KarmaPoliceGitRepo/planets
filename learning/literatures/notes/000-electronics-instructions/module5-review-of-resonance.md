# Module 5 – Review of Resonance

- **Source:** module5 - Review of resonance.pdf
- **Drive link:** https://drive.google.com/file/d/1XohAhJI0c7oNNdXrn27jDfw8VXzMDRs4/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (42 pages) reviewing series and parallel RLC resonator behavior, Q factor definitions, transmission-line resonators, and high-Q technologies including crystal and MEMS resonators. Foundational for understanding oscillators, filters, and matching networks.

## Unique contribution
Collects Q factor definitions across multiple resonator types (lumped, distributed, crystal, MEMS) in one place, clarifying differences in loaded vs. unloaded Q and showing how T-line resonators mimic lumped RLC behavior near resonance.

## Key concepts
- Series RLC resonance
- Parallel RLC resonance
- Q factor (quality factor)
- Bandwidth Δω = ω0/Q
- Loaded Q vs. unloaded Q
- Transmission line resonators (λ/2, λ/4)
- Crystal resonators (quartz)
- MEMS resonators
- Energy stored vs. energy dissipated
- Equivalent parallel resistance Rp

## Methods / results / takeaways
- Series RLC: ω0 = 1/√(LC), Q = ω0L/R = 1/(ω0RC), 3dB bandwidth Δω = ω0/Q.
- Parallel RLC: same ω0; Q = R/(ω0L) = ω0RC; Rp = Q²·R for equivalent series-to-parallel transformation.
- T-line resonators: a λ/2 open-circuited line and a λ/4 short-circuited line both act as parallel resonators near resonance; Q ≈ β/(2α).
- Crystal resonators: quartz mechanical resonance gives Q ~ 10⁵–10⁶, frequency stability ~ppm; modeled as LCR series branch in parallel with parasitic Cp.
- MEMS resonators achieve Q > 10⁴ and sub-GHz frequencies in silicon processes, offering potential for on-chip high-Q references.
- Loaded Q (with external load) is always lower than unloaded Q; insertion loss IL = 1 − Q_L/Q_u.
- In matching and oscillator design, high Q improves selectivity and reduces phase noise.
