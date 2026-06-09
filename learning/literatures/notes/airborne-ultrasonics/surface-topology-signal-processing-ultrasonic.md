# The Determination of Surface Topology by the Signal Processing of Ultrasonic Pulses

- **Source:** Smith 1988 surface topology ultrasonic signal processing
- **Drive link:** https://drive.google.com/file/d/1jNlbEux0eOvJBn7ZuyrbPd2y7fVR1DK2/view
- **Type:** paper
- **Author/Year:** Smith, Player & Collie, 1988 (J. Phys. E: Sci. Instrum. 21, 397–401)
- **Coverage:** full

## Overview
Demonstrates deconvolution of broadband pulse-echo ultrasound from surfaces using the Maximum Entropy Method (MEM) to recover height distribution curves. Uses 10 MHz immersion probe in water bath. Compared MEM with Wiener-Hopf filter; MEM produces superior noise-free results. Tests on grooved aluminium blocks, stepped NDT surfaces, paint layers, and hidden (internal) surfaces.

## Unique contribution
Demonstrates MEM-based deconvolution for ultrasonic surface topography, resolving grooves down to <15 μm depth and outperforming the Wiener-Hopf filter in noise immunity and artifact suppression. Can extract height distributions for areas (not just 1D profiles) and inspect surfaces inaccessible to stylus instruments.

## Key concepts
- Maximum entropy method (MEM) deconvolution
- Ultrasonic surface topography
- Wiener-Hopf filter comparison
- Height distribution (amplitude distribution)
- Immersion transducer 10 MHz
- Water bath coupling
- Fredholm equation deconvolution
- Tilt sensitivity
- Internal/hidden surface inspection

## Methods / results / takeaways
- System: 10 MHz NDT probe, water bath, Tektronix 2430 digitising scope (150 MHz, 10-bit H × 8-bit V), HP300 microcomputer.
- Test surfaces: duralumin grooved blocks (70 μm and 25 μm depth), standard NDT step calibration, paint-coated block, hidden step (steel-block through-transmission).
- MEM resolves <15 μm groove depth; Wiener-Hopf shows noise amplification and artifacts.
- Tilt sensitivity: 0.04° tilt produces measurable differences in peak heights; tilt correction is a key remaining challenge.
- Hidden surface (510 μm step through steel): resolved via through-transmission MEM.
- Baseline SNR ~45 dB (single), improved to ~62 dB by 50-shot averaging.
- Validation against Talysurf stylus instrument (after convolution correction for resolution difference).
