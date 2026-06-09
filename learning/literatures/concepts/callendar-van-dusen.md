# Callendar–Van Dusen Equation

**Aliases:** Callendar-Van Dusen equation; CVD equation; Pt100 R-T equation; platinum RTD calibration equation

**Definition:** The Callendar–Van Dusen (CVD) equation is the polynomial formula relating the resistance R(t) of a platinum RTD to temperature t (°C): R(t) = R₀[1 + At + Bt² + C(t−100)t³] for −200 °C ≤ t < 0 °C, and R(t) = R₀[1 + At + Bt²] for 0 °C ≤ t ≤ 850 °C, where A = 3.9083 × 10⁻³, B = −5.775 × 10⁻⁷, C = −4.183 × 10⁻¹² (per IEC 60751). The cubic term is significant only below 0 °C. The equation enables conversion between measured resistance and temperature and is the basis for linearisation in RTD signal-conditioning circuits.

**Key relations:**
- [rtd](rtd.md) — governs all platinum RTD types
- [pt100-pt1000](pt100-pt1000.md) — applies to both, with different R₀ values
- [en-60751-rtd-accuracy](en-60751-rtd-accuracy.md) — tolerance classes use this equation as reference

**Discussed in:**
- [WIKA DS IN0017 Platinum RTD Tolerances](../notes/temperature-measurement-probes/wika-ds-in0017-platinum-rtd-tolerances.md) — CVD constants tabulated; formula used to compute tolerance bands
