# Stress Dependency on Ultrasonic Wave Propagation Velocity — Part 1: Eulerian Viewpoint

- **Source:** Takahashi Part 1 Eulerian viewpoint
- **Drive link:** https://drive.google.com/file/d/1opoGilI__y49kW0FT02HA6NM7F2Ep5ol/view
- **Type:** paper
- **Author/Year:** S. Takahashi & R. Motegi, 1987
- **Coverage:** full

## Overview
A companion paper to Takahashi & Motegi Part 2, re-deriving the acoustoelastic velocity equations from the Eulerian (rather than the Lagrangian) viewpoint. Introduces the "pseudo elastic coefficient" (PEC) to handle the equation of motion of infinitesimal waves superposed on a finitely deformed solid. Provides Eulerian-frame velocity–stress equations for all principal wave configurations under uniaxial tension and hydrostatic pressure.

## Unique contribution
Explicit Eulerian derivation using the PEC framework, showing that the Eulerian and Lagrangian TOE constants (l,m,n vs l',m',n') differ and providing the conversion relations. Demonstrates that coordinate-system choice matters for finite deformation acoustoelasticity; most prior work (Hughes-Kelly, Hearmon) was Lagrangian.

## Key concepts
- Eulerian viewpoint / Lagrangian viewpoint
- Pseudo elastic coefficient (PEC)
- Finite deformation acoustoelasticity
- Murnaghan TOE constants (Eulerian)
- Eulerian vs. Lagrangian strain
- Equation of motion under finite deformation

## Methods / results / takeaways
- Three coordinate states defined: undeformed, statically/finitely deformed, state with dynamic infinitesimal deformation superposed
- PEC M_{ij,kl} has 54 components (due to symmetry of stress increments); connects stress increments linearly to infinitesimal displacement gradients
- Velocity equations derived for:
  - Longitudinal wave propagating along tensile axis: ρ₀V₁₁² = λ+2μ − (σ₁₁/E)·[72λ+14μ−6l−2ν(3λ−6l−2m)]
  - Shear waves (various polarization/propagation combos): equations (22) in the paper
  - Under hydrostatic pressure: V₁₁² = (λ+2μ)/ρ₀ − (p/(3λ+2μ))·(13λ+14μ−18l−4m) etc.
- Conversion between Eulerian (l,m,n) and Lagrangian (l',m',n') TOE constants:
  l = 2(λ+2μ) + ½(l'+2m'),  m = −4λ−12μ−2m',  n = 12μ+n'
- Jacobian det J ≈ 1+I₁ used to approximate density change in deformed state
- Demonstrates self-consistency with Hughes-Kelly when Eulerian/Lagrangian conversions are applied
