# Separation of Variables in PDE (Wave Equation)

- **Source:** SeparationOfVariables.pdf
- **Drive link:** https://drive.google.com/file/d/1zrQZBTpUSRZNcL0fnJsk9fz2gR-L9KNT/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, 2012-05-02
- **Coverage:** full

## Overview
A short mathematical note demonstrating how to apply separation of variables to the 3D wave equation in Cartesian coordinates. Applies a Fourier transform in time to convert the wave equation to the Helmholtz equation, then separates variables to obtain four independent ODEs for X(x), Y(y), Z(z), and T(t), each with sinusoidal (plane-wave) solutions.

## Unique contribution
Provides a clean, self-contained derivation showing how the plane-wave solution Φ = ρ exp[j(k·r – ωt)] emerges from the separation-of-variables technique, including the identification of separation constants as wave-vector components.

## Key concepts
- Wave equation in 3D: ∇²Φ = (1/c²) ∂²Φ/∂t²
- Helmholtz equation: ∇²Φ + k²Φ = 0 (after Fourier transform in time)
- Separation of variables in Cartesian coordinates
- Separation constants p, q, r, s and their relation to wave-vector components
- Principle of superposition for forward and backward propagation
- Plane wave solution: Φ = ρ exp[j(kx·x + ky·y + kz·z – ωt)]

## Methods / results / takeaways
- The Fourier transform in time converts ∂²/∂t² to (jω)², yielding the Helmholtz equation with k = ω/c.
- Separating X(x)Y(y)Z(z)T(t) yields four decoupled ODEs with constant-coefficient solutions A exp(±jpx), etc.
- The forward-propagating plane-wave solution is Φ = ρ exp[j(k·r – ωt)] where |k| = 2π/λ and cs = ω.
- The derivation applies to any scalar wave (acoustic, EM component), with boundary conditions determining the specific constants A, B, ... H.
