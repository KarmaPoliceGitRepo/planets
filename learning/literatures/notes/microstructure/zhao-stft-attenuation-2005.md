# Ultrasonic Attenuation Measurement Using STFT and Its Application in Grain Size Estimation

- **Source:** Zhao - STFT ultrasonic attenuation grain size 2005
- **Drive link:** https://drive.google.com/file/d/1J3NTSep.../view
- **Type:** paper
- **Author/Year:** X. Zhao et al. / 2005
- **Coverage:** full

## Overview
A paper proposing the use of the Short-Time Fourier Transform (STFT) for frequency-dependent attenuation measurement in polycrystalline metals, and applying the resulting attenuation coefficients to estimate grain size via fitting to Rayleigh/stochastic scattering models.

## Unique contribution
Demonstrates that STFT-based time-frequency analysis allows spatially resolved attenuation measurement within a specimen, enabling grain size estimation even in materials with gradual microstructural gradients (e.g., cast materials with columnar grains), unlike conventional single-measurement methods.

## Key concepts
- Short-Time Fourier Transform (STFT)
- Frequency-dependent attenuation
- Rayleigh scattering regime
- Grain size estimation
- Time-frequency analysis
- Polycrystalline metals

## Methods / results / takeaways
- STFT applied to pulse-echo signal: window slides along time axis, FFT computed at each position → spectrogram.
- Attenuation at each frequency estimated from decay rate of spectral amplitude with depth.
- Grain size estimated by fitting α(f) = A·f⁴ (Rayleigh) or α(f) = B·f² (stochastic) to extracted attenuation.
- Applied to cast aluminum with inhomogeneous grain structure; spatially varying grain size maps obtained.
- Results show ~15% agreement with metallographic measurements; columnar grain regions identified.
- Window length tradeoff: shorter windows give better spatial resolution but poorer frequency resolution; optimal window ~3–5 wavelengths.
- Beam spreading correction still required; diffraction correction applied using Papadakis model.
