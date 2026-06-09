# Gaussian Process Regression: An Introduction

- **Source:** Gaussian process regression An introduction - Ebden.pdf
- **Drive link:** https://drive.google.com/file/d/11TfIzDZIruEDcEGYLWo2sAYA6pTKXsLP/view
- **Type:** notes
- **Author/Year:** Ebden / 2008
- **Coverage:** full

## Overview
An introductory tutorial on Gaussian Process Regression (GPR) from Oxford University. Covers the prior distribution over functions, the squared exponential covariance function, the posterior prediction equations, hyperparameter optimisation via log marginal likelihood, and a brief extension to Gaussian Process Classification (GPC).

## Unique contribution
Provides a concise, self-contained GPR tutorial with worked examples and clear derivations, including the marginal likelihood optimisation approach for setting hyperparameters without cross-validation.

## Key concepts
- Gaussian process (GP)
- Prior over functions
- Posterior (predictive distribution)
- Covariance function (kernel)
- Squared exponential (RBF) kernel
- Length-scale hyperparameter
- Signal variance, noise variance
- Log marginal likelihood
- Hyperparameter optimisation
- Gaussian process classification (GPC)

## Methods / results / takeaways
- GPR: a GP is a distribution over functions; specified by a mean function (often zero) and a covariance function k(x,x').
- Squared exponential kernel: k(x,x') = σ_f² exp(−|x−x'|²/(2l²)); hyperparameters are length-scale l, signal variance σ_f², noise variance σ_n².
- Prediction: posterior mean and variance are derived analytically by conditioning the GP prior on training data.
- Key equations: μ* = k(X*,X)[K+σ_n²I]⁻¹y and σ²* = k(x*,x*)−k(X*,X)[K+σ_n²I]⁻¹k(X,X*).
- Hyperparameter optimisation: maximise log marginal likelihood p(y|X,θ) with respect to θ = {l, σ_f, σ_n}; gradient-based optimisation.
- Advantage: GPR provides calibrated uncertainty estimates (predictive variance).
- GPC: extension using a probit/logit link; requires approximate inference (Laplace approximation, EP).
