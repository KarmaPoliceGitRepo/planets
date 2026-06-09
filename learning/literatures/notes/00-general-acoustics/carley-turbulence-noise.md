# Turbulence and Noise — Lecture Notes

- **Source:** `Michael Carley - Turbulance and noise.pdf` (Drive ID: 1hToDguqUtXvInP_kGbUZbxOvztFgfmUy)
- **Drive link:** https://drive.google.com/file/d/1hToDguqUtXvInP_kGbUZbxOvztFgfmUy/view
- **Type:** lecture notes (73 pages, Bath University)
- **Author/Year:** Michael Carley, University of Bath (undated, ~2010s)
- **Coverage:** partial (large file; content from pages 1-73 extracted but may be incomplete)

## Overview
Graduate-level lecture notes on turbulence physics and aeroacoustics, covering the fluid dynamics foundations through to the generation of aerodynamic noise. Organized in six content chapters: (1) fluid dynamics basics and statistical treatment of turbulence; (2) simplifications — turbulence vs. acoustics limits; (3) characterizing turbulence (kinetic energy, length/time scales, correlations); (4) instability and transition to turbulence (Kelvin-Helmholtz); (5) generation of sound (monopoles, dipoles, Lighthill's analogy, circular piston, asymmetric sources); (6) propagation of sound (reflections, ducts, silencers, Helmholtz resonator, circular ducts, radiation). The notes are accompanied by exam questions drawn from past papers.

## Unique contribution
Connects turbulence fluid mechanics with aeroacoustics in a unified framework. Emphasizes Lighthill's acoustic analogy (T_ij stress tensor) as the bridge between turbulent flow statistics and radiated noise. Key references: Lighthill 1952, Tyler & Sofrin 1962 (axial flow compressor noise), Lilley 1995 (jet noise), Hussain 1986 (coherent structures).

## Key concepts
- **Reynolds decomposition:** u = U + u'; mean and fluctuating velocity components; Reynolds averaging; correlation functions R(r,τ)
- **Turbulence kinetic energy:** k = ½ ⟨u'²⟩; energy cascade from large eddies to small scales; Kolmogorov scales
- **Integral length and time scales:** L_integral = ∫R(r)dr; T_integral = ∫R(τ)dτ; Taylor's hypothesis: L = U·T
- **Kelvin-Helmholtz instability:** shear flow between two uniform streams; perturbation analysis → unstable modes; vortex sheet roll-up; transition to turbulence
- **Lighthill's acoustic analogy:** ∂²p/∂t² − c²∇²p = ∂²T_ij/∂x_i∂x_j; T_ij = ρu_iu_j (Lighthill stress tensor); quadrupole source term
- **Point sources (monopole/dipole/quadrupole):** monopole p ∝ 1/r; dipole p ∝ cos θ/r; quadrupole p ∝ cos²θ/r; power ∝ M^n (n=4 monopole → 8 quadrupole)
- **Circular piston radiation:** near-field (Fresnel) vs. far-field (Fraunhofer); directivity pattern; ka product determines beam shape
- **Duct acoustics:** plane wave modes below cutoff frequency f_c = c/(2d); higher modes above cutoff; Helmholtz resonator as frequency-selective absorber
- **Pressure autocorrelation from Lighthill sources:** p(x,t)p(x,t+τ) = B∫∫[T_ij(y,t−R/c)T_ij(y',t−R'/c+τ)/(RR')]dV dV'
- **Tyler-Sofrin rule:** rotor-stator interaction in compressors; tone generation at harmonics m·BPF; spatial spinning modes m=n·B−r·V

## Methods / Results / Takeaways
- Statistical approach: treats turbulence as a random field characterized by probability density functions and correlation tensors
- Two-point velocity correlations → power spectral density via Fourier transform; Wiener-Khinchin theorem
- Lighthill's 8th-power law for jet noise: acoustic power ∝ U^8 (from dimensional analysis of quadrupole sources)
- Instability analysis uses linear perturbation theory → dispersion relation for Kelvin-Helmholtz modes; growth rate σ = k(U₁−U₂)/2
- Piston radiation efficiency (radiation impedance): real part ∝ (ka)² for ka << 1; approaches 1 for ka >> 1

## See also
- `carley-bath-acoustics-notes.md` — companion notes on acoustics (same author)
- `fundamentals-acoustics-wikibooks.md` — basic acoustics background
