# A Unified Theory for Elastic Wave Propagation in Polycrystalline Materials

- **Source:** Stanke and Kino JASA 75 1984
- **Drive link:** https://drive.google.com/file/d/11ViFems1RHxF4WUKgJ5rB4FUxCFGPSWL/view
- **Type:** paper
- **Author/Year:** F. E. Stanke, G. S. Kino / 1984
- **Coverage:** full (deep read)

## Overview
The landmark paper establishing a unified perturbation theory for elastic wave propagation (velocity and attenuation) in randomly oriented, single-phase polycrystalline aggregates. Extends earlier work by Lifshitz-Parkhomovskii, Merkulov, and Huntington to a self-consistent Keller (second-order, multiple-scattering) formulation valid across all frequency regimes: Rayleigh, stochastic, and geometric/diffusive. Numerical results are presented for polycrystalline aluminum and iron over six decades of normalized frequency.

## Unique contribution
Derives a single set of algebraic equations (one each for longitudinal and shear complex wavenumber) for untextured, cubic-symmetry, equiaxed polycrystals using an inverse-exponential spatial autocorrelation function. These equations recover all known limiting-case results — the f⁴ Rayleigh law, the f² stochastic asymptote, and the geometric limit — as analytic sub-cases, and uniquely describe the cross-over transitions, including a previously unexplained "hump" in longitudinal attenuation near the Rayleigh-stochastic transition. Validated on Al and Fe covering more than two decades of frequency. The formalism is stated for general symmetry and texture, though numerical results are only given for the cubic/untextured case.

## Key concepts
- Unified scattering theory
- Keller approximation (second-order, multiple-scattering)
- Dyson equation / Bourret approximation
- Self-consistent perturbation
- Rayleigh, stochastic, geometric frequency regimes
- Rayleigh-stochastic hump (longitudinal waves)
- Cubic polycrystal
- Exponential two-point spatial autocorrelation function (correlation length l)
- Effective medium (Voight-averaged)
- Equiaxed grains
- Grain correlation function W(r)
- Anisotropy factor ν = C₁₁ − C₁₂ − 2C₄₄
- Inhomogeneity parameter ε
- Mode conversion (L → S scattering)
- Scalar, dielectric, isotropic, anisotropic characterizations

## Methods / results / takeaways
- **Theoretical framework:** Uses the stochastic process model for grain geometry. The local elastic tensor is written C_ijkl(r) = C̄_ijkl + δC_ijkl(r) where fluctuations are characterized by an autocorrelation function W(r) = exp(−r/l) and an eighth-rank covariance tensor.
- **Keller vs. Born:** The second-order Keller approximation accounts for multiple scattering (mean field re-enters as source); this is what makes the solution valid at all frequencies. The simpler Born approximation is valid only for x₀ ≪ 1/ε. At high frequency the EMKA (EM analogy) is nearly indistinguishable from the full unified theory for aluminum.
- **Final coupled equations:** Implicit algebraic equations for x_l = k_l·d and x_s = k_s·d (complex), depending only on x₀l, x₀s, and ε_l, ε_s. No closed-form solution; solved numerically with Newton's method.
- **Rayleigh limits (explicit):** α_l ∝ ε_l²·x₀l⁵, α_s ∝ ε_s²·x₀s⁵, recovering Lifshitz-Parkhomovskii and Bhatia-Moore results exactly.
- **Stochastic asymptotes:** α_l ∝ ε_l²·x₀l², α_s ∝ ε_s²·x₀s², also matching Lifshitz-Parkhomovskii.
- **Geometric limit:** α → 1/d (independent of frequency and elastic properties).
- **The Rayleigh-stochastic hump for L waves:** The Rayleigh and stochastic asymptotes for longitudinal waves intersect at x₀l ≈ 0.17 — well inside the Rayleigh region. The stochastic asymptote under-predicts attenuation at the transition because most scattering at these frequencies is into shorter-wavelength shear waves. The unified solution therefore shows a "hump" (local slope < f²) in the Rayleigh-stochastic crossover for longitudinal waves. This resolves discrepancies noted by Papadakis for Ni and α-Brass.
- **Aluminum (low ε):** ε_l = 8.87×10⁻³, ε_s = 3.38×10⁻². Rayleigh limit, Born, and unified theory agree closely; stochastic-geometric transition at x₀l ≈ 113. The EMKA approximation is accurate to within ~35% at low frequency and indistinguishable at high frequency.
- **Iron (high ε):** ε_l = 4.34×10⁻², ε_s = 0.135. Rayleigh limit under-predicts by 12% for shear; stochastic asymptote deviates markedly in geometric region. Multiple scattering corrections become important at all frequencies.
- **Phase velocity:** In the Rayleigh region, velocity approaches the Voigt average (Hashin bound, to second order). A dispersive region spans the Rayleigh-stochastic transition. At high frequency velocity approaches a different, higher-order average. The unified theory lies closest to the Hashin upper bound in the quasistatic limit for both Al and Fe.
- **Dependence on grain size (Fig. 6):** When plotted as αλ vs. kd, the maximum of attenuation per wavelength occurs at d ≈ 1/(ε·k₀) where the material appears "most inhomogeneous." In the Rayleigh region α ∝ d³; in stochastic α ∝ d; in geometric α ∝ 1/d.
- **Experimental validation:** Agreement within ~10% over two decades of normalized frequency for aluminum; for iron, the high anisotropy makes even Born approximation inaccurate except in the geometric region.
- **Practical limitations:** Assumes single-phase cubic grains, untextured, equiaxed, weak anisotropy (ε ≪ 1), and an inverse-exponential grain correlation function. The paper notes extensions to texture and elongated grains (later pursued by Ahmed/Thompson and Turner).

## Figures
- **Fig. 1 (page 13 rendered):** Table I giving C₁₁, C₁₂, C₄₄ for Al and Fe. Adjacent: FIG. 1 — normalized attenuation for shear waves in Al vs. log(x₀s). Curves: (a) unified theory, (b) Rayleigh limit, (c) stochastic asymptote, (d) EMKA. The unified curve transitions smoothly through a sharp stochastic-geometric crossover; EMKA closely follows (a) except at very low frequency.
- **Fig. 2 (page 13):** Same layout for longitudinal waves in Al — the "hump" near the Rayleigh-stochastic transition is clearly visible as a region where slope is less than f². SKA (scalar analogy, d) diverges at low frequency.
- **Figs. 3–4 (page 14):** Same plots for iron. Stochastic asymptote and EMKA deviate substantially from the unified theory across a wider frequency range due to higher ε.
- **Fig. 5 (page 14):** Normalized velocity perturbation (v_p − V₀)/V₀ for shear waves in iron vs. frequency — dispersive S-curve shape between two plateau velocities; notable negative dispersion (velocity decreases) through the stochastic region.
- **Fig. 6 (page 16):** Attenuation per wavelength αλ vs. normalized grain size log(k₀d) for all four cases. The maxima shift with material; the geometric 1/d regime is visible as the downward-sloping portion at high k₀d.
- **Figs. 7–10 (page 16–17):** Phase velocity variations for Al (figs. 7–8) and Fe (figs. 9–10). Al shows near-indistinguishable unified/Born results; Fe shows large differences. The qSV-analog shows an intermediate plateau confirming non-trivial higher-order averaging.
