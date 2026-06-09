# Complete Characterization of the Piezoelectric, Dielectric, and Elastic Properties of Motorola PZT 3203 HD, Including Losses and Dispersion

- **Source:** Sherrit 1997 complete characterization Motorola PZT-3203HD
- **Drive link:** https://drive.google.com/file/d/1m2Roax7oyWQRNtCLIW0Z_XOZfKAWfwbY/view
- **Type:** paper (conference, SPIE Medical Imaging 1997: Ultrasonic Transducer Engineering)
- **Author/Year:** S. Sherrit, H. D. Wiederick, B. K. Mukherjee / 1997
- **Coverage:** full

## Overview
Determines the complete reduced complex material constant matrix for Motorola 3203HD PZT (C∞ symmetry: 10 independent constants) from five resonance modes — thickness extensional (TE), thickness shear (TS), length extensional (LE), length-thickness extensional (LTE), and radial (RAD) — at both the fundamental and second resonance frequencies. Analyses frequency dispersion of all constants between first and second resonance, classifying sources as intrinsic (material) vs extrinsic (electrode sheet resistance, mode coupling). Provides linear frequency-dependence coefficients ∂x/∂f for each constant.

## Unique contribution
First published complete characterisation of Motorola 3203HD PZT including all loss terms and dispersion, using complex Smits' and Sherrit non-iterative methods simultaneously. Identifies two distinct dispersion mechanisms: electrode sheet/contact resistance (increases resistance baseline, shifts imaginary permittivity) vs mode coupling (increases real permittivity, decreases imaginary component). Demonstrates that imaginary parts of material constants change significantly between fundamental and second resonance — making them frequency-dependent in a quantifiable way. Aging effect also identified: shear piezoelectric constant d₁₅ was >20% higher in freshly poled samples.

## Key concepts
- Motorola PZT 3203HD: C∞ symmetry, 10 complex material constants
- Five resonance modes: TE, TS, LE, LTE, RAD
- Smits' iterative method for TS, LE, LTE, TE; Sherrit non-iterative method for radial mode
- s₁₃^E determination: matrix inversion vs Smits' formula (both used)
- Frequency dispersion: linear model ∂x/∂f over fundamental-to-second-resonance range
- Extrinsic dispersion sources: electrode sheet resistance (Im ε decreases, Re ε stable) vs mode coupling (Re ε increases, Im ε decreases)
- Aging: d₁₅ decreases >20% over 1 year after poling

## Methods / results / takeaways
- Key constants at fundamental resonance (Table 2): s^E₁₁ = 1.56×10⁻¹¹(−0.031i), c^D₃₃ = 1.77×10¹¹, d₁₃ = −295 pC/N, d₃₃ = 564 pC/N, d₁₅ = 560 pC/N, ε^T₃₃ = 1.06×10⁻⁸ F/m, k_t = 0.536, k₃₃ = 0.706, k₁₃ = 0.447, k₁₅ = 0.611
- Poisson's ratio from radial mode: derived from series resonance frequency ratio
- s₁₃^E: matrix inversion gives agreement to within factor of 2 for imaginary part vs Smits formula — attributed to error amplification in subtraction of similar-magnitude quantities
- Dispersion table (Table 4): linear coefficients ∂x/∂f (real and imaginary) for all 10 constants
- LE mode: overestimates second resonance frequency → major dispersion in s^E₃₃; stray capacitance correction does not account for all observed dispersion
- Conclusion: losses and dispersion are significant; ignoring them reduces accuracy of transducer models
