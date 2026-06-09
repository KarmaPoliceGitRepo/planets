# Chebyshev Filter

**Aliases:** Tschebyscheff filter; Chebyshev approximation; equiripple passband filter; Chebyshev polynomial filter; inverse Chebyshev filter

**Definition:** The Chebyshev filter is an all-pole low-pass approximation with equiripple (equal-height) ripple in the passband and monotonically increasing attenuation in the stopband. For a given order n and passband ripple ε, it achieves steeper roll-off at the passband edge than the Butterworth filter of the same order. Poles lie on an ellipse in the left half s-plane. The inverse Chebyshev (Chebyshev Type II) has a flat passband and equiripple stopband, with finite-frequency transmission zeros providing faster initial stopband attenuation. Both types are widely used in anti-aliasing and channel filters where a specific stopband attenuation target must be met with minimum order.

**Key relations:**
- [analogue-filter-basics](analogue-filter-basics.md) — Chebyshev is a standard LP prototype
- [butterworth-filter](butterworth-filter.md) — less ripple but slower roll-off
- [elliptic-filter](elliptic-filter.md) — both passband and stopband ripple; fastest roll-off
- [sallen-key-topology](sallen-key-topology.md) — active implementation of each 2-pole section

**Discussed in:**
- [Chapter 8: Analogue Filters](../notes/00-general-hardware-design-stuff/chapter8-analogue-filters.md) — pole locations on ellipse; design equations; ripple-order tradeoff
