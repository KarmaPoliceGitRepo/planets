# Transfer Function and System Response
**Aliases:** transfer function; frequency response function; FRF; Bode plot; poles; zeros; impulse response; Green's function; asymptotic stability; BIBO stability; damping ratio; natural frequency; step response

**Definition:** The transfer function H(s) = Y(s)/X(s) is the ratio of the Laplace-transformed output to input for a linear time-invariant (LTI) system with zero initial conditions. Its poles determine stability and the natural modes of the homogeneous response; zeros shape the frequency response. The Bode plot displays |H(jω)| in dB and phase vs. log ω; a pair of complex conjugate poles at −ζωₙ ± jωₙ√(1−ζ²) produces a resonance peak whose height depends on damping ratio ζ. Green's function is the impulse response of a PDE operator, giving the response to a unit impulse source; the general response follows by convolution.

**Key relations:**
- related: [laplace-and-z-transform](laplace-and-z-transform.md)
- related: [digital-filters](digital-filters.md)
- related: [partial-differential-equations](partial-differential-equations.md)

**Discussed in:**
- [Pole-Zero Analysis (MIT notes)](../notes/maths/pole-zero-mit.md) — relationship between pole locations and system response; BIBO and asymptotic stability
- [Kreyszig Advanced Engineering Mathematics](../notes/maths/kreyszig-advanced-engineering-mathematics.md) — transfer function in Laplace domain; partial fractions; inverse Laplace
- [Signals and Systems for Bioengineers](../notes/00-general-electronics/signals-systems-for-bioengineers.md) — frequency response; Bode plots; damping ratio and natural frequency
- [Compensation Filtering Pulse-Echo](../notes/signal-processing/compensation-filtering-pulse-echo.md) — estimates transducer transfer function from pulse-echo data for inverse filtering
