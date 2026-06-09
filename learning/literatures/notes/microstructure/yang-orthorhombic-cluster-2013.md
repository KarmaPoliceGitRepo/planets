# Ultrasonic Scattering in Polycrystals with Orientation Clusters of Orthorhombic Crystallites

- **Source:** Yang, Li, Rokhlin - orthorhombic crystallite clusters Wave Motion 2013
- **Drive link:** https://drive.google.com/file/d/1bY4HdJTLt5IFQJtxpFrg6UViN0fun8Mj/view
- **Type:** paper
- **Author/Year:** L. Yang, J. Li, S. I. Rokhlin / 2013
- **Coverage:** full (deep read)

## Overview
A theoretical paper developing a two-scale elastic wave scattering model for polycrystals composed of orthorhombic crystallites arranged in orientation clusters (microtexture regions, MTRs). Both individual crystallites and their clustering arrangements are treated as ellipsoidal; the crystallite texture within each cluster is described by a 3D generalized Gaussian ODF with three independent texture parameters (σ_θ, σ_φ, σ_ζ). The effective orthorhombic elastic constants of each cluster are computed by volume-averaging and used as the scattering input for a cluster-level Born-approximation model. The total attenuation and backscattering are the sum of cluster-scale and crystallite-scale contributions. Targeted specifically at titanium alloys (Ti-6Al-2Sn-4Zr-2Mo, near-α) where MTRs dominate inspection noise. Validated on two Ti-6242 samples with very different degrees of MTR development.

## Unique contribution
First model treating orthorhombic crystallite symmetry (rather than cubic or hexagonal) in a two-scale MTR+crystallite framework. Key innovations: (1) general 3D three-parameter ODF allowing orthorhombic cluster symmetry; (2) closed-form Rayleigh and stochastic asymptotes for orthorhombic elongated grains; (3) texture transition function M(σ) that smoothly connects the two asymptotic regimes for crystallite attenuation; (4) demonstration that several orders-of-magnitude variation in attenuation are possible for the same crystallite size simply by changing MTR texture strength; (5) experimental validation linking backscattering-derived cluster size to attenuation model without fitting adjustment.

## Key concepts
- Orthorhombic crystal symmetry (9 independent elastic constants)
- Microtexture regions (MTRs) / orientation clusters
- Two-scale scattering (cluster + crystallite)
- Three-parameter generalized Gaussian ODF
- Effective elastic constants of cluster (Cijkl from ODF averaging)
- Ellipsoidal grain and cluster shape
- Rayleigh and stochastic attenuation asymptotes for orthorhombic grains
- Texture transition function ⟨δc₃₃₃₃(σ)δc₃₃₃₃(σ)⟩
- Born approximation
- Backscattering coefficient (two-scale duplex)
- Attenuation-to-backscattering ratio for MTR size determination
- Ti-6Al-2Sn-4Zr-2Mo alloy

## Methods / results / takeaways
- **Physical model (Fig. 1a):** A polycrystal volume is completely filled with small crystallites (α phase, ~10 µm) grouped in large ellipsoidal MTRs (~100–500 µm containing ~thousands of crystallites). MTR preferred orientations are randomly distributed, so the macroscopic medium is elastically isotropic.
- **Covariance decomposition (Eq. 3):** Total covariance = cluster term + crystallite term: ⟨δc δc⟩_total = ⟨δC(σ)δC(σ)⟩_r · w_r + M(σ)·⟨δc δc⟩_α · w_α, where w_r, w_α are the spatial correlation functions of clusters and crystallites respectively.
- **ODF (Eq. 5):** F(θ,φ,ζ) = F₀ exp[(cosθ)/(2σ_θ) + (cosφ)/(2σ_φ) + (cosζ)/(2σ_ζ)]. At σ → 0: perfect crystal alignment; at σ → ∞: random orientation. The special case σ_φ = σ_ζ = ∞ reduces to the single-parameter ODF used in earlier work.
- **Effective elastic constants (Eq. 6):** C_ijkl = (1/8π²)∫∫∫ F(θ,φ,ζ) c_ijkl sin(θ) dφ dζ dθ. At σ = 0 all constants equal single-crystal values; at σ = ∞ they reduce to the isotropic Voigt average (C₁₁ = 145, C₁₂ = 74, C₄₄ = 35.6 GPa for the Ti alloy used).
- **Attenuation for orthorhombic grains (Eq. 7–10):** General integrals over scattering sphere for L→L, L→T, T→L, T→T modes, with inner products I_LL(X) = A_LL + B_LL·X² + C_LL·X⁴ and similarly for cross-mode terms. Full coefficients in Appendices B–C.
- **Rayleigh limit (Eq. 11):** α_L,T ∝ f⁴·V_eff·Δ_i/V^5, independent of grain shape — only the effective volume V = 8πa_x a_y a_z matters. Important: different shapes give the same Rayleigh attenuation if they have the same volume.
- **Stochastic limit (Eq. 12–14):** α^Stochastic_L ≈ π²f²·Δ₅/(V_L^6 ρ²)·a_ell, where a_ell is the ellipsoid radius in the propagation direction. Ratios of stochastic attenuations in different directions are simply proportional to the corresponding ellipsoid radii.
- **Total attenuation (Eq. 16):** α_total = α_cluster + α_crystallites, where α_cluster uses effective C_ij of the MTR and α_crystallites is multiplied by M(σ).
- **Texture transition function M(σ) (Eq. 17–18):** Approximates the averaged attenuation of crystallites whose orientation is statistically distributed (not perfectly random). For the uniaxial one-parameter case, M(σ) = ⟨δc₃₃₃₃(σ)δc₃₃₃₃(σ)⟩/BS_α; at σ → ∞, M = 1 (fully random, original crystallite attenuation); at σ → 0, M → 0 (perfect crystal-cluster, no crystallite scatter).
- **Backscattering (Eq. 19):** η^total = [BS_r/Q_r]·k⁴·V_r/(…)² + M(σ)·[BS_α/Q_α]·k⁴·V_α/(…)², where the first term represents cluster backscattering and the second crystallite backscattering.
- **Drastic clustering effect (Fig. 7 numerical):** For unified σ, changing σ from 0.05 to 5.0 changes total attenuation by orders of magnitude (cluster-dominated → crystallite-dominated) while cluster size stays constant. The dominant contributor switches: at σ = 0.05, clusters behave like large single crystals with high scattering contrast; at σ = 5.0, no clustering exists.
- **Two transitions in frequency response (Fig. 8):** At intermediate σ = 0.5, two characteristic humps appear in α vs. f: first at ~5 MHz (cluster Rayleigh → stochastic crossover) and second at ~40 MHz (crystallite Rayleigh → stochastic). The first is smoother because it is a Rayleigh-to-Rayleigh transition (cluster → crystallite, both ∝ f⁴).
- **Backscattering vs. frequency (Fig. 9):** At high frequency (>30 MHz), crystallite backscattering (X direction) becomes comparable to cluster backscattering even though clusters are 20× larger than crystallites — because backscattering is determined by the spectral content at spatial frequencies matching the scatterer size.
- **Experimental Ti-6242 samples:** Sample #1 (strong MTR, σ = 0.031): cluster radii 0.145×0.19×0.19 mm; attenuation coefficients ~1–3 dB/cm. Sample #3 (weaker MTR, σ = 0.22): cluster radii 0.035×0.08×0.025 mm; much lower attenuation. Tenfold attenuation difference between the two despite similar crystallite sizes.
- **Fitting procedure:** Step 1 — cluster radii from attenuation/backscattering ratio (ratio is MTR-orientation-parameter independent). Step 2 — σ from backscattering frequency dependence using cluster radii from step 1. Attenuation then predicted without additional fitting; reasonable agreement (Fig. 10).
- **Macroscopic Voigt velocities:** Insensitive to σ because the macroscopic average elastic constants depend only on the full random average; confirmed numerically.

## Figures
- **Fig. 1 (page 3, rendered p. 2 of PDF):** (a) Schematic of MTR microstructure — circles/ellipses representing crystallites grouped into dashed-ellipse MTRs; arrows show crystallographic orientation. (b) Geometry of ellipsoidal cluster showing wave propagation p and scattering s directions, with major ellipsoid axes ax, ay, az.
- **Fig. 2 (page 5, from TOC):** Crystallite crystallographic system x,y,z defined by 3 Euler angles in MTR coordinate system XT, YT, ZT. θ is the rotation about axis A.
- **Fig. 3 (p. 10 rendered):** Effective elastic constants C_ij(σ) vs. unified texture parameter σ (σ_ϕ = 3σ, σ_θ = σ, σ_ζ = 10σ). Shows smooth interpolation from single-crystal orthorhombic values (σ → 0) to isotropic values (σ → ∞, C₁₁ = 145, C₁₂ = 74 GPa). Non-monotonic curves reflect complex ODF averaging.
- **Fig. 4 (p. 10):** Same for two special symmetry cases where σ_ϕ ≈ ∞ with σ_θ varying — effective constants reduce to hexagonal symmetry for any σ in this case; the two parameter sets overlay.
- **Fig. 6 (p. 11 rendered):** Attenuation coefficients vs. frequency for single-phase orthorhombic grains (no clustering), propagation in Z and X directions. Rayleigh (f⁴) and stochastic (f²) asymptotes shown as dotted/dashed. Clear hump visible in longitudinal wave near Rayleigh-stochastic transition for Z direction.
- **Fig. 7 (p. 11 rendered):** Total attenuation vs. σ at 10, 15, 25 MHz (wave in Z). Orders-of-magnitude decrease in attenuation as σ increases. Cluster component (dashed) dominates at small σ; crystallite component (dotted) dominates at large σ.
- **Fig. 8 (p. 13 rendered):** Total attenuation vs. frequency at σ = 0.05, 0.5, 5.0. Two-transition behavior visible at σ = 0.5; total α at σ = 5.0 ≈ crystallite α at σ = 0.5 (clustering absent).
- **Fig. 9 (p. 14 rendered):** Total backscattering amplitude √η vs. frequency for X, Y, Z propagation (solid lines). Dashed: cluster contribution; dotted: crystallite in X direction. Above ~30 MHz, crystallite backscattering in X direction is comparable to cluster backscattering.
- **Fig. 10 (p. 13 rendered):** Comparison of theoretical (solid) and measured (dashed) attenuation vs. frequency for two Ti alloy samples #1 and #3 in three directions. Sample #1 has ~10× higher attenuation than #3. Model without additional fitting shows reasonable agreement once σ and cluster radii are determined from backscattering.
