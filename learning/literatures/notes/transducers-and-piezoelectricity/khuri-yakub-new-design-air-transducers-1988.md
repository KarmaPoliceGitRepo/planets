# A New Design for Air Transducers

- **Source:** Khuri-Yakub new design air transducers 1988
- **Drive link:** https://drive.google.com/file/d/1VQF2SWGYOC1R8DSh40oSs0Xs4tQ1UhrF/view
- **Type:** paper (1988 IEEE Ultrasonics Symposium Proceedings, pp. 503–506)
- **Author/Year:** B. T. Khuri-Yakub, J. H. Kim, C-H. Chou, P. Parent, G. S. Kino / 1988
- **Coverage:** full

## Overview
Introduces silica aerogel as a practical matching layer material for air transducers and derives a bandwidth-maximizing design criterion for two-matching-layer air transducers. Uses a resonant circuit model with mechanical Q (q) to account for matching layer loss, showing that overall Q_L = q·Q/(q+Q) → for maximum bandwidth at given insertion loss, one should choose q ≈ Q. Demonstrates 30 dB round-trip insertion loss at 1 MHz with double aerogel + glass-bubble composite matching layers, and C-scan imaging of a seeded 1 cm defect in Kevlar-epoxy composite.

## Unique contribution
First use of silica aerogel (from Physikalisches Institut, Universität Würzburg; density 0.071–0.285 g/cm³, Z = 0.01–0.1 MRayl, c = 120 m/s) as a matching layer for air transducers. Derives design criterion: insertion loss vs bandwidth tradeoff governed by mechanical Q of matching layer, not just impedance mismatch. Achieves 35 dB insertion loss at 1 MHz with 30% fractional bandwidth — significant improvement over prior silicone rubber designs. Shows C-scan air-coupled imaging of Kevlar-epoxy composite.

## Key concepts
- Optimum single ML for PZT-air: Z_opt = 0.11 MRayl; lowest available material: 0.3 MRayl (microsphere composite)
- Two matching layers: Z₁ (inner, high, e.g. 5.8 MRayl epoxy composite) + Z₂ (outer, low, aerogel 0.01–0.1 MRayl)
- Resonant circuit model: Z₂ = -jZ_m/(2Qδ) near resonance; Q_L⁻¹ = q⁻¹ + Q⁻¹ → bandwidth limited by smaller of q (ML mechanical Q) and Q (PZT mechanical Q)
- Insertion loss: IL = L₀(1 + a₂δ² + a₄δ⁴); depends on Q_L and fractional frequency deviation δ
- Design criterion: for maximum bandwidth at given IL, choose q ≈ Q (match ML mechanical Q to transducer Q)
- Silica aerogel: density 0.071–0.285 g/cm³; Z = 0.01–0.1 MRayl; c = 120 m/s; provided by J. Fricke (Würzburg)
- Glass bubble composite: Z = 0.3 MRayl; used as first (inner) ML at Z₂ = 5.8 MRayl → 0.3 MRayl cascade

## Methods / results / takeaways
- Transducer: PZT-5H, 1 MHz center frequency; 1-3 composite geometry
- Two ML design: first layer Z = 5.8 MRayl (epoxy + glass microsphere composite); second layer Z = 0.3 MRayl aerogel
- Measured round-trip insertion loss: 35 dB at 1 MHz; bandwidth ~30% fractional
- Theory-experiment agreement: excellent for both insertion loss and impulse response
- C-scan NDE: 1 cm × 1 cm seeded defect in Kevlar-epoxy composite (3 cm × 3 cm panel); defect clearly detected at 1 MHz with 6 dB SNR margin
- Electronics: Velonex 2 kV pulser; Airscan, Inc. receiver; signal averaged 100 times
- Application: air-coupled NDE of aerospace composites (carbon-epoxy, Kevlar-epoxy); robotic sensing
