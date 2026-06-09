# Theory of Structural Dynamics (CIV4180/6180)

- **Source:** Theory of Structural Dynamics.pdf
- **Drive link:** https://drive.google.com/file/d/1Pn2HEaSPKhnNMjdxtv1H3002_RQKGQkw/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Unknown (university course notes for CIV4180/6180 Vibration Engineering / Structural Dynamics; circa 2017 based on upload)
- **Coverage:** partial (large file, ~170 kchar extracted; covers full table of contents and core SDOF and MDOF theory through modal analysis)

## Overview
Comprehensive lecture notes for a structural dynamics / vibration engineering course (CIV4180/6180) covering single-degree-of-freedom (SDOF) and multi-degree-of-freedom (MDOF) systems. The content progresses from basic vibration concepts and mathematical modelling to damping, forced response, resonance, modal analysis, continuous systems, and finite element applications in dynamics. Practical engineering focus throughout with coverage of measurement and signal processing.

## Unique contribution
Serves as a standalone theory reference for a graduate structural dynamics course, consolidating content typically spread across multiple textbooks. Includes continuous system models (strings, rods, beams — exact eigenfunctions) alongside discrete SDOF/MDOF, enabling direct comparison of continuous vs. discrete approaches. Covers random vibration concepts and earthquake response spectra — less common in basic dynamics texts.

## Key concepts
- SDOF system (spring-mass-dashpot)
- Natural frequency (ωn = √(k/m))
- Damping ratio (ζ) and critical damping
- Free undamped and damped vibration
- Forced harmonic response and resonance
- Dynamic amplification factor
- Frequency response function (FRF)
- Impulse response function
- Duhamel's integral
- Springs in series and parallel
- MDOF systems and equations of motion
- Modal analysis (eigenvalue problem, mode shapes)
- Modal superposition
- Orthogonality of mode shapes
- Mass and stiffness matrices
- Continuous systems (strings, beams in transverse vibration)
- Euler-Bernoulli beam dynamics
- Random vibration and spectral analysis
- Power spectral density (PSD)
- Earthquake response spectra

## Methods / results / takeaways
- Equation of motion for SDOF: mẍ + cẋ + kx = F(t); characteristic equation gives ωn = √(k/m), ζ = c/(2mωn), ωd = ωn√(1−ζ²).
- Resonance: dynamic amplification factor DAF = 1/(2ζ) at resonance for damped harmonic forcing (displacement amplitude).
- Frequency response function H(ω) = 1/(k − mω² + icω); |H| peaks near ω_n for lightly damped systems.
- MDOF: [M]{ẍ} + [C]{ẋ} + [K]{x} = {F(t)}; normal modes satisfy ([K] − ω²[M]){φ} = {0}; modal mass m_r = {φ_r}^T[M]{φ_r}.
- Continuous beam: EI ∂⁴w/∂x⁴ + ρA ∂²w/∂t² = q(x,t); mode shapes are sinusoidal/hyperbolic combinations satisfying boundary conditions.
- Practical note: for lightly damped systems (ζ < 0.1), undamped natural frequencies give good approximations to damped ones.
- Random vibration: mean-square response σ_x² = ∫₋∞^∞ |H(ω)|² S_F(ω) dω where S_F is the input PSD.
