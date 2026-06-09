# Some Notes on Acoustics — Bath University

- **Source:** `Michael Carley - Some notes on acoustics_bath notes.pdf` (Drive ID: 1blzPHR_4edDC-LkMCP3isWji33L07DdX)
- **Drive link:** https://drive.google.com/file/d/1blzPHR_4edDC-LkMCP3isWji33L07DdX/view
- **Type:** lecture notes (University of Bath)
- **Author/Year:** Michael Carley, University of Bath (undated, ~2010s)
- **Coverage:** partial (large file; first ~60 pages extracted)

## Overview
Undergraduate/graduate-level acoustics lecture notes from Bath University covering sound waves from first principles through to applied topics. Organized in chapters: (1) What is sound? — wave equation, single-frequency waves, quantifying sound, plane waves, 3D solutions, acoustic velocity and intensity; (2) Making sound — pulsating sphere, point sources, loudspeakers, combustion noise; (3) Modifying sound — reflection by hard/soft walls, ducts and silencers, Helmholtz resonator; (4) Measuring sound — microphones, ears, microphone arrays; (5) Moving sources — Doppler effect, aeroacoustics; (6) Aircraft noise: propellers. Additional chapters presumed on aircraft noise, room acoustics, and further topics.

## Unique contribution
Companion notes to the Turbulence and Noise notes by the same author, providing the acoustics foundation before the aeroacoustics treatment. Practical examples (bugging an embassy, wine bottle resonance, aircraft engine noise) make the theory concrete. Includes the full derivation chain from the Navier-Stokes equations through linearization to the wave equation.

## Key concepts
- **Wave equation derivation:** linearization of Euler equations (momentum + continuity) → ∂²p/∂t² = c²∇²p; c = √(γp₀/ρ₀) for ideal gas
- **Acoustic quantities:** particle displacement, pressure, particle velocity, specific acoustic impedance Z = ρc; acoustic intensity I = p·v
- **Plane waves:** p = A·e^{i(kx−ωt)}; phase velocity c = ω/k; relationship p = Z·v for positive-traveling wave
- **Spherical waves:** p = (A/r)·e^{i(kr−ωt)}; near field (1/r² ≪ 1/r) and far field behavior; radiation impedance
- **Point source (monopole):** Green's function G(x,y,ω) = e^{ikr}/(4πr); source strength Q (volume velocity); power W = ρω²Q²/(8πc)
- **Loudspeakers / circular piston:** baffle radiation; near field (Fresnel zone D = a²/λ); far field diffraction pattern with zeros at sin θ = 1.22λ/d
- **Combustion noise:** heat release rate Q_H as acoustic source; entropy fluctuations → entropy noise; entropy-generated pressure ∝ ∂Q_H/∂t
- **Wall reflection:** hard wall (rigid): pressure doubles, velocity node; soft wall (pressure release): pressure node, velocity doubles; impedance boundary conditions
- **Duct modes and silencers:** plane wave propagation below cutoff f_c = c/2h; expansion chamber muffler; reactive vs. resistive attenuation
- **Helmholtz resonator:** f = (c/2π)√(S/VL) where S = neck area, V = cavity volume, L = effective neck length; used for narrow-band noise control
- **Microphone arrays:** beamforming; delay-and-sum; spatial aliasing for d > λ/2; directivity patterns
- **Moving sources:** Doppler shift f' = f(c±v_obs)/(c∓v_src); Mach cone for supersonic sources; sonic boom

## Methods / Results / Takeaways
- Systematic use of complex exponential notation; phasor representation
- Energy balance: acoustic power = (1/2)Re[p v*] for harmonic waves
- Radiation efficiency: ka << 1 (compact source) → poor radiator (monopole strength ∝ (ka)⁴ for dipole, ∝ (ka)⁶ for quadrupole in far field power)
- Practical design of silencers: reactive (geometric — expansion chamber, quarter-wave tube) vs. absorptive (lined duct)
- Worked examples build physical intuition throughout

## See also
- `carley-turbulence-noise.md` — companion aeroacoustics notes by same author
- `fundamentals-acoustics-wikibooks.md` — parallel basic acoustics treatment
- `rayleigh-theory-of-sound.md` — classical reference for spherical waves, resonators
