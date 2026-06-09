# Ultrasonic Backscattering in Cubic Polycrystals with Ellipsoidal Grains and Texture

- **Source:** Yang and Rokhlin J. Nondestruct. Eval. 2013
- **Drive link:** https://drive.google.com/file/d/1-jsZE3S7nT48PtYDWqUR9K0rdJiAxAoZ/view
- **Type:** paper
- **Author/Year:** L. Yang, S. I. Rokhlin / 2013
- **Coverage:** full (deep read)

## Overview
A theoretical paper deriving ultrasonic backscattering coefficients and high-frequency attenuation for textured polycrystals with cubic crystallites having ellipsoidal (elongated) grain shapes. The crystallographic texture is described by a modified Gaussian ODF with a single texture parameter σ; the macroscopic symmetry of the textured medium is hexagonal (transverse isotropy). Both attenuation and backscattering are given as explicit analytical functions of propagation direction, frequency, texture parameter, and grain aspect ratio. Compared against two rolled aluminum-alloy samples (Al-7075 rod and Al-7475 plate) from Guo et al.'s earlier dataset.

## Unique contribution
Provides the first combined analytical treatment of simultaneous grain shape anisotropy (ellipsoidal elongation) and crystallographic texture (Gaussian ODF) for both backscattering coefficient and stochastic attenuation in cubic polycrystals, enabling interpretation of directional measurements in deformed metals where both effects coexist. The texture direction and grain elongation direction are independently defined and can differ. Shows that the directional ratio of backscattering coefficients is a product of a texture-dependent term and an inverse-squared grain-size term, which provides a separable diagnostic for texture vs. elongation.

## Key concepts
- Backscattering coefficient η(k,p)
- Cubic polycrystals with ellipsoidal grains
- Ellipsoidal grain aspect ratio (a_x, a_y, a_z)
- Modified Gaussian ODF with single texture parameter σ
- Elastic covariance ⟨δC_αααα δC_αααα⟩
- Macroscopic hexagonal (fiber) symmetry from texture
- Figure of Merit (FOM) = √η
- Stochastic regime attenuation
- Directional backscattering ratios
- Born approximation
- Forward scattering dominance in stochastic attenuation

## Methods / results / takeaways
- **Backscattering model (Eq. 1–4):** Based on Rose's Born-approximation framework extended to include arbitrary propagation direction p relative to texture direction T. The backscattering coefficient is η(k,p) = Q(p)·V·k⁴ / (1 + 4k²_x a²_x + 4k²_y a²_y + 4k²_z a²_z)², where Q(p) encodes texture through the elastic covariance ⟨δC_pppp δC_pppp⟩ and V = 8πa_x a_y a_z is the effective grain volume.
- **Elastic covariance for cubic symmetry (Eq. 11):** The ODF-averaged covariance is expressed as a polynomial in cos α (angle between wave propagation and texture direction) with coefficients S₁–S₈ that are functions of the texture integrals I^m_σ. The anisotropy constant is c = c₁₁ − c₁₂ − 2c₄₄.
- **Limiting cases (Eq. 16):** As σ → ∞ (random/untextured), ⟨δC⟩ → (16/525)c²; as σ → 0 (perfectly aligned), ⟨δC⟩ → (1/32)c² sin⁸α. At σ = 0 and α = 0° (wave along texture axis), no scattering; at α = 90° the scattering is close to the isotropic limit.
- **Stochastic attenuation with texture (Eq. 21–23):** In the high-frequency limit, α_L ≈ ⟨δC_αααα δC_αααα⟩ · π²f² / (ρ²V_l(α)⁶) · a_ell, where a_ell is the ellipsoidal radius in the propagation direction. Thus, for propagation along principal axes, α^i_L ≈ C · f² · T_i · a_i where T_i is the direction-dependent elastic covariance term.
- **Directional ratios (Eq. 25–27):** For the backscattering amplitude ratio √(η_x/η_z) ≈ (T_x/T_z)^½ · (a_z/a_x); for the attenuation ratio α^x_L / α^z_L ≈ (T_x/T_z) · (a_x/a_z). The backscattering amplitude has inverse-square dependence on grain size; attenuation has linear dependence. This difference provides the basis for separating texture from elongation effects experimentally.
- **Sample A1 (Al-7075 rod, Fig. 7):** Grain sizes: a_x = a_y = 70 µm, a_z = 437 µm (rod direction elongated). Measured backscattering ratio η_S3/η_S2 shows strong size-dependent behavior. Best fit: texture parameter σ ≈ 0.05, elastic covariance ratio ⟨δCδC⟩_S3/⟨δCδC⟩_S2 = 0.75 (weak texture). Without texture correction, model over-predicts the ratio; with texture, good agreement in the 10–20 MHz reliable range.
- **Sample A1 attenuation (Fig. 8):** Despite 6× grain elongation, measured attenuations in three directions are nearly equal — explained by mutual compensation: grain elongation favors higher attenuation for waves crossing grain cross-section, but texture reduces the covariance in the elongation direction. Model with combined effects reproduces this near-isotropy in attenuation.
- **Sample A3 (Al-7475 plate, Figs. 9–11):** Actual texture is a superposition of "Copper", "Brass" and "S" components. Since the stochastic regime attenuation is dominated by the grain radius in the propagation direction, the uniaxial-texture approximation is applied direction-by-direction with independent σ values. Good agreement for backscattering ratios; stochastic model slightly underestimates attenuation anisotropy.
- **Velocity ratios (Fig. 10):** Voigt-averaged velocity ratios calculated from σ overestimate the measured ratios by ~0.3–0.6%, partially attributed to use of the upper-bound (Voigt) average vs. true effective velocity, and to the simplification of the texture model.
- **Key finding on grain size vs. texture dominance:** For both samples, the grain size (elongation) effect dominates backscattering in the high-frequency stochastic regime because η ∝ a⁻² vs. attenuation ∝ a. Texture accounts for at most a factor of ~4/3 in the covariance ratio for these samples.

## Figures
- **Fig. 1 (page 2–3, text description):** Geometry of ellipsoidal grains (a) with radii a_x, a_y, a_z in global X,Y,Z; wave propagation direction p and texture direction T independently defined by angles τ,φ_τ and ξ,φ_ξ. (b) Local coordinate system x',y',z' aligned with texture direction showing angle α between propagation and texture. (c) ODF schematic.
- **Fig. 2 (page 5):** Elastic covariance ⟨δC_αααα δC_αααα⟩/c² vs. σ for various propagation angles α (0°, 30°, 60°, 90°). At σ ≳ 0.1 the covariance is nearly direction-independent (isotropic limit); at very small σ (strong texture) there is a strong angular dependence with zero covariance at α = 0°.
- **Fig. 3 (page 6):** Elastic covariance vs. propagation angle α for various σ values — strongly peaked near 90° for small σ; nearly flat (isotropic) for σ > 1.
- **Fig. 4 (page 6):** Polar diagram of ⟨δC_αααα δC_αααα⟩ vs. α for σ = 0.01, 0.05, 0.5, 1.0, ∞. Strong peanut-shaped pattern at small σ; circle at large σ.
- **Fig. 5 (page 7):** Backscattering amplitude √η vs. σ for various propagation directions at 15 MHz, ellipsoidal grains 0.1×0.1×0.3 mm. At large σ, backscattering depends mainly on grain shape; at small σ, strong texture dependence with near-zero backscattering at α = 0°.
- **Fig. 6 (page 7):** Polar diagram of √η vs. α for various σ — elongated ellipse at large σ (shape dominated); modified peanut shape at small σ (texture dominated).
- **Fig. 7 (page 10):** Backscattering ratio √(η_S3/η_S2) vs. frequency for Sample A1. Solid line: model with texture (σ = 0.05); dashed inset curve: no texture (σ = ∞). Good agreement in 10–20 MHz range. Insert shows importance of texture correction.
- **Fig. 8 (page 11):** Attenuation vs. frequency in three directions for Sample A1. Solid lines: model; dots: experiment. Three directional attenuations converge to nearly the same values — mutual compensation of elongation and texture effects.
- **Fig. 9 (page 12):** Backscattering ratio for Sample A3 (rolled plate) in S1, S2, S3 directions. Two dot-dashed "isotropic ratio" reference lines shown. Model with texture fits well in reliable frequency range.
- **Fig. 10 (page 12):** Velocity ratios for S1/S2, S1/S3 directions vs. σ — measured points (A1: ~0.3% deviation; A3: 0.3–0.6%) compared to Voigt-average calculated lines.
- **Fig. 11 (page 13):** Attenuation coefficients for Sample A3. S3 direction (lowest attenuation) also shows highest backscattering — direction of shortest grain dimension.
