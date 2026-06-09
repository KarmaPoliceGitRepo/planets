# High-Frequency Ultrasonic Transducer Operating in Air

- **Source:** Tone high frequency air transducer 1984
- **Drive link:** https://drive.google.com/file/d/12snRrRq9SdwNJeHoOJ-0Byg4Mk7s27zW/view
- **Type:** paper (Japanese Journal of Applied Physics 23(6), L436–L438, 1984)
- **Author/Year:** M. Tone, T. Yano, A. Fukumoto / 1984
- **Coverage:** full

## Overview
Short letter describing design and demonstration of a 1 MHz double matching layer (ML) piezoelectric air transducer using Mason's equivalent circuit. First ML (inner): epoxy-SiC composite (Z₁ = 5 MRayl); second ML (outer): silicone rubber-microsphere composite (Z₂ = 0.3 MRayl). Achieves insertion loss of 52 dB (vs ~90 dB without ML), ring-down period of 9 μs at −20 dB, and range measurement accuracy of 0.1 mm at 1 MHz over 0–20 cm.

## Unique contribution
First demonstration of a silicone rubber–hollow microsphere composite (Z = 0.3 MRayl, c = 500 m/s, ρ ≈ 600 kg/m³) as the low-impedance second matching layer for 1 MHz air transducer — enabling a practical double matching layer design. Shows that double ML (52 dB) achieves similar insertion loss to single ML (50 dB) but significantly better pulse response (bandwidth). First to propose double ML scheme for high-frequency air transducers.

## Key concepts
- Optimum single ML for PZT-to-air: Z_opt = √(Z_PZT × Z_air) = √(30 MRayl × 4.2×10⁻⁴ MRayl) = 0.11 MRayl — not achievable with known materials
- Silicone rubber (single ML): Z = 1.0 MRayl → achievable but large mismatch; single ML insertion loss ~50 dB
- Double ML: Z₁ = 5 MRayl (epoxy-SiC composite), Z₂ = 0.3 MRayl (silicone rubber-microsphere composite)
- Microsphere-silicone composite: Z = 0.3 MRayl, c ≈ 500 m/s, ρ ≈ 600 kg/m³; Z tunable by microsphere wt%
- Double ML advantage: broader bandwidth (better pulse response) at similar insertion loss to single ML
- Insertion loss comparison: no ML = ~90 dB; single ML = ~50 dB; double ML = ~52 dB (2 dB difference but much wider BW)
- Mason circuit: used for all design calculations; includes backing load (Z_back = 5 MRayl ferrite rubber)

## Methods / results / takeaways
- PZT ceramic vibrator (PCM-33), diameter 30 mm, thickness resonance 1 MHz
- Backing: ferrite rubber, Z = 5 MRayl; tuning inductors used for electrical matching
- Ring-down −20 dB period: 9 μs → range resolution ~1.5 mm in air
- Distance measurement: 0–20 cm range; accuracy 0.1 mm
- Applications: cloth surface characterisation (nap length estimation from surface echoes), proximate distance measurement
- Temperature compensation: c_air = 0.18%/°C temperature coefficient accounted for
- Follow-up: expanded in Yano et al. 1987 (IEEE TUFFC 34(2))
