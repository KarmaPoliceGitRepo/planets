# Hilbert-Huang Transform
**Aliases:** HHT; Empirical Mode Decomposition; EMD; Intrinsic Mode Function; IMF

**Definition:** The Hilbert-Huang Transform (HHT) is a fully data-adaptive time-frequency analysis method for nonlinear, non-stationary signals. It consists of two stages: Empirical Mode Decomposition (EMD), which iteratively extracts Intrinsic Mode Functions (IMFs) — zero-mean oscillatory components that satisfy local symmetry conditions — via the sifting algorithm; followed by Hilbert spectral analysis applied to each IMF to obtain instantaneous amplitude and frequency. Unlike the STFT or wavelet transform, HHT requires no pre-selected basis and resolves instantaneous frequency changes with high temporal resolution.

**Key relations:**
- related: [hilbert-transform](hilbert-transform.md)
- related: [wavelet-transform](wavelet-transform.md)
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [time-of-flight](time-of-flight.md)

**Discussed in:**
- [Hilbert-Huang Transform Intro](../notes/signal-processing/hilbert-huang-transform-intro.md) — introduces EMD algorithm, IMF conditions, and HHT Hilbert spectral analysis
- [Hilbert Transform notes (Coffee Morning)](../notes/signal-processing/hilbert-transform-notes-coffee-morning.md) — comparison of HHT with classical Hilbert transform; practical notes on mode-mixing
