# Characterization of Transducers and Resonators under High Drive Levels

- **Source:** Sherrit 2001 high drive characterization
- **Drive link:** https://drive.google.com/file/d/1PQfSUCtVvckw2EoRNYP2zA40xFTK9yxS/view
- **Type:** paper (conference, IEEE Ultrasonics Symposium)
- **Author/Year:** S. Sherrit, X. Bao, D.A. Sigel, M.J. Gradziel, S.A. Askins, B.P. Dolgin, Y. Bar-Cohen / 2001
- **Coverage:** full

## Overview
Describes an experimental system for characterising piezoelectric transducers and resonators under high AC drive levels. The system measures electric field E, displacement D, strain S, impedance Z, and temperature T simultaneously. Applies Fourier analysis to detect nonlinear harmonics in the displacement response. Identifies thermal hysteresis and frequency jumping in resonator admittance curves as arising (at least partially) from temperature-dependent resonant frequency shifts — not only from elastic nonlinearities as previously assumed.

## Unique contribution
Provides thermal model showing that the spatial distribution of power dissipation in a resonator is cos²(πx/L) at resonance (concentrated near centre) versus uniform off-resonance. Derives a transcendental equation linking resonator surface temperature T₁(ω) and the admittance Y(f_s), explaining asymmetric admittance curves and frequency jump hysteresis. Recommends that impedance frequency sweeps be done in fractions of seconds (or duty-cycled single-frequency steps) to maintain isothermal measurement conditions.

## Key concepts
- High-power piezoelectric characterisation system
- Simultaneous E, D, S, Z, T measurement under large AC drive
- Fourier harmonic analysis for non-linearity detection
- Thermal hysteresis in admittance vs frequency (cos² power dissipation at resonance)
- Power dissipation: P_D = P_M × cos²(πx/L) at resonance; uniform off-resonance
- Time constant τ = ρL²C_p/k ≈ 1 s for 1 mm PZT sample
- Thermal equilibrium temperature vs frequency (transcendental equation)
- Soft PZT (Motorola 3203HD) vs hard PZT (Channel 5800) comparison

## Methods / results / takeaways
- Setup: waveform generator → power amplifier → sample + series resistor (1–1000 Ω); current inferred from V_R/R; D from time integral of current/area; T from thermocouple
- D-E nonlinearity: soft PZT 3203HD has higher harmonic content (2nd harmonic: 7.8% vs 2.6% for hard PZT C5800)
- Ultrasonic horn (stepped): admittance and tip displacement vs frequency shown for 3 drive levels; agrees with prior horn model
- Temperature frequency hysteresis: for Channel 5800 ring resonator at high drive (180 V_p), frequency jumps seen when sweeping up vs down; attributed to temperature-dependent frequency shift creating positive feedback near resonance
- Thermal model: time constant ≈ 1 s for 1 mm sample → measurement must be done in <<1 s or duty-cycled for isothermal conditions
- Key conclusion: apparent dispersion and nonlinearity at high drive may be thermal artefacts; proper characterisation requires isothermal measurement protocol
