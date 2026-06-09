# Foundations for Microwave Engineering — Electromagnetic Resonators (Chapter 7)

- **Source:** Electromagnetic Resonators.pdf
- **Drive link:** https://drive.google.com/file/d/1fcxGKjRWpm-2A2li2FYFGpDdE9YU7-1s/view?usp=drivesdk
- **Type:** book (chapter)
- **Author/Year:** Robert E. Collin, 2001
- **Coverage:** partial (large file, truncated extraction)

## Overview
Chapter 7 covers resonant cavities and dielectric resonators as the microwave equivalent of lumped LC resonators. Derives the resonant modes and Q-factors of rectangular and cylindrical cavities, discusses coupling to cavities, and introduces dielectric resonators for modern microwave oscillator and filter applications.

## Unique contribution
Provides the rigorous field-theory derivation of cavity resonant modes and their Q-factors, showing why cavities have Q values far exceeding lumped LC circuits (Q > 10,000). The coupling-to-cavity analysis shows how external circuits must be designed to couple efficiently to specific cavity modes.

## Key concepts
- Cavity resonator as 3D electromagnetic boundary-value problem
- Resonant frequencies of rectangular cavity: f_mnp = (c/2)√((m/a)² + (n/b)² + (p/d)²)
- Rectangular cavity TE and TM modes
- Cylindrical cavity resonant modes
- Unloaded Q (Qu): due to conductor losses and dielectric losses
- Loaded Q (QL): including coupling to external circuit
- Coupling coefficient β = Qu/Qexternal
- Equivalent LC circuit near resonance
- Dielectric resonators (high-permittivity, low-loss ceramic materials)

## Methods / results / takeaways
- Cavity Q is inversely proportional to surface resistance: Q ∝ Volume/Surface × (1/Rs) where Rs = √(ωμ/2σ) = 1/(σδ).
- Rectangular cavity TM010 mode has the simplest field pattern; TE101 is often used in practice (no axial field on broad wall).
- Cylindrical cavity TM010 mode: Q ≈ 2.4 × a/δ where a is the radius; values of 10,000–50,000 are typical in copper cavities at X-band.
- Dielectric resonators (e.g., barium titanate composites) have εr ~ 30–100 with Q factors of thousands; they are small, cheap, and stable — used in DROs (dielectric resonator oscillators).
- Overcoupled cavity (β > 1): useful for bandpass filters; undercoupled (β < 1): useful for oscillator stabilization.
