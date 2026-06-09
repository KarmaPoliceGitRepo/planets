# Time of Flight
**Aliases:** ToF; TOF; time-of-flight measurement; time delay estimation; cross-correlation TOF; pulse-echo TOF; TOFD; time-of-flight diffraction; vernier principle; parabolic interpolation

**Definition:** Time of flight is the elapsed time between transmission and reception of a pulse (or a chosen feature of its waveform), used to measure distances, layer thicknesses, or material velocity. In ultrasonic systems the propagation velocity v relates distance d to round-trip ToF by d = v·t/2. Sub-sample precision (beyond the digitiser resolution Δt) is achieved by interpolation: parabolic interpolation fits a three-point parabola to the cross-correlation or envelope peak; the Hilbert-transform envelope peak, zero-crossing, and phase-slope methods are alternatives. The Cramér–Rao Lower Bound gives the theoretical minimum variance in ToF estimation. Time-of-Flight Diffraction (TOFD) is a pulse-echo technique that locates defects from diffracted tip signals. The vernier principle encodes delay in the beat frequency between two slightly different frequencies to give fine resolution with coarse measurement.

**Key relations:**
- related: [cross-correlation](cross-correlation.md)
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)
- related: [hilbert-transform](hilbert-transform.md)
- related: [phase-unwrapping](phase-unwrapping.md)
- related: [temperature-compensation](temperature-compensation.md)
- related: [sampling-and-aliasing](sampling-and-aliasing.md)

**Discussed in:**
- [Digital ToF Ultrasonic (Marioli)](../notes/signal-processing/digital-tof-ultrasonic-marioli.md) — systematic comparison of threshold, zero-crossing, and cross-correlation ToF algorithms with digitisation noise analysis
- [ToF Interpolation Techniques (Svilainis)](../notes/signal-processing/tof-interpolation-techniques-svilainis.md) — parabolic, Hilbert, and polynomial interpolation methods for sub-sample ToF
- [ToF Accuracy and Digitisation (Svilainis)](../notes/signal-processing/tof-accuracy-digitization-svilainis.md) — quantitative accuracy limits imposed by digitiser resolution and sampling jitter
- [TOFD Neural-Network Defect Detection](../notes/signal-processing/tofd-neural-network-defect.md) — TOFD signal interpretation using machine learning
- [Multifrequency AM Ultrasonic Ranging](../notes/signal-processing/multifrequency-am-ultrasonic-ranging.md) — AM-phase and vernier ranging principles for absolute distance measurement
