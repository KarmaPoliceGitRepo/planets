# Low Cost Matching Network for Ultrasonic Transducers

- **Source:** 2010 - Low cost matching network for ultrasonic transducers - Garcia-Rodriguez.pdf
- **Drive link:** https://drive.google.com/file/d/15KvKWSuRRo-KjfQ7aY0HN-t6iGPYX5SO/view
- **Type:** paper (conference)
- **Author/Year:** M. Garcia-Rodriguez, J. Garcia-Alvarez, Y. Yañez, M.J. Garcia-Hernandez, J. Salazar, A. Turo, J.A. Chavez / 2010
- **Coverage:** full

## Overview
Proposes a simple two-component LC electrical matching network for high-impedance ultrasonic transducers, as an alternative to complex transformer-based or multi-element matching networks. Uses the Butterworth-Van-Dyke (BVD) model for transducer impedance representation, derives the LC values analytically for conjugate matching, and demonstrates ~9× power improvement (300% amplitude improvement) in both simulation and experiment for an 800 kHz air-coupled transducer and a 100 kHz shear wave transducer.

## Unique contribution
Shows that a single L-C (inductor + capacitor) matching network can match both real and imaginary parts of a high-impedance transducer to a 50 Ω source, providing ~9× more acoustic power than an unmatched system, while requiring only two components — practical for multi-channel array systems where complex matching per element is infeasible.

## Key concepts
- Butterworth-Van-Dyke (BVD) equivalent circuit model for piezoelectric transducer
- Electrical matching network (L-C matching)
- Conjugate impedance matching
- Transducer series resonance and parallel resonance
- Air-coupled ultrasonic transducer (800 kHz, Rs=1.8 kΩ)
- Shear wave transducer (100 kHz, Rs=1.5 kΩ)
- Power transfer maximisation
- Signal-to-noise ratio improvement

## Methods / results / takeaways
- BVD model: C₀ (parallel capacitance), Rs (radiation/mechanical loss), Ls (motional inductance), Cs (motional capacitance)
- Matching conditions: X₁ = (R_g/R_t)^½ × [Q_g×R_g − X_g], X₂ = −X_g − X₁ × R_t/R_g; simplified for R_g ≪ R_t to standard L-C network
- Air-coupled transducer (800 kHz): BVD params Rs=1.8 kΩ, Ls=1.6 mH, Cs=26 pF, C₀=65 pF → matching L_m=58.8 μH, C_m=588 pF
- Shear wave transducer (100 kHz): Rs=1.5 kΩ, Ls=8.6 mH, Cs=278 pF, C₀=692 pF → L_m=430 μH, C_m=5 nF
- Simulation: power improvement ~9× (900%) for both transducer types with matching network
- Experiment (air-coupled): signal amplitude improved ~3× (300%) at hydrophone 1.7 cm away — consistent with ×9 power prediction
- Experiment (shear wave): similar ~3× amplitude improvement in through-transmission
- Low-pass filter topology preferred to avoid harmonic excitation of nonlinear systems
