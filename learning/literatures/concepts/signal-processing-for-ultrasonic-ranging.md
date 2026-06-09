# Signal Processing for Ultrasonic Ranging
**Aliases:** ultrasonic ranging; AM ranging; amplitude modulation ranging; multifrequency ranging; vernier principle; gated FFT; B-scan imaging; compound resonator; bond layer effect

**Definition:** Ultrasonic ranging measures absolute distance by measuring the round-trip ToF of a transmitted pulse or tone-burst. For sub-wavelength precision without phase ambiguity, the vernier principle uses the beat between two closely spaced frequencies; multifrequency AM ranging encodes distance in the phase of the modulation envelope across several carrier frequencies. A gated FFT windows a short portion of a time trace before FFT to isolate a specific echo in time. The bond layer effect refers to the phase shift introduced by coupling layers (glue, grease) that must be corrected for accurate ToF. Compound resonators are coupled piezo-mechanical systems that shift the resonance to a desired frequency.

**Key relations:**
- related: [time-of-flight](time-of-flight.md)
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [spectral-leakage-and-windowing](spectral-leakage-and-windowing.md)
- related: [phase-unwrapping](phase-unwrapping.md)

**Discussed in:**
- [Multifrequency AM Ultrasonic Ranging](../notes/signal-processing/multifrequency-am-ultrasonic-ranging.md) — multifrequency AM phase ranging; vernier principle; absolute distance measurement without phase ambiguity
- [Resonance Spectrum FFT of Elastic Bodies](../notes/signal-processing/resonance-spectrum-fft-elastic-bodies.md) — gated FFT and compound resonator theory for resonance-based ranging
