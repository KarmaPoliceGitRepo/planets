# Laplace and Z-Transform
**Aliases:** Laplace transform; Z-transform; transfer function; poles; zeros; BIBO stability; asymptotic stability; Bode plot; damping ratio; pole-zero plot; s-plane

**Definition:** The Laplace transform L{x(t)} = X(s) = ∫₀^∞ x(t)e^{−st}dt converts linear ODEs into algebraic equations; the complex frequency s = σ + jω generalises the Fourier variable jω to allow analysis of transient and unstable systems. The Z-transform Z{x[n]} = X(z) = Σ x[n]z^{−n} is the discrete-time analogue; poles inside the unit circle correspond to stable causal systems. A system transfer function H(s) is the ratio of output to input Laplace transforms; its poles and zeros determine the frequency response, step response, and stability. BIBO stability requires all poles to lie in the left half s-plane (continuous) or inside the unit circle (discrete). The Bode plot displays |H(jω)| in dB and ∠H(jω) vs. log ω, with each real pole contributing −20 dB/decade and −45°/decade.

**Key relations:**
- related: [fourier-transform](fourier-transform.md)
- related: [digital-filters](digital-filters.md)
- related: [partial-differential-equations](partial-differential-equations.md)

**Discussed in:**
- [DSP Matlab (Proakis)](../notes/maths/dsp-matlab-proakis.md) — Z-transform definitions, region of convergence, inverse Z; pole-zero analysis
- [Pole-Zero Analysis (MIT notes)](../notes/maths/pole-zero-mit.md) — BIBO stability criterion; relationship between pole location and impulse response decay
- [Signals and Systems (Chaparro)](../notes/signal-processing/signals-systems-matlab-chaparro.md) — Laplace and Z-transform side-by-side; transfer function; block diagram algebra
- [Kreyszig Advanced Engineering Mathematics](../notes/maths/kreyszig-advanced-engineering-mathematics.md) — Laplace transform tables; inverse transform; ODE solution via Laplace
- [Signals and Systems for Bioengineers](../notes/00-general-electronics/signals-systems-for-bioengineers.md) — Laplace in LTI system analysis; Bode plots; damping ratio and natural frequency
