# Iterative Method for Accurate Determination of the Real and Imaginary Parts of the Materials Coefficients of Piezoelectric Ceramics

- **Source:** 1976 - Iterative Method for Accurate Determination of the Real and imaginary Parts of the Materials Coefficients of Piezoelectric Ceramics.pdf
- **Drive link:** https://drive.google.com/file/d/1VKhLoNKZ9xw_JxHbwnUFUchLFtc101lK/view
- **Type:** paper
- **Author/Year:** Jan G. Smits / 1976
- **Coverage:** full

## Overview
Presents a new iterative method for determining all real and imaginary parts of the complex material coefficients of piezoelectric ceramics from only three immittance measurements near resonance, without approximations. Converges in approximately 8 iterations to 10^-11 accuracy. Outperforms the IRE Standards method and the Holland-EerNisse method across all Q and coupling factor ranges.

## Unique contribution
First exact (non-approximate) iterative procedure for obtaining complex piezoelectric material constants from only three frequency-domain immittance measurements. Works for materials with low Q and low coupling factor where IRE and Holland-EerNisse methods fail (loop degenerates). Also shows a complete measurement scheme using only four resonator geometries to determine the full material constant matrix of a ferroelectric ceramic.

## Key concepts
- Complex piezoelectric material constants (s^E, d, ε^T)
- Immittance measurement of piezoelectric resonators
- Iterative algorithm for complex coefficient extraction
- IRE Standards method comparison
- Holland-EerNisse method comparison
- Low-Q, low-coupling material characterisation
- Positive definiteness constraint on imaginary parts
- Convergence of iteration (typically 8 steps)

## Methods / results / takeaways
- Algorithm: initial guess for s^E (purely real) → linear system solved for ε^T and d → updated s^E from third immittance point → iterate to convergence criterion C < 10^-11
- Convergence: ~10 decades accuracy per step; typically 8 steps required
- Compared against IRE and HEH methods on 4 material types: HQHk (high Q high k), LQHk, HQLk, LQLk
- New method always most accurate; IRE method inapplicable for low-k materials; HEH method inapplicable for low-Q low-k materials (admittance loop degenerates)
- Method independent of singular loop points (extrema of admittance) — robust against spurious resonances
- Full matrix determination: uses bar-length, bar-thickness, plate-thickness, and thickness-shear resonators — 4 geometries cover all 11 independent constants
- Used as foundation for Sherrit characterisation methods
