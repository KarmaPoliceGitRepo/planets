# Noise Figure

**Aliases:** NF; noise factor; F; minimum noise figure; Fmin; noise figure F; noise factor F

**Definition:** Noise figure F (or NF in dB) quantifies the signal-to-noise ratio degradation introduced by a two-port network: F = SNR_in/SNR_out (linear), NF = 10 log F (dB). For a noiseless network F = 1 (0 dB). The minimum noise figure F_min = 1 + 2√(Rn·Gu) is achieved at the optimal source admittance Y_opt = G_u + jB_opt; any other source admittance gives F = F_min + (Rn/Gs)|Y_s − Y_opt|² where Rn is the equivalent noise resistance. For cascaded stages, the Friis formula F_total = F₁ + (F₂−1)/G₁ + (F₃−1)/(G₁G₂) + ... shows that the first stage dominates. Noise figure is the fundamental performance criterion for LNAs in ultrasonic receivers and radio front-ends.

**Key relations:**
- [friis-cascade-formula](friis-cascade-formula.md) — cascaded noise figure calculation
- [s-parameters](s-parameters.md) — noise figure analysis uses S-parameters at the operating point
- [q-factor](q-factor.md) — component noise contributes to system noise figure
- [signal-to-noise-ratio](signal-to-noise-ratio.md) — noise figure directly determines SNR degradation

**Discussed in:**
- [Module 9: Noise in Communication Systems](../notes/000-electronics-instructions/module9-noise-in-communication-systems.md) — noise factor definition, two-port noise model
- [Module 11: Two-Port Noise Analysis](../notes/000-electronics-instructions/module11-two-port-noise-analysis.md) — Fmin, Rn, Yopt; noise circles on Smith Chart
- [Noise Figure (Collin)](../notes/00-general-electronics/collin-solid-state-amplifiers.md) — theoretical basis; transistor noise models
