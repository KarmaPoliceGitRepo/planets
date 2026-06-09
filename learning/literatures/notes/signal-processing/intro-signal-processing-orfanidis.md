# Introduction to Signal Processing

- **Source:** Signal processing - Rutgers University book
- **Drive link:** https://drive.google.com/file/d/1kbUQPdDv2nO2glcm1AA4cUiaM8lTInQh/view
- **Type:** book
- **Author/Year:** Sophocles J. Orfanidis (Rutgers University) / 2010 (originally Prentice Hall 1996)
- **Coverage:** partial (large file, truncated extraction)

## Overview
A comprehensive DSP textbook by Orfanidis covering sampling and reconstruction, quantisation, discrete-time systems, FIR and IIR filter design, spectral analysis (DFT, FFT, STFT), multirate signal processing, adaptive filtering, and array signal processing. Available freely from Rutgers.

## Unique contribution
A complete, mathematically rigorous DSP textbook with extensive coverage of both design theory and MATLAB implementation. Particularly strong on quantisation, oversampling, and noise shaping; covers multirate processing (polyphase filters, filter banks) and adaptive algorithms (LMS, RLS).

## Key concepts
- Sampling and reconstruction, Nyquist theorem
- Quantisation, oversampling, noise shaping, delta-sigma
- Discrete-time systems (FIR, IIR), LTI
- Convolution (block, sample-by-sample, overlap-add)
- Filter design (Parks-McClellan, Butterworth, Chebyshev, elliptic)
- DFT, FFT, STFT, short-time Fourier transform
- Spectral analysis, windowing
- Multirate processing, polyphase filters
- Adaptive filtering (LMS, RLS)
- Array processing

## Methods / results / takeaways
- Chapter 1: sampling, aliasing, Nyquist; Chapter 2: quantisation noise, oversampling, noise shaping (delta-sigma), D/A and A/D converters.
- Chapter 3: discrete-time systems; Chapter 4: FIR filtering, convolution, overlap-add; Chapter 5+: IIR filters.
- Quantisation noise model: uniform, white, variance = Δ²/12.
- Oversampling by factor M reduces in-band quantisation noise by 10 log10(M) dB; noise shaping improves this further.
- DFT: Chapters cover DFT properties, FFT algorithms, fast convolution; STFT for time-frequency analysis.
- Adaptive filtering: LMS (steepest descent, gradient-based), RLS (exact least-squares, exponential forgetting).
