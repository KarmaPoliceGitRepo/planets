# Bessel Filter

**Aliases:** Thomson filter; Bessel-Thomson filter; maximally flat group delay filter; linear phase filter; Bessel approximation

**Definition:** The Bessel filter (also called Thomson or Bessel-Thomson filter) is designed for maximally flat group delay in the passband, which gives linear phase and therefore no waveform distortion of broadband signals passing through. The magnitude roll-off is the slowest of all standard filter types for a given order — significantly less selective than Butterworth or Chebyshev. In ultrasonic and pulse applications where preserving pulse shape is important, a Bessel filter is preferred over amplitude-optimised types. The transitional filter (Gaussian–Chebyshev) is a compromise with steeper roll-off and near-linear phase.

**Key relations:**
- [analogue-filter-basics](analogue-filter-basics.md) — Bessel is the linear-phase LP prototype
- [butterworth-filter](butterworth-filter.md) — more roll-off but non-linear phase
- [chebyshev-filter](chebyshev-filter.md) — fastest roll-off but most phase distortion among all-pole types
- [sallen-key-topology](sallen-key-topology.md) — active realisation of each pole pair

**Discussed in:**
- [Chapter 8: Analogue Filters](../notes/00-general-hardware-design-stuff/chapter8-analogue-filters.md) — group delay flatness, pole locations, comparison to Butterworth; transitional filter
