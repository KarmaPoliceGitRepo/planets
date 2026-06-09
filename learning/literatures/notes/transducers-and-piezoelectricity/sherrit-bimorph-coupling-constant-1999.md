# An Analytical Solution for the Electromechanical Coupling Constant of an Unloaded Piezoelectric Bimorph

- **Source:** Sherrit 1999 bimorph coupling constant
- **Drive link:** https://drive.google.com/file/d/1dsIF62IO2ukPfaVcuVqXE4DwkOyIUG5i/view
- **Type:** paper (IEEE TUFFC Correspondence)
- **Author/Year:** S. Sherrit, B. K. Mukherjee, R. J. Tasker / 1999
- **Coverage:** full

## Overview
Derives an analytical closed-form expression for the electromechanical coupling constant k₁₃ of an unloaded two-layer piezoelectric bimorph using the series and parallel resonance frequencies. Extends Smits et al. capacitance equation for a bimorph. The method gives k₁₃ from frequency data without requiring a full material constant measurement, and also provides a corrected expression for the low-frequency permittivity of the bimorph.

## Unique contribution
Provides the first analytical (non-iterative) solution for bimorph coupling constant from resonance data. Shows that the bimorph k₁₃ can be written in closed form via the function F(x) = tanh(x)/x using the first root R₁=1.8751 of the characteristic equation cos(ΩL)·cosh(ΩL)+1=0. Also derives the low-frequency permittivity correction ε_LF = ε^T₃₃(1 − k²₃₁/4), which differs from the standard single-element result.

## Key concepts
- Unloaded piezoelectric bimorph: two identical PZT layers in series/parallel electrical connection
- Characteristic equation for bimorph resonance: cos(ΩL)·cosh(ΩL) + 1 = 0; first root R₁ = 1.8751
- F(x) = tanh(x)/x function for k₁₃ computation
- Coupling constant: k₁₃ = [1 − (3/4)·F(x)/x]^(−1/2) (from series/parallel frequency ratio)
- Low-frequency permittivity: ε_LF = ε^T₃₃·(1 − k²₃₁/4)
- Smits et al. capacitance equation for bimorphs

## Methods / results / takeaways
- Bimorph resonance equations solved analytically by substituting the characteristic root R₁ into the admittance/impedance expressions
- k₁₃ extracted from ratio of parallel to series resonance frequency using the F(x) function
- Low-frequency permittivity correction derived from static analysis; standard ε^T₃₃ overestimates bimorph clamped capacitance
- Practical implication: enables direct k₁₃ determination for bimorph transducers from a simple impedance sweep without iterative fitting
- Validated against Smits et al. bimorph equations; results consistent with single-layer k₁₃ when k₃₁ is small
