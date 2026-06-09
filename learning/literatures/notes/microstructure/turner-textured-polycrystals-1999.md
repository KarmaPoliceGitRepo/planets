# Elastic Wave Propagation and Scattering in Heterogeneous, Anisotropic Media: Textured Polycrystalline Materials

- **Source:** Turner JASA 106 541 1999
- **Drive link:** https://drive.google.com/file/d/17Y0BNfnHZnxGGC4_7f7QlLdaLqlIqQYR/view
- **Type:** paper
- **Author/Year:** J. A. Turner / 1999
- **Coverage:** full (deep read)

## Overview
A theoretical paper extending the Dyson equation / Keller (FOSA) framework to textured polycrystalline materials, using anisotropic Green's dyadics appropriate for a transversely isotropic (fiber-textured) effective medium. The formalism is first stated for general global anisotropy, then specialized to cubic grains with one aligned crystallographic axis (remaining axes random about that axis), yielding transverse isotropy. Closed-form inner products on the covariance tensor are derived for the shear horizontal (SH), quasi-P (qP), and quasi-SV (qSV) wave types. Results are given for equiaxed stainless steel with aligned [001] axes. The derivation uses the Born approximation for the frequency range below the geometric optics limit.

## Unique contribution
First systematic Dyson-equation treatment of scattering attenuation in a globally anisotropic (textured) polycrystal using the appropriate anisotropic Green's dyadic (rather than the isotropic dyadic of Weaver's untextured treatment). The key advance is using the transversely isotropic bare Green's dyadic G₀, which contains the correct wave polarizations and directional phase velocities, yielding the correct angular dependence of attenuation including the effect of wave mode mixing through the polarization vectors. Provides explicit, simple expressions (single angular integrals over the unit circle) for all three wave-type attenuations that are directly usable for NDE and materials characterization.

## Key concepts
- Textured polycrystal (fiber texture / single aligned axis)
- Dyson equation for mean Green's function
- First-order smoothing approximation (FOSA) / Keller approximation
- Anisotropic (transversely isotropic) Green's dyadic G₀
- Eighth-rank covariance tensor of modulus fluctuations J_ijkl^αβγδ
- Shear horizontal (SH), quasi-compressional (qP), quasi-shear (qSV) wave types
- Single-crystal anisotropy parameter h = c₁₁ − c₁₂ − 2c₄₄
- Generalized spherical harmonics / Roe ODF coefficients
- Wave polarization vectors (ûₙ, v̂ₙ) in transversely isotropic medium
- Slowness surface for textured medium
- Attenuation angular dependence in Rayleigh limit
- qSV attenuation peak angle shift with frequency

## Methods / results / takeaways
- **Formulation:** The elastic moduli are C_ijkl(x) = C⁰_ijkl + δC_ijkl(x) where C⁰ = ⟨C⟩ is the average (anisotropic) modulus and δC has zero mean. The covariance L(x−y) = ⟨δC(x)δC(y)⟩ is an eighth-rank tensor. The self-energy operator M̃(p) convolutions the bare Green's dyadic G₀(s) with the Fourier-transformed covariance, and the Dyson equation gives ⟨G(p)⟩ = [G₀(p)⁻¹ − M̃(p)]⁻¹.
- **Anisotropic Green's dyadic (Section II):** For transverse isotropy with fiber direction n̂, the bare G₀ is expressed in terms of three wave-type propagators for SH (polarized ⊥ to p̂-n̂ plane), qP, and qSV (both in p̂-n̂ plane). The dispersion relations define directional phase velocities c_SH(Q), c_qP(Q), c_qSV(Q) where Q is the angle between propagation and fiber directions. The mixing angle ψ for qP/qSV polarization directions satisfies tan(2ψ) = −2E sin2Q / (P + E cos2Q).
- **Covariance for cubic grains with aligned [001] axis:** The eighth-rank covariance J^αβγδ_ijkl depends only on the single fiber direction n̂ and is parametrized by 14 independent coefficients. For the aligned [001] case: d₈ = b₆ = −2d₆ = 9h²/288; b₄ = −d₄ = −2h₄ = h₅ = 3h²/288; d₂ = c₂ = b₀ = −d₀ = −b₂ = −c₄ = h²/288; h₄ = 5h²/288. All coefficients scale as h² where h = c₁₁ − c₁₂ − 2c₄₄.
- **Inner products (Eqs. 49–51):** After choosing reference geometry with n̂ = ẑ, the required polarization inner products simplify to quadratic forms in sin²Q, sin²(Q'+ψ'), etc. For SH: J‥ û₁p̂ŝv̂₁ = (h²/32)sin²Q' sin²Q; for qP: J‥ û₂p̂ŝv̂₂ = (h²/32) sin²Q' sin²(Q'+ψ') sin²ψ sin²Q; etc.
- **Final attenuation expressions (Eqs. 57–59):** After φ' integration in closed form, each attenuation reduces to a simple 1D integral over Q' (scattering direction) involving the slowness surface functions r_b(Q) and the spatial correlation function W̃. The form is α_b(Q)·L = x_b⁴ · (h²/64ρ²c̄_b⁴) · r_b³(Q) · sin²Q · (polarization factor) × [I_{b→SH} + I_{b→qP} + I_{b→qSV}].
- **Correlation function (Eq. 36):** Equiaxed grains with W(r) = exp(−r/L), giving W̃(q) = L³/[π²(1 + L²q²)²]. The argument of W̃ is |k_b(Q)p̂ − k_g(Q')ŝ|², which couples the incoming and outgoing wave vectors.
- **Rayleigh limit (Eqs. 62):** Integrals I_{b→g} become constants independent of direction and frequency, equal to ∫ r_g⁵(Q') × (polarization factor) × sin³Q' dQ'. Attenuation varies as ∝ x⁴ · f(Q) where f(Q) encodes the directional dependence through the slowness surface and polarization. All wave types have zero attenuation in the fiber direction (Q = 0°) because properties do not vary along the fiber.
- **Stainless steel results:** Using c₁₁ = 2.16×10¹¹, c₁₂ = 1.45×10¹¹, c₄₄ = 1.29×10¹¹ Pa, density 7860 kg/m³. Integrals at Rayleigh limit: I_{b→SH} = 1.623, I_{b→qP} = 1.068, I_{b→qSV} = 0.627.
- **Angular dependence of Rayleigh attenuation (Fig. 2):** SH and qP maxima are perpendicular to fiber (Q = 90°); qSV has zero at 0° and 90°, with maximum at 47.1° rather than 45° — the difference from previous works is attributed to proper inclusion of wave polarization through the anisotropic Green's dyadic.
- **qSV anomaly at 69.3° (Figs. 5–6):** A secondary peak appears in both SH and qSV attenuations at the angle where the SH and qSV slowness surfaces intersect (69.3°). This is NOT a stochastic-geometric transition artifact (unlike suggestion by Ahmed and Thompson) — it appears in this purely Born approximation formulation below the geometric limit. The intersection of slowness surfaces maximizes the spatial correlation function's contribution.
- **Frequency evolution of qSV maximum (Figs. 5–6):** The direction of maximum qSV attenuation shifts from 47.1° in the Rayleigh limit, peaks at 51.8° at x_SH ≈ 1.8, then decreases at higher frequencies. This is more dramatic than Ahmed and Thompson's result and is attributed to the inclusion of polarization direction in G₀.
- **Cross-fiber attenuation increase (Figs. 3–4):** As frequency increases, the cross-fiber (Q = 90°) SH and qP attenuations increase more rapidly than other directions — a well-known result that is confirmed with the present formalism.
- **Normalization choice:** Rather than Voigt velocities, average wave speeds c̄_b = (1/2)∫ c_b(Q) sinQ dQ are used as reference, giving dimensionless frequency x_b = ωL/c̄_b.
- **Relationship to diffuse field:** The same inner products J‥ appear in backscatter and diffuse field problems; the attenuation expressions are directly linked to these.
- **Limitations:** Restricted to frequencies below the geometric optics limit (x_SH < ~10 for stainless steel). Mode conversion from one fiber-texture class to another (e.g., rolling texture with ODF W_lmn) would require different covariance expressions.

## Figures
- **Fig. 1 (p. 10 rendered):** Slowness surfaces for stainless steel with texture — closed polar curves for SH, qP, qSV showing anisotropy (deviation from circles). The SH curve is elongated in the cross-fiber direction; qP and qSV cross near 69°.
- **Fig. 2 (p. 10):** Dimensionless Rayleigh attenuation α·L/x⁴ vs. direction Q (polar plot) for SH, qP, qSV. SH and qP peak at Q = 90°; qSV has figure-8 shape peaking at ~47° and ~133° (symmetric) with zero at 0° and 90°.
- **Figs. 3–4 (p. 11 rendered):** Angular dependence of normalized SH and qP attenuations at five dimensionless frequencies x_SH = 0.2, 1, 2, 5, 10. Both show increasing cross-fiber attenuation with frequency. For qP a local maximum vs. Q evolves with frequency.
- **Fig. 5 (p. 11):** Angular dependence of normalized qSV attenuation at five frequencies. Notable secondary peak developing near 69.3° at intermediate frequencies, coinciding with SH/qSV slowness-surface intersection.
- **Fig. 6 (p. 11–12 rendered):** Direction of maximum qSV attenuation vs. dimensionless frequency x_SH — starts at 47.1° in Rayleigh limit, rises to ~51.8° at x_SH ≈ 1.8, then decreases. Smooth monotonic except near the secondary peak.
- **Figs. 7–8 (p. 12 rendered):** Normalized SH and qP attenuations vs. frequency for propagation at Q = 45°, 69.5°, 90°. Cross-fiber (90°) attenuation increases most rapidly; local maximum in qP at intermediate frequency visible.
- **Fig. 9 (p. 12):** Normalized qSV attenuation vs. frequency for Q = 45° and 69.5°. At 69.5° the attenuation is initially smaller but rises more steeply; their ratio appears to plateau at higher frequencies.
