# Aerogel Matching Layer for Air-Coupled Ultrasonic Tactile Display

- **Source:** Korres aerogel matching layer 2013
- **Drive link:** https://drive.google.com/file/d/1Tt0h-R3uKiCrI5gq3m2VxwSzslfI7idS/view
- **Type:** paper (2013 IEEE International Conference on Systems, Man, and Cybernetics / haptics proceedings)
- **Author/Year:** G. Korres, M. Bhatt, M. Eid / 2013
- **Coverage:** full

## Overview
Evaluates cross-linked aerogel alloy (Airloy X103L) as a replacement for the manufacturer-supplied matching layer on commercial Murata MA40S4S 40 kHz air-coupled transducers for mid-air ultrasound tactile display applications. Machines Airloy X103L discs to fit the transducer front face, measures acoustic pressure at fixed distance, and compares directivity patterns and voltage-to-pressure response. Achieves 2–3 dBV average improvement over Murata's built-in matching layer.

## Unique contribution
First use of Airloy X103L cross-linked aerogel alloy (a commercially available, machineable solid aerogel) as a drop-in replacement matching layer for a standard commercial air transducer. Shows practical viability of machined aerogel for tactile display applications where conventional quarter-wave impedance matching is difficult. Characterises directivity pattern modification and identifies manual machining variability as the main performance limitation.

## Key concepts
- Transducer: Murata MA40S4S, 40 kHz nominal; 16 mm diameter; existing horn + matching layer built in
- Aerogel alloy: Airloy X103L; Z ≈ 0.044 MRayl; cross-linked polymer network — machinable (unlike fragile silica aerogel)
- Impedance matching target: Z_opt ≈ √(Z_PZT × Z_air) = √(33 × 0.000429) ≈ 0.12 MRayl (approximate)
- Airloy X103L vs target: Z = 0.044 MRayl — closer to ideal than most solid materials
- Measured improvement: 2–3 dBV average increase in received voltage at fixed distance
- Directivity: beam FWHM ≈ 40° (±20°); comparable to Murata built-in design
- Variability: manual machining to precise λ/4 thickness (≈ 4.3 mm at 40 kHz, c_aerogel ≈ 350 m/s) causes sample-to-sample inconsistency (±1–2 dBV spread)
- Application: mid-air ultrasound tactile display arrays; focused pressure field generation

## Methods / results / takeaways
- Machining: Airloy X103L slab hand-machined to circular disc, glued to transducer front face
- Test setup: single-frequency 40 kHz CW; calibrated microphone at fixed distance; angular sweep for directivity
- Results: 2–3 dBV improvement vs MA40S4S bare (unmodified); highest individual sample: 3.5 dBV
- Directivity comparison: aerogel ML narrows beam slightly vs bare transducer — consistent with improved near-axis radiation
- Variability: 3 machined samples showed ±1.5 dBV spread; attributed to thickness inconsistency
- Limitation: Airloy X103L is brittle under manual cutting; CNC or laser cutting would improve consistency
- Comparison to Khuri-Yakub 1988: same aerogel principle; Airloy X103L is denser / more robust than silica aerogel but still low-Z
- Application: Ultrahaptics-type mid-air tactile displays; gesture recognition systems; air-coupled NDE
