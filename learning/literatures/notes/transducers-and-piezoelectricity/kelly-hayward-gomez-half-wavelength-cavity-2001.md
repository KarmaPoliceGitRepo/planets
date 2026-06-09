# An Air-Coupled Ultrasonic Matching Layer Employing Half Wavelength Cavity Resonance

- **Source:** Kelly Hayward Gomez half wavelength cavity 2001
- **Drive link:** https://drive.google.com/file/d/19t-YMzDb8WdzYyn-eBQdq2MZgyS_Aesm/view
- **Type:** paper (2001 IEEE Ultrasonics Symposium Proceedings, pp. 965–968)
- **Author/Year:** S. P. Kelly, G. Hayward, T. E. Gomez / 2001
- **Coverage:** full

## Overview
Conference paper (precursor to Kelly et al. 2004 TUFFC journal paper) introducing an integrated matching layer combining porous membrane filter (MF) with silicone rubber (SR) for air-coupled piezoelectric transducers at 600 kHz. Uses SEM and optical microscopy to reveal four-sublayer structure, then characterises each sublayer acoustically and fits a 1D linear model. Demonstrates 30 dB improvement in received signal amplitude in pitch-catch mode vs unmatched 1-3 composite transducers.

## Unique contribution
First presentation of the MF+SR composite matching layer concept for air transducers. Shows that SR impregnation into MF creates a modified SR (MSR) sublayer with reduced acoustic velocity (570 m/s vs 985 m/s) — forming a natural impedance gradient that functions as a λ/2 cavity resonator. This gradient approach avoids the need for ideal Z_opt = 0.11 MRayl material and achieves 30 dB improvement at 100 mm pitch-catch separation with no preamplifier.

## Key concepts
- Four sublayers: (1) SR (silicone rubber, ~variable thickness, Z ≈ 951×985 ≈ 0.94 MRayl), (2) MSR (modified SR at boundary, c=570 m/s, Z lower), (3) SF (MF saturated with SR, 10 μm, c=980 m/s), (4) MF (membrane filter, 110 μm, c=343 m/s, Z≈360×343 ≈ 0.12 MRayl)
- MF properties: thickness 120 μm, resonance 1.42 MHz, c=343 m/s, α=120 dB/cm, ρ=360 kg/m³
- SR properties: c≈985 m/s, α≈3.2 dB/cm at resonance, ρ≈951 kg/m³; Z ≈ 0.94 MRayl
- MSR (modified SR): c=570 m/s (slower than bulk SR); 80 μm thick; lower Z provides smoother gradient
- λ/2 cavity resonance: total thickness sets resonant frequency; SR thickness variable to tune frequency
- 1D model: 4-sublayer transmission line; includes SR thickness as free design variable
- Pitch-catch at 100 mm, 600 kHz: 30 dB improvement both transducers matched vs unmatched

## Methods / results / takeaways
- Transducers: 1-3 piezoelectric composite at 600 kHz; Perspex front plate (2.3 mm)
- SEM: SR penetration into MF ≈ 10 μm; MSR band extends 80 μm from MF interface
- Acoustic characterisation: air-coupled resonance transmission (T = |FFT_sample|²/|FFT_ref|²); resonance position → velocity; Q factor → attenuation; T_min → density
- SF properties estimated via Biot's theory (pore-saturated MF)
- Results: prototype with SR+MF matching layer achieves 30 dB improvement in pitch-catch at 100 mm; electrostatic reference transducer used for reception in some tests
- Note: this is the abbreviated conference version; full parameter tables and design methodology are in Kelly et al. 2004 (TUFFC 51(10):1314–1323)
