# STAMINA — STAnding wave Measurements of INterfaces and lAyers (White Paper)

- **Source:** STAMINA white paper v7 2015-12-07 (1).pdf
- **Drive link:** https://drive.google.com/file/d/1AY1NQxKhFBywMfVOTROV4Rh_Dg2d6H2G/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** R. S. Dwyer-Joyce, December 2015 (University of Sheffield, v7)
- **Coverage:** full

## Overview
This white paper is the primary technical reference document for the STAMINA (STAnding wave Measurements of INterfaces and lAyers) method. It describes the physics of ultrasonic standing wave formation in a solid component, the signal processing framework, and several application examples: film thickness measurement, viscosity measurement of a thin liquid layer, detection of a contacting element, wear/material removal tracking, and precision deflection or thermal expansion measurement. The key hardware consists of a transducer pair bonded to the back face of the component, a signal generator performing a frequency sweep, and a digitiser connected to a PC.

## Unique contribution
Provides the complete mathematical treatment of the STAMINA superimposed standing wave — summing infinite reflections with attenuation and phase shifts — and derives working equations for both frequency-based (Δf_s → deflection/layer thickness) and amplitude-based (standing wave reflection coefficient S → viscosity/film properties) measurement modes. The derivation is self-contained and serves as the theoretical backbone for all subsequent STAMINA experimental work in the research group.

## Key concepts
- Standing wave / resonance in a solid bar
- Superimposed continuous wave reflection coefficient S
- Resonant frequency f_s; frequency sweep method
- Amplitude-based and frequency-based STAMINA measurement modes
- Ultrasonic attenuation coefficient α
- Reflection coefficient R and phase shift ϕ at boundaries
- Acoustic impedance z of solid and liquid (shear waves)
- Thin film stiffness K (Schoenberg model); bulk modulus B
- Shear wave viscosity measurement: z_L = sqrt(ρ·η·ω)
- Piezoelectric transducer bandwidth and response function
- Continuous wave (CW) vs. pulsed ultrasound
- Matching layer design
- EMAT (non-contact driving option)
- Polar (spiral) plot for reflection amplitude/phase visualization

## Methods / results / takeaways
- **Standing wave formation:** A continuous-wave transducer drives a frequency sweep. At the resonant frequency f_s = c/(2L), reflected waves constructively interfere, maximising amplitude. Successive reflections accumulate effect on S, providing high sensitivity to interface changes.
- **Amplitude method:** Measure RMS amplitude at resonance with and without surface layer; ratio S = A_r/A_i encodes R via the infinite-sum formula. Once R is known, viscosity (shear wave) or film thickness (bulk modulus) follows from standard acoustic impedance equations.
- **Frequency method:** Track the shift Δf_s as component length or surface layer thickness changes. Solving the quadratic in Δf_s gives deflection ΔL to high precision (equations 21–22).
- **Three advantages over pulse-echo:** (1) Very high sensitivity — effect magnified at each reflection; (2) Very fast time resolution — each wave cycle is a data point; (3) Low cost — no pulsed ultrasonic hardware required, standard function generator and oscilloscope suffice.
- **Apparatus:** Transmitter and receiver PZT (1–50 MHz) bonded to back face; arbitrary function generator (e.g., TG5011); digital oscilloscope (e.g., GDS-2204A); or integrated IC-based driving board.
- **Practical sweep:** Frequency swept over 1–100 ms; RMS of received signal plotted vs. frequency; peaks identified at multiples of f_s. Frequency window narrows around the peak to track Δf_s with time.
