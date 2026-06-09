# Introduction to Experimental Error

- **Source:** Introduction to Experimental Error - Susan Cartwright.pdf
- **Drive link:** https://drive.google.com/file/d/1BK8Ji1QMXVWIWTeiGWImkodXsbkcmtqK/view
- **Type:** notes
- **Author/Year:** Cartwright / 2003
- **Coverage:** full

## Overview
Undergraduate lecture notes from the University of Sheffield covering statistical error analysis for physics experiments: statistical vs. systematic errors, Gaussian distribution, error propagation, weighted mean, and linear least-squares fitting.

## Unique contribution
Concise, practical treatment of experimental error analysis with worked examples, covering both random and systematic errors and their propagation through calculations.

## Key concepts
- Statistical error, systematic error
- Gaussian (Normal) distribution
- Mean, standard deviation, standard error of the mean
- Error propagation
- Weighted mean
- Linear least-squares fitting (regression)
- Chi-squared goodness of fit

## Methods / results / takeaways
- Statistical errors: arise from random fluctuations; characterised by σ (standard deviation); reduce as 1/√N with repeated measurements.
- Systematic errors: do not average out; must be identified and estimated separately.
- Gaussian distribution: most random errors are approximately Normal; ≈68% of measurements within ±σ, ≈95% within ±2σ.
- Error propagation: for y = f(x₁, x₂,...), σ_y² = Σ(∂f/∂xᵢ)²σ_xᵢ² (assuming uncorrelated errors).
- Weighted mean: x̄_w = Σ(xᵢ/σᵢ²) / Σ(1/σᵢ²); uses measurement precision as weights; uncertainty = 1/√Σ(1/σᵢ²).
- Linear least squares: minimise Σ[(yᵢ − a − bxᵢ)²/σᵢ²]; closed-form formulae for slope b and intercept a.
- Chi-squared test: χ² = Σ[(yᵢ−y_fit)²/σᵢ²] measures goodness of fit; expected value equals degrees of freedom for good fit.
