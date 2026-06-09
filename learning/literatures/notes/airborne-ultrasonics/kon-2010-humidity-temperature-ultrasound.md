# Noncontact Measurement of Humidity and Temperature Using Airborne Ultrasound

- **Source:** Kon 2010 humidity temperature ultrasound
- **Drive link:** https://drive.google.com/file/d/1R8SUt-JtUBuQ3z0epYo2c3YI4iWo_Bl-/view
- **Type:** paper
- **Author/Year:** Kon, Mizutani & Wakatsuki, 2010 (Japanese Journal of Applied Physics, 49, 046601)
- **Coverage:** full

## Overview
Proposes and validates a noncontact method to measure relative humidity (RH) and dry-bulb temperature simultaneously using airborne ultrasound at 40 kHz. Water vapour increases sound velocity; this shift is measured via time-of-flight (TOF) of a 40 kHz continuous wave over a 98.5 mm ultrasonic delay line. Combining measured sound velocity c_m, atmospheric pressure P, and either a conventional thermometer (for RH) or conventional RH sensor (for dry-bulb T), the system extracts: RH error ≤ 16.4%; dry-bulb temperature error ≤ 0.7 K. Application: HVAC duct monitoring and air-conditioning energy control.

## Unique contribution
Derives a closed-form equation [RHU = f(c_m, T_d, P)] from thermodynamic first principles linking relative humidity to measurable ultrasonic quantities. Shows that conventional ultrasonic temperature sensors measure "virtual temperature" (overestimate due to humidity), and provides the correction. First demonstration of 40 kHz CMUT-scale approach (Nippon Ceramic PT40/PR40 transducers) for simultaneous humidity and temperature sensing in a controlled chamber.

## Key concepts
- Sound velocity in moist air: c_m = √((P_d + P_v)/(ρ_d + ρ_v))
- Virtual temperature T_v vs. dry-bulb temperature T_d
- Relative humidity from sound velocity: RHU = (ρ₀c²_m T₀/P₀T_d − 1) / (1 − M_v/M_d × (ρ₀c²_m T₀/P₀T_d − 1)) × P/P_s(T_d)
- 40 kHz airborne ultrasound delay line, L = 98.5 mm
- Humidity mixing ratio from c_m and T_d
- Psychrometric chart / specific enthalpy application
- Air-conditioning duct monitoring

## Methods / results / takeaways
- Transducers: Nippon Ceramic PT40-18N (TX) and PR40-18N (RX) at 40 kHz; dew-proof; L = 98.5 mm; fixed rail.
- Chamber: ESPEC PR-3KF; T = 283–323 K; RH = 30–100%; foam absorbers on walls.
- Measurement: Sony Tektronix function generator for CW; Tektronix 2230 oscilloscope for TOF; pressure sensor VITEC TSD01V.
- RH measurement (eq. 7): measure c_m via TOF; measure T_d via hot-wire thermometer; measure P; compute RHU — error ≤ 16.4% across all conditions.
- Dry-bulb temperature (eq. 12): measure c_m + virtual T_v + RH from sensor → iterative solve for T_d (convergence criterion ΔT < 0.05 K) — error ≤ 0.7 K.
- Humidity mixing ratio x (eq. 14): derived from c_m and T_d — maximum error 10.0%.
- Condensation test: supersaturated conditions caused ≤ 0.48 m/s velocity change — transducers robust to condensation.
- Application: AHU duct sensor for simultaneous heat energy monitoring.
- Limitation: requires known atmospheric pressure; 16.4% RH error may be too large for precision climate control.
