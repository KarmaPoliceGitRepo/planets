# Measurement of Distance and Medium Velocity Using Frequency-Modulated Sound/Ultrasound

- **Source:** Sahu Gupta 2008 FMCW distance medium velocity
- **Drive link:** https://drive.google.com/file/d/1MYIFvSOUb-ZmnRN6iWgAOwXpPsM0Lkqq/view
- **Type:** paper
- **Author/Year:** Sahu & Gupta, 2008 (IEEE Trans. Instrum. Meas. 57(4), 838–842)
- **Coverage:** full

## Overview
Proposes frequency-modulated continuous-wave (FMCW) acoustic radiation for simultaneous distance and medium-velocity measurement. Uses a PLL to demodulate the received FM signal; the DC component of the demodulated output is proportional to medium velocity, and the phase of the AC component encodes transit time. Implemented with COTS ICs (OPA741, 8038, PLL 565, XOR 7486).

## Unique contribution
Derives a closed-form model showing that the PLL demodulated output separates cleanly into a DC velocity term and an AC transit-time term, enabling simultaneous distance and flow velocity extraction from a single FMCW measurement with simple hardware.

## Key concepts
- FMCW acoustic ranging
- Phase-locked loop (PLL) demodulation
- Transit time measurement
- Medium velocity (Doppler effect)
- XOR phase detection
- Bessel function expansion
- Speaker/microphone system

## Methods / results / takeaways
- Carrier: fc = 10 kHz; modulating frequency: fm = 250 Hz; modulation index: β = 11; implemented with loudspeaker + microphone.
- Minimum measurable distance limited by near-field distortion: xi = 0.05 m.
- Transit time extracted from XOR on-time of TTL square waves from demodulated signals.
- Distance measurement: transit time vs distance follows expected linear relationship (verified vs ruler).
- Medium velocity: DC component of PLL output ∝ ±vr/vs; more sensitive than AC approach.
- Limitation: distance range ≤ c/(2fm) = 0.7 m for unambiguous measurement.
- Hardware limitation: low-frequency (audio range) system; not truly ultrasonic in implementation.
