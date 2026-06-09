# A Multi-Frequency Method for Ultrasonic Ranging

- **Source:** Queiros 2015 multi-frequency ultrasonic ranging
- **Drive link:** https://drive.google.com/file/d/1r48tED86gp3JnVWc5zE-6XStFAPy28lR/view
- **Type:** paper
- **Author/Year:** Queirós, Alegria, Girão & Serra, 2015 (Ultrasonics 63, 86–93)
- **Coverage:** full

## Overview
Proposes a multi-frequency stepped-frequency TOF method for airborne ultrasonic ranging using cross-correlation of a signal composed of several narrow-band sine-wave bursts at slightly different frequencies, all close to the 40 kHz transducer resonance. Achieves <0.3 mm experimental error (2σ) over 200–1000 mm range.

## Unique contribution
Shows that narrow-bandwidth piezoelectric transducers can be used for multi-frequency cross-correlation by choosing burst frequencies satisfying an orthogonality condition (Δf·Td = integer), which minimises sidelobe interference while remaining within the transducer bandwidth. Spline interpolation applied to the correlation peak yields sub-sample TOF resolution.

## Key concepts
- Multi-frequency (stepped-frequency) ranging
- Cross-correlation TOF estimation
- Orthogonality condition for burst frequencies
- Spline interpolation for sub-sample resolution
- Narrow-bandwidth piezoelectric transducer 40 kHz
- Phase ambiguity in single-frequency methods
- Temperature/humidity compensation for speed of sound

## Methods / results / takeaways
- Transducers: SensComp 40L16 at 40 kHz.
- Signal: 3 bursts at 39.6, 40.2, 39.9 kHz (orthogonality condition Δf·Td = 300 Hz × 3.358 ms = 1 satisfied).
- DAQ: NI6110 12-bit card at 5 MS/s; Agilent 33220A AWG for TX.
- Cross-correlation computed in frequency domain (FFT). Spline interpolation applied to main peak.
- Results: mean error <0.25 mm, σ <0.15 mm over 200–1000 mm; 2σ error <0.3 mm.
- Measurement rate ~0.3 s.
- Key insight: bursts with wide frequency spacing reduce sidelobes but transducer bandwidth constrains spacing → orthogonality condition bridges these constraints.
- Uses Cramer 1993 formula for speed-of-sound compensation.
