# Analysis of Beams with Non-Uniform Temperature Profile Due to Fire Exposure

- **Source:** Analysis of beams with non-uniform temperature profile due to fire exposure (1990) IW Burgess.pdf
- **Drive link:** https://drive.google.com/file/d/1H-i2FRttrhpKprQj_eXbifcxiglBW6M2/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** I. W. Burgess, J. A. El-Rimawi, R. J. Plank / 1990
- **Coverage:** full

## Overview
A journal paper (J. Construct. Steel Research, 1990) from the University of Sheffield that extends an earlier secant-stiffness method to analyse steel beams whose cross-sections have non-uniform temperature distributions under fire loading. It presents the theory, a PC-compatible implementation (program CBSTIFF), and validation against published fire test data for three beam types: conventional floor beams, shelf-angle floor beams, and slim-floor beams.

## Unique contribution
Prior work by the same group handled only uniformly heated beams. This paper adds two critical extensions: (1) an iterative procedure to locate the neutral axis when temperature gradients break cross-sectional symmetry in strength, and (2) a formulation for thermal curvature caused by differential expansion across the section, converted to equivalent fixed-end moments so the beam can be analysed with linear secant-stiffness matrices. The entire analysis runs on an 80286 PC — a deliberate departure from mainframe-only codes such as FASBUS, FIRES-T3 and TASEF-2.

## Key concepts
- Secant stiffness method
- Non-uniform temperature profile (fire)
- Neutral axis location under thermal gradient
- Thermal curvature / thermal bowing
- Ramberg-Osgood stress-strain-temperature model
- Cross-section strip discretisation
- Fixed-end moments from thermal loading
- Fire resistance of steel beams
- Slim-floor, shelf-angle, conventional floor beam types
- Standard fire time-temperature curve (ISO 834 / BS 476)

## Methods / results / takeaways
- **Strip discretisation:** the cross-section is divided into rectangular strips of constant temperature and width; different temperatures give different local elastic moduli and strengths.
- **Neutral axis search:** equilibrium of internal forces (compression above = tension below) is solved iteratively by a trial-and-error shift; symmetry of the strain profile cannot be assumed when temperatures vary.
- **Thermal curvature formula:** derived from compatibility and equilibrium for a section with temperature-dependent elastic moduli, leading to eq. (21); for non-linear material behaviour the elastic modulus is replaced by a secant modulus and the solution becomes iterative.
- **Equivalent moments:** thermal curvature is converted to fixed-end moments (eq. 10: M_a = -M_b = k_th · S_s) and added to the load vector, allowing the existing secant-stiffness matrix solver to handle thermal bowing without structural changes.
- **Validation:** good agreement with British Steel Corporation fire tests for all three beam types; some discrepancy at temperatures above 800 °C where steel properties are poorly characterised.
- **Illustrative examples:** continuous multi-span beams and an industrial portal frame analogue; moment redistribution between spans is captured as temperatures rise.
- **Practical note:** execution time ~20 min for 14 temperature steps on an 80286 PC at 10 MHz; considered acceptable for the complexity.
- **Limitation noted:** analysis does not yet include axial thrust or semi-rigid connection behaviour (scope of future work).
