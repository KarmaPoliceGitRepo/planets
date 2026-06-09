# Characterization and Assessment of an Integrated Matching Layer for Air-Coupled Ultrasonic Applications

- **Source:** Kelly Hayward Gomez integrated matching 2004
- **Drive link:** https://drive.google.com/file/d/15tiMbPKdKQTFbiGTg3NdBe5Gdz3NwN-p/view
- **Type:** paper (IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control 51(10), 1314–1323, 2004)
- **Author/Year:** S. P. Kelly, G. Hayward, T. E. Gómez Alvarez-Arenas / 2004
- **Coverage:** full

## Overview
Full journal paper (expanded from Kelly et al. 2001 conference paper) presenting complete characterisation, modelling, and experimental validation of an integrated SR+MF matching layer for air-coupled NDE at 600 kHz. Develops four-sublayer 1D linear model, validates against transmission coefficient measurements, and demonstrates design strategy by sweeping SR sublayer thickness. Achieves 8.7× improvement in transmitted pressure at 600 kHz vs unmatched, and 30 dB pitch-catch improvement at 100 mm with matched transmitter (TxP) and receiver (RxP).

## Unique contribution
Full characterisation and modelling of all four sublayers (SR, MSR, SF, MF) of the integrated matching layer. Identifies that the modified SR (MSR) sublayer (c = 570 m/s, Z ≈ 0.54 MRayl) is the key element enabling smooth impedance gradient from SR (1 MRayl) to MF (0.12 MRayl) — forming a λ/2 cavity resonator rather than a conventional λ/4 converter. Provides parameter extraction methodology using air-coupled transmission coefficient resonances + Biot theory for the SR-saturated MF sublayer. Shows that optimal matching layer thickness is tuneable by SR thickness alone.

## Key concepts
- Four sublayers (from transducer to air): (1) SR: c=985–995 m/s, ρ=951–960 kg/m³, Z≈0.94 MRayl, α≈3.2–3.4 dB/cm; (2) MSR: c=570 m/s, Z≈0.54 MRayl, α=18 dB/cm; (3) SF: c=980 m/s, ρ=697 kg/m³, Z=0.68 MRayl, α=100 dB/cm; (4) MF: c=343 m/s, ρ=360 kg/m³, Z=0.12 MRayl, α=120 dB/cm
- MF: Whatman cellulose nitrate membrane, 120 μm thick, 0.45 μm pore size; very low impedance
- MSR: 80 μm layer of SR modified at MF boundary; velocity reduced by factor 1.7 from bulk SR
- SF: 10 μm SR-saturated MF; Biot theory gives c=930–1030 m/s (fast wave dominant)
- λ/2 cavity resonance: total transit time τ = 0.82 μs → resonant at 610 kHz (≈ design frequency)
- Parameter extraction: T = |FFT_sample/FFT_ref|²; f(resonance) → velocity; T_min → density; Q → attenuation
- Design: only SR thickness is variable; MF, SF, MSR thicknesses essentially fixed by manufacturing
- Performance: matched TxP: 8.7× pressure improvement vs unmatched; matched RxP: 4× improvement; both matched: 30 dB (pitch-catch, 100 mm separation)

## Methods / results / takeaways
- Transducers: PZT5H (TxP, 70% vol frac) and PZT5A (RxP, 30% vol frac) 1-3 composites at 600 kHz; Perspex front plate 2.3 mm
- 11 matching layers (M1–M11) manufactured with SR thickness 0.01–0.86 mm; total thickness 0.21–1.06 mm
- Electrostatic transducers as reference for reception; wideband response 0–3 MHz
- Transmission mode experiments: narrowband (600 kHz, 20-cycle tone burst) + wideband (impulse) at 50 mm separation
- Cavity resonance frequencies (M10, SR=0.74mm): λ/2 at ~373 kHz; 3λ/4 at 279 kHz; etc. — all agree with theory
- Theory-experiment correlation: very good for both narrowband SR thickness sweep and wideband frequency response
- Factor 2.5× better than λ/4 silicone rubber alone (theoretical comparison)
- Application: air-coupled NDE of aerospace composites; CFRP, Perspex, aluminium inspection at stand-off
