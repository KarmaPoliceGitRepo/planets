# Wavelet Transform
**Aliases:** wavelet transform; discrete wavelet transform; DWT; Daubechies wavelets; Haar wavelet; multiresolution analysis; MRA; Intrinsic Mode Function; SURE threshold; universal threshold; hard thresholding; soft thresholding; Non-Local Means; Orthogonal Matching Pursuit; sparse representation; P-wave arrival picking; AIC picker

**Definition:** The wavelet transform decomposes a signal into contributions from translated and dilated copies of a mother wavelet, providing simultaneous time and frequency localisation (unlike the STFT whose window width is fixed). Multiresolution analysis (MRA) is the framework in which discrete wavelet bases (Haar, Daubechies, etc.) provide orthogonal decompositions; the DWT splits a signal into approximation and detail coefficients via successive filtering and downsampling. Wavelet shrinkage denoising applies a threshold to detail coefficients: hard thresholding zeros all coefficients below the threshold; soft thresholding additionally shrinks remaining coefficients toward zero. The SURE threshold (Stein's Unbiased Risk Estimator) and the universal threshold (√(2 log N) σ) are standard choices. Orthogonal Matching Pursuit and related greedy methods select sparse wavelet representations.

**Key relations:**
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [hilbert-huang-transform](hilbert-huang-transform.md)
- related: [regularisation](regularisation.md)
- related: [time-of-flight](time-of-flight.md)
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)

**Discussed in:**
- [Wavelets for Kids](../notes/signal-processing/wavelets-for-kids.md) — accessible introduction to MRA, Haar wavelet, and DWT; filter-bank interpretation
- [Wavelet Cortical Bone Thickness](../notes/signal-processing/wavelet-cortical-bone-thickness.md) — DWT applied to ultrasonic signals for cortical bone thickness estimation; SURE thresholding
- [P-Wave Arrival (Multiscale Wavelet)](../notes/signal-processing/p-wave-arrival-multiscale-wavelet.md) — multiscale wavelet modulus maxima for automatic seismic phase picking; AIC-picker comparison
- [Image Denoising Algorithms Review](../notes/signal-processing/image-denoising-algorithms-review.md) — wavelet shrinkage (hard/soft threshold), Non-Local Means, anisotropic diffusion compared
