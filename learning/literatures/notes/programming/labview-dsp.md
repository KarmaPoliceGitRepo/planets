# LabVIEW Digital Signal Processing and Digital Communications

- **Source:** Cory Clark - LabVIEW Digital Signal Processing-McGraw-Hill Professional (2005).pdf
- **Drive link:** https://drive.google.com/file/d/1M86LM6jm2PEKcn2bgwVQD54X7nM6CuF6/view?usp=drivesdk
- **Type:** book
- **Author/Year:** Cory L. Clark (Motorola) / 2005
- **Coverage:** partial (large file, truncated extraction)

## Overview
A practical McGraw-Hill guide for engineers who already know both LabVIEW and DSP theory, bridging the gap between textbook knowledge and real implementation. The book walks through getting analog signals into LabVIEW via conventional and subsampling receivers, building DSP blocks (spectral analysis, digital filters, signal generation), and assembling a complete digital communication system inside LabVIEW.

## Unique contribution
Focuses specifically on digital communications applications of LabVIEW DSP — not just signal processing in isolation. It covers subsampling receiver architecture (a less common but hardware-efficient technique), multirate signal processing, and NI's Modulation Toolset. The appendix provides a reference of all custom Virtual Instruments (VIs) developed in the book.

## Key concepts
- Virtual Instrument (VI)
- Conventional vs. subsampling digital receiver architectures
- Subsampling SNR and signal placement
- FFT (Fast Fourier Transform), DFT
- Spectral leakage, windowing
- FIR filter design (windowing method, equiripple)
- IIR filter design
- FIR vs. IIR comparison (phase response, magnitude)
- Pulse-shaping filter
- Upsampling, downsampling, resampling
- Halfband filters, polyphase filters
- Rayleigh fading channel model
- White Gaussian noise generation
- Modulator and demodulator design
- Channel impairments
- Matched filter detection
- Threshold decisions
- Time and frequency synchronization
- NI Modulation Toolset
- Bit error rate (BER) measurement
- Error vector magnitude (EVM)
- Channel estimation and coding
- Viterbi decoder
- Linear convolution via FFT
- Linear predictive speech coder
- CompactDAQ, PXI hardware interfaces
- Soundcard as sampling device

## Methods / results / takeaways
- Subsampling can capture bandpass signals at rates below Nyquist for the carrier frequency, reducing hardware cost; SNR degradation must be carefully characterized.
- Spectral leakage from finite-length signals is mitigated by window functions (Hann, Hamming, Kaiser); choice of window involves a trade-off between main-lobe width and sidelobe level.
- Equiripple (Parks-McClellan) FIR filters achieve optimal transition-band steepness for a given filter length; IIR filters are more compact but introduce phase nonlinearity.
- Polyphase decomposition enables efficient multirate filtering by reducing the number of multiplications compared to a direct resampling approach.
- BER vs. Eb/N0 curves are the standard performance metric for digital communication systems; the book shows how to measure these inside LabVIEW.
- Adding C routines to LabVIEW via DLL calls is covered for compute-intensive DSP tasks.
