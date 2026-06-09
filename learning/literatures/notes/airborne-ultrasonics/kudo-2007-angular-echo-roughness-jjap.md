# Measurement of Angular Dependence of Ultrasonic Echo for Estimation of Surface Roughness

- **Source:** Kudo 2007 angular echo roughness JJAP
- **Drive link:** https://drive.google.com/file/d/1hUBaqXZgKL92_evc4O6nMwR2Aw1Pv2J6/view
- **Type:** paper
- **Author/Year:** Kudo, Hasegawa & Kanai, 2007 (Japanese Journal of Applied Physics, 46(7B), 4873–4880)
- **Coverage:** full

## Overview
Full journal paper expanding the 2006 conference results. Measures angular dependence of 10 MHz ultrasonic echo from micron-order steps and gaps in aluminium, and from sandpaper surfaces (Rq = 0.2–4.1 μm), using phased-array beam steering (up to ±32.6°, l = 9.4 mm). Shows that the normalised power P(θ)/P(0°) increases monotonically with Rq for θ ≥ 20°. Introduces an unequally-spaced 2D DFT to compute the spatial-frequency spectrum of the angular echo distribution. Gap geometry is modelled by superposition of step responses.

## Unique contribution
Full quantitative development of the two-domain (angular amplitude + 2D Fourier) characterisation of micron-order surface roughness using phased-array beam steering in water. Proves that P(θ)/P(0°) at θ ≥ 20° is a monotone roughness estimator for Rq = 0.2–4.1 μm. Derives unequally-spaced DFT for non-uniform beam-angle sampling. Gap superposition model validated by comparison with measured angular patterns.

## Key concepts
- Angular dependence of ultrasonic echo
- Electronic beam steering, phased array
- 10 MHz water-immersion measurement
- Normalised power P(θ)/P(0°) as roughness metric
- Unequally-spaced discrete Fourier transform (DFT)
- 2D spatial-temporal power spectrum of RF echo
- Step and gap specimens (d = 35, 57, 90 μm; gap depth 30–64 μm, width 60–122 μm)
- Sandpaper specimens Rq = 0.206–4.131 μm
- Atherosclerosis / arterial wall roughness motivation
- Gap superposition principle

## Methods / results / takeaways
- Probe: Aloka SSD-6500, 10 MHz linear array; L = 0.4 mm; N = 30 beams per frame; 40 MHz sampling, 16-bit; stage scans at 2.17 mm/s, 5 μm/frame.
- Beam steering: all beams pass through point Oj; max angle θmax = 32.6° at l = 9.4 mm; θ = 24.3° at l = 13.7 mm.
- Unequally-spaced DFT: twiddle factor W(i) = exp[−j2π(Σₙ Δθₙ)/Θ] to handle non-uniform angle spacing.
- Step results: wavefront distortion at step position; echo number of cycles increases with d; 2D FFT center-frequency band narrows in temporal domain with d.
- Gap results: echo amplitude in |θ| ≥ 15° increases as gap width w increases; gap modelled by superposition of two steps — simulated pattern matches measurement.
- Sandpaper results (Rq = 0.206–4.131 μm): P(θ)/P(0°) at θ ≥ 20° increases monotonically with Rq — clear separation between all 4 roughness classes.
- Quantitative relationship: Fig. 23 — P(θ)/P(0°) vs. Rq at θ = 20°, 25°, 30° are all monotone increasing; larger θ gives larger dynamic range.
- Limitation: absolute calibration not provided; no theoretical model fitted to P(θ)/P(0°) vs. Rq; requires reference smooth surface (P(0°) measurement).
