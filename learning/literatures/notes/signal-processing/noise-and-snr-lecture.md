# Noise Types and Signal-to-Noise Ratio (Lecture Notes)

- **Source:** Lez_12_Noises.pdf
- **Drive link:** https://drive.google.com/file/d/15Dk0ZgFKsTdsBTh2aiIFbSGV1vdV6oiG/view
- **Type:** slides
- **Author/Year:** Unknown / undated
- **Coverage:** full

## Overview
Lecture slides (Lesson 12) covering signal-to-noise ratio definitions and a taxonomy of noise types encountered in signal processing and electronics, together with ensemble and time-averaging methods for noise reduction.

## Unique contribution
Provides a concise, unified catalogue of noise types (white, pink/1/f, Brownian/red, Gaussian, shot/Poisson, thermal/Johnson, phase, multiplicative, flicker) with their power spectral density characteristics, plus practical hardware noise-reduction tips.

## Key concepts
- Signal-to-noise ratio (SNR, dB)
- White noise, pink noise (1/f), Brownian noise (red/1/f²)
- Gaussian noise, shot noise (Poisson), thermal noise (Johnson-Nyquist)
- Phase noise, multiplicative noise, flicker noise
- Stationary process, ergodic process
- Ensemble averaging, boxcar averaging
- Hardware noise reduction (shielding, grounding, filtering)

## Methods / results / takeaways
- SNR defined as ratio of signal power to noise power; expressed in dB as 20·log10(Vsignal/Vnoise).
- White noise: flat PSD; pink noise: PSD ∝ 1/f (equal power per octave); Brownian noise: PSD ∝ 1/f².
- Gaussian noise: amplitude distribution is Normal; shot noise: arises from discrete charge carriers, Poisson statistics.
- Thermal (Johnson) noise power: P = kTB; depends on temperature and bandwidth.
- Phase noise: random phase fluctuations in oscillators.
- Signal averaging: ensemble average over N repeated trials reduces noise by √N; boxcar (moving average) is time-domain equivalent.
- Hardware mitigation: differential signalling, shielding, low-pass filtering, cooling.
