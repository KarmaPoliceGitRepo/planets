# A Review of Image Denoising Algorithms, with a New One

- **Source:** A review of image denoising algorithms with a new one.pdf
- **Drive link:** https://drive.google.com/file/d/1BiyafXH-AfcHTZGN_fmS6slHITzHBgrU/view
- **Type:** paper
- **Author/Year:** Buades, Coll & Morel / 2005
- **Coverage:** partial (large file, truncated extraction)

## Overview
A comprehensive review paper (likely Multiscale Modeling & Simulation, 2005) surveying classical and modern image denoising algorithms including Gaussian filtering, anisotropic diffusion, wavelet thresholding, and total variation methods, culminating in the introduction of the Non-Local Means (NL-Means) algorithm.

## Unique contribution
Introduces the Non-Local Means (NL-Means) denoising algorithm, which averages similar patches found non-locally throughout the entire image (not just spatial neighbours), demonstrating superior performance over existing methods while providing a mathematical framework for comparing denoising approaches.

## Key concepts
- Image denoising
- Gaussian filtering
- Anisotropic diffusion (Perona-Malik)
- Total Variation (TV) denoising (Rudin-Osher-Fatemi)
- Wavelet thresholding (hard/soft)
- Non-Local Means (NL-Means)
- Patch similarity
- PSNR (Peak Signal-to-Noise Ratio)
- Neighbourhood filtering

## Methods / results / takeaways
- Gaussian filtering: convolution with Gaussian kernel; blurs edges.
- Anisotropic diffusion: PDEbased; diffuses parallel to edges but not across them; preserves edges better than Gaussian.
- TV denoising: minimises total variation subject to data fidelity; produces piecewise-smooth results; excellent for cartoon-like images.
- Wavelet thresholding: DWT + threshold detail coefficients; VisuShrink, BayesShrink methods; effective for spatially smooth signals.
- NL-Means: weight w(i,j) based on patch similarity between pixel i and j; denoised pixel = Σ_j w(i,j) x(j); exploits non-local self-similarity.
- NL-Means outperforms all reviewed methods quantitatively (PSNR) and visually, especially for textured images.
- Unifying framework provided: all algorithms can be interpreted as weighted local averages with different weight functions.
