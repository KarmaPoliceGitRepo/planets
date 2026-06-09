# Module 20 – The ABC's of PA's

- **Source:** module20 - The ABC's of PA's.pdf
- **Drive link:** https://drive.google.com/file/d/1jvJ-uD5yHtYgcPWMWmKgDvurFD8LPw3K/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (26 pages) covering PA operating class taxonomy: Class A (linear, 360° conduction), Class B (180° conduction, push-pull or tuned), Class AB (practical hybrid), and Class C (sub-180° conduction, high efficiency). Derives efficiency and power capacity for each class analytically.

## Unique contribution
Derives the Class B maximum efficiency of π/4 ≈ 78.5% from Fourier analysis of half-sinusoid current pulses, and shows the Class C efficiency → 100% as conduction angle → 0 while power capacity simultaneously → 0, quantifying the fundamental efficiency-linearity-power trade-off in a single framework.

## Key concepts
- PA operating class (A, AB, B, C)
- Conduction angle
- Class B efficiency (π/4 ≈ 78.5%)
- Tuned Class B
- Class C efficiency
- Power capacity PC
- Push-pull amplifier
- Dynamic PA (envelope tracking)
- Polar modulation
- Collector modulation

## Methods / results / takeaways
- Class A: 360° conduction; max efficiency 50% with inductive load; linear; best for linear modulations.
- Class B: 180° conduction; average supply current IQ = Ip/π scales with output power → efficiency drops gracefully at back-off; max ηB = π/4 ≈ 78.5%.
- Tuned single-transistor Class B: high-Q tank filters harmonics; only fundamental delivered to load; same efficiency as push-pull version.
- Power capacity PC = Pout/(Vmax·Imax) = 0.125 for both Class A and Class B.
- Class C: conduction angle < 180°; as angle → 0°, efficiency → 100% but current pulse → delta function requiring infinite peak current; power capacity → 0.
- Class AB: practical compromise between A and B; allows small trickle current to avoid crossover distortion; efficiency between 50% and 78.5%.
- Dynamic PA: envelope-tracking supply tracks output amplitude; maintains Class A near peak efficiency (~30%) regardless of PAR; requires fast DC-DC converter.
- Polar modulation: Class C driven into saturation; amplitude modulation applied via supply voltage; separates amplitude and phase paths.
- Class C linearity: only suitable for constant-envelope modulations (FM, GMSK); non-linear for amplitude-modulated signals.
