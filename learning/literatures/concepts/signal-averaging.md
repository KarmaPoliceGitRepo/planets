# Signal Averaging
**Aliases:** coherent averaging; ensemble averaging; stochastic averaging

**Definition:** Signal averaging improves SNR by summing N synchronised (coherent) repetitions of a signal; because noise adds incoherently, the signal amplitude grows as N while noise amplitude grows as √N, giving an SNR improvement of √N (or 10 log₁₀ N dB). Coherent averaging requires a stable trigger reference to align pulses before summation; if trigger jitter is non-negligible it blurs the averaged waveform (bandwidth loss). Ensemble averaging of a stationary random process estimates the power spectral density (Welch method); the variance of the PSD estimate decreases with the number of averages.

**Key relations:**
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)
- related: [noise-types](noise-types.md)
- related: [power-spectral-density](power-spectral-density.md)
- related: [error-analysis](error-analysis.md)

**Discussed in:**
- [Noise and SNR Lecture](../notes/signal-processing/noise-and-snr-lecture.md) — derives √N SNR improvement; coherent vs. incoherent averaging
- [Intro to Signal Processing (Orfanidis)](../notes/signal-processing/intro-signal-processing-orfanidis.md) — averaging as an SNR enhancement technique in digital signal processing
