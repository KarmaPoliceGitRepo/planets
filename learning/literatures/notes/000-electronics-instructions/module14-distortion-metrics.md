# Module 14 – Distortion Metrics

- **Source:** module14 - Distortion Metrics.pdf
- **Drive link:** https://drive.google.com/file/d/1h7_G_gsyhg0x27NSvwqRxjwcMDVf3-Rn/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (34 pages) defining and applying the standard RF linearity metrics: 1 dB gain compression point (P−1dB), second- and third-order intercept points (IP2, IP3), and cascade IIP3. Also covers desensitization, cross-modulation, and the role of blockers and jammers in receiver design.

## Unique contribution
Systematically derives the relationship P−1dB = IIP3 − 9.6 dB and the cascade IIP3 formula, and introduces the blocker/jammer problem in the context of real receiver specifications — bridging lab-bench metrics to system-level specification compliance.

## Key concepts
- 1 dB compression point (P−1dB, OP−1dB)
- IIP2 (input-referred second-order intercept)
- IIP3 (input-referred third-order intercept)
- OIP3
- Gain compression
- Blocker / jammer
- Desensitization
- Cross-modulation
- Cascade IIP3 formula
- Spurious-free dynamic range (SFDR)

## Methods / results / takeaways
- 1 dB compression: output power is 1 dB below the linear extrapolation; occurs approximately when |a3|·A² = 4/(3)·a1 → P−1dB (input) ≈ IIP3 − 9.6 dB.
- IIP3: extrapolated intersection of fundamental (slope 1 on log-log) and IM3 product (slope 3); IIP3 = √(4a1/3|a3|) in amplitude.
- IIP2: intersection of fundamental and IM2 product; important for direct-conversion receivers (IM2 falls at baseband).
- Cascade IIP3: 1/IIP3_total ≈ 1/IIP3_1 + G1/IIP3_2 + G1·G2/IIP3_3 + ...; last high-gain stage usually dominates.
- Blocker desensitization: a large out-of-band signal compresses the LNA gain, reducing sensitivity for the wanted signal.
- Cross-modulation: AM on a blocker is transferred to the wanted signal via the a3 term; CM = 4·IM3 (6 dB higher for same power levels).
- Spurious-free dynamic range: SFDR = (2/3)·(IIP3 − N_floor) dB, defining the range over which IM3 stays below the noise floor.
