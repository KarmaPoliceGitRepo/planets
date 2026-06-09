# Approximation of the Rayleigh Wave Speed

- **Source:** Approximation of the Rayleigh wave speed.pdf
- **Drive link:** https://drive.google.com/file/d/1ByflrhLtQnpaSFi9RWSZWsvMMuHAyBsE/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** A. V. Pichugin (University of Sheffield) / 2008 (preprint submitted to Elsevier)
- **Coverage:** full

## Overview
A brief mathematical note presenting an alternative asymptotic method (Graeffe's iterative squaring method) for computing the Rayleigh wave speed accurately without using Cardan's formula for cubic equations. The method converges quadratically to the physically relevant root of the secular equation and is applicable to both isotropic and incompressible orthotropic media. Interpolation polynomial approximations are also derived for practical use.

## Unique contribution
Unlike prior exact solutions (which all relied on Cardan's formula), this approach uses Graeffe's iterative method to amplify the dominant root of the cubic, automatically selecting the physically relevant one. The resulting n = 5 approximation achieves relative error < 10⁻¹³ across all valid Poisson ratios. Simple polynomial approximations (Eqs. 14–15) with errors < 0.14% and 0.05% respectively are derived for direct use.

## Key concepts
- Rayleigh wave secular equation (cubic)
- Rayleigh wave speed formula
- Graeffe's method (iterated squaring for polynomial roots)
- Poisson ratio dependence
- Cardan's formula alternative
- Incompressible orthotropic half-space
- Asymptotic convergence

## Methods / results / takeaways
- The secular equation reduces to a cubic in ζ = cR²/β²; the Graeffe procedure transforms it iteratively so the dominant root is well-separated.
- Key recurrences: pn = 2qn₋₁ − pn₋₁², qn = 2pn₋₁ + qn₋₁², then xn is approximated from pn by a simple formula.
- After n = 5 iterations the error in cR is < 10⁻¹³; for ν > 0, n = 4 suffices with error < 10⁻¹⁵.
- Classical estimate cR ≈ (0.87 + 1.12ν)/(1 + ν) has ~0.46% error and is valid for ν > 0 only.
- Improved interpolation polynomial (Eq. 15) reduces max error to 0.05% for all Poisson ratios.
- The technique extends to orthotropic media governed by a secular equation of the same cubic structure.
