# Digital Filters
**Aliases:** FIR filter; IIR filter; finite impulse response; infinite impulse response; Butterworth filter; Chebyshev filter; Bessel filter; polyphase filter; polyphase filter bank; multirate signal processing; inverse filter; ARMA model

**Definition:** A digital filter processes a discrete-time sequence to modify its spectral content. FIR (Finite Impulse Response) filters have a finite-length impulse response; when symmetric, they provide exact linear (constant group-delay) phase; they are always stable. IIR (Infinite Impulse Response) filters include feedback and can achieve steep roll-off with fewer coefficients than FIR, but introduce non-linear phase and can become unstable; classic designs (Butterworth, Chebyshev, Bessel, elliptic) are derived from analogue prototypes via bilinear transform. An inverse filter deconvolves the system response from measured signals. Polyphase filter banks split a signal into sub-band channels; combined with decimation, they implement multirate signal processing. The ARMA (AutoRegressive Moving Average) model is the general parametric form of an IIR filter and is used for system identification.

**Key relations:**
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [sampling-and-aliasing](sampling-and-aliasing.md)
- related: [laplace-and-z-transform](laplace-and-z-transform.md)
- related: [regularisation](regularisation.md)

**Discussed in:**
- [Intro to Signal Processing (Orfanidis)](../notes/signal-processing/intro-signal-processing-orfanidis.md) — FIR and IIR design methods; window-based and equiripple FIR; Butterworth/Chebyshev IIR
- [Digital Signal Processing Textbook 2017](../notes/signal-processing/digital-signal-processing-textbook-2017.md) — filter implementation; direct-form structures; round-off noise
- [Digital Signal & Image Processing (Blanchet)](../notes/signal-processing/digital-signal-image-processing-matlab-blanchet.md) — MATLAB filter design toolbox examples
- [LabVIEW DSP and Digital Communications](../notes/matlab-and-labview/labview-dsp-digital-communications.md) — FIR vs. IIR tradeoffs; polyphase decimation/interpolation filters
- [Compensation Filtering Pulse-Echo](../notes/signal-processing/compensation-filtering-pulse-echo.md) — ARMA system-identification approach to compensate transducer response; inverse filter design
- [LabVIEW DSP](../notes/programming/labview-dsp.md) — FIR and IIR filter VIs in LabVIEW
