# Analysis of the Interpolation Techniques for TOF Estimation

- **Source:** Analysis of the Interpolation Techniques for TOF Estimation - (2008) Svilainis, Dumbrava.pdf
- **Drive link:** https://drive.google.com/file/d/17bBgfFpFm8-mHnJkc-hGZ7TpQKVohKOz/view
- **Type:** paper
- **Author/Year:** Svilainis & Dumbrava / 2008
- **Coverage:** full

## Overview
Published in Ultragarsas 63(4), 2008. Analyses and compares three ToF interpolation techniques — parabolic interpolation on the cross-correlation peak, and linear zero-crossing interpolation on both the real signal and its Hilbert transform (imaginary part) — providing analytical error equations and simulation validation.

## Unique contribution
Derives closed-form analytical expressions for the ToF estimation error as a function of sampling frequency ratio, noise, and signal bandwidth for each technique. Shows that x16 resampling (upsampling before interpolation) significantly improves accuracy at low sampling ratios.

## Key concepts
- Time-of-flight (TOF) estimation
- Parabolic interpolation
- Linear zero-crossing interpolation
- Hilbert transform
- Sampling frequency ratio
- Resampling / upsampling
- Analytical error equations

## Methods / results / takeaways
- Three methods compared: (1) parabolic interpolation on the cross-correlation peak, (2) linear interpolation on real zero-crossing, (3) linear interpolation on Hilbert transform zero-crossing.
- Analytical error derived as function of fs/fc (sampling to carrier frequency ratio) and SNR.
- Hilbert transform zero-crossing method performs best at high fs/fc; parabolic interpolation on correlation peak is most robust at lower fs/fc.
- x16 resampling prior to interpolation markedly reduces errors when fs is only 2–4× the signal bandwidth.
- Simulation results match analytical predictions.
- Practical recommendation: use parabolic interpolation when sampling rate is limited; use upsampling + zero-crossing for highest precision.
