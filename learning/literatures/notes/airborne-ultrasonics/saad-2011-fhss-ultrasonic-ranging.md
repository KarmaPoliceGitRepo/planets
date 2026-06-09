# Robust High-Accuracy Ultrasonic Range Measurement System

- **Source:** Saad 2011 FHSS ultrasonic ranging
- **Drive link:** https://drive.google.com/file/d/1JXJhdR6yDe1pxqSIWFYj50ZWNCwODY7k/view
- **Type:** paper
- **Author/Year:** Saad, Clarke & Zoubir, 2011 (IEEE Transactions on Instrumentation and Measurement, 60(10), 3334–3341)
- **Coverage:** full

## Overview
Proposes a frequency-hopping spread spectrum (FHSS) ranging system for airborne ultrasound that combats narrowband interference, multipath, and reverberation. Uses cross-correlation with earliest-peak search to find TOF, then refines to sub-sample accuracy via minimum-variance phase-shift estimation. Achieves <0.5 mm accuracy in 90% of trials in a reverberant office environment.

## Unique contribution
Combines FHSS waveform design (16 hops, 28–36 kHz, 250 Hz hop spacing) with a two-stage TOF estimator: (1) cross-correlation envelope peak to get coarse TOF within one wavelength, (2) minimum-variance weighted phase-shift refinement across hops for sub-mm accuracy. Unlike single-frequency or DSSS systems, hop diversity averages out narrowband interference and multipath notches.

## Key concepts
- FHSS (frequency-hop spread spectrum) ranging
- Cross-correlation TOF estimation
- Minimum variance phase-shift refinement
- Prowave 250ST180 transmitter (ultrasonic)
- SPM0204 CMUT receiver
- 28–36 kHz frequency range, 16 hops
- Multipath and reverberation robustness
- Sub-mm accuracy

## Methods / results / takeaways
- Transmitter: Prowave 250ST180 (narrowband 40 kHz class, driven off-resonance at 28–36 kHz via tone burst); receiver: Knowles SPM0204 CMUT (flat 20–80 kHz response).
- FHSS waveform: 16 hops × 250 Hz spacing = 8 kHz bandwidth; each hop is a tone burst; total waveform ~200 ms.
- Stage 1: matched-filter cross-correlation; earliest significant peak taken as coarse TOF (avoids multipath).
- Stage 2: cross-multiply phases of received vs. reference across hops; minimum-variance weighted average of phase delays → fractional sample refinement.
- Results: RMS error <0.35 mm; 90th-percentile error <0.5 mm; standard deviation <0.2 mm over 0.5–3 m range in office with furniture, moving people.
- Compared to single-frequency: FHSS reduces outliers from ~5% to ~0.5%.
- Temperature compensation: speed-of-sound corrected via thermistor (standard approach).
