# Wideband and Efficient Polymer Transducers Using Multiple Active Piezoelectric Films

- **Source:** Zhang Lewin PVDF multilayer wideband 1993
- **Drive link:** https://drive.google.com/file/d/1zh6_GM9wJ1Q3_49gLyR5FuBZJ26-KNqh/view
- **Type:** paper (IEEE Ultrasonics Symposium 1993, pp. 757–760)
- **Author/Year:** Q. Zhang, P. A. Lewin / 1993
- **Coverage:** full

## Overview
Introduces a non-resonant multilayer PVDF transducer design using a 7-element Barker-coded polarization stack. The Barker coding principle (from digital communications) is applied to piezoelectric layer polarization directions so that the transducer sensitivity scales with the number of layers while bandwidth is determined by the single-layer thickness. Demonstrates with computer simulations and a 3-layer prototype that an 11-layer Barker coded transducer can match the sensitivity of an optimized PZT transducer while providing twice the bandwidth.

## Unique contribution
First application of Barker-code pulse compression principle to PVDF multilayer transducer design as a sensitivity-enhancement scheme without sacrificing bandwidth. Demonstrates 6.3 dB sensitivity advantage and 2x bandwidth increase of 11-layer SBCT over optimized 5 MHz PZT with quarter-wavelength matching layers. Introduces the switchable Barker-coded transducer (SBCT) concept enabling pulse-echo operation with switches.

## Key concepts
- Barker code: 7-element binary sequence [+1,+1,+1,-1,-1,+1,-1]; autocorrelation peak ∝ N layers
- PVDF multilayer: polarization direction of each layer follows Barker code sign pattern
- SBCT (switchable Barker-coded transducer): parallel connection during TX, series during RX
- Bandwidth = 1/(single PVDF layer transit time), independent of number of layers
- Sensitivity ∝ N (number of active layers); equivalent to N-times PVDF single-layer sensitivity
- Pulse compression: h(t) = hl(t) ⊗ h2(t); two-way response is autocorrelation of hl(t)

## Methods / results / takeaways
- Theoretical model from Zhang & Lewin (1992) SPIE paper; applied to 11-layer P(VDF-TrFE) SBCT
- Simulation: SBCT 11-layer peak amplitude −21.8 dB vs PZT −27.7 dB; SBCT bandwidth 2× wider
- 3-layer prototype: measured waveform matches prediction; noise from inadequate electrical shielding
- Reference PZT: air-backed, two λ/4 matching layers, 5 MHz center frequency, 50 Ω excitation
- Application: medical ultrasound imaging; improved image quality via wider bandwidth + higher sensitivity
