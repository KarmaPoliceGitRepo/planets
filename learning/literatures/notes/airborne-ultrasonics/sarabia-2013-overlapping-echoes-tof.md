# Accurate Estimation of Airborne Ultrasonic Time-of-Flight for Overlapping Echoes

- **Source:** Sarabia 2013 overlapping echoes TOF
- **Drive link:** https://drive.google.com/file/d/1D-b5gSfzaD6Z47-3s_zLJ2GEQoqN3r5T/view
- **Type:** paper
- **Author/Year:** Sarabia, Llata, Robla, Torre-Ferrero & Oria, 2013 (Sensors 13, 15465–15488)
- **Coverage:** full

## Overview
Develops a physics-based model of the ultrasonic pulse-echo transient response (2nd-order overdamped system) for 40 kHz SensComp piezoelectric sensors, then uses the modelled peak-time relation to extract accurate start times for overlapping echoes. The maximum-time method outperforms threshold and cross-correlation in accuracy and computation time.

## Unique contribution
Derives a 2nd-order linear model for the sensor's transient response to short and long excitation pulses, enabling the start time of any echo (including multiple overlapping sub-echoes) to be estimated from peak time alone — without needing signal amplitude information. Demonstrates simultaneous extraction of multiple TOF values from one received signal.

## Key concepts
- Pulse-echo TOF estimation
- 2nd-order overdamped transient model
- Overlapping echo separation
- Maximum-time method
- Threshold method comparison
- Cross-correlation (auto-correlation) comparison
- 40 kHz piezoelectric sensor (SensComp 40LT16)
- Gaussian beam directivity approximation
- Autonomous robot navigation

## Methods / results / takeaways
- Sensor: SensComp 40LT16/40LR16 at 40 kHz; time constant τ = 160 μs (short pulses <50 cycles), 135 μs (long pulses).
- Model validated for: transmitter-to-receiver facing, perpendicular wall rebound, 10° and 20° angled wall.
- Directivity approximated as Gaussian: H(θ) = exp(−θ²/0.24).
- Maximum method: find tmax, subtract t(ymax) from model → start time tm. Not affected by amplitude.
- Threshold: inaccurate when multiple echoes; only detects first echo.
- Cross-correlation: more accurate than threshold but computationally expensive; misses secondary echoes.
- Maximum method computation time lowest; can find 2–3 overlapping echo start times from single signal.
- Application: structured indoor robot navigation; simultaneous multi-surface distance measurement.
