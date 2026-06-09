# Introduction to Elastic Wave Propagation

- **Source:** 1994 - A Bedford, DS Drumheller - Introduction to Elastic Wave Propagation.pdf
- **Drive link:** https://drive.google.com/file/d/1Te7nDwCD5G087UGUM1RzDEEUWpyUibmF/view?usp=drivesdk
- **Type:** book
- **Author/Year:** A. Bedford, D.S. Drumheller, 1994 (John Wiley & Sons; this copy includes an added FEM section)
- **Coverage:** partial (large file, truncated extraction)

## Overview
A graduate text developing elastic wave propagation from first principles of linear elasticity. Covers 1-D waves in bars and columns, plane waves in infinite media, reflection/transmission at interfaces, surface waves, and guided waves in plates and rods. A section on the finite element method has been added to the online version of the text.

## Unique contribution
Self-contained derivation of all governing equations from continuum mechanics (strain tensor, stress tensor, equations of motion) before specialising to waves. Provides clear derivations of Rayleigh and Love waves starting from boundary conditions. The appended FEM section connects classical wave theory to modern computational methods.

## Key concepts
- Index notation, tensor algebra
- Strain tensor, stress tensor, Cauchy tetrahedron
- Linear elastic constitutive law, Lamé constants
- Equations of motion (Navier–Lamé equations)
- Helmholtz decomposition
- 1-D wave equation, d'Alembert solution
- P-waves and S-waves in 3-D elastic solid
- Plane wave reflection and transmission at planar interfaces
- Rayleigh surface waves
- Love waves in a layer
- Guided waves (plates and rods), dispersion

## Methods / results / takeaways
The isotropic linear elastic constitutive law is σ_ij = λε_kk δ_ij + 2μ ε_ij. The equations of motion then yield two decoupled wave equations for dilatation (P-wave velocity α = sqrt((λ+2μ)/ρ)) and rotation (S-wave velocity β = sqrt(μ/ρ)). Reflection coefficients at a solid–solid interface satisfy energy conservation; mode conversion generates both P and SV reflected/transmitted waves. Rayleigh waves are found by requiring decaying exponential solutions satisfying traction-free boundary conditions; the Rayleigh secular equation is a cubic in (c/β)². Love wave dispersion requires β₁ < c_Love < β₂ across the relevant frequency range.
