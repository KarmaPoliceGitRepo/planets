# Real and Imaginary Parts of the Propagation Constant in EM Waves

- **Source:** PropagationConstant.pdf
- **Drive link:** https://drive.google.com/file/d/13Bp3AWvJlAV9XbBR6tAetZONQrwl6fIJ/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, 2012-09-26 (references Griffiths and Pozar)
- **Coverage:** full

## Overview
A detailed mathematical derivation of the propagation constant γ = α + jβ for both electromagnetic waves in a lossy medium and for transmission lines. Starts with a general formula for the square root of a complex number, then applies it to the Helmholtz equation from Maxwell's equations and to the telegrapher's equation from the transmission-line circuit model.

## Unique contribution
Provides a single unified formula γ = √(a + jb) = √((r+a)/2) + j·sgn(b)·√((r–a)/2) where r = √(a²+b²), applied twice: once for the EM wave case and once for the transmission-line case, making explicit how α (attenuation) and β (phase) depend on material parameters.

## Key concepts
- Propagation constant: γ = α + jβ
- Attenuation constant α, phase constant β
- Square root of complex number (rectangular and polar coordinate derivations)
- EM wave in lossy medium: γ = √(jωμ(σ + jωε)) → α and β in terms of μ, ε, σ, ω
- Telegrapher's equation from KVL/KCL on lumped transmission-line model
- Transmission-line propagation constant: γ = √((R+jωL)(G+jωC))
- Characteristic impedance: Z0 = √((R+jωL)/(G+jωC))
- Curl of curl identity: ∇×∇×A = ∇(∇·A) – ∇²A

## Methods / results / takeaways
- For a lossy EM medium: α = ω√(με/2)·[√(1+(σ/ωε)²) – 1], β = ω√(με/2)·[√(1+(σ/ωε)²) + 1].
- The ratio σ/ωε (loss tangent) determines the regime: σ ≫ ωε = good conductor; σ ≪ ωε = good dielectric.
- For the transmission line: γ = √((RG – ω²LC) + j(ωLG + ωRC)) with attenuation α and phase β given by analogous formulas.
- In both cases the approach is identical: identify a + jb, compute r = |a + jb|, and split into real and imaginary parts using the general formula.
- KVL/KCL on differential transmission-line segments leads to the telegrapher's equations, from which the wave equation and γ follow by differentiation.
