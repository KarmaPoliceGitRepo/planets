# General Impedance Converter

**Aliases:** GIC; General Impedance Converter; Frequency Dependent Negative Resistor; FDNR; D element; active inductor; simulated inductor

**Definition:** A General Impedance Converter (GIC) is a two op-amp circuit whose input impedance is Z_in = Z₁Z₃Z₅/(Z₂Z₄). By choosing the five impedances (resistors and capacitors), it synthesises impedances not realisable with passive components alone. The most important cases: (1) Simulated inductor: two resistors, two capacitors, one resistor → Z_in = jωL_eq (avoids physical inductor parasitics); (2) Frequency Dependent Negative Resistor (FDNR, "D element"): two capacitors, two resistors, one capacitor → Z_in = D/(s²) with D real, used in leapfrog filter realisations. GICs enable high-order, high-Q active filters with low sensitivity.

**Key relations:**
- [analogue-filter-basics](analogue-filter-basics.md) — GIC used in high-Q filter sections
- [sallen-key-topology](sallen-key-topology.md) — alternative lower-sensitivity topology for high-Q
- [q-factor](q-factor.md) — GIC-based sections achieve high Q with lower sensitivity than Sallen-Key

**Discussed in:**
- [Chapter 8: Analogue Filters](../notes/00-general-hardware-design-stuff/chapter8-analogue-filters.md) — GIC circuit derivation; FDNR and simulated inductor cases; use in Bruton transformation
