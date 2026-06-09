# Parameters in Lossless Transmission Line with a Load

- **Source:** TransmissionLineParameters.pdf
- **Drive link:** https://drive.google.com/file/d/1Srm3-eihOnJdQEXH1X-njMNTB9_d-HKD/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, September 14, 2013
- **Coverage:** full

## Overview
A compact mathematical derivation document covering the key parameters of a lossless transmission line terminated with a load: reflection coefficient, standing wave ratio, time-average power, return loss, input impedance formula, and transmission coefficient. Covers matched, short-circuit, and open-circuit termination cases and derives insertion loss.

## Unique contribution
Derives all standard transmission-line parameters from first principles using phasor analysis, showing explicitly how the reflection coefficient Γ leads to circle equations (the basis of the Smith chart). Covers the two-line junction (transmission coefficient T) and insertion loss.

## Key concepts
- Reflection coefficient: Γ = (ZL – Z0) / (ZL + Z0)
- Standing Wave Ratio (SWR) = (1 + |Γ|) / (1 – |Γ|)
- Time-average power: Pavg = |V0+|² / (2Z0) × (1 – |Γ|²) = PI + PR
- Return loss = –20 log|Γ| dB
- Input impedance: Z(−l) = Z0 × (ZL + jZ0 tan βl) / (Z0 + jZL tan βl)
- Transmission coefficient: T = 1 + Γ = 2ZL / (ZL + Z0)
- Insertion loss = –20 log|T| dB
- Matched load: Γ = 0, SWR = 1, Z independent of length
- Short circuit: Γ = –1, SWR = ∞, Z = jZ0 tan βl (purely reactive)
- Open circuit: Γ = +1, SWR = ∞, Z = –jZ0 cot βl (purely reactive)

## Methods / results / takeaways
- For a matched load, the transmission line acts as a resistive element (Z = Z0).
- For a short- or open-circuit termination, all power is reflected and the line acts purely as a reactive (inductive or capacitive) element depending on its electrical length.
- The voltage and current magnitudes trace circles in the complex Γ plane — this is the geometric foundation of the Smith chart.
- Incident power PI and reflected power PR are explicitly separated; Pavg = PI – PR = PI(1 – |Γ|²).
