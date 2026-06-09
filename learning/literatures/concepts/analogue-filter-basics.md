# Analogue Filter Fundamentals

**Aliases:** analogue filter; active filter; passive filter; filter design; low-pass prototype; filter order; passband; stopband; cutoff frequency; transfer function H(s); s-plane; pole; zero; passband ripple; stopband attenuation; frequency transformation; step response; impulse response; damping ratio

**Definition:** An analogue filter is a frequency-selective circuit characterised by its transfer function H(s), a rational polynomial in the Laplace variable s = σ + jω. Design starts with a normalised low-pass prototype (cutoff at 1 rad/s, 1 Ω) of order n (equal to the number of reactive elements); the order determines the roll-off rate (20n dB/decade above cutoff). Key specifications: passband (frequencies passed with ≤ Amax dB loss), stopband (frequencies attenuated by ≥ Amin dB), and transition band between them. Frequency transformations convert the LP prototype to high-pass, band-pass, or notch responses. Poles in the left half s-plane ensure stability; pole Q determines peaking. The damping ratio ζ = 1/(2Q) governs transient behaviour.

**Key relations:**
- [butterworth-filter](butterworth-filter.md) — maximally flat LP prototype
- [chebyshev-filter](chebyshev-filter.md) — equiripple passband LP prototype
- [bessel-filter](bessel-filter.md) — maximally flat group delay (linear phase)
- [elliptic-filter](elliptic-filter.md) — equiripple passband and stopband
- [notch-filter](notch-filter.md) — band-reject response
- [sallen-key-topology](sallen-key-topology.md) — common 2-pole active realisation
- [q-factor](q-factor.md) — pole Q determines peaking and bandwidth

**Discussed in:**
- [Chapter 8: Analogue Filters](../notes/00-general-hardware-design-stuff/chapter8-analogue-filters.md) — comprehensive treatment of LP prototypes, frequency transformations, active topologies, component sensitivity
