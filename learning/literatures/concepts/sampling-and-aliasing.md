# Sampling and Aliasing
**Aliases:** Nyquist sampling theorem; Nyquist rate; aliasing; anti-aliasing; oversampling; delta-sigma modulation; noise shaping; subsampling; equivalent time sampling; sampling interval

**Definition:** The Nyquist–Shannon sampling theorem states that a band-limited signal with maximum frequency f_max must be sampled at f_s ≥ 2 f_max to allow exact reconstruction; frequencies above f_s/2 alias (fold back) and corrupt lower-frequency content. Oversampling (f_s ≫ 2 f_max) spreads quantisation noise over a wider band; combining it with noise-shaping (delta-sigma modulation) pushes that noise out of the signal band and, after decimation, achieves resolution beyond the raw ADC word length. Equivalent-time sampling reconstructs a repetitive waveform from multiple trigger-synchronised samples, effectively multiplying the apparent sample rate. In surface metrology, the sampling interval Δx must satisfy Nyquist relative to the shortest surface wavelength of interest.

**Key relations:**
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [spectral-leakage-and-windowing](spectral-leakage-and-windowing.md)
- related: [digital-filters](digital-filters.md)
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)

**Discussed in:**
- [LabVIEW DSP and Digital Communications](../notes/matlab-and-labview/labview-dsp-digital-communications.md) — Nyquist criterion, oversampling, delta-sigma, subsampling receiver architectures
- [Intro to Signal Processing (Orfanidis)](../notes/signal-processing/intro-signal-processing-orfanidis.md) — formal derivation of sampling theorem; aliasing examples; noise shaping
- [Digital Signal Processing Textbook 2017](../notes/signal-processing/digital-signal-processing-textbook-2017.md) — ADC quantisation noise, oversampling gain
