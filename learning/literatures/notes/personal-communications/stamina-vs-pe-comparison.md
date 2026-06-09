# STAMINA vs. Pulse-Echo Comparison

- **Source:** Accuracy of STAMINA vsPE.docx
- **Drive link:** https://drive.google.com/file/d/1vGmEKnYOtLU-JQboRljyFPxg9l-W3zT4/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Unknown (University of Sheffield research group, ~2018)
- **Coverage:** full

## Overview
A short working document comparing the thickness measurement accuracy of two ultrasonic methods: Pulse-Echo (PE) and the Multiple Standing Wave Method (STAMINA). Quantitative sensitivity analyses are presented for a cast iron plate of 5 mm thickness, examining the effect of a 1 µm thickness change and a 10 °C temperature rise on measured time-of-flight (for PE) and resonant frequency shift (for STAMINA). A future MATLAB coding task is outlined.

## Unique contribution
Provides a direct side-by-side numerical comparison of PE and STAMINA sensitivity using concrete examples. Shows that a 10 °C temperature change produces a signal shift approximately 20× larger than a 1 µm thickness change in both methods, quantifying the dominant error source in thermal environments.

## Key concepts
- Pulse-echo (PE) method — time-of-flight thickness measurement
- Multiple Standing Wave Method (STAMINA) — resonant frequency shift
- Time-of-flight (TOF), Δt sensitivity
- Resonant frequency shift ΔF sensitivity
- Coefficient of thermal expansion (CTE)
- Speed of sound temperature dependence
- Oscilloscope bit rate and minimum resolvable thickness
- Signal processing: MATLAB, noise addition, signal cleaning methods

## Methods / results / takeaways
- **PE equation:** T = v·t/2; minimum detectable TOF change with 8-bit oscilloscope at 4400 m/s is ~2 ns, giving T_min ≈ 4.4 µm for cast iron.
- **STAMINA equation:** F_res = v/(2T); a 1 µm change in a 5 mm cast iron plate shifts the first resonant frequency by ~88 Hz.
- **Temperature sensitivity (10 °C, cast iron, v = 4400 m/s, CTE = 12×10⁻⁶):** Both methods see a ~20× larger signal from temperature than from a 1 µm mechanical thickness change. This ratio is identical for PE (Δt ≈ 5.5 ns thermal vs. 0.27 ns mechanical) and STAMINA (ΔF ≈ 1053 Hz thermal vs. 53 Hz mechanical), confirming that temperature compensation is equally critical for both methods.
- **Proposed future work:** MATLAB code to simulate measurement accuracy at varying oscilloscope sampling rate and bit-depth, with noise addition and signal cleaning, to determine optimal instrument settings.
