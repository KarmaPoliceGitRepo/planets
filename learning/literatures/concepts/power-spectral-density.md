# Power Spectral Density
**Aliases:** PSD; spectral density; Welch method; periodogram; ergodic process; autocorrelation; Wiener-Khinchin theorem

**Definition:** The power spectral density (PSD) S(f) describes how the mean-square value (power) of a stationary random signal is distributed across frequency (units: V²/Hz or Pa²/Hz). For ergodic processes, the PSD equals the Fourier transform of the autocorrelation function (Wiener–Khinchin theorem). The periodogram (squared FFT magnitude / N) is an inconsistent estimator; the Welch method averages periodograms from overlapping windowed segments to reduce variance at the cost of frequency resolution. An ergodic process is one for which time averages equal ensemble averages, allowing single-record PSD estimation.

**Key relations:**
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [noise-types](noise-types.md)
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)
- related: [spectral-leakage-and-windowing](spectral-leakage-and-windowing.md)

**Discussed in:**
- [Fundamentals of Signal Processing (Sound & Vibration)](../notes/signal-processing/fundamentals-signal-processing-sound-vibration.md) — PSD estimation via Welch method; engineering units; octave-band analysis
- [Noise and SNR Lecture](../notes/signal-processing/noise-and-snr-lecture.md) — PSD of thermal noise; bandwidth and total noise power calculation
- [Intro to Signal Processing (Orfanidis)](../notes/signal-processing/intro-signal-processing-orfanidis.md) — autocorrelation–PSD duality; ergodic processes; periodogram variance
