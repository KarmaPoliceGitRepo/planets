# Notch Filter

**Aliases:** notch filter; band-reject filter; band-stop filter; Twin-T notch; Bainter notch; Boctor notch; Wien-Robinson; null filter

**Definition:** A notch filter (band-reject filter) provides strong attenuation at a specific frequency (the notch frequency f_n) while passing all other frequencies with minimal loss. It is the complement of a band-pass filter. Common active single-frequency notch topologies include: Twin-T (passive RC bridge, used as op-amp feedback element), Bainter (two op-amps, independently adjustable notch depth and Q), and Boctor (single op-amp, low component count). The notch depth (dB) and Q (= f_n/bandwidth at −3 dB) are the key specifications. Notch filters are used to suppress power-line interference (50/60 Hz), structural resonances, or specific noise frequencies.

**Key relations:**
- [analogue-filter-basics](analogue-filter-basics.md) — notch is a special band-reject response
- [elliptic-filter](elliptic-filter.md) — elliptic filter incorporates notches in its stopband
- [sallen-key-topology](sallen-key-topology.md) — Sallen-Key used in some notch realisations
- [q-factor](q-factor.md) — notch Q = fn/bandwidth determines selectivity

**Discussed in:**
- [Chapter 8: Analogue Filters](../notes/00-general-hardware-design-stuff/chapter8-analogue-filters.md) — Twin-T, Bainter, Boctor topologies; design equations; component sensitivity
