# Butterworth Filter

**Aliases:** maximally flat filter; Butterworth approximation; Butterworth low-pass; Butterworth polynomial

**Definition:** The Butterworth filter is an all-pole low-pass approximation with maximally flat magnitude response in both the passband and stopband: |H(jω)|² = 1/(1 + (ω/ωc)^{2n}), where n is the filter order. There is no ripple anywhere, but the roll-off in the transition band is gentler than Chebyshev or elliptic filters of the same order. Poles lie equally spaced on a unit circle in the left half s-plane at angles π(2k+n−1)/(2n) for k = 1,...,n. It is the simplest and most widely used approximation for general-purpose filtering where phase linearity is more important than sharp roll-off.

**Key relations:**
- [analogue-filter-basics](analogue-filter-basics.md) — Butterworth is the simplest LP prototype
- [chebyshev-filter](chebyshev-filter.md) — sharper roll-off with equal ripple passband
- [bessel-filter](bessel-filter.md) — better phase linearity but slower roll-off
- [sallen-key-topology](sallen-key-topology.md) — common implementation of each 2-pole stage

**Discussed in:**
- [Chapter 8: Analogue Filters](../notes/00-general-hardware-design-stuff/chapter8-analogue-filters.md) — pole positions, normalised element values, design tables
