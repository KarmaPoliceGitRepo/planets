# Module 2 – Transmission Lines in the Frequency Domain

- **Source:** Module2 - transmission lines in frequency domain.pdf
- **Drive link:** https://drive.google.com/file/d/1JleVv7MuxlXyd60TJMUhHkrmPosU2qKj/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (38 pages) extending transmission line theory to sinusoidal steady-state analysis. Derives input impedance, VSWR, and the standard λ/4 impedance transformer, building toward practical matching network design.

## Unique contribution
Presents a clean derivation of the transmission line input impedance formula and uses VSWR to quantify mismatch; the λ/4 section as a stand-alone impedance inverter is clearly motivated here before Smith Chart treatment in Module 4.

## Key concepts
- Sinusoidal steady-state
- Propagation constant γ = α + jβ
- VSWR (voltage standing wave ratio)
- Input impedance of transmission line
- Standing waves
- λ/4 impedance transformer (impedance inverter)
- Lossless transmission line
- Phase velocity
- Wavelength

## Methods / results / takeaways
- For a lossless line: γ = jβ = jω√(LC); phase velocity vp = 1/√(LC) = c/√(ε_r).
- Input impedance: Zin = Z0 · (ZL + jZ0 tan βl) / (Z0 + jZL tan βl).
- Special cases: βl = λ/4 → Zin = Z0²/ZL (impedance inverter); βl = λ/2 → Zin = ZL (repeats load).
- VSWR = (1+|Γ|)/(1−|Γ|); ranges from 1 (matched) to ∞ (open/short).
- Return loss RL = −20 log|Γ| dB; higher RL means better matching.
- Standing wave pattern: voltage maxima at distances where reflected wave adds constructively with forward wave.
- Power delivered to load: P_L = |V⁺|²(1−|Γ|²)/(2Z0).
