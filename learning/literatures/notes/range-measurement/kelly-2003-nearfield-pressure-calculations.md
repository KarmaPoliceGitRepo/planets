# Near-Field Pressure Calculations for Circular Transducers

- **Source:** 2003 - Nearfield_Pressure_Calculations_for_Circular_Transducers - (2003) JF Kelly.pdf
- **Drive link:** https://drive.google.com/file/d/1JJv5UJSUngh7oi122FhFXc0W_z-3Cwm6/view
- **Type:** paper
- **Author/Year:** J.F. Kelly / 2003 (MSU report)
- **Coverage:** full

## Overview
Analyses the error in far-field approximations for circular transducer beam patterns and presents the McGough fast near-field method (1D integral via Gauss quadrature) as a numerically efficient alternative. Quantifies the range at which far-field models become sufficiently accurate and shows beam pattern development in the transition zone.

## Unique contribution
Provides explicit error estimates for far-field approximations at multiples of the transition distance a²/λ, and benchmarks the McGough fast near-field method (64-point Gauss quadrature) for accuracy and computation time.

## Key concepts
- Near-field / far-field transition
- Circular transducer beam pattern
- Far-field approximation error
- McGough fast near-field method
- Gauss quadrature
- Major / side lobe development
- Rayleigh integral

## Methods / results / takeaways
- Far-field approximation at Z = a²/λ (standard transition): ~60% error relative to exact near-field calculation.
- Error at Z = 3 × a²/λ: ~6%.
- Error at Z = 10 × a²/λ: ~1.5%.
- Major and side lobes are not fully developed until R > 5a from the transducer face.
- **McGough fast near-field method**: reduces the 2D Rayleigh integral to a 1D integral using analytical geometry; avoids the 1/r singularity; numerically stable. Implemented with 64 Gauss abscissas.
- Computation time significant for a/λ = 25 (dense computation needed) but substantially faster than full 2D numerical integration.
- Practical implication: far-field formulas should not be used inside 3–10× the standard transition distance for precision calculations.
