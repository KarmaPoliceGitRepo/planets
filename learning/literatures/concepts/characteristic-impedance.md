# Characteristic Impedance

**Aliases:** Z0; surge impedance; characteristic impedance Z₀; transmission line impedance; Z_0

**Definition:** The characteristic impedance Z₀ of a transmission line is the ratio of the forward-travelling voltage wave amplitude to the forward-travelling current wave amplitude: Z₀ = √((R + jωL)/(G + jωC)). In the lossless case Z₀ = √(L/C), which is real and frequency-independent. Standard coaxial cable is 50 Ω (RF/microwave) or 75 Ω (video/broadcast); microstrip values range widely depending on track width and substrate. A load impedance Z_L = Z₀ produces no reflection. Mismatch causes standing waves and reflected power characterised by the reflection coefficient Γ = (Z_L − Z₀)/(Z_L + Z₀).

**Key relations:**
- [transmission-line](transmission-line.md) — Z₀ is the fundamental parameter of a transmission line
- [telegrapher-equations](telegrapher-equations.md) — Z₀ derived from RLGC parameters
- [reflection-coefficient](reflection-coefficient.md) — Γ = (ZL−Z₀)/(ZL+Z₀)
- [smith-chart](smith-chart.md) — impedances plotted normalised to Z₀
- [quarter-wave-transformer](quarter-wave-transformer.md) — uses Z₀ selection to match impedances

**Discussed in:**
- [Module 1: Introduction to Transmission Lines](../notes/000-electronics-instructions/module1-introduction-to-transmission-lines.md) — derivation of Z₀ from the Telegrapher's equations
- [Transmission Line Parameters](../notes/00-general-electronics/transmission-line-parameters.md) — Z₀ formulas for coaxial and microstrip; tables of standard values
