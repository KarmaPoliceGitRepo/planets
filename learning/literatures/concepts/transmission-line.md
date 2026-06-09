# Transmission Line

**Aliases:** T-line; TL; t-line; coaxial line; coaxial cable; microstrip line; stripline; distributed parameter line; transmission-line

**Definition:** A transmission line is a two-conductor (or planar) distributed electrical structure that guides electromagnetic energy from source to load when the line length is a significant fraction of a wavelength. It is characterised by distributed RLGC parameters per unit length (resistance R, inductance L, conductance G, capacitance C), governed by the Telegrapher's equations. In the lossless limit the characteristic impedance is Z₀ = √(L/C) and the phase velocity is vₚ = 1/√(LC). Common physical implementations include coaxial cable, microstrip, stripline, and twin-lead; all support the TEM principal mode at low frequencies.

**Key relations:**
- [telegrapher-equations](telegrapher-equations.md) — the governing PDEs
- [characteristic-impedance](characteristic-impedance.md) — Z₀ = √(L/C) in the lossless case
- [propagation-constant](propagation-constant.md) — γ = √((R+jωL)(G+jωC))
- [reflection-coefficient](reflection-coefficient.md) — arises from impedance mismatch at termination
- [smith-chart](smith-chart.md) — graphical tool for transmission line analysis
- [quarter-wave-transformer](quarter-wave-transformer.md) — λ/4 section used for impedance transformation

**Discussed in:**
- [Module 1: Introduction to Transmission Lines](../notes/000-electronics-instructions/module1-introduction-to-transmission-lines.md) — distributed model, characteristic impedance, reflections
- [Transmission Line Circuit Model](../notes/00-general-electronics/transmission-line-circuit-model.md) — RLGC model derivation and Telegrapher's equations
