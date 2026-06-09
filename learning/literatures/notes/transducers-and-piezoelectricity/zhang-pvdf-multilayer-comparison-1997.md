# PVDF Transducers — A Performance Comparison of Single-Layer and Multilayer Structures

- **Source:** Zhang PVDF multilayer comparison 1997
- **Drive link:** https://drive.google.com/file/d/1pGjQizf_KGaGziwYfczw8qKHJt5Di4PJ/view
- **Type:** paper (IEEE Transactions on UFFC 44(5), 1148–1156, 1997)
- **Author/Year:** Q. Zhang, P. A. Lewin, P. E. Bloomfield / 1997
- **Coverage:** full

## Overview
Derives complete matrix formulae for three multilayer PVDF transducer designs — folded (FT), Barker-coded (BCT), and switchable Barker-coded (SBCT) — and compares their pulse-echo sensitivity and bandwidth against an equivalent optimized 5 MHz PZT transducer. Demonstrates analytically and experimentally that only SBCT provides adequate pulse-echo sensitivity for medical imaging while maintaining bandwidth twice that of the PZT reference. Includes tissue loading analysis.

## Unique contribution
First comprehensive theoretical treatment providing closed-form matrix equations for all three multilayer PVDF designs (FT, BCT, SBCT). Establishes that FT improves electrical matching but not sensitivity; BCT improves bandwidth but not sensitivity (due to reduced electric field per layer in series connection); only SBCT (combining parallel TX / series RX with Barker-code polarization) achieves both goals. Shows 6 dB peak sensitivity advantage and 7.8 MHz vs 2.8 MHz (-6 dB) bandwidth with 11 P(VDF-TrFE) layers.

## Key concepts
- FT (folded transducer): layers in acoustic series, electrical parallel → better impedance matching, same sensitivity
- BCT (Barker-coded transducer): layers in acoustic series, electrical series → wide bandwidth but low sensitivity
- SBCT (switchable BCT): switches for parallel TX / series RX → sensitivity ∝ N layers; bandwidth = single layer
- PVDF properties used: kt = 0.3, Qm = 0.49; PZT: kt = 0.49, Qm = 76.9
- Tissue loading: SBCT ≈ 15 dB sensitivity advantage over PZT due to wider bandwidth (tissue low-pass filter)
- Transfer matrix A: 5×5 matrix for single layer thickness expander; cascaded as A_total = A₁·A₂···Aₙ

## Methods / results / takeaways
- Matrix expression (1) for single thickness-expander plate derived; FT uses modified form with Eq. (3)
- 11-layer SBCT: P(VDF-TrFE) layers 120 μm thick; f₀ = 10 MHz half-λ but operates off-resonance at 5 MHz
- PZT reference: air backing, two λ/4 matching layers, optimal design per DeSilets-Fraser-Kino (1978)
- SBCT -6 dB BW = 7.8 MHz vs PZT 2.8 MHz; SBCT pulse duration 4.5× shorter than PZT with spike excitation
- 7-layer prototype: measured amplitude ≈ 5× single PVDF layer (theory: 7×); adhesive thickness excess reduces gain
- Application: medical ultrasound imaging at 3.5–10 MHz; array applications benefit from PVDF's low lateral coupling
