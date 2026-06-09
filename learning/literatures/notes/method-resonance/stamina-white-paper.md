# STAMINA: STAnding wave Measurements of INterfaces and lAyers

- **Source:** STAMINA white paper v6 2015-08-19.docx
- **Drive link:** https://drive.google.com/file/d/1EBM8hAsy8I1E-h8yDMdCJ09v9u67W39u/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Unknown (institutional, likely University of Sheffield / Robin Dwyer-Joyce group) / 2015
- **Coverage:** full

## Overview
A technical white paper introducing STAMINA, a continuous-wave ultrasonic measurement method that exploits standing wave formation in a component to measure interface/surface properties from its back face. Rather than pulsing, a piezoelectric transducer drives the component at swept frequencies; the superposition of multiple reflections creates a standing wave whose amplitude (RMS) and resonant frequency shift are sensitive to surface layers, deflection, and viscosity. Four case studies demonstrate applications: paint film thickness, oil viscosity, roller bearing skew detection, and bolt tension measurement.

## Unique contribution
Provides the complete mathematical framework for superimposed continuous-wave standing waves (summing n-passage wave trains, Eq. 13–16), derives the standing wave reflection coefficient S relating amplitude to interface reflection coefficient R, and shows how frequency shift Δfs maps to surface-layer thickness and component elongation. Demonstrates that sensitivity is amplified by the number of reflections n — enabling micron/nanometre-level resolution impossible with single-pulse techniques. Introduces an integrated low-cost driving circuit as an alternative to lab instruments.

## Key concepts
- STAMINA method (continuous-wave standing wave measurement)
- Standing wave, nodes and antinodes
- Superimposed continuous wave / standing wave reflection coefficient S
- Resonant frequency fs; characteristic frequency Δf
- Acoustic impedance mismatch; reflection coefficient R
- Attenuation coefficient α
- Spring model / contact stiffness K
- Thin film reflection; bulk modulus B
- Shear wave viscosity measurement
- Phase shift at interface
- Piezoelectric transducer (longitudinal and shear polarised)
- Frequency sweep; RMS envelope
- Acoustoelastic effect (noted, not fully treated)
- Bolt tension measurement; roller skew detection; paint film thickness; oil viscosity

## Methods / results / takeaways
- Principle: drive transducer with swept frequency; at resonant frequency fs = c/(2L) all reflections constructively interfere and standing wave amplitude peaks; amplitude and frequency of peaks encode interface state.
- Standing wave reflection coefficient S (Eq. 16) = ratio of measurement-state to reference (solid-air) RMS amplitude; used to extract R, then K, film thickness, or viscosity.
- Frequency shift method: a surface layer of thickness l shifts fs by Δfs given by Eq. 27; solving the quadratic yields l directly.
- Extension/bolt tension: nth standing-wave peak shifts by −n·dΔf; at 10 MHz centre frequency on a 100 mm M14 bolt, amplification factor n ≈ 339, giving ~34 kHz apparent peak shift per 100 Hz change in Δf — enabling micron elongation resolution.
- Case Study 1 (paint): 10 µm acrylic layers on 0.96 mm Al; STAMINA vs profilometer agreement within ~10% across 4 layers (10–40 µm).
- Case Study 2 (viscosity): shear-wave standing wave reflection coefficient tracks Newtonian oil viscosity from ~29 to ~5800 mPa·s; model (Eqs. 10 + 22) fits data; measurement accuracy varies (~20–40% error at extremes).
- Case Study 3 (roller skew): time difference between dips in two spatially separated sensor signals reveals skew angle; continuous wave essential for temporal resolution needed.
- Case Study 4 (bolt tension): direct Δf measurement via autocorrelation of multi-peak spectrum; load cell vs ultrasonic load shows good agreement for M14 grade 8.8 bolt.
- Instrumentation: arbitrary function generator + digital oscilloscope, or a custom integrated IC-based driving system; transducer frequencies typically 1–50 MHz.
- Three key advantages over pulse-echo: higher sensitivity (multi-reflection amplification), faster response (each wave peak = one measurement), lower cost hardware.
