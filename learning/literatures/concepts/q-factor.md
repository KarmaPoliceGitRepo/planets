# Q Factor

**Aliases:** quality factor; Q; loaded Q; unloaded Q; resonator Q; filter Q; Q factor; mechanical Q

**Definition:** The Q factor (quality factor) of a resonant system is defined as Q = ω₀ × (energy stored)/(power dissipated) = ω₀/Δω, where Δω is the 3-dB bandwidth of the resonance. For a series RLC circuit Q = ω₀L/R = 1/(ω₀CR); for parallel RLC, Q = R/(ω₀L) = ω₀CR. The unloaded Q (Q_u) represents the resonator alone; the loaded Q (Q_L) includes external coupling losses; Q_L < Q_u. In filter design, Q controls the pole locations and therefore bandwidth and selectivity; in matching networks, Q = √(n−1) for an L-network determines the bandwidth of the match. Higher Q gives narrower bandwidth and more selective response.

**Key relations:**
- [mechanical-quality-factor](mechanical-quality-factor.md) — Qm is the acoustic/mechanical version
- [analogue-filter-basics](analogue-filter-basics.md) — Q determines filter pole locations and bandwidth
- [impedance-matching-network](impedance-matching-network.md) — Q links impedance ratio to bandwidth
- [resonant-frequency](resonant-frequency.md) — Q = f₀/Δf

**Discussed in:**
- [Module 5: Review of Resonance](../notes/000-electronics-instructions/module5-review-of-resonance.md) — series and parallel RLC Q; crystal resonator high Q
- [Chapter 8: Analogue Filters](../notes/00-general-hardware-design-stuff/chapter8-analogue-filters.md) — Q in filter transfer functions; relationship to damping ratio
- [Q Factor (Collin)](../notes/00-general-electronics/collin-em-resonators.md) — cavity and distributed resonator Q definitions
