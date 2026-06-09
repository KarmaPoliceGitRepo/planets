# Evaluation of the Angular Spectrum Approach for Simulations of Near-Field Pressures

- **Source:** 2008 - Evaluation of the angular spectrum approach for simulations of near-field pressures - (2008) X Zeng.pdf
- **Drive link:** https://drive.google.com/file/d/1Rpn1ydigDyLn_EEFCAooixthzfGsYqBG/view
- **Type:** paper
- **Author/Year:** X. Zeng, R.J. McGough / 2008 (J. Acoust. Soc. Am. 123, 68–76)
- **Coverage:** full

## Overview
Comparative evaluation of two angular spectrum implementations — spectral propagator (FFT-based) and spatial propagator (direct convolution in space) — for near-field pressure simulations of a square piston source. Analyses aliasing, circular convolution errors, and numerical accuracy in both attenuating and non-attenuating media.

## Unique contribution
Shows that the spatial propagator is 2–4× more accurate than the spectral propagator in the central L×L region (L = D − 2a) for non-attenuating media, while the spectral propagator suffers aliasing near the evanescent-to-propagating boundary. For attenuating media or apodized sources, both methods achieve similar accuracy.

## Key concepts
- Angular spectrum approach (ASA)
- Spectral propagator (FFT)
- Spatial propagator (spatial convolution)
- Aliasing (angular spectrum)
- Circular convolution error
- Near-field pressure simulation
- Square piston transducer
- Attenuating medium
- Apodization

## Methods / results / takeaways
- Test case: 3 cm × 3 cm square piston at 1 MHz.
- **Spectral propagator**: aliasing near kx² + ky² = k²; fixed with angular restriction cutoff kc = k√(D²/2 / (D²/2 + z²)).
- **Spatial propagator**: circular convolution error at edges (width ~a); accurate in central L×L region where L = D − 2a.
- **Non-attenuating media**: spatial propagator 2–4× more accurate in L×L region.
- **Attenuating media or apodized source**: both propagators achieve similar accuracy (evanescent contribution suppressed).
- Computation time: spatial propagator takes 1.1–1.9× longer than spectral for equivalent accuracy.
- Practical recommendation: use spatial propagator for higher accuracy in central region; spectral propagator with angular restriction for speed.
