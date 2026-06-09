# Module 9 – Noise in Communication Systems

- **Source:** module9 - Noise in Communication Systems.pdf
- **Drive link:** https://drive.google.com/file/d/1jUtr7Y_tzA-d34S5GP6VIqdkXVkXZ3ar/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (19 pages) introducing noise figure (NF) as a system-level metric for receiver sensitivity, deriving the Friis cascade noise formula, and establishing the design requirements for low-noise amplifiers (LNAs) in the receive chain.

## Unique contribution
Connects the abstract NF definition directly to the minimum detectable signal formula Pin = SNR_min + NF − 174 dBm + 10log(B), providing a concise path from system specification to LNA design targets.

## Key concepts
- Noise figure (NF) / noise factor F
- SNR (signal-to-noise ratio)
- Friis cascade noise formula
- Minimum detectable signal (MDS)
- LNA (low-noise amplifier)
- Thermal noise floor (−174 dBm/Hz at 290 K)
- Gain G
- System sensitivity
- kTB noise power

## Methods / results / takeaways
- Noise factor F = SNR_in/SNR_out; noise figure NF = 10 log(F) in dB.
- For a noiseless amplifier with gain G: F = 1 (NF = 0 dB); any real device has F > 1.
- Friis cascade formula: F_total = F1 + (F2−1)/G1 + (F3−1)/(G1·G2) + ...
- The first stage (LNA) dominates the cascade NF; subsequent stages are divided by the preceding gain.
- Minimum detectable signal: MDS = −174 dBm + NF + 10log(B) + SNR_min.
- Typical LNA target: G ≈ 15 dB, NF < 1.5 dB to limit system noise figure.
- Reducing NF of the first stage by 1 dB improves receiver sensitivity by 1 dB — directly increasing range (≈12% in distance for free-space path loss).
