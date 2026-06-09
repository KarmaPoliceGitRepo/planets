# Kalman Filter
**Aliases:** Kalman filter; Kalman-Bucy filter; Bayesian estimator; state-space estimator; recursive Bayesian estimator; Gaussian process regression; GPR; Riccati equation

**Definition:** The Kalman filter is the optimal linear recursive estimator for discrete-time state-space systems driven by Gaussian process noise and corrupted by Gaussian measurement noise. At each step it computes: (1) a predict step propagating the state estimate and covariance forward in time, and (2) an update step blending the prediction with the new measurement, weighting by the Kalman gain K = PH^T(HPH^T + R)^{-1}. The steady-state gain satisfies the discrete algebraic Riccati equation. Gaussian Process Regression (GPR) is the nonparametric Bayesian counterpart: it models the signal as a GP with a prior covariance (kernel), then conditions on observations to give a posterior mean and variance; the squared exponential (RBF) kernel is the most common.

**Key relations:**
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)
- related: [error-analysis](error-analysis.md)
- related: [temperature-compensation](temperature-compensation.md)
- related: [laplace-and-z-transform](laplace-and-z-transform.md)

**Discussed in:**
- [Kalman-Bucy Linear Filtering](../notes/signal-processing/kalman-bucy-linear-filtering.md) — full derivation of Kalman and Kalman-Bucy (continuous-time) filters; Riccati equation; optimality proof
- [Gaussian Process Regression Intro](../notes/signal-processing/gaussian-process-regression-intro.md) — GP priors, squared exponential kernel, hyperparameter optimisation via log marginal likelihood
