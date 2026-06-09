# Fast Fourier Transform
**Aliases:** FFT; DFT; Discrete Fourier Transform; split-radix FFT; DTFT; DSP; Digital signal processing; 2D-DFT; 2D-CTFT

**Definition:** The Discrete Fourier Transform (DFT) maps N time-domain samples to N equally spaced complex frequency coefficients via X[k] = Σ x[n] e^{−j2πkn/N}; it is associated with circular (periodic) convolution. The Fast Fourier Transform (FFT) is a family of algorithms that computes the same result in O(N log N) operations rather than O(N²), making large spectral analyses practical. The Discrete-Time Fourier Transform (DTFT) is the FT of a discrete aperiodic sequence, producing a continuous and periodic spectrum. The 2D extension applies the transform along both spatial dimensions and is used in image processing and angular-spectrum field propagation.

**Key relations:**
- related: [fourier-transform](fourier-transform.md)
- related: [spectral-leakage-and-windowing](spectral-leakage-and-windowing.md)
- related: [power-spectral-density](power-spectral-density.md)
- related: [time-of-flight](time-of-flight.md)
- related: [cross-correlation](cross-correlation.md)
- related: [laplace-and-z-transform](laplace-and-z-transform.md)

**Discussed in:**
- [DSP Matlab (Proakis)](../notes/maths/dsp-matlab-proakis.md) — defines DFT, DTFT, and Z-transform; formal treatment of circular convolution
- [2D Fourier Transform notes](../notes/maths/2d-fourier.md) — covers 2D-DFT, DTFT, and Parseval equality
- [Fundamentals of Signal Processing (Sound & Vibration)](../notes/signal-processing/fundamentals-signal-processing-sound-vibration.md) — practical FFT for spectral analysis of vibration data
- [Resonance Spectrum FFT of Elastic Bodies](../notes/signal-processing/resonance-spectrum-fft-elastic-bodies.md) — FFT applied to extract resonance frequencies from elastic-wave signals
- [LabVIEW DSP and Digital Communications](../notes/matlab-and-labview/labview-dsp-digital-communications.md) — FFT implementation details; split-radix algorithm; spectral leakage and windowing in LabVIEW
- [LabVIEW DSP](../notes/programming/labview-dsp.md) — FFT as a LabVIEW built-in VI for frequency-domain analysis
- [Digital Signal Processing Textbook 2017](../notes/signal-processing/digital-signal-processing-textbook-2017.md) — filter and spectral analysis using FFT
