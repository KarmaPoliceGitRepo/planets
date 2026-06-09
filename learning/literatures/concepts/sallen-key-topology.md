# Sallen-Key Topology

**Aliases:** VCVS filter; Sallen-Key filter; voltage-controlled voltage source filter; SK topology

**Definition:** The Sallen-Key topology is a two-pole active filter section using an op-amp configured as a non-inverting voltage-controlled voltage source (VCVS). It realises any second-order transfer function (LP, HP, BP) with a minimum of components (4 passives + 1 op-amp), is non-inverting, and is easy to cascade into higher-order filters. Its main drawback is Q sensitivity to component tolerances: at high Q values (> 5–10), component matching becomes critical. Unity-gain Sallen-Key (K = 1) has the lowest sensitivity. It is the most commonly used active filter building block in discrete analogue design.

**Key relations:**
- [analogue-filter-basics](analogue-filter-basics.md) — Sallen-Key implements LP prototype sections
- [butterworth-filter](butterworth-filter.md) — each 2-pole stage implemented as Sallen-Key section
- [chebyshev-filter](chebyshev-filter.md) — high-Q Chebyshev poles require careful component matching
- [general-impedance-converter](general-impedance-converter.md) — GIC is an alternative for high-Q sections
- [q-factor](q-factor.md) — Q of each section set by passive component ratios

**Discussed in:**
- [Chapter 8: Analogue Filters](../notes/00-general-hardware-design-stuff/chapter8-analogue-filters.md) — topology derivation, design equations, sensitivity analysis, unity-gain vs. amplified forms
