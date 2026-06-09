# The TOF Estimation Accuracy Versus Digitisation Parameters

- **Source:** The TOF Estimation Accuracy Versus Digitization Parameters - Svilainis, Dumbrava.pdf
- **Drive link:** https://drive.google.com/file/d/1nV65q8F69nyqFjeMjwAzj9yJZitXJICJ/view
- **Type:** paper
- **Author/Year:** Svilainis & Dumbrava / 2008
- **Coverage:** full

## Overview
Published in Ultragarsas 63(1), 2008. Provides a Cramér-Rao Lower Bound (CRLB) based analysis of how digitisation parameters — sampling frequency, ADC resolution, signal bandwidth, and carrier frequency — jointly affect the achievable accuracy of ToF estimation.

## Unique contribution
Uses CRLB as a theoretical minimum error bound for ToF estimation under various digitisation scenarios, identifying the critical interplay between sampling frequency and ADC resolution. Shows that parabolic interpolation achieves near-CRLB performance when sampling frequency exceeds twice the noise-signal PSD interception frequency.

## Key concepts
- Cramér-Rao Lower Bound (CRLB)
- TOF estimation accuracy
- Sampling frequency
- ADC resolution (number of bits)
- Signal bandwidth
- Carrier frequency
- Parabolic interpolation

## Methods / results / takeaways
- CRLB for ToF: σ²_ToF ≥ 1/(SNR · 8π² · f_eff²) where f_eff is the effective (RMS) frequency of the signal.
- ADC resolution affects dynamic range and therefore SNR; each additional bit adds ~6 dB SNR.
- Carrier frequency: higher carrier gives larger f_eff and lower CRLB (potentially more accurate ToF).
- Bandwidth: broader signal bandwidth improves resolution (larger effective frequency).
- Sampling frequency must satisfy Nyquist; oversampling below the noise-signal PSD crossing offers diminishing returns.
- Key finding: parabolic interpolation on the correlation peak performs at or near CRLB when fs > 2 × f_intersection (where noise PSD crosses signal PSD).
- Below this threshold, the interpolation error dominates the CRLB.
