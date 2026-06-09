# Wavelets for Kids

- **Source:** WAVELETS FOR KIDS.pdf
- **Drive link:** https://drive.google.com/file/d/1OFWTfgGGJufWYaLYrMZBZy0DN3LdnL_2/view
- **Type:** notes
- **Author/Year:** Vidakovic & Mueller (Duke University) / undated (1990s)
- **Coverage:** full

## Overview
An accessible tutorial introduction to wavelet theory aimed at advanced undergraduates, covering Haar wavelets, Mallat's multiresolution analysis, filter bank implementation, thresholding for denoising, and image processing applications, with a MATLAB/Mathematica code appendix.

## Unique contribution
Bridges the gap between abstract wavelet theory and practical computation: uses the Haar wavelet as a concrete entry point, then generalises to Daubechies wavelets; covers multiple thresholding strategies (universal, SURE, cross-validation) and shows image compression/denoising examples with code.

## Key concepts
- Haar wavelet
- Daubechies wavelets
- Multiresolution analysis (MRA)
- Filter banks (H/G operators, low-pass / high-pass)
- Mallat algorithm
- Discrete wavelet transform (DWT)
- Hard thresholding, soft thresholding
- Universal threshold (VisuShrink), SURE threshold, cross-validation threshold
- Image compression, image denoising
- Wavelet packet

## Methods / results / takeaways
- Haar wavelet: simplest orthogonal wavelet; piecewise constant; DWT via averaging and differencing.
- Mallat MRA: signal decomposed via iterated two-channel filter bank (H = smoothing, G = differencing); downsampling at each level gives approximation and detail coefficients.
- Reconstruction (IDWT): upsampling and filtering with time-reversed (synthesis) filters.
- Daubechies wavelets: compact support, higher vanishing moments than Haar; better frequency selectivity.
- Thresholding for denoising: apply threshold to detail coefficients; hard threshold sets small coefficients to zero; soft threshold shrinks by threshold amount.
- Universal threshold: λ = σ√(2 log N); works well in practice for white Gaussian noise.
- SURE (Stein's Unbiased Risk Estimate) threshold: data-adaptive; minimises estimated risk.
- Image applications: 2D DWT applied separably; thresholding detail subbands denoises while preserving edges.
- Mathematica and MATLAB code for DWT/IDWT included.
