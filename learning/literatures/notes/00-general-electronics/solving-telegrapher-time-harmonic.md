# Solving the Telegrapher's Equation for Time-Harmonic Signals

- **Source:** SolvingTelegrapher_TimeHamonic.pdf
- **Drive link:** https://drive.google.com/file/d/1bJ7sybz_Bd-pgzl4Vfxi-ruy2VCy51ki/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, September 12, 2013
- **Coverage:** full

## Overview
Derives the voltage and current solutions to the telegrapher's equations for time-harmonic (phasor) excitation. Starting from the KVL/KCL telegrapher's equations for a general lossy line, converts to phasor form, then solves the resulting second-order ODEs to obtain the forward- and backward-traveling wave amplitudes V0+ and V0–.

## Unique contribution
Shows the complete solution pipeline: time-domain telegrapher's equations → phasor substitution → wave equations in γ → ODE solution → identification of Z0 from Ohm's law → time-domain reconstruction via inverse phasor. Also explicitly states the lossless special case (R = G = 0).

## Key concepts
- Telegrapher's equations (phasor form): dV/dz = –(R+jωL)I, dI/dz = –(G+jωC)V
- Wave equations: d²V/dz² – γ²V = 0, with γ = √((G+jωC)(R+jωL))
- General solution: V = V0+e^(–γz) + V0–e^(γz), I = (V0+e^(–γz) – V0–e^(γz))/Z0
- Characteristic impedance: Z0 = √((R+jωL)/(G+jωC))
- Phase velocity: vphase = ω/β
- Lossless limit: R = G = 0 → α = 0, β = ω√(LC), Z0 = √(L/C), vp = 1/√(LC)

## Methods / results / takeaways
- Phasor substitution (∂/∂t → jω) converts the time-domain equations to coupled first-order ODEs in z.
- Differentiating and substituting yields d²V/dz² = γ²V, solved by V = Ae^(λz) → λ = ±γ.
- The two unknowns V0+ and V0– are determined by boundary conditions at load and source.
- Using the first telegrapher equation to find I gives Z0 = γ/(R + jωL) = √((R+jωL)/(G+jωC)).
- Time-domain reconstruction: V(z,t) = |V0+|e^(–αz)cos(ωt – βz + ∠V0+) + |V0–|e^(αz)cos(ωt + βz + ∠V0–).
- The forward wave has phase velocity vp = ω/β and wavelength λ = 2π/β.
