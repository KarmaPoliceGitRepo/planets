# Angular Spectrum Method
**Aliases:** angular spectrum approach; ASA; plane-wave decomposition; spectral propagator; FFT-based angular spectrum

**Definition:** The angular spectrum method decomposes a transducer's radiated pressure field on a source plane into a superposition of plane waves (2D spatial Fourier transform). Each plane-wave component is propagated independently — multiplied by a phase shift e^{jkz cos θ} — and the field at any axial distance is recovered by the inverse transform. The approach is exact for monochromatic fields in homogeneous media and O(N² log N) via 2D FFT. The spectral propagator must set evanescent components (|k_⊥| > k₀) to zero; aliasing near the evanescent boundary is the main numerical pitfall.

**Key relations:**
- related: [fast-fourier-transform](fast-fourier-transform.md)
- related: [fourier-transform](fourier-transform.md)
- related: [dispersion-curves](dispersion-curves.md)

**Discussed in:**
- [Zeng & McGough 2008 — Angular Spectrum](../notes/range-measurement/zeng-mcgough-2008-angular-spectrum.md) — angular spectrum propagator for focused transducer field simulation; aliasing analysis
