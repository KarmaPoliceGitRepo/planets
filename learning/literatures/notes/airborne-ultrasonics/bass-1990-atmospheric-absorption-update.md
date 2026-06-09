# Atmospheric Absorption of Sound: Update

- **Source:** Bass 1990 atmospheric absorption update
- **Drive link:** https://drive.google.com/file/d/1szzssofeycbKqugPk9CJBRODXY7MddZI/view
- **Type:** paper
- **Author/Year:** Bass, Sutherland & Zuckerwar, 1990 (Journal of the Acoustical Society of America, 88(4), 2019–2021)
- **Coverage:** full

## Overview
Short letter updating the Evans et al. 1972 atmospheric absorption curves with improved relaxation time formulas for O₂ and N₂ from Zuckerwar & Meredith 1985 experiments. Provides a compact total-absorption formula (eq. 1) in nepers/m, with updated f_r,O and f_r,N expressions (eqs. 2–3) and water vapour mole fraction formula (eqs. 4–5). Updated figures replace Fig. 8 of Evans 1972. This formula became ANSI S1.26 and the basis for ISO 9613-1. Corrected and extended by Bass 1995.

## Unique contribution
Supersedes the widely reproduced but incorrect Evans 1972 "Fig. 8" with updated absorption curves based on more accurate relaxation frequencies. Provides the definitive compact formula for total atmospheric absorption applicable from audio to low-ultrasonic range that formed the basis of international standards (ANSI S1.26-1978 update, ISO 9613-1). The single equation covers all humidity levels and temperatures; it is the standard reference for absorption correction in airborne ultrasonic systems.

## Key concepts
- Total absorption formula: α = f²{1.84×10⁻¹¹(P_s/P_s0)⁻¹(T/T_0)^(1/2) + (T/T_0)^(−5/2) × [0.01278 exp(−2239.1/T)/(f_r,O + f²/f_r,O) + 0.1068 exp(−3352/T)/(f_r,N + f²/f_r,N)]}
- Updated O₂ relaxation frequency: f_r,O = (P_s/P_s0)[24 + 4.04×10⁴h(0.02+h)/(0.391+h)]
- Updated N₂ relaxation frequency: f_r,N = (P_s/P_s0)(T/T_0)^(−1/2)[9 + 280h·exp(−4.17((T/T_0)^(−1/3) − 1))]
- Water vapour mole fraction h from relative humidity h_r and saturation vapour pressure P_sat
- P_sat formula (eq. 5): log₁₀(P_sat/P_s0) = −10.79584(1−T_01/T) − 5.02808 log₁₀(T/T_01) + ... (corrected in Bass 1995)
- Reference: T_0 = 293.15 K, T_01 = 273.16 K, P_s0 = 1 atm

## Methods / results / takeaways
- Improvement: new f_r,O based on Zuckerwar & Meredith 1985 low-frequency measurements (below 200 Hz) — previously underestimated at low h.
- New f_r,N: improved temperature dependence from updated laboratory data.
- Updated curves (Figs. 1, 2): absorption in dB/1000 ft vs f/P for 0–100% RH at 20°C; also dB/100 m vs f/P.
- Agreement with Evans 1972: similar at moderate humidity; differences mainly at low humidity and low frequency.
- Error note: eq. 5 for P_sat contains a sign error — corrected in Bass 1995 (the error produces < 0.3% change in α at most conditions).
- Limitation: valid at 20°C; temperature variation not explicitly verified; P_sat error corrected in Bass 1995.
