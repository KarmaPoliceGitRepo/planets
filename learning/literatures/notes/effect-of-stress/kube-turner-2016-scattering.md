# Stress-Dependent Ultrasonic Scattering in Polycrystalline Materials

- **Source:** Kube & Turner 2016 stress-dependent scattering
- **Drive link:** https://drive.google.com/file/d/13BRgDczkKywLswJ7SUe5Hm8TtdSdwRgh/view
- **Type:** paper
- **Author/Year:** Christopher M. Kube & Joseph A. Turner, 2016
- **Coverage:** full (deep read)

## Overview
A 14-page theoretical paper (J. Acoust. Soc. Am. 139, 811–824, 2016) that derives stress-dependent differential scattering cross-sections for ultrasonic waves in polycrystalline materials. Extends the Born approximation grain-scattering framework by substituting stress-dependent elastic moduli (from Kube & Turner 2015) into the scattering coefficient expression, yielding nine mode-specific cross-sections (qP, qSV, SH combinations) as a function of uniaxial stress. Demonstrates for polycrystalline aluminum that scattering amplitude sensitivity to applied stress is 10–50× larger than phase velocity sensitivity over the same stress range.

## Unique contribution
First comprehensive derivation of stress-dependent grain scattering in polycrystals, providing nine explicit scattering cross-section formulas. Shows that amplitude-based scattering measurements can detect stress changes that would be nearly invisible to phase-velocity measurements. Identifies optimal scattering geometries (e.g., backscatter parallel to stress direction) and shows that the ratio of forward-scattered SH coefficients for perpendicular vs. parallel incidence deviates from unity only when stress is present, providing a potentially texture-independent stress indicator. Explicitly separates grain scattering from dislocation absorption, arguing that direct backscatter measurement is less contaminated by dislocation effects than either attenuation or phase velocity.

## Key concepts
- Stress-dependent scattering coefficients (nine modes: qP→qP, qP→qSV, qP→SH, qSV→qP, qSV→qSV, qSV→SH, SH→qP, SH→qSV, SH→SH)
- Differential scattering cross-section (Born approximation for polycrystals)
- Stress-dependent elastic moduli of polycrystal (covariance tensor N^{abcd}_{ijkl})
- Acoustoelastic effect in polycrystals; stress-induced transverse isotropy
- Grain boundary scattering; Rayleigh scattering regime
- Quasi-longitudinal (qP) and quasi-shear (qSV, SH) wave modes
- Stress-induced rotation of displacement vectors (angle ψ(θ))
- Thomsen anisotropy parameters (j₁, j₂, j₃) adapted for stress-induced anisotropy
- Uniaxial stress sensitivity; compressive vs. tensile asymmetry
- Texture vs. stress effects in backscatter

## Methods / results / takeaways

### Scattering model
- Scattering coefficient Ξ^{I→S} (Eq. 1) is derived via Born approximation for a randomly oriented polycrystal with stress-dependent single-grain elastic properties; depends on incident/scattered phase velocities v, v', directions n̂, n̂', polarizations ê, ê', grain radius L, density ρ, frequency ω, and the stress-dependent covariance tensor N^{abcd}_{ijkl}
- Under uniaxial stress σ₃₃, the phase velocities become anisotropic: three wave types (qP, qSV, SH) with velocities depending on propagation angle θ from the stress axis (Eq. 2, using Thomsen-like anisotropy parameters j₁, j₂, j₃)
- Displacement vectors of qP and qSV rotate by angle ψ(θ) (Eq. 6) away from principal directions, vanishing at θ=0 and θ=π/2 and when stress is absent
- All nine explicit scattering coefficients are given for backscatter (Eqs. 8, 9) and forward scatter (Eqs. 11, 12) in principal directions (parallel and perpendicular to stress)

### Numerical results for aluminum (σ₃₃ range ±500 MPa, f=10 MHz, L=15 μm)
- **qPk→qPk backscatter** (parallel to stress): changes by +38.8% from 0 to −500 MPa compression; phase velocity changes only ~2% for the same stress — scattering sensitivity is ~19× greater
- **qP⊥→qP⊥ backscatter** (perpendicular to stress): decreases by 8.3% from 0 to −500 MPa — directional asymmetry is large
- **Stress dependence is nonlinear**: N components are quadratic in stress for aluminum; tension and compression produce different magnitudes of change. Iron's N is linear in stress, predicting linear scattering stress-dependence
- **Frequency and grain size**: stress sensitivity of XqPk→qPk increases significantly above the Rayleigh scattering limit (larger ka); at high f or L, coefficient changes by +50% under 500 MPa compression, −22.5% under 500 MPa tension
- **Forward scatter ratios**: XqSVk→qSVk / XqSV⊥→qSV⊥ deviates from unity only under stress (Eq. 13); the qP and SH ratios also deviate and depend on N components, making them sensitive to texture as well as stress
- **3D scattering surfaces** (Figs. 3, 4): for incident wave normal to stress, the 3D scattering surface (plotted in θ', φ' space) changes shape and amplitude across nine mode combinations as stress varies from −500 to +500 MPa; qP→qP shows lobes concentrated forward; mode-converted surfaces show distinct off-axis structure

### Key tables
- **Table I**: Single-crystal elastic constants for aluminum (c₁₁, c₁₂, c₄₄; third-order constants c₁₁₁, c₁₁₂, c₁₂₃, c₁₄₄, c₁₅₅, c₄₅₆)
- **Table II**: All 44 independent components of the covariance tensor N for aluminum, in terms of K₀ (GPa²), K₁ (GPa), K₂ (dimensionless)
- **Table III**: Components K'_{ijkl} for aluminum

### Limitations and outlook
- Model assumes randomly textured (statistically isotropic) unstressed state; crystallographic texture creates competing effects that must be accounted for via a weighting factor on ensemble averages
- Dislocation contribution to attenuation not included — intentional; direct scattered response measurement is argued to be weakly influenced by dislocations relative to attenuation or phase velocity
- Experimental validation via pulse-echo or pitch-catch backscatter is the primary stated future direction

## Figures

- **Fig. 1** (p. 6): Spherical coordinate system showing incident wave direction n̂ (angles θ, φ from stress axis ẑ), scattered direction n̂' (angles θ', φ'), and stress-induced rotation of qP and qSV displacement vectors by angle ψ. Diagram illustrates how ψ rotates the polarization plane within the plane containing ẑ and n̂.

- **Fig. 2** (p. 7): Nine scattering coefficients Ξ^{I→S} (m⁻¹) vs. scattering angle θ' for incident wave parallel to uniaxial stress (θ=0), at f=10 MHz, L=15 μm. Five stress levels: −500 MPa (circles), −250 MPa, 0 (stars), +250 MPa, +500 MPa. Curves show strong, nonlinear dependence on stress level; compressive stress generally increases scattering amplitude, tensile decreases it. All nine mode combinations plotted in a 3×3 panel grid. qPk→qPk at backscatter (θ'=0) shows 38% change from 0 to −500 MPa.

- **Fig. 3** (p. 8, top): 3D forward-scattering surface plots for each of nine mode combinations with incident wave normal to stress (θ=π/2) under 500 MPa compression. Color encodes amplitude (blue=low, red=high). Surfaces show complex directionality: qP→qP has a broad forward lobe; mode-converted coefficients (qP→qSV, qSV→qP) show off-axis concentration. Forward scattering view (observer looking in −x direction into incoming wave).

- **Fig. 4** (p. 8, bottom): Backscatter view of the same nine 3D surfaces as Fig. 3. XqP→qP backscatter (into +x direction) changes from 5.12×10⁻⁴ to 6.73×10⁻⁴ m⁻¹ (+31.4%) as stress goes from −500 to +500 MPa. Backscatter along stress direction shows larger sensitivity than perpendicular.

- **Fig. 5** (p. 9–10): Backscatter coefficient Ξ vs. incident angle θ (from 0 to π/2) for all nine mode combinations; five stress values; f=10 MHz, L=15 μm. Shows that SH-mode backscatter is most sensitive to stress when propagating parallel to stress; qPk→qPk increases 38.8% while qP⊥→qP⊥ decreases 8.3% for the same compression range. In the stress-free isotropic case, qPk→qPk = qP⊥→qP⊥.

- **Fig. 6** (p. 10): Normalized stress-dependent backscatter qPk→qPk, plotted vs. σ₃₃ for multiple grain radii L (1–100 μm, fixed f=10 MHz) and multiple frequencies (1–100 MHz, fixed L=15 μm). Curves show that stress sensitivity is amplified at larger ka (beyond Rayleigh limit); at high frequency or large grain size the coefficient changes by +50%/−22.5% for ±500 MPa.

- **Fig. 7** (p. 12): Ratios of forward-scatter coefficients (qPk/qP⊥, qSVk/qSV⊥, SHk/SH⊥) vs. σ₃₃. All three ratios equal unity at zero stress (isotropic). Under 500 MPa compression: qP ratio increases 50.2%, SH ratio 40.3%, qSV ratio 7.8%. The qSV ratio depends only on the eighth power of the velocity ratio and thus responds purely to stress-induced anisotropy; the other two ratios additionally carry dependence on N components (and hence texture in real materials).
