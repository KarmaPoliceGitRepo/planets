# Ultrasonic Frequency Analysis

**Aliases:** pulse spectrum analysis; ultrasonic spectroscopy; RF spectrum analysis; frequency-domain ultrasonic analysis

**Definition:** Ultrasonic frequency analysis is the examination of ultrasonic echoes or transmitted signals in the frequency domain via Fourier transform. The frequency spectrum of a pulse-echo signal encodes material attenuation (spectral amplitude decay), thin-layer resonances (periodic dips or peaks), transducer bandwidth, and bond quality. Key metrics extracted: centre frequency, −6 dB bandwidth, spectral ratio (for attenuation coefficient), and spectral peaks/dips (for layer thickness). Gate width and shape affect the spectral resolution and leakage; the STAMINA and frequency-tracking methods are implementations that exploit frequency-domain resonances.

**Key relations:**
- [stamina-method](stamina-method.md) — STAMINA is a frequency-sweep implementation
- [frequency-tracking-technique](frequency-tracking-technique.md) — frequency-tracking uses spectral peak position
- [fast-fourier-transform](fast-fourier-transform.md) — FFT is the computational tool
- [resonant-frequency](resonant-frequency.md) — spectral peaks correspond to resonances

**Discussed in:**
- [Ultrasonic Spectrum Analysis Frequency-Tracked RF](../notes/method-resonance/ultrasonic-spectrum-analysis-frequency-tracked-rf.md) — echo gating, spectral analysis, frequency-tracking implementation
