# The Variation of the Specific Heat Ratio and the Speed of Sound in Air with Temperature, Pressure, Humidity, and CO2 Concentration

- **Source:** Cramer 1993 speed sound air
- **Drive link:** https://drive.google.com/file/d/1mYgFRi25LJtISdtVd6KgWrWp1McycPv6/view
- **Type:** paper
- **Author/Year:** Cramer, 1993 (Journal of the Acoustical Society of America, 93(5), 2510–2516)
- **Coverage:** full

## Overview
Derives accurate expressions for the speed of sound Co and the specific heat ratio γ in humid air as functions of temperature t (°C), pressure p (kPa), mole fraction of water vapour x_w, and mole fraction of CO2 x_c. Uses a real-gas equation of state with virial coefficients for the mixture. Provides a practical interpolating polynomial (eq. 15) with 16 coefficients for Co, validated against experimental data. Valid range: T = 0–30°C, p = 75–102 kPa, x_w ≤ 0.06, x_c ≤ 0.01. Uncertainty: < 300 ppm for Co, < 320 ppm for γ.

## Unique contribution
Most widely cited reference for accurate Co in moist air in the acoustics and ultrasonic metrology community. Accounts for non-ideal gas behaviour through second virial coefficients and frequency-independent dispersion. The compact 16-coefficient polynomial makes it directly programmable. Explicitly quantifies the CO2 contribution (often neglected), which matters for laboratory work and elevated-CO2 environments.

## Key concepts
- Speed of sound in moist air: Co = f(t, p, x_w, x_c)
- Specific heat ratio γ in real moist air (γ_dry = 1.4029 at STP)
- Virial equation of state for gas mixture
- Water vapour mole fraction x_w; CO2 mole fraction x_c
- Interpolating polynomial: Co = a₀ + a₁t + a₂t² + (a₃+a₄t+a₅t²)x_w + (a₆+a₇t+a₈t²)p + (a₉+a₁₀t+a₁₁t²)x_c + a₁₂x_w² + a₁₃p² + a₁₄x_c² + a₁₅x_w·p·x_c
- Reference value: Co = 331.46 m/s at 0°C, 101.325 kPa, dry air with 0.03% CO2
- Enhancement factor for saturation vapour pressure over liquid water

## Methods / results / takeaways
- Theory: start from Newton-Laplace formula Co = √(γP/ρ); expand γ and ρ in virial series for real gas mixture (N₂, O₂, Ar, CO2, H2O).
- Virial coefficients: second virial coefficients B_ij(T) for all pairs fitted to published data.
- γ_dry air at 0°C = 1.4029 (classic ideal value 1.4000 is slightly low; difference due to polyatomic corrections and virial terms).
- Humidity effect: water vapour (lighter molecule, higher heat capacity ratio) increases Co by ~0.6 m/s per 1% RH at 20°C.
- CO2 effect: increases CO2 from 0.03% to 1% decreases Co by ~0.2 m/s at 20°C.
- Pressure effect: very weak over 75–102 kPa range (< 100 ppm change).
- Polynomial (eq. 15): 16 coefficients; all fit within ±0.1 m/s over valid range.
- Comparison with experimental data: O'Connor & Wyber (1979), Younglove (1982), and others — agreement within 300 ppm.
- Limitation: not valid above 30°C or below 0°C; single-frequency result (no dispersion); CO2 term approximate.
