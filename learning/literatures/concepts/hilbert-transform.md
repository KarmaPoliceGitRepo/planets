# Hilbert Transform
**Aliases:** analytic signal; instantaneous phase; instantaneous frequency; envelope detection

**Definition:** The Hilbert transform of a real signal x(t) is its convolution with 1/(πt), rotating every frequency component by 90°; the complex analytic signal z(t) = x(t) + j·H{x(t)} has a one-sided spectrum. The modulus |z(t)| gives the instantaneous envelope (amplitude), and the angle arg(z(t)) gives the instantaneous phase, whose time derivative is the instantaneous frequency. In ultrasonic ToF estimation, the envelope peak is used instead of the raw-signal peak to remove carrier-frequency dependence; in bearing measurements, instantaneous phase extraction removes contact-stiffness-dependent phase shifts.

**Key relations:**
- related: [hilbert-huang-transform](hilbert-huang-transform.md)
- related: [time-of-flight](time-of-flight.md)
- related: [cross-correlation](cross-correlation.md)
- related: [phase-unwrapping](phase-unwrapping.md)
- related: [fast-fourier-transform](fast-fourier-transform.md)

**Discussed in:**
- [Hilbert Transform notes (Coffee Morning)](../notes/signal-processing/hilbert-transform-notes-coffee-morning.md) — tutorial derivation of the analytic signal and instantaneous amplitude/phase
- [ToF Interpolation Techniques (Svilainis)](../notes/signal-processing/tof-interpolation-techniques-svilainis.md) — uses Hilbert envelope peak for sub-sample ToF precision
- [Baseline Signal Reconstruction — Temperature Compensation](../notes/signal-processing/baseline-signal-reconstruction-temperature-compensation.md) — instantaneous phase used in temperature-compensation signal processing
