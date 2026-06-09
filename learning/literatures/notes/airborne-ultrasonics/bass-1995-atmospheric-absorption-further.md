# Atmospheric Absorption of Sound: Further Developments

- **Source:** Bass 1995 atmospheric absorption further
- **Drive link:** https://drive.google.com/file/d/1AzXdmAcfMheQkJZoWT8b1lkKMRYdXUEC/view
- **Type:** paper
- **Author/Year:** Bass, Sutherland, Zuckerwar, Blackstock & Hester, 1995 (Journal of the Acoustical Society of America, 97(1), 680–683)
- **Coverage:** full

## Overview
Corrects a sign error in the saturation vapour pressure equation (eq. 5) of Bass et al. 1990, provides an alternative simpler P_sat formula from the new ISO 9613-1:1993 standard, and re-presents the absorption formula with all quantities scaled by atmospheric pressure p_s — making the curves universally applicable at any altitude/pressure. New, more readable absorption figures are presented (α/p_s vs f/p_s, with h_r/p_s as parameter). The 1995 paper + 1995 erratum (JASA 99, 1259) together provide the definitive absorption formulas corresponding to ISO 9613-1.

## Unique contribution
Finalises the atmospheric absorption standard by: (1) correcting the P_sat error from Bass 1990, (2) introducing the ISO 9613-1 P_sat formula (log₁₀(P_sat/P_s0) = −6.8346(T_01/T)^1.261 + 4.6151), (3) showing that all absorption curves collapse onto pressure-scaled master curves (α/p_s vs f/p_s), enabling easy lookup at non-standard altitudes. This is the paper that confirmed alignment between the ANSI S1.26 and ISO 9613-1 formulations.

## Key concepts
- Corrected P_sat formula: log₁₀(P_sat/P_s0) = 10.79586[1−(T_01/T)] − 5.02808 log₁₀(T/T_01) + 1.50474×10⁻⁴{1−10^(−8.29692[(T/T_01)−1])} − 4.2873×10⁻⁴{1−10^(−4.76955[(T/T_01)−1])} − 2.2195983
- Alternative ISO 9613-1 P_sat: log₁₀(P_sat/P_s0) = −6.8346(T_01/T)^1.261 + 4.6151
- Pressure-scaled formulation: α/p_s (nepers/m·atm) vs F = f/p_s (Hz/atm); parameter h_r/p_s (%/atm)
- Same α formula as Bass 1990 eq. (1), with corrected P_sat
- Altitude applicability: h_r/p_s can exceed 100%/atm at altitude — figures extend to 100%/atm coverage for conditions up to ~3 km altitude

## Methods / results / takeaways
- P_sat error correction: sign error in the exponential term of Bass 1990 eq. (5) causes < 0.3% error in α at most conditions (≤ ±0.3% at −40°C, negligible at 20°C).
- ISO vs ANSI P_sat comparison: both formulas agree to < ±0.02% at 20°C; max divergence ±0.3% at −40°C over 10–90% RH/atm.
- New figures (Figs. 1 and 2): absorption in dB/(100 m·atm) and dB/(1000 ft·atm) vs F (Hz/atm); parameter h_r/p_s from 0 to 100%/atm; more readable than Evans 1972 and Bass 1990 figures.
- Example usage: 1000 Hz at 20°C, 10% RH, 0.5 atm → f/p_s = 2000 Hz/atm, h_r/p_s = 20%/atm → α/p_s ≈ 2.2 dB/(100 m·atm) → α ≈ 1.1 dB/100 m.
- Status: together with erratum (JASA 99, 1259, 1996) this is the current standard reference for atmospheric absorption; directly equivalent to ISO 9613-1:1993.
- Limitation: valid for temperatures and pressures consistent with the standard atmosphere model; does not extend to ultrasonic frequencies above ~10 kHz (where Bond 1992 applies).
