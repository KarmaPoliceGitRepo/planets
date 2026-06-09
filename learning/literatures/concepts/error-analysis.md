# Error Analysis and Uncertainty
**Aliases:** error propagation; uncertainty propagation; addition in quadrature; systematic error; random error; statistical error; experimental error; standard deviation; variance; standard error of the mean; confidence limit; significant figures; weighted mean; method of least squares; residuals; normal distribution; Poisson distribution

**Definition:** Measurement uncertainty distinguishes systematic error (reproducible bias from a fixed source) from random error (zero-mean scatter reducing with √N repeats). For a derived quantity f(x₁, …, xₙ) with independent inputs, the propagated uncertainty is σ_f = √Σ(∂f/∂xᵢ)²σᵢ² (addition in quadrature), valid when the partial derivatives are evaluated at the mean values. The standard deviation σ estimates the spread of a single observation; the standard error of the mean σ/√N estimates the uncertainty on the sample mean. The weighted mean assigns higher weight to more precise measurements: x̄_w = Σwᵢxᵢ/Σwᵢ with wᵢ = 1/σᵢ². The method of least squares minimises Σ(residual)² to fit a model to data. The normal distribution (Gaussian) is the limiting distribution for the sum of many independent errors; the Poisson distribution applies to counting experiments.

**Key relations:**
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)
- related: [statistical-methods](statistical-methods.md)
- related: [experimental-design](experimental-design.md)
- related: [regression-and-least-squares](regression-and-least-squares.md)

**Discussed in:**
- [Introduction to Experimental Error (Cartwright)](../notes/00-general-error-measurement/introduction-to-experimental-error-cartwright.md) — comprehensive treatment: systematic vs. random error, propagation in quadrature, normal distribution, weighted mean, least squares
- [Experimental Error Intro (signal-processing notes)](../notes/signal-processing/experimental-error-intro.md) — applied examples of error propagation for ultrasonic velocity and ToF measurement
