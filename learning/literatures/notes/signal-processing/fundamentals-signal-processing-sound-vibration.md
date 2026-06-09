# Fundamentals of Signal Processing for Sound and Vibration Engineers

- **Source:** Fundamentals of Signal Processing for Sound and Vibration Engineers.pdf
- **Drive link:** https://drive.google.com/file/d/1SRqOnxe3_hhY82PJPBOOa9gUuxlYDzC1/view
- **Type:** book
- **Author/Year:** Unknown (textbook) / undated
- **Coverage:** partial (large file, truncated extraction)

## Overview
A textbook covering signal processing fundamentals specifically for sound and vibration engineering applications, including digital signal representation, spectral analysis, filter design, random signal analysis, and correlation methods.

## Unique contribution
Application-focused treatment of DSP with emphasis on acoustic and vibration signals, bridging mathematical signal processing theory with practical measurement and analysis scenarios in acoustics and structural dynamics.

## Key concepts
- Discrete Fourier Transform (DFT), FFT
- Power spectral density (PSD)
- Windowing (Hanning, Hamming, flat-top)
- Leakage, aliasing
- FIR and IIR digital filters
- Correlation function
- Random signals, stationarity
- Octave-band analysis
- Transfer function estimation (H1, H2 estimators)
- Coherence

## Methods / results / takeaways
- DFT/FFT: transforms discrete time-domain sequences to frequency domain; frequency resolution = fs/N.
- Windowing reduces spectral leakage at the cost of reduced frequency resolution; Hanning window commonly used.
- Aliasing: signals above Nyquist frequency (fs/2) alias to lower frequencies; anti-aliasing filters required.
- PSD estimation: Welch method uses overlapping windowed segments and averages their periodograms.
- Correlation: autocorrelation reveals periodicity; cross-correlation identifies time delay between signals.
- H1/H2 FRF estimators: H1 minimises output noise; H2 minimises input noise; coherence γ² = |H1/H2| indicates noise level.
- Octave-band analysis: logarithmic frequency bands; standard in acoustic noise measurements.
