# Friis Cascade Formula

**Aliases:** Friis noise formula; cascaded noise figure; Friis cascade formula; Friis formula

**Definition:** The Friis cascade formula gives the total noise factor of a chain of N two-port stages: F_total = F₁ + (F₂−1)/G₁ + (F₃−1)/(G₁G₂) + ... + (F_N−1)/(G₁G₂...G_{N-1}). Here F_n is the noise factor and G_n is the available power gain of stage n. The formula shows that the noise contribution of each subsequent stage is divided by the cumulative gain of all preceding stages, so the first stage (typically a low-noise amplifier) dominates the total system noise figure. High first-stage gain and low first-stage noise figure are therefore the primary design goals in receiver chain design.

**Key relations:**
- [noise-figure](noise-figure.md) — Friis formula combines individual stage noise figures
- [s-parameters](s-parameters.md) — available gain G is derived from S-parameters

**Discussed in:**
- [Module 9: Noise in Communication Systems](../notes/000-electronics-instructions/module9-noise-in-communication-systems.md) — Friis formula derivation and cascade examples
