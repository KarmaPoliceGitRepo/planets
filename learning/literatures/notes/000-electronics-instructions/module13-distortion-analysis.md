# Module 13 – Distortion Analysis

- **Source:** module13 - Distortion Analysis.pdf
- **Drive link:** https://drive.google.com/file/d/1Jlcr4kT2pyYgUSjiB95mdU0CRQ0VKYHj/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (48 pages) on nonlinear distortion in RF circuits. Uses the power series model to derive harmonic distortion (HD), intermodulation distortion (IM), and cross-modulation products; analyzes specific device types (BJT, long-channel MOSFET) for their inherent distortion characteristics.

## Unique contribution
Provides a systematic derivation of all distortion products from the power series coefficients and explicitly shows that the long-channel MOSFET's square-law I-V relationship makes a3 = 0, giving infinite third-order intercept — a fundamental device insight affecting circuit topology choices.

## Key concepts
- Power series nonlinearity model
- Harmonic distortion HD2, HD3
- Intermodulation distortion IM2, IM3
- Intermodulation products
- Taylor series coefficients a1, a2, a3
- Third-order intercept point (IIP3 concept introduced)
- BJT CE amplifier distortion
- Long-channel MOSFET square-law
- Cross-modulation
- Gain compression

## Methods / results / takeaways
- Output modeled as: so = a1·si + a2·si² + a3·si³ + higher order terms.
- Single tone (si = A·cosωt): HD2 = a2·A/(2a1), HD3 = a3·A²/(4a1); HD grows with input amplitude.
- Two-tone (si = A·cos(ω1t) + A·cos(ω2t)): IM3 = 3a3·A²/(4a1) at 2ω1−ω2 and 2ω2−ω1; IM3 = 3·HD3 + 10 dB for same input level.
- BJT CE distortion: HD2 ≈ vi/(4VT) where VT = kT/q ≈ 26 mV; BJT is inherently highly nonlinear for large signals.
- Long-channel MOSFET: iD = (μCox/2)(W/L)(vGS−VT)²; perfect square law → a3 = 0 → no third-order IM; only even-order distortion.
- Short-channel MOSFETs deviate from square law → a3 ≠ 0; IIP3 degrades.
- Distortion depends strongly on operating point and signal amplitude; hand analysis valid only for small signals (weakly nonlinear regime).
