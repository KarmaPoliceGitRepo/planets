# Cross-Correlation
**Aliases:** cross-correlation ToF estimation; conjugate multiplication; cross-correlation velocity measurement; correlation; cross-spectrum

**Definition:** Cross-correlation R_xy(τ) = ∫ x(t) y(t+τ) dt measures the similarity between two signals as a function of time lag τ; its peak locates the time delay between them. In the frequency domain it equals conjugate multiplication X*(f)·Y(f), making it computable via FFT in O(N log N). For ToF estimation in ultrasound, the delay between successive echoes is found at the peak of the cross-correlation; sub-sample precision is obtained by parabolic interpolation or Hilbert-transform envelope fitting. The Cramér–Rao Lower Bound sets the theoretical minimum variance achievable for time-delay estimation from a cross-correlation.

**Key relations:**
- related: [time-of-flight](time-of-flight.md)
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)
- related: [hilbert-transform](hilbert-transform.md)
- related: [power-spectral-density](power-spectral-density.md)

**Discussed in:**
- [Single-Bit Cross-Correlation Ultrasonic](../notes/signal-processing/single-bit-cross-correlation-ultrasonic.md) — one-bit quantization scheme retaining cross-correlation peak for fast ToF measurement
- [Digital ToF Ultrasonic (Marioli)](../notes/signal-processing/digital-tof-ultrasonic-marioli.md) — cross-correlation as the reference ToF algorithm; comparison with threshold and zero-crossing methods
- [ToF Interpolation Techniques (Svilainis)](../notes/signal-processing/tof-interpolation-techniques-svilainis.md) — interpolation methods applied after cross-correlation peak finding
