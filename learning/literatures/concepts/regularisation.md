# Regularisation
**Aliases:** Tikhonov regularization; L2 regularization; ridge regression; Total Variation regularization; TV regularization; elastic net; sparse regularization; L1 regularization; LASSO; inverse problem; deconvolution

**Definition:** Regularisation stabilises ill-posed inverse problems by adding a penalty term to the least-squares objective. Tikhonov (L2) regularisation penalises the squared norm of the solution (or its derivative), producing smooth solutions: min ‖Ax − b‖² + λ‖Lx‖². Total Variation (TV) regularisation penalises the L1 norm of the gradient, preserving edges while suppressing noise: min ‖Ax − b‖² + λ‖∇x‖₁. The elastic net combines L1 (LASSO, which promotes sparsity) and L2 penalties. The regularisation parameter λ balances data fidelity against the smoothness/sparsity prior; it is chosen by cross-validation, L-curve, or discrepancy principle. In ultrasonics, regularisation is applied to deconvolution problems (recovering broadband material response from band-limited measurements).

**Key relations:**
- related: [digital-filters](digital-filters.md)
- related: [regression-and-least-squares](regression-and-least-squares.md)
- related: [wavelet-transform](wavelet-transform.md)
- related: [error-analysis](error-analysis.md)

**Discussed in:**
- [TV and Tikhonov Regularization Ultrasonic](../notes/signal-processing/tv-tikhonov-regularization-ultrasonic.md) — applies Tikhonov and Total Variation regularisation to deconvolve ultrasonic pulse-echo signals; compares L-curve and discrepancy-principle λ selection
- [Intro to Signal Processing (Orfanidis)](../notes/signal-processing/intro-signal-processing-orfanidis.md) — elastic net and LASSO as sparse signal-recovery penalties
