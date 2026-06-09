# Signal-to-Noise Ratio
**Aliases:** SNR; signal-to-noise; noise floor; Cramér-Rao Lower Bound; CRLB

**Definition:** Signal-to-noise ratio (SNR) is the ratio of signal power to noise power, usually expressed in decibels: SNR = 10 log₁₀(P_signal / P_noise). It governs the precision of time-delay and amplitude measurements: the standard deviation of a cross-correlation ToF estimate scales as σ_τ ∝ 1/(B·√(2·SNR)), where B is the signal bandwidth (Cramér–Rao Lower Bound). In ultrasonic pulse-echo measurements, SNR determines the minimum detectable layer thickness and the achievable velocity precision; it is improved by signal averaging (reduces noise by √N for N uncorrelated records), matched filtering, and bandwidth selection.

**Key relations:**
- related: [cross-correlation](cross-correlation.md)
- related: [time-of-flight](time-of-flight.md)
- related: [signal-averaging](signal-averaging.md)
- related: [noise-types](noise-types.md)
- related: [power-spectral-density](power-spectral-density.md)

**Discussed in:**
- [Noise and SNR Lecture](../notes/signal-processing/noise-and-snr-lecture.md) — derives SNR in dB; relates to Cramér–Rao bound for ToF estimation; discusses Johnson and shot noise floors
- [Digital ToF Ultrasonic (Marioli)](../notes/signal-processing/digital-tof-ultrasonic-marioli.md) — SNR is the primary predictor of ToF algorithm performance
