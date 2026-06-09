# Gaussian Process Regression
**Aliases:** Gaussian process regression; GPR; Gaussian process; squared exponential kernel; RBF kernel; log marginal likelihood; kriging; Bayesian non-parametric regression

**Definition:** Gaussian Process Regression (GPR) models the unknown function f(x) as a Gaussian process — any finite collection of function values follows a multivariate Gaussian distribution — with prior covariance specified by a kernel (covariance function). The squared exponential (RBF) kernel k(x,x') = σ_f² exp(−|x−x'|²/2ℓ²) encodes smoothness and length-scale ℓ. Given observations y = f(X) + ε (with Gaussian noise σ_n²), the posterior mean and variance are obtained analytically, providing calibrated uncertainty estimates. Hyperparameters (σ_f, ℓ, σ_n) are learned by maximising the log marginal likelihood. GPR is also known as kriging in geostatistics.

**Key relations:**
- related: [kalman-filter](kalman-filter.md)
- related: [error-analysis](error-analysis.md)
- related: [regression-and-least-squares](regression-and-least-squares.md)

**Discussed in:**
- [Gaussian Process Regression Intro](../notes/signal-processing/gaussian-process-regression-intro.md) — GP prior/posterior derivation; squared exponential and Matérn kernels; hyperparameter optimisation via log marginal likelihood; predictive uncertainty
