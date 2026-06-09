# Probability and Random Processes
**Aliases:** probability; random process; stochastic process; ergodic process; stationary process; autocorrelation; variance; Gaussian process; Poisson distribution; normal distribution; central limit theorem; Cramér-Rao Lower Bound

**Definition:** A random process X(t) is a family of random variables indexed by time (or space). A wide-sense stationary (WSS) process has constant mean and autocorrelation depending only on lag τ: R_X(τ) = E[X(t)X(t+τ)]. An ergodic process allows time averages to replace ensemble averages, making single-record PSD estimation valid. The Gaussian (normal) distribution N(μ, σ²) arises from the central limit theorem; the Poisson distribution describes rare counts. The Cramér–Rao Lower Bound (CRLB) gives the minimum variance of any unbiased estimator as the inverse Fisher information.

**Key relations:**
- related: [error-analysis](error-analysis.md)
- related: [power-spectral-density](power-spectral-density.md)
- related: [noise-types](noise-types.md)
- related: [kalman-filter](kalman-filter.md)
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)

**Discussed in:**
- [Introduction to Experimental Error (Cartwright)](../notes/00-general-error-measurement/introduction-to-experimental-error-cartwright.md) — normal and Poisson distributions; central limit theorem; confidence intervals
- [Fundamentals of Signal Processing (Sound & Vibration)](../notes/signal-processing/fundamentals-signal-processing-sound-vibration.md) — stationary, ergodic random processes; autocorrelation and PSD; ensemble vs. time averaging
- [Noise and SNR Lecture](../notes/signal-processing/noise-and-snr-lecture.md) — Cramér–Rao bound for time-delay estimation; SNR and Fisher information
