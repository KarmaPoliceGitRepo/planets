# Angular Dependence of Ultrasonic Echo in Frequency Domain for Measurement of Surface Roughness

- **Source:** Kudo 2006 angular echo frequency domain
- **Drive link:** https://drive.google.com/file/d/1oNZg-3HADuthXs-QFNFhzZPZsGd9T1yu/view
- **Type:** paper
- **Author/Year:** Kudo, Hasegawa & Yamamoto, 2006 (conference proceedings, Tohoku University group)
- **Coverage:** full

## Overview
Extends angular echo roughness measurement into the 2D spatial frequency domain. A 10 MHz probe steers the beam to multiple angles; the spatial distribution of echo amplitudes is processed by 2D Fourier transform. Applied to step-height specimens (0, 35, 57, 90 μm single steps). The spatial frequency at which the angular spectrum peaks increases with step height, providing a quantitative roughness signature in the frequency domain rather than just an amplitude ratio.

## Unique contribution
Introduces 2D Fourier analysis of the angular echo distribution for surface roughness characterisation — moving beyond simple P(θ)/P(0°) ratios to a full spectral description. Shows that step-height geometry produces a specific spatial-frequency peak whose position encodes the height, potentially enabling single-frequency inversion rather than angle-sweep calibration. Precursor / companion to Hasegawa 2007 (angular dependence in amplitude domain).

## Key concepts
- 2D Fourier transform of angular echo distribution
- Spatial frequency of echo vs. step height
- 10 MHz ultrasonic probe beam steering
- Step-height specimens (0, 35, 57, 90 μm)
- Spatial echo distribution analysis
- Surface roughness frequency-domain characterisation
- Water-immersion measurement
- Relationship between echo spatial frequency and surface height

## Methods / results / takeaways
- Probe: 10 MHz (same Aloka-type setup as Hasegawa 2007); water immersion; beam steered to multiple angles.
- Specimens: flat plates with machined single steps of 0, 35, 57, 90 μm depth; step width large relative to beam.
- Processing: angular echo amplitude vs. beam angle θ treated as 1D spatial signal; 2D Fourier transform computed.
- Result: spatial frequency of the dominant peak in the angular spectrum increases monotonically with step height; 0 μm (flat) has narrow peak at low spatial freq; 90 μm step produces higher spatial-frequency peak.
- Physical interpretation: deeper steps create finer angular interference fringes (shorter spatial period) in the echo pattern → higher spatial frequency in the 2D FFT.
- Potential inversion: measure peak spatial frequency → infer step height without full angular scan calibration.
- Limitation: step geometry (single, regular) differs from random roughness; extension to random surfaces requires statistical spatial-frequency treatment; conference paper — limited validation.
- Connection: complements Hasegawa 2007 which uses amplitude-domain P(θ)/P(0°); together they form a multi-modal angular-echo roughness measurement framework.
