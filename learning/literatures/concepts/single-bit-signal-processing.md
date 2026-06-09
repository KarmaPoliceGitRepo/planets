# Single-Bit Signal Processing
**Aliases:** single-bit signal processing; one-bit quantization; binary signal processing; delta-sigma; PRBS; single-bit cross-correlation

**Definition:** Single-bit signal processing quantises the analogue signal to ±1 at high clock rates, performing all arithmetic with XOR gates and counters rather than multipliers. Cross-correlation is computed as XNOR (logical equivalence) followed by counting; the peak of the binary cross-correlation function gives the time delay. This approach reduces hardware cost dramatically and enables very high sample rates in embedded systems. Accuracy degrades gracefully compared to multi-bit schemes; the SNR loss is approximately π/4 (−1 dB) for Gaussian noise.

**Key relations:**
- related: [cross-correlation](cross-correlation.md)
- related: [sampling-and-aliasing](sampling-and-aliasing.md)
- related: [time-of-flight](time-of-flight.md)

**Discussed in:**
- [Single-Bit Cross-Correlation Ultrasonic](../notes/signal-processing/single-bit-cross-correlation-ultrasonic.md) — hardware implementation and accuracy analysis of one-bit cross-correlation for ultrasonic ToF; SNR comparison with 8-bit reference
