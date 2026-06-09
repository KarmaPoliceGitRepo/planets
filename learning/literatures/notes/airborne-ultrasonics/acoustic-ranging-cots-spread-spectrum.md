# Robust Acoustic Ranging with COTS Hardware Using Spread Spectrum

- **Source:** Girod & Estrin 2001 acoustic ranging with COTS hardware
- **Drive link:** https://drive.google.com/file/d/1Cs_TYreCApR7j54ycieoonKtfflfYXTd/view
- **Type:** paper
- **Author/Year:** Girod & Estrin, 2001
- **Coverage:** full

## Overview
Demonstrates BPSK m-sequence (pseudo-noise) spread-spectrum acoustic ranging using commercial off-the-shelf (COTS) audio hardware, achieving ~1 cm accuracy over 6.5 m range. Targeted at low-cost indoor localisation and sensor network positioning.

## Unique contribution
Shows that spread-spectrum cross-correlation with m-sequences enables cm-level ranging using cheap COTS speaker/microphone hardware (no specialised ultrasonic transducers), providing a viable low-cost alternative to dedicated ultrasonic ranging modules for indoor sensor network localisation.

## Key concepts
- BPSK m-sequence / pseudo-noise ranging
- Spread-spectrum acoustics
- COTS audio hardware
- Indoor localisation
- Cross-correlation TOF detection
- Multipath mitigation
- Sensor network positioning

## Methods / results / takeaways
- Signal: BPSK-modulated m-sequence (maximal-length binary sequence) broadcast via COTS loudspeaker.
- Detection: cross-correlation of received audio with known m-sequence.
- Accuracy: ~1 cm over 6.5 m range under indoor multipath conditions.
- Multipath: spread-spectrum cross-correlation suppresses multipath by processing gain; sidelobe level related to sequence length.
- Hardware: standard PC soundcard + commodity speaker/mic — no custom transducers.
- Temperature compensation: GPS-like approach using multiple known-distance references.
- Limitation: audible frequencies → interference with human speech; system uses bandpass filtering and quiet periods.
- Demonstrated on sensor network nodes for room-scale positioning.
