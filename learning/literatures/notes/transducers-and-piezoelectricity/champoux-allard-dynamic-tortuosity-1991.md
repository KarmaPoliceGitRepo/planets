# Dynamic Tortuosity and Bulk Modulus in Air-Saturated Porous Media

- **Source:** Champoux Allard dynamic tortuosity 1991
- **Drive link:** https://drive.google.com/file/d/1nUmCs7mdxc3ukMi_36j0wbLetJZopvsX/view
- **Type:** paper (Journal of Applied Physics 70(4), 1975–1979, 1991)
- **Author/Year:** Y. Champoux, J.-F. Allard / 1991
- **Coverage:** full

## Overview
Extends the Johnson-Koplik-Dashen (1987) characteristic length framework for dynamic tortuosity to also describe the frequency dependence of the bulk modulus of the saturating fluid. Introduces a second characteristic length Λ' (thermal characteristic length) = 2V/A (volume-to-pore-surface ratio, unweighted) to describe thermal effects at high frequencies. The viscous characteristic length Λ is weighted by the square of local inviscid fluid velocity. Experimental validation uses a Filtros porous ceramic (φ = 0.432, a∞ = 1.70).

## Unique contribution
Provides the first complete two-characteristic-length model (Λ for viscous, Λ' for thermal effects) for both dynamic tortuosity and dynamic bulk modulus in air-saturated porous media. The model captures the correct high-frequency asymptotic behavior of K(ω) and predicts the isothermal-to-adiabatic transition of the bulk modulus. Replaces the earlier Zwikker-Kosten and simplified Biot models for air-filled porous acoustics.

## Key concepts
- Dynamic tortuosity Z(ω): relates effective density ρe(ω) = Z(ω)·ρ₀; determines inertial + viscous effects
- Viscous characteristic length Λ: Λ = 2∫|v(r)|²dV / ∫|v(r_s)|²dA (velocity-weighted; favors narrow pores)
- Thermal characteristic length Λ': Λ' = 2V/A (unweighted volume-to-area ratio; > Λ for non-uniform pores)
- Johnson-Koplik-Dashen expression for Z(ω): Z(ω) = a∞[1 + (σφ/iωρ₀a∞)(1 + 4ia²∞ρ₀ωη/σ²φ²Λ²)^½]
- Dynamic bulk modulus K(ω): transitions from isothermal (K→P₀) at low ω to adiabatic (K→γP₀) at high ω
- K(ω) model uses same functional form as Z(ω) but with Λ' instead of Λ and σ' instead of σ
- Parameter c (typically 0.5–1): relates σ·φ²Λ²/a∞ to known constants

## Methods / results / takeaways
- Filtros QF-130 ceramic: φ = 0.432, a∞ = 1.70, σ = 44,500 N·m⁻⁴·s
- Estimated Λ = 73 μm, Λ' = 153 μm (Λ' ≈ 2.09Λ for this material)
- Model fit parameters: c = 0.64, c' = 1.34
- Measured dynamic tortuosity and bulk modulus match model for 50–5000 Hz
- Real K(ω)/P₀ → 1 at low ω (isothermal), → 1.4 at high ω (adiabatic) — verified experimentally
- Application: acoustic modelling of porous absorbers, aerogel matching layers, air-coupled transducer design
