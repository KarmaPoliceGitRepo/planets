# Quarter-Wave Transformer

**Aliases:** λ/4 transformer; quarter-wave transformer; λ/4 section; impedance inverter; quarter-wavelength transformer

**Definition:** A quarter-wave transformer is a transmission line section of electrical length λ/4 with characteristic impedance Z' = √(Z₀ · Z_L). It achieves perfect conjugate matching between a source impedance Z₀ and a real load Z_L at the design frequency, acting as an impedance inverter: Z_in = Z'²/Z_L. The bandwidth over which |Γ| < Γ_max depends on the impedance ratio Z_L/Z₀; multiple cascaded quarter-wave sections with progressively graded impedances (Chebyshev or binomial taper) can broaden the bandwidth. It is directly analogous to the acoustic quarter-wavelength matching layer.

**Key relations:**
- [transmission-line](transmission-line.md) — the transformer is a λ/4 section of transmission line
- [characteristic-impedance](characteristic-impedance.md) — Z' must be set to √(Z₀·ZL)
- [smith-chart](smith-chart.md) — λ/4 corresponds to 180° rotation on the chart
- [quarter-wavelength-matching-layer](quarter-wavelength-matching-layer.md) — acoustic analogue
- [impedance-matching-network](impedance-matching-network.md) — alternative matching approaches

**Discussed in:**
- [Module 2: Transmission Lines Frequency Domain](../notes/000-electronics-instructions/module2-transmission-lines-frequency-domain.md) — input impedance formula and λ/4 special case
- [Quarter-Wavelength Transformer](../notes/00-general-electronics/quarter-wavelength-transformer.md) — derivation of Z' = √(Z₀ZL); bandwidth analysis
