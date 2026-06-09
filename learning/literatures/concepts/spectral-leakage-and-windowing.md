# Spectral Leakage and Windowing
**Aliases:** window function; windowing; Hanning window; Hamming window; Blackman-Harris window; scalloping loss; spectral leakage; aperture weighting

**Definition:** Spectral leakage occurs when a signal is not exactly periodic within the observation window: energy from a frequency component not aligned to a DFT bin spreads into neighbouring bins. Multiplying the time-domain record by a window function (Hann, Hamming, Blackman-Harris, flat-top, etc.) tapers the record to zero at its edges, trading a wider main lobe for strongly reduced side-lobe levels. Scalloping loss is the maximum amplitude error (typically 1.4 dB for a Hann window) that occurs when the true frequency lies between bins. The window choice is a bias-variance trade-off: flat-top windows minimise amplitude error; Kaiser-Bessel windows allow adjustable sidelobe suppression.

**Key relations:**
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [power-spectral-density](power-spectral-density.md)
- related: [sampling-and-aliasing](sampling-and-aliasing.md)
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)

**Discussed in:**
- [LabVIEW DSP and Digital Communications](../notes/matlab-and-labview/labview-dsp-digital-communications.md) — window types, scalloping loss table, and FFT bin resolution rules
- [Intro to Signal Processing (Orfanidis)](../notes/signal-processing/intro-signal-processing-orfanidis.md) — theory of windowed DFT; DTFT of window functions
- [Fundamentals of Signal Processing (Sound & Vibration)](../notes/signal-processing/fundamentals-signal-processing-sound-vibration.md) — practical windowing in vibration spectrum analysis
