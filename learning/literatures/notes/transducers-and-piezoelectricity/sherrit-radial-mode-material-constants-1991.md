# Accurate Evaluation of the Real and Imaginary Material Constants for a Piezoelectric Resonator in the Radial Mode

- **Source:** Sherrit 1991 accurate evaluation (radial mode)
- **Drive link:** https://drive.google.com/file/d/17vbwYT-a2LxDfNbYE95oz1msC8X0WSz9/view
- **Type:** paper
- **Author/Year:** S. Sherrit, N. Gauthier, H. D. Wiederick, B. K. Mukherjee / 1991
- **Coverage:** full

## Overview
Presents a method to determine the complex (real and imaginary) material constants governing the radial mode resonance of piezoelectric disks, extending the IEEE standard approach (Meitzler et al.) which only yields real constants. Uses critical frequencies from the real and imaginary admittance/impedance data (series resonance, parallel resonance, and half-band frequencies) to calculate the complex Poisson's ratio σ^P, complex radial stiffness c^P₁₁, coupling constant K^P, and dielectric constant ε^S₃₃. Also provides polynomial fits (3rd/4th order) to replace IEEE table lookup, enabling computer automation.

## Unique contribution
First published technique for full complex material constant determination in the radial mode. Circumvents the coupling problem between radial and thickness modes by using only frequency data near the first and second radial resonances (not impedance magnitude). Validates via three synthetic datasets with known input constants (errors generally <1% for real, <5% for imaginary parts) and demonstrates on a Navy Type V PZT BM532 specimen.

## Key concepts
- Radial mode resonance of fully-electroded piezoelectric disk
- IEEE Standard (Meitzler et al.) automation via polynomial fits to σ^P vs r_s and η vs r_s
- Complex Poisson's ratio σ^P = σ^P_r + iσ^P_i
- Half-band frequencies for imaginary constant determination
- Complex series resonance ratio r_s = f^(1)_s / f^(2)_s
- Holland convention: material constants written as (real - i·imaginary)
- Complex Bessel function evaluation J(x) with x complex
- Navy Type V PZT (BM532) characterisation: s^E₁₁, s^E₁₂, d₃₁, ε^T₃₃
- Radial mode coupling coefficient K^P vs planar coupling k_p

## Methods / results / takeaways
- Automation: 3rd/4th-order polynomial fits replace IEEE table lookup for σ^P and η; errors <0.1% for σ^P, <0.05% for η in range 0 < σ^P < 0.7
- Complex constants: use corrected complex resonance frequencies from both real and imaginary admittance data in Eq.(14)-(16); substitute complex r_s into polynomial fits for complex σ^P and η
- Error analysis (Tables III-V): for Q₂₁ = -20 to -50, errors in real constants <0.7%; imaginary constants <4%; larger imaginary constants (lower Q) → larger errors
- PZT BM532 (Navy V): s^E₁₁ = 1.704×10⁻¹¹ m²/N (tan~1.8%), s^E₁₂ = -6.394×10⁻¹² m²/N, d₃₁ = -222.5×10⁻¹² C/N, ε^T₃₃ = 2.74×10⁻⁸ F/m; excellent fit quality
- Limitation: method breaks down for Q < 10 (loss too high) or very high Q (frequency precision limiting)
- Combined with Smits' thickness mode method, all relevant complex constants of a disk can be determined from a single sample
