# Variation of the Speed of Sound in Air with Humidity and Temperature

- **Source:** Wong 1985 speed sound humidity temperature
- **Drive link:** https://drive.google.com/file/d/1JUJaddXfpE3vmuw8LqJ3N6HXFxplV0V9/view
- **Type:** paper
- **Author/Year:** Wong & Embleton, 1985 (Journal of the Acoustical Society of America, 77(5), 1710–1712)
- **Coverage:** full

## Overview
Short paper extending the prediction of sound speed in moist air to temperatures from 0°–30°C, based on theoretical and experimental measurements of the specific heat ratio γ in humid air. Provides a compact polynomial equation (eq. 5) for c_h/c_0 as a function of relative humidity h and temperature t (°C). Maximum uncertainty ~400 ppm over the full range. Comparison with Harris 1971 data and Morfey & Howell 1980 predictions shows agreement within ~50 ppm for h ≥ 0.1 after correcting Morfey's γ_a value.

## Unique contribution
Extends the Harris/Morfey database to a 0–30°C temperature range through a compact, programmable polynomial. The γ/M approach separates the equilibrium (thermodynamic) sound speed contribution from the relaxation-dispersion contribution, clarifying that relaxation effects are negligible above ~30% RH for audio frequencies. The polynomial eq. 5 is one of the simplest accurate formulae for c_h/c_0 and is frequently cited in ultrasonic thermometry work.

## Key concepts
- Sound speed ratio: c_h/c_0 = √[(γ_h/M_h)/(γ_0/M_0)]
- Polynomial eq. 5: c_h/c_0 = 1 + h(9.66×10⁻⁴ + 7.2×10⁻⁵t + 1.8×10⁻⁶t² + 7.2×10⁻⁸t³ + 6.5×10⁻¹⁰t⁴)
- Specific heat ratio γ and molar mass M in humid air: functions of h and t
- Valid range: t = 0–30°C, h = 0–1.0, p = 101.325 kPa
- Uncertainty: ~400 ppm (driven by γ uncertainty)
- Comparison with Morfey & Howell 1980: agrees to 50 ppm for h ≥ 0.1 after γ₀ correction

## Methods / results / takeaways
- Approach: compute γ_h/M_h from theoretical + experimental thermodynamic data on air and H₂O mixture (Wong & Embleton 1984 J. Acoust. Soc. Am. 76, 555).
- Intermediate formula (eq. 3): γ_h/M_h = 0.04833 + (h − 0.023)×A_t; A_t = 9.2×10⁻⁵ + 5.5×10⁻⁶t + 4.25×10⁻⁷t².
- Polynomial eq. 5 fit error: < 2 digits in fifth decimal place over full valid range.
- Fig. 1: curves of c_h/c_0 vs h at t = 0, 5, 10, 15, 20, 25, 30°C — all monotonically increasing (pure equilibrium effect; relaxation dip not captured because the equilibrium c_0 is frequency-independent).
- Fig. 2 vs Harris 1971 data at 20°C: discrepancy at h < 0.2 remains unexplained (same as in Morfey 1980).
- Practical use: eq. 5 directly gives humidity correction factor for ultrasonic range-finding or TOF thermometry up to ~500 kHz where relaxation dispersion is negligible.
- Limitation: equilibrium speed only; does not include frequency-dependent dispersion from vibrational relaxation (relevant below ~100 kHz); pressure assumed 101.325 kPa.
