# Introduction to Experimental Error

- **Source:** Introduction to Experimental Error - Susan Cartwright.pdf
- **Drive link:** https://drive.google.com/file/d/1rKwXWKRxBrkq98kDnPAn8fX5bbjgq1xt/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Susan Cartwright, 2003
- **Coverage:** full

## Overview
A concise 12-page pedagogical introduction to experimental error for undergraduate physics students, covering the nature of measurement uncertainty, how to estimate and propagate errors, how to combine data sets, and how to present and compare results rigorously. It bridges conceptual grounding (why errors matter for scientific reproducibility and theory-testing) with practical recipes.

## Unique contribution
Provides an unusually clear, self-contained treatment that integrates conceptual motivation, statistical theory, and hands-on practice rules in a single short document. Particularly strong on the distinction between statistical and systematic errors, on the logic of weighted means (showing the 1/σ² weighting emerges naturally from averaging N and M repeated measurements), and on practical guidance for quoting and comparing results including explicit probability thresholds for discrepancy levels (1σ, 2σ, 3σ). The worked examples anchoring each section (glass block lengths, marble sampling, Planck's constant, specific heat of iron) make the abstract machinery concrete.

## Key concepts
- Experimental error / experimental precision
- Statistical error (random error)
- Systematic error
- Normal (Gaussian) distribution
- Standard deviation (σ)
- Standard error of the mean (σ/√N)
- Poisson distribution / shot noise
- Error propagation (single variable: Δf ≈ |df/dx|Δx)
- Error propagation (multiple variables: addition in quadrature)
- Variance
- Weighted mean (weight = 1/σ²)
- Method of least squares / linear least-squares fit
- Residuals
- Confidence limits / significance levels
- Quoting significant figures in errors

## Methods / results / takeaways
**Estimating errors on measured quantities**
- Single measurements: estimate from knowledge of the setup; digital displays read to ±½ last digit but instrument accuracy may be worse; hand-timing is dominated by reaction time.
- Repeated measurements: use sample standard deviation s = √[Σ(xᵢ − x̄)²/(N−1)]; error on the mean (standard error) = s/√N.
- Counting experiments: assign error ±√N (Poisson / shot noise), valid for N ≳ 5.

**Error propagation**
- Single variable: ΔF ≈ |df/dx| Δx (first-order Taylor expansion).
- Multiple independent variables: add partial-derivative contributions in quadrature: (Δf)² = (∂f/∂x Δx)² + (∂f/∂y Δy)² + …
- Key standard results: Δ(x²) = 2x Δx; Δ(ln x) = Δx/x; for products/quotients use fractional errors added in quadrature.

**Combining data**
- Weighted mean: x̄_w = Σ(xᵢ/σᵢ²) / Σ(1/σᵢ²); error: 1/σ² = Σ(1/σᵢ²). A less precise observation contributes negligibly (e.g., 1.5±0.2 combined with 1.70±0.05 yields 1.69±0.05).
- Cross-check: scatter-based error estimate should roughly match weight-based estimate; large discrepancy flags bad error estimates or non-independence.
- Linear least-squares fit (y = ax + b): minimise Σ(yᵢ − axᵢ − b)². Formulas for a, b, Δa, Δb given. Key assumptions: errors on y larger than on x; errors on y all similar size; errors independent. Weighted fit needed when error sizes differ; Excel's LINEST does unweighted fit only.

**Practical gotchas**
- Inspect residuals after fitting: ~2/3 of points should lie within 1 error bar of the fit line; if all 20 points lie exactly on the line, the errors are wrong.
- A single outlier can dominate the gradient; consider omitting after justification.
- Systematic errors often appear as curvature on log plots, nonzero intercepts, or irreproducibility under ambient-condition changes.
- Recalibration can correct a systematic bias retrospectively without re-running the experiment.

**Quoting results**
- Quote error to 1–2 significant figures; align decimal places of value to match error.
- Use the same exponent for value and error in scientific notation.
- Label statistical and systematic errors separately: e.g., 1.57 ± 0.09 (stat.) ± 0.05 (syst.).

**Comparing with theory or book values**
- Compute (result − book value) / combined error:
  - |diff| < 1σ: good agreement
  - 1–2σ: consistent
  - 2–3σ: probable problem (~1 in 20 chance by fluctuation)
  - > 3σ: definite problem (< 1% chance)
- Never dismiss a 4σ discrepancy as "close in percentage terms"; always investigate systematic sources.
- Always cite the specific source and conditions of a book value.
