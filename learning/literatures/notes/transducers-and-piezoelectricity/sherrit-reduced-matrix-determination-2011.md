# Determination of the Reduced Matrix of the Piezoelectric, Dielectric, and Elastic Material Constants for a Piezoelectric Material With C∞ Symmetry

- **Source:** Sherrit 2011 reduced matrix determination
- **Drive link:** https://drive.google.com/file/d/1TO0dxgzy5nfwXH6ajBFAOYcZs5Xn_a4W/view
- **Type:** paper
- **Author/Year:** Stewart Sherrit, Tony J. Masys, Harvey D. Wiederick, Binu K. Mukherjee / 2011
- **Coverage:** full

## Overview
Presents a complete procedure for determining the full reduced matrix of complex (lossy) piezoelectric, dielectric, and elastic material constants for a C∞ symmetry material (such as PZT ceramic) from a single disk sample. Uses five resonance geometries (radial, thickness, length-thickness, length shear extensional, length extensional) measured on a Channel 5804 Navy Type III PZT ceramic disk. Also provides the sub-matrix transform equations for converting between the four standard constant sets (s,d,ε; c,e,ε; c,h,β; s,g,β).

## Unique contribution
Demonstrates that the full 10-element reduced complex material constant matrix can be obtained from a single disk plus derived bars — without needing multiple custom geometries. Provides the complete transform relations in reduced sub-matrix form. Identifies dispersion between 100 kHz (elastic modes) and 2.5 MHz (thickness mode) as the main source of s₁₃^E discrepancy between calculation methods. Warns that error propagation is particularly severe for imaginary components (5–20%) and for hydrostatic coefficients d_h when d₃₃ ≈ -2d₃₁.

## Key concepts
- C∞ symmetry PZT: 10 independent real constants (2 dielectric + 5 elastic + 3 piezoelectric) → 20 complex constants
- Five resonance modes: radial (series), thickness, length-thickness (LTE), longitudinal shear (LSE), length extensional (LE)
- PRAP software (TASI Technical Software) for iterative Smits-type fitting
- Non-iterative technique for radial mode (from earlier Sherrit work)
- Sub-matrix transform equations: [s,d,ε] ↔ [c,e,ε] ↔ [c,h,β] etc.
- s₁₃^E determination: matrix inversion vs Smits' equations
- Error propagation in complex constants and in hydrostatic coefficients

## Methods / results / takeaways
- Channel 5804 PZT (Navy Type III): disk dia=19.03 mm, thickness=0.875 mm, density=7550 kg/m³
- Key results (Table II): s^E₁₁ = 1.20×10⁻¹¹ m²/N, d₁₃ = -1.12×10⁻¹⁰ C/N, d₃₃ = 2.19×10⁻¹⁰ C/N, d₁₅ = 4.3×10⁻¹⁰ C/N, ε^T₃₃ = 9.82×10⁻⁹ F/m; real errors ~1-2%, imaginary errors ~5-20%
- Coupling coefficients (Table III): k_p = 0.538, k_t = 0.489, k₁₃ = 0.334, k₁₅ = 0.655
- s₁₃^E discrepancy: matrix inversion gives -4.99×10⁻¹² vs Smits' -4.92×10⁻¹² (due to frequency dispersion between thickness and elastic modes); matrix inversion preferred
- Dispersion: length extensional mode permittivity is 10% smaller than radial/LTE mode value — attributed to frequency dependence
- Hydrostatic coefficient d_h = d₃₃ + 2d₃₁: small errors in piezoelectric constants give >100% error when d_h is small
- Large imaginary component errors arise from error propagation when inverting nearly-singular sub-matrices
