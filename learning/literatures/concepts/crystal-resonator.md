# Crystal Resonator

**Aliases:** quartz resonator; crystal; quartz crystal; XTAL; piezoelectric crystal resonator; crystal oscillator

**Definition:** A crystal resonator is a piezoelectric quartz element with mechanical Q of 10⁵–10⁶ and ppm-level frequency stability. It is modelled electrically as a series LCR (motional arm) in parallel with the shunt capacitance C₀; the series resonance f_s ≈ 1/(2π√(L_m C_m)) and parallel resonance f_p are very close, separated by a fraction of a percent. This extremely high Q and temperature-stable f₀ make crystal resonators the standard for frequency reference in oscillators (TCXO, OCXO), clocks, and filters. In Pierce, Colpitts, or Butler oscillator topologies the crystal operates between f_s and f_p as an inductor to satisfy the Barkhausen criterion.

**Key relations:**
- [piezoelectric-constants](piezoelectric-constants.md) — quartz is a piezoelectric material (though not a ceramic)
- [resonant-frequency](resonant-frequency.md) — crystal has a very precise resonant frequency
- [q-factor](q-factor.md) — crystal Q ~ 10⁵–10⁶ far exceeds LC resonators
- [phase-locked-loop](phase-locked-loop.md) — crystal oscillator often provides PLL reference

**Discussed in:**
- [Module 5: Review of Resonance](../notes/000-electronics-instructions/module5-review-of-resonance.md) — crystal equivalent circuit; series/parallel resonance; use in oscillators
