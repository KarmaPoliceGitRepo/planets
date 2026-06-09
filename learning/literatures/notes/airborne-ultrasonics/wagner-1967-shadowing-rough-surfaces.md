# Shadowing of Randomly Rough Surfaces

- **Source:** Wagner 1967 shadowing rough surfaces
- **Drive link:** https://drive.google.com/file/d/1CVnq03XlyT7ASsw_JL04-22e4ItE1Fg8/view
- **Type:** paper
- **Author/Year:** Wagner, 1967 (Journal of the Acoustical Society of America, 41(1), 138–147)
- **Coverage:** full

## Overview
Derives analytical formulas for the shadowing function S(θ) for scattering from randomly rough Gaussian surfaces, and for the bistatic shadowing function S(θ₁, θ₂). Also derives the probability density of heights and slopes of the illuminated surface. Results agree well with computer simulation data of Brockelman & Hagfors. Shadowing function depends only on ratio of ray slope to rms surface slope (v = tanθ / (2|φ₀"|)^½).

## Unique contribution
Provides an analytically tractable expression for the shadowing function of a stationary Gaussian random rough surface that agrees well with numerical simulation, improving on Beckmann's initial calculation. Derives bistatic shadowing (simultaneous illumination from two directions) and shows that apparent surface roughness (Z²/φ₀) is significantly reduced at small grazing angles by shadowing.

## Key concepts
- Shadowing function S(θ) for randomly rough surfaces
- Bistatic shadowing S(θ₁, θ₂)
- Gaussian random rough surface statistics
- Conditional shadowing probability
- Ray-optics (geometric) scattering approximation
- rms height σ and correlation length T
- Grazing angle dependence
- Probability density of illuminated slopes

## Methods / results / takeaways
- Surface model: stationary Gaussian random process z = ξ(x); rms height σ = (φ₀)^½, Gaussian autocorrelation φ(r) = σ² exp(−r²/T²).
- Shadowing function: S(θ) = ½(1 + erfv)(1 − e^(−v²))/(4Bv) where v = tanθ/(2|φ₀"|)^½ — depends only on ratio of ray slope to rms surface slope.
- Bivariable Backmann result: S(0) → 0 exponentially; Wagner result: S → 0 linearly in tanθ — more physical.
- Bistatic S(θ₁, θ₂): depends on both ray directions; for π/2 < θ₂ < π − θ₁, S(θ₁, θ₂) = S(θ₁) (bistatic contribution from same side only).
- Apparent roughness Z² < φ₀ at small grazing angles due to shadowing; surface appears smoother when shadowing is significant.
- S(θ) agrees well with Brockelman & Hagfors simulation for θ > 10°; slight overestimate below 10°.
- Application: correction factor for Kirchhoff-based scattering theories used in ultrasonic roughness measurement.
