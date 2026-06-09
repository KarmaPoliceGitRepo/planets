# Absorption of Ultrasonic Waves in Air at High Frequencies (10–20 MHz)

- **Source:** Bond 1992 absorption air high frequencies
- **Drive link:** https://drive.google.com/file/d/1LXp03zMr9rSl3p5slR2XUmqEk5rKLcby/view
- **Type:** paper
- **Author/Year:** Bond, Chiang & Fortunko, 1992 (Journal of the Acoustical Society of America, 92(4), 2006–2015)
- **Coverage:** full

## Overview
Measures and models sound absorption in air at 10–20 MHz, a regime where classical+rotational (viscothermal) losses dominate and molecular relaxation of N₂ and O₂ is negligible. Derives the classical+rotational absorption coefficient: α_cr = 1.83×10⁻¹¹ (T/T₀)^(1/2) f²/(P/P₀) Np/m [equivalent: 15.895×10⁻¹¹ (T/T₀)^(1/2) f²/(P/P₀) dB/m]. Validated at P = 80–90 kPa, T = 15–25°C. At 20 MHz, 83 kPa, 22.5°C: measured α ≈ 79–81 dB/mm; theory gives 77.5 dB/mm. Concludes humidity has negligible influence above ~500 kHz.

## Unique contribution
Extends the validated range of classical+rotational absorption formula to 20 MHz in air — filling a gap between audio-range absorption tables (ISO 9613-1) and the multi-MHz regime needed for high-frequency ACU and airborne NDT. Provides the key design equation for standoff distance budgets in air-coupled ultrasound above 0.5 MHz, where humidity no longer matters (simplifying system design).

## Key concepts
- Classical + rotational absorption: α_cr ∝ f²/P (viscothermal losses)
- Formula: α_cr = 1.83×10⁻¹¹ (T/T₀)^(1/2) f²/(P/P₀) Np/m
- T₀ = 293.16 K, P₀ = 101.325 kPa reference conditions
- Molecular relaxation absorption of N₂ and O₂ (negligible above 500 kHz at normal P)
- Frequency regime: classical+rotational dominant above 500 kHz
- Humidity effect on absorption: significant at audio frequencies, negligible above 500 kHz
- Pressure dependence: α_cr ∝ 1/P (higher altitude → higher attenuation per metre)
- Temperature dependence: α_cr ∝ T^(1/2)

## Methods / results / takeaways
- Experiment: resonant cavity and pulse-echo methods; f = 10–20 MHz; P = 80–90 kPa (high altitude lab, Gaithersburg, MD, ~100 m elevation); T = 15–25°C; dried air (< 5% RH) and ambient humidity compared.
- Results: measured α at 20 MHz, 83 kPa, 22.5°C ≈ 79–81 dB/mm; classical+rotational theory gives 77.5 dB/mm — agreement within ±2%.
- Sound velocity: at 10 MHz, 83 kPa, 24.3°C measured 347.6 m/s vs calculated 346.4 m/s — 0.3% agreement.
- Humidity comparison: at 5% vs 60% RH, absorption difference < 1% above 500 kHz — confirms classical+rotational dominance.
- Below 500 kHz: N₂ and O₂ vibrational relaxation contribute; α formula underestimates; use ISO 9613-1 tables.
- Practical implication for ACU at 5 MHz: α_cr ≈ 2.4 dB/mm at STP — limits standoff to < a few mm. At 500 kHz: α_cr ≈ 0.024 dB/mm — standoff up to ~100 mm feasible.
- Limitation: measurements only at 80–90 kPa; theoretical extrapolation to 101 kPa is straightforward but not validated at 10–20 MHz.
