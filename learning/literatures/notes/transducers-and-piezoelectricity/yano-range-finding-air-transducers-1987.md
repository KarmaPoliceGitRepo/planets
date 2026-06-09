# Range Finding and Surface Characterization Using High-Frequency Air Transducers

- **Source:** Yano range finding air transducers 1987
- **Drive link:** https://drive.google.com/file/d/1lFrw3Ouc2_z2rZEbYsL3xtWRDkhb_OcL/view
- **Type:** paper (IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control UFFC-34(2), 232–236, 1987)
- **Author/Year:** T. Yano, M. Tone, A. Fukumoto / 1987
- **Coverage:** full

## Overview
Full journal paper (extended from Tone et al. 1984) presenting two 1 MHz air transducer designs: (1) unfocused double matching layer (DML) using epoxy-SiC (Z=5 MRayl) + microsphere-silicone rubber (Z=0.3 MRayl); (2) focused single matching layer using concave PZT + microporous polyolefin membrane (Z=0.24 MRayl). Demonstrates applications in proximate range finding, surface profile measurement of glass bottles, defect detection in bottle openings, and cloth surface state analysis. Achieves 45–52 dB insertion loss improvement over unmatched transducer.

## Unique contribution
Introduces microporous polyolefin membrane (porosity >70%, average pore diameter 0.2 μm) as second matching layer material with Z = 0.24 MRayl, c = 800 m/s, ρ = 300 kg/m³ — lower attenuation than the microsphere-silicone composite. Provides experimental data showing frequency-dependent air attenuation: 1.6 dB/cm at 1 MHz (consistent with f² law). Shows that focused single ML transducer (1.3 mm focal spot) enables surface profile and defect measurement at 0.1 mm accuracy over 50 cm at 0.5 MHz.

## Key concepts
- Two matching layer materials:
  1. Microsphere-silicone rubber composite: Z = 0.3 MRayl, c = 600 m/s, ρ = 500 kg/m³, α = 10 dB/mm at 1 MHz
  2. Microporous polyolefin membrane: Z = 0.24 MRayl, c = 800 m/s, ρ = 300 kg/m³, α = 3 dB/mm at 1 MHz; porosity >70%, pore d ≈ 0.2 μm
- Optimal single ML impedance: Z_opt = 0.11 MRayl (not achievable; practical choices 0.24–0.3 MRayl)
- DML design: Z₁ = 5 MRayl (epoxy-SiC, λ/4), Z₂ = 0.3 MRayl (microsphere-silicone, λ/4); backing Z = 5 MRayl
- DML insertion loss improvement: +47 dB calculated, +52 dB measured (vs no ML)
- Single ML improvement: +45 dB measured (focused, microporous polyolefin)
- Air attenuation: 1.6 dB/cm at 1 MHz (measured); max range at 1 MHz = 20 cm (with 120 dB dynamic range)
- Focused transducer: concave PZT vibrator; focal spot diameter 1.3 mm; profile accuracy 0.1 mm

## Methods / results / takeaways
- PZT vibrator: PCM-33 (Matsushita); plane (unfocused) and concave (focused) geometries; 1 MHz center frequency
- Backing: ferrite rubber (Z=5 MRayl) for DML; polyurethane composite (Z=1.5 MRayl) for focused SML
- DML ring-down −20 dB period: 9 μs → range resolution 1.5 mm in air
- SML ring-down: 7 μs → narrower (higher Q); suitable for profile scanning
- Range accuracy: 0.1 mm (both designs); limited by acoustic wavelength at 1 MHz in air (λ = 0.34 mm)
- Cloth surface analysis: amplitude of through-transmitted waves classifies nap density and length (nap grade 1–5 quantified)
- Cloth overlap: detects boundary position of overlapping cloth layers with 1 mm resolution
- Temperature correction: 0.18%/°C speed variation compensated in range finder system
- Application: factory automation NDE, glass bottle inspection, textile quality control
