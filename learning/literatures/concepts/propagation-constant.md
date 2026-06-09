# Propagation Constant

**Aliases:** γ; gamma; complex propagation constant; attenuation constant α; phase constant β; phase propagation factor

**Definition:** The propagation constant γ = α + jβ characterises how a wave changes as it travels along a transmission line or through a medium. It is given by γ = √((R + jωL)(G + jωC)) for a transmission line with RLGC parameters. The real part α (Np/m or dB/m) is the attenuation constant, describing exponential amplitude decay; the imaginary part β = 2π/λ (rad/m) is the phase constant, describing the spatial phase progression. In the lossless case γ = jβ = jω√(LC). The wavelength λ = 2π/β and phase velocity vₚ = ω/β.

**Key relations:**
- [transmission-line](transmission-line.md) — γ is a key transmission line parameter
- [telegrapher-equations](telegrapher-equations.md) — γ is the eigenvalue of the Telegrapher's equations
- [characteristic-impedance](characteristic-impedance.md) — Z₀ = (R+jωL)/γ
- [skin-depth](skin-depth.md) — skin effect increases α at high frequencies
- [insertion-loss](insertion-loss.md) — attenuation α contributes to insertion loss over distance

**Discussed in:**
- [Propagation Constant](../notes/00-general-electronics/propagation-constant.md) — definition, derivation, numerical examples for coax
- [Module 2: Transmission Lines Frequency Domain](../notes/000-electronics-instructions/module2-transmission-lines-frequency-domain.md) — γ in the context of phasor analysis
