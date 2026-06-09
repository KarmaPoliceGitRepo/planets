# Multiple Reflection Method for Measuring Surface Films: Model and Experiment

- **Source:** Introduction to ultrasound and the multiple reflection method..docx
- **Drive link:** https://drive.google.com/file/d/1iSQQoL104ZoVNNryvIvWDOF7FR6d2uUt/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Unknown (student/research report, marked CONFIDENTIAL) / ~2016
- **Coverage:** full

## Overview
A research report (likely a student project or internal document) that develops and experimentally validates a mathematical model for measuring thin oil film thickness between glass plates using the multiple reflection (continuous-wave standing wave) method. It surveys the underlying theory of ultrasonic attenuation, reflection at interfaces, spring-model contact stiffness, phase shift, standing wave formation, and derives the standing wave reflection coefficient S. MATLAB modelling is compared with bench experiments using an oscilloscope and signal generator at 8–10 MHz.

## Unique contribution
Provides an accessible derivation of the full n-passage standing wave amplitude equation (Eqs. 11–16) from first principles, explicitly tracking attenuation and phase shift at both the measurement interface and the transducer face. Evaluates the sensitivity of S to driving frequency between 8 and 10 MHz, highlighting the importance of selecting the correct resonant frequency for reliable measurement. Identifies key limitations: the spring model breaks down for films that are large compared to the acoustic wavelength; the multiple reflection method extends the measurable range (thinner and thicker films, >0.5–15 µm).

## Key concepts
- Multiple reflection method (continuous-wave standing wave technique)
- Standing wave reflection coefficient S
- Spring model; contact stiffness K
- Reflection coefficient R; acoustic impedance z
- Attenuation coefficient; Beer-Lambert amplitude decay
- Phase shift at interface (0 for thick film K→0, π/2 for thin film K→∞)
- Bulk modulus B; oil film thickness h
- Constructive/destructive interference; standing wave nodes and antinodes
- Piezoelectric transducer; longitudinal and shear waves
- Signal-to-noise limitation of conventional pulse-echo (R near 0 or 1)
- Resonant frequency selection; frequency sensitivity of S

## Methods / results / takeaways
- Experimental setup: piezoelectric transducer bonded to glass plate with static oil film; signal generator drives continuous sinusoidal wave; oscilloscope captures standing wave amplitude; reference taken at solid-air boundary (R ≈ 1).
- Standing wave reflection coefficient S = A_meas / A_ref; derived by summing n superimposed reflection passes and taking ratio (Eq. 16), analogous to the STAMINA framework.
- Phase shift at the transducer and measurement interfaces both shift the resonant condition; driving frequency must be selected to satisfy constructive interference criteria.
- The frequency sensitivity study (8–10 MHz range) shows S varies significantly with frequency away from resonance, confirming that off-resonance driving degrades measurement accuracy.
- Model vs experiment: good qualitative agreement; some residual discrepancy in reference amplitude prediction requires further model refinement.
- Spring model limitation: accurate only when film thickness h ≪ wavelength (roughly h < λ/10); at larger thicknesses the stiffness K → B/h approximation breaks down.
- Multiple reflection method advantage: each reflection multiplies the effect of R on amplitude, enabling discrimination of very thin films (<0.5 µm) and thicker films (>15 µm) outside the conventional spring-model range.
