# Elliptic Filter

**Aliases:** Cauer filter; Zolotarev filter; elliptic approximation; equiripple passband and stopband filter; Cauer-Chebyshev filter

**Definition:** The elliptic filter (Cauer filter) achieves equiripple in both the passband and the stopband, and places finite-frequency transmission zeros (notches) in the stopband using elliptic function mathematics. It provides the sharpest possible roll-off transition for a given filter order among standard approximations. The price is phase non-linearity and complexity of design. It is specified by four parameters: order n, passband ripple A_max, stopband attenuation A_min, and selectivity factor k = Ωp/Ωs. Widely used where the order (and thus component count) must be minimised to meet a given specification.

**Key relations:**
- [analogue-filter-basics](analogue-filter-basics.md) — elliptic is the most selective LP prototype
- [chebyshev-filter](chebyshev-filter.md) — flat stopband; elliptic has finite zeros
- [notch-filter](notch-filter.md) — the stopband zeros in an elliptic filter are notch-type
- [sallen-key-topology](sallen-key-topology.md) — biquad sections realise the complex pole-zero pairs

**Discussed in:**
- [Chapter 8: Analogue Filters](../notes/00-general-hardware-design-stuff/chapter8-analogue-filters.md) — elliptic design method; comparison of roll-off for equal order
