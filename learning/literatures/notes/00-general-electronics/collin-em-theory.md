# Foundations for Microwave Engineering — Electromagnetic Theory (Chapter 2)

- **Source:** Electromagnetic Theory.pdf
- **Drive link:** https://drive.google.com/file/d/1m3-Du9DFQFDptR8_TVlt3cy1GBvSd1Bc/view?usp=drivesdk
- **Type:** book (chapter)
- **Author/Year:** Robert E. Collin, 2001
- **Coverage:** partial (large file, truncated extraction)

## Overview
Chapter 2 of Collin's textbook, providing the electromagnetic theory foundation for the rest of the book. Covers Maxwell's equations in both time-domain and phasor (time-harmonic) forms, boundary conditions, wave equation derivation, plane waves in lossy and lossless media, Poynting's theorem, and potential functions (vector and scalar).

## Unique contribution
Provides the formal electromagnetic theory backbone that allows the rest of the book to derive waveguide and transmission-line properties rigorously from Maxwell's equations, rather than relying on circuit intuition alone.

## Key concepts
- Maxwell's equations (time-domain and phasor forms)
- Boundary conditions at material interfaces
- Wave equation: ∇²E – με ∂²E/∂t² = 0 (in source-free lossless region)
- Phasor Helmholtz equation: ∇²E + k²E = 0, k = ω√(με)
- Plane wave propagation in free space and lossy media
- Skin effect, skin depth: δ = √(2/ωμσ)
- Poynting vector and power flow: S = E × H
- Complex Poynting theorem, stored vs. dissipated energy
- Vector potential A and scalar potential φ
- Reciprocity theorem

## Methods / results / takeaways
- In a lossy medium (σ ≠ 0), the complex permittivity is ε_c = ε – jσ/ω; the wave number k becomes complex, giving attenuation α and phase β.
- Skin depth at 10 GHz in copper (~6×10⁷ S/m): δ = √(2/(2π×10¹⁰ × 4π×10⁻⁷ × 6×10⁷)) ≈ 0.66 µm — fields are essentially confined to a thin surface layer.
- Poynting theorem: ∮S·dA = –d/dt(WE + WM) – Pd, relating surface power flow to rate of change of stored energy and dissipated power.
- The reciprocity theorem (Lorentz reciprocity) is used later to derive coupling coefficients between waveguide modes and antenna patterns.
