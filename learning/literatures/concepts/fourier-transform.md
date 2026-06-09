# Fourier Transform
**Aliases:** CTFT; continuous-time Fourier transform; Fourier series; Parseval equality; Plancherel equality; Gibbs phenomenon; circular convolution

**Definition:** The continuous-time Fourier transform (CTFT) decomposes a signal x(t) into a continuous spectrum X(f) = ∫ x(t) e^{−j2πft} dt; convolution in time equals pointwise multiplication in frequency. For periodic signals, the Fourier series represents the function as a discrete sum of harmonics; truncating this sum produces the Gibbs phenomenon (ringing near discontinuities). Parseval's theorem states that total energy is conserved between time and frequency domains. Circular convolution arises when the DFT is used for convolution without zero-padding and corresponds to wrap-around aliasing.

**Key relations:**
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [laplace-transform](laplace-transform.md)
- related: [spectral-leakage-and-windowing](spectral-leakage-and-windowing.md)
- related: [power-spectral-density](power-spectral-density.md)
- related: [hilbert-transform](hilbert-transform.md)

**Discussed in:**
- [2D Fourier Transform notes](../notes/maths/2d-fourier.md) — defines CTFT, DFT, DTFT, and Parseval / Plancherel equality; treats circular convolution
- [Kreyszig Advanced Engineering Mathematics](../notes/maths/kreyszig-advanced-engineering-mathematics.md) — Fourier series and transform as part of PDE toolbox
- [Stroud Advanced Engineering Mathematics](../notes/maths/stroud-advanced-engineering-mathematics.md) — worked examples of Fourier series
- [Infinite Powers (epub)](../notes/maths/infinite-powers-epub.md) — historical and conceptual overview of integral transforms
- [Signals and Systems for Bioengineers](../notes/00-general-electronics/signals-systems-for-bioengineers.md) — Fourier transform in linear systems context; convolution theorem
