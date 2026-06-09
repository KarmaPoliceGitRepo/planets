# Air-Coupled and Resonant Pulse-Echo Ultrasonic Technique

- **Source:** Alvarez-Arenas 2019 resonant pulse-echo ACU
- **Drive link:** https://drive.google.com/file/d/1R3h3TvOkeMkVurekUKXsTz1G5GZFvP9q/view
- **Type:** paper
- **Author/Year:** Gómez Álvarez-Arenas, 2019 (Sensors, 19, 2221)
- **Coverage:** full

## Overview
Introduces a resonant pulse-echo air-coupled ultrasonic (ACU) technique for characterising high-acoustic-impedance, low-attenuation materials (metals, ceramics) from a single side. Exploits high-Q plate resonances: a short burst excites standing waves in the plate; the reverberant decay lasts milliseconds (well outside the dead zone), enabling accurate thickness and elastic stiffness measurement. Tested on steel and aluminium plates and pipes.

## Unique contribution
Bypasses the ACU dead-zone problem by using the long resonant decay (Q > 6200, τ > 8 ms for steel) rather than the direct pulse-echo. Single-sided access; no water coupling needed; spatial C-scan by tracking resonant frequency. Demonstrates simultaneous thickness + elastic constant extraction from resonance spectrum without separate calibration of transducer bandwidth.

## Key concepts
- Resonant pulse-echo ACU
- High-Q plate resonances
- Dead zone elimination
- Air-coupled ultrasound NDE
- Through-thickness resonances
- C-scan imaging
- Steel and aluminium plate characterisation
- 1-3 piezocomposite transducer
- Quality factor Q measurement
- Elastic stiffness from resonance spacing

## Methods / results / takeaways
- Transducer: 400 kHz ACU 1-3 piezocomposite; bandwidth ~30% at −6 dB; single-sided pulse-echo.
- Excitation: short burst (2–5 cycles); plate resonances excited within burst bandwidth.
- Signal recorded: long decaying resonant oscillation (τ = Q/πf); for 6 mm steel: f_res ≈ 460 kHz, Q > 6200, τ > 8 ms.
- Measurement: FFT of decay → resonance frequencies → thickness = c/(2Δf); elastic constant from absolute freq.
- C-scan: raster scan with resonant frequency mapped → wall thickness image; defect detection by local Q drop or frequency shift.
- Pipes: inner wall accessible from outside only; resonance technique gives wall thickness at each scan point.
- Accuracy: ±5 μm thickness on 6 mm steel plate; lateral resolution limited by transducer beam diameter (~5 mm).
- Compared to standard ACU through-transmission: resonant technique needs only one transducer side; handles materials with high Z where transmission loss > 80 dB.
