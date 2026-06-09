# Foundations for Microwave Engineering — Oscillators and Mixers (Chapter 12)

- **Source:** Oscillators and Mixers.pdf
- **Drive link:** https://drive.google.com/file/d/1UFqOsW8qFrnQcy2-xkRbGF-7jXJzpbyC/view?usp=drivesdk
- **Type:** book (chapter)
- **Author/Year:** Robert E. Collin, 2001
- **Coverage:** partial (large file, truncated extraction)

## Overview
The final main chapter of Collin, covering microwave oscillator design principles and mixer design. Oscillators are treated using negative-resistance, feedback, and Kurokawa stability approaches. Mixer design covers resistive (diode) mixers, single-balanced, double-balanced topologies, and conversion loss/noise figure analysis.

## Unique contribution
Provides a thorough treatment of mixer theory that goes beyond the simple product detector model, including image-frequency noise, noise figure of mixers, and the analysis of balanced mixers using S-parameter methods. The Kurokawa oscillator theory for negative-resistance oscillators is carefully developed.

## Key concepts
- Oscillator design: Barkhausen criterion (loop gain = 1, phase = 0°)
- Negative-resistance oscillator: Zin = –R + jX; oscillation when –R + Rload = 0
- Kurokawa stability theory: oscillator stability with respect to amplitude and frequency perturbations
- Gunn diode and IMPATT diode oscillators (transferred-electron and avalanche devices)
- Mixer: frequency conversion using nonlinear device (diode or transistor)
- Single-diode mixer, single-balanced mixer, double-balanced mixer
- Conversion loss, noise figure, isolation, image rejection
- Image frequency and image-frequency noise contribution

## Methods / results / takeaways
- Barkhausen criterion: in a feedback oscillator, the loop gain must equal 1 and the phase shift must be 0° (or 360°) at the oscillation frequency.
- Negative-resistance oscillator stability (Kurokawa): stable if ∂|Zin|/∂A > 0 (device resistance decreases with amplitude) and the frequency pulling characteristic has the right sign.
- Gunn diodes (GaAs) work by transferred-electron effect (Gunn effect) at fields above ~3 kV/cm, creating negative differential resistance; useful to ~100 GHz.
- Double-balanced mixer: uses a diode quad and two baluns; provides high isolation between LO, RF, and IF ports; cancels LO noise; rejects even-order harmonics.
- Image frequency: in a down-converter with LO at fLO, the desired RF at fLO + fIF and the image at fLO – fIF both mix to fIF; image rejection requires filtering before the mixer.
- Conversion loss of a single-diode mixer: typically 6–9 dB; double-balanced mixer similar conversion loss but better isolation and linearity.
