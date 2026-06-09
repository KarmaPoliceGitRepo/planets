# High-Accuracy Measurement of Small Movement of an Object Behind Cloth Using Airborne Ultrasound

- **Source:** Hoshiba 2013 movement detection behind cloth
- **Drive link:** https://drive.google.com/file/d/1Ww6LKnpNXOvBPDtpMbD7UXk1AREMw2Yj/view
- **Type:** paper
- **Author/Year:** Hoshiba, Hirata & Hachiya, 2013 (Jpn. J. Appl. Phys. 52, 07HC15)
- **Coverage:** full

## Overview
Measures sub-6 mm/s movement of a target behind cloth at 25 kHz using M-sequence spread-spectrum correlation and MTI (moving target indicator) filter plus phase tracking. Canvas cloth introduces 27.4 dB attenuation round-trip. SNR < 0 dB before processing, successfully resolved after 27 dB M-sequence processing gain.

## Unique contribution
Combines M-sequence pulse compression, MTI filtering (difference between successive time frames), and phase tracking for breathing/heartbeat-scale movement detection through textile, achieving measurement at SNR < 0 dB. Provides theoretical error analysis of the MTI + phase tracking chain as a function of target speed and SNR.

## Key concepts
- M-sequence spread spectrum correlation
- MTI (moving target indicator) filter
- Phase tracking
- Airborne ultrasound 25 kHz
- Through-cloth ultrasound
- Vital sign monitoring (breathing, heartbeat)
- Pulse compression
- SNR under 0 dB

## Methods / results / takeaways
- Frequency: 25 kHz (λ ≈ 14 mm); speaker/microphone system.
- Canvas cloth: 0.60 mm thick, 309.5 g/m²; attenuation 27.4 dB round-trip at 25 kHz.
- M-sequence: 9th order (L=511); processing gain 27 dB; compensates cloth attenuation.
- MTI filter: difference between successive frames (0.2 s interval); rejects static reflections (walls, cloth).
- Phase tracking: integrates phase difference between successive MTI outputs to get displacement.
- Results: movement at 6 mm/s clearly tracked; 0.6 mm/s (heartbeat scale) difficult (systematic error increases as target speed decreases).
- Systematic error grows at low speed/low SNR — characterized theoretically.
- Application: unobtrusive monitoring of breathing and heartbeat through clothing in home healthcare.
