# Impedance Conversion of Matching Layer for Air Ultrasonic Transducers

- **Source:** Toda impedance conversion matching layer 2015
- **Drive link:** https://drive.google.com/file/d/1L57FpxRfvkSZx85cLopxuEFiPs_MIini/view
- **Type:** paper (2015 IEEE International Ultrasonics Symposium Proceedings, 10.1109/ULTSYM.2015.0374)
- **Author/Year:** M. Toda / 2015
- **Coverage:** full

## Overview
Derives an approximate closed-form expression for the impedance seen from inside a λ/4 matching layer (Z₂) when the external load is air, including the effect of internal mechanical loss (Qm). Shows that when the radiation loss (QR) is much smaller than the internal loss (Qm⁻¹) — as in air transducers — the well-known lossless formula Z₂ = Zm²/Z₁ fails, and the correct expression is Z₂ ≈ (4/π)ZmQm, which is independent of air impedance Z₁. Validates by measuring PZT impedance with commercial matching layer in air vs vacuum.

## Unique contribution
Proves analytically and experimentally that for air-coupled transducers, the matched impedance Z₂ ≈ (4/π)ZmQm — governed entirely by the matching layer's own mechanical Q, not by the air load. This resolves the apparent paradox that changing from air to vacuum has little effect on the transducer impedance. Shows that high-Qm materials (Qm = 80–100) are essential for air matching layers; typical polymers (Qm = 10–20) give inadequate Z₂. Provides mass-spring model interpretation: matching layer is a resonator whose Q is dominated by internal loss, not radiation loss.

## Key concepts
- Standard lossless formula: Z₂ = Zm²/Z₁ (requires Qm = ∞); for air: Z₂ = (0.3)²/(447×10⁻⁶) ≈ 200 MRayl — far too high
- Lossy formula: Z₂ ≈ (4/π)ZmQm at λ/4 resonance; valid when (4/π)Z₁Qm << Zm (always true for air)
- Derivation: complex tan(ωd/Vs) with Vs = Vs'(1 + j/2Qm); at d = λ/4: tan → −j(4Qm/π)
- For Zm = 0.3 MRayl, Qm = 100: Z₂ ≈ (4/π) × 0.3 × 100 ≈ 38 MRayl (matches PZT impedance)
- For Zm = 0.3 MRayl, Qm = 20 (typical polymer): Z₂ ≈ 7.6 MRayl (too low)
- Physical interpretation: air transducer matching layer is underdamped resonator; radiation Q_R >> Q_m; external load negligible
- Mass-spring analogy: matching layer = spring (Zm) + mass (radiating face); stiffness sets Z₂, not radiation medium
- Measurement: PZT impedance peak height measured in air vs vacuum; difference < predicted for Qm = 100

## Methods / results / takeaways
- PZT material: PZT5A, thickness 7.45 mm, area 64 mm²; kT = 0.721, Qm = 120
- Matching layer: proprietary material (tiny air bubbles in stiff polymer), Zm = 0.3 MRayl, ρ = 140 kg/m³, Vs = 2150 m/s, thickness 3.0 mm, Qm = 80–100
- Measurement: input electrical impedance of PZT+ML in air and in vacuum; peak ~ 30 kΩ in both cases
- Model agrees: Qm = 100 gives best fit; air vs vacuum difference is small as predicted
- Design guideline: use Z₂ = (4/π)ZmQm for matching layer material selection, not Zm = √(ZPZA)
- Application: design of air-coupled PZT transducers; selection criterion for low-impedance matching materials
