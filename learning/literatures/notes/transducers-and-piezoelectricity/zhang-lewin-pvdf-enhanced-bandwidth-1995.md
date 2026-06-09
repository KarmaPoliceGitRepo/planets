# Enhanced Bandwidth Multilayer Transducers for Imaging Applications

- **Source:** Zhang Lewin PVDF enhanced bandwidth 1995
- **Drive link:** https://drive.google.com/file/d/17_692qxHk5_vO5yOJuC80hf6tbtSP8Qv/view
- **Type:** paper (Archives of Acoustics 20(1), 77–90, 1995)
- **Author/Year:** Q. Zhang, P. A. Lewin / 1995
- **Coverage:** full

## Overview
Full journal paper (extended from 1993 IEEE Ultrasonics Symposium) presenting the Switchable Barker Code Transducer (SBCT) design using multiple P(VDF-TrFE) layers arranged in Barker code polarization patterns. Develops a complete matrix model for lossy multilayer piezoelectric transducers, derives closed-form expressions for a thickness-mode free resonator with complex stiffness and permittivity, and compares 11-layer SBCT performance against an optimized two-matching-layer PZT transducer at 5 MHz center frequency. Builds and tests 3-layer Barker code transducer prototypes.

## Unique contribution
Derives a full transfer matrix for lossy multilayer PVDF transducers (eq. A.11) incorporating complex elastic stiffness c'D = cD(1+jφ) and complex permittivity ε = ε₀(1−jσ). Proves mathematical equivalence of this matrix to the KLM model. Shows that SBCT provides −6 dB bandwidth of 7.8 MHz vs 2.8 MHz for optimized PZT at the same 5 MHz center frequency — a 2.8× bandwidth improvement — with pulse-echo sensitivity 6 dB higher than PZT (−15.6 dB vs −21.9 dB re 1V/V). Demonstrates that backing impedance has no effect on SBCT sensitivity (unlike resonant designs), but matched backing (Z = 4.5 MRayl) is needed to avoid pulse distortion.

## Key concepts
- SBCT operation: layers arranged per Barker code; TX mode (switches ON) = parallel layers; RX mode (switches OFF) = series layers
- TX mode: all layers electrically parallel → low impedance; acoustic output ∝ N (number of layers)
- RX mode: layers electrically series → high impedance; polarization mirrors TX → output adds coherently at time t=tp
- Bandwidth: determined by single-layer transit time (not total stack), unlike folded multilayer designs
- Matrix model: 5×5 transfer matrix per layer; cascaded for full stack; includes losses via complex c'D and ε
- KLM equivalence: proved that matrix (A.11) with propagation constant γ = jω√(ρ/c'D) is equivalent to KLM
- Backing: SBCT insensitive to backing impedance (non-resonant operation); matched backing (Z=4.5 MRayl) required for clean pulse
- 11-layer SBCT: 11 × 120 μm P(VDF-TrFE) layers → f_resonance = 10 MHz; operating center frequency 5 MHz

## Methods / results / takeaways
- Material: P(VDF-TrFE) copolymer; kt = 0.3, ρ = 1.89 g/cm³, Z = 4.5 MRayl; high mechanical and electrical loss
- 11-layer SBCT: backed by piezoelectrically inactive P(VDF-TrFE) rod (matched, Z = 4.5 MRayl)
- PZT reference: air-backed, two quarter-wavelength matching layers; center frequency 5 MHz
- SBCT −6 dB BW: 7.8 MHz; PZT −6 dB BW: 2.8 MHz (SBCT is 2.8× wider)
- SBCT peak pulse-echo sensitivity: −15.6 dB re V(Rx)/V(Tx); PZT: −21.9 dB (SBCT is 6.3 dB better)
- SBCT insertion loss: 8.3 dB re V(Rx)/V(Tx); PZT: 4 dB (SBCT is worse; high impedance RX mode issue)
- Solution: voltage follower near transducer layers converts high impedance to 50 Ω for cable matching
- 3-layer prototype tested: waveform at 5 mm distance; measured vs calculated in good agreement
- Prototype noise: attributed to inadequate electrical shielding
- Application: off-resonance wideband ultrasonic imaging; resolution tailored to clinical need without changing frequency
