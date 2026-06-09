# Wave-Induced Fluid Flow in Random Porous Media: Attenuation and Dispersion of Elastic Waves

- **Source:** 2005 - Wave-induced fluid flow in random porous media- Attenuation and dispersion of elastic waves - Tobias M. Muller.pdf
- **Drive link:** https://drive.google.com/file/d/1HzkboDcrVLH_8fMJuQw1Lzfw4_ewzwpf/view
- **Type:** paper
- **Author/Year:** Tobias M. Müller, Boris Gurevich / 2005 (J. Acoust. Soc. Am. 117(5), pp. 2732–2741)
- **Coverage:** full (deep read)

## Overview
An 11-page theoretical paper (Paper II in a series; Paper I treated wave propagation theory in the same setting) deriving closed-form analytical expressions for elastic wave attenuation Q⁻¹(ω) and phase velocity v(ω) in 3-D randomly inhomogeneous fluid-saturated porous media. The mechanism is wave-induced fluid flow (WIFF) between mesoscopic heterogeneities driven by pressure gradients set up during wave passage. The model applies first-order statistical smoothing approximation (FSSA) to Biot's poroelasticity equations with spatially varying coefficients. Attenuation and dispersion are expressed as linear integral transforms of the spatial autocorrelation function of the medium fluctuations, enabling closed-form results for exponential, Gaussian, and von Kármán correlation functions. The relationship to 1-D results (O'Doherty-Anstey theory, White's periodic model) and universal frequency asymptotics is established.

## Unique contribution
Extends WIFF attenuation theory from 1-D periodic/layered models to full 3-D randomly inhomogeneous poroelastic media. Shows that the universal frequency asymptotics — Q⁻¹ ∝ ω at low frequencies and Q⁻¹ ∝ ω⁻¹/² at high frequencies — hold in 3-D random media (not just periodic 1-D). Demonstrates that maximum attenuation occurs when the diffusion wavelength of Biot's slow wave equals the characteristic heterogeneity scale (ld = a). Provides explicit closed-form Q⁻¹(ω) and v(ω) for three standard correlation models and proves the causal Kramers-Kronig link between attenuation and dispersion as an intrinsic property of the model.

## Key concepts
- Biot theory / Biot poroelasticity
- Wave-induced fluid flow (WIFF) / mesoscopic fluid flow
- Patchy saturation / partial saturation
- Biot slow wave
- First-order statistical smoothing approximation (FSSA)
- Correlation function (exponential, Gaussian, von Kármán)
- Spectral filter function
- Kramers-Kronig relations in porous media
- Gassmann equation / Gassmann-Wood / Gassmann-Hill limits
- Quasi-static (relaxed) and no-flow (unrelaxed) velocity limits
- Seismic attenuation in heterogeneous rocks
- Squirt flow (discussed as related mechanism)

## Methods / results / takeaways

### Physical setup
- A 3-D porous elastic solid (background material: e.g., sandstone) is saturated with pore fluid. The poroelastic parameters H (saturated P-wave modulus), G (shear modulus), and C = αM have a random spatial component with normalized correlation function B(r) and variances σ²_HH, σ²_GG, σ²_CC, and cross-variances σ²_HG, σ²_HC, σ²_GC.
- Inhomogeneity scale a (correlation length) satisfies the mesoscopic condition: wavelength λ >> a >> pore size a_pore.

### Effective wave number (from Paper I)
The effective P-wave number k̄_p is:
k̄_p = k_p [1 + (D₂ - D₁·k_ps² ∫₀^∞ r B(r) exp(ik_ps r) dr)]

where k_ps = √(iωη / k₀N) is Biot's slow wave number, k₀ is permeability, η is fluid viscosity, N = MP_d/H is a Biot modulus combination, and D₁, D₂ are dimensionless coefficients depending on the variance combinations (Eqs. 2–3).

### Closed-form attenuation and dispersion
For exponential correlation B(r) = exp(-|r|/a):
- Q⁻¹(ω) = D₁ · 4(ak̄)²(2k̄a+1) / (1+2k̄a+2k̄²a²)²   [Eq. 24]
- v(ω) = v₀[1 + D₁ · 4(ak̄)³(1+k̄a) / (1+2k̄a+2k̄²a²)² − D₂]   [Eq. 25]
where k̄ = Im(k_ps).

For Gaussian correlation B(r) = exp(-r²/a²): involves complementary error function (erfc) sums.

For von Kármán correlation: involves generalized hypergeometric function ₃F₂ (Eqs. 31–32).

### Spectral filter function and resonance condition
Using the fluctuation spectrum (Fourier transform of B(r)), attenuation is expressed as:
Q⁻¹(ω) = 16πD₁ ∫₀^∞ [k̄²k⁴ / (4k̄⁴+k⁴)] F(k) dk   [Eq. 15]

The spectral filter U(k,k̄) = k̄²k⁴/(4k̄⁴+k⁴) peaks when k̄a ≈ 1, i.e., when diffusion wavelength ld = a. This is the resonance condition for maximum WIFF attenuation. Fig. 1 in paper illustrates the interplay of F(k) and U for different regimes.

### Frequency asymptotics
- Low frequency (k̄a << 1, relaxed regime): Q⁻¹ ∝ ω (attenuation coefficient α ∝ ω²).
- High frequency (k̄a >> 1, unrelaxed regime): Q⁻¹ ∝ ω⁻¹/² for exponential/von Kármán correlations; Q⁻¹ ∝ ω⁻¹ for Gaussian (because Gaussian is smooth at origin: B(r) → 1 + O(r²), so small-scale medium is nearly homogeneous).
- These asymptotes are universal in 3-D, coinciding with those for 1-D periodic structures (White's model, Norris 1993) — unexpected since 1-D random and periodic structures differ in their asymptotics.

### 3-D vs. 1-D comparison (Fig. 3)
For the same sandstone model with fluid bulk modulus fluctuations only (σ²_KfKf = 0.2, a = 25 cm):
- Magnitude of peak Q⁻¹ similar in 1-D and 3-D, but 3-D is slightly larger.
- Maximum attenuation frequency in 3-D: ω_max^3D = 2k₀N/(a²η), twice that of 1-D (ω_max^1D = k₀N/(a²η)).
- Implication: at seismic frequencies (10–100 Hz), 3-D attenuation due to WIFF is larger than 1-D prediction.

### Velocity limits
- Quasi-static (relaxed) limit: v_qs = v₀(1 − D₂) — fluid pressure fully equilibrated between patches; governed by Wood's harmonic average of fluid moduli.
- No-flow (unrelaxed) limit: v_nf = v₀(1 + D₁ − D₂) — fluid cannot flow between patches; governed by Hill average of saturated P-wave moduli.
- Relative dispersion magnitude: (v_nf − v_qs)/v₀ = D₁ — independent of correlation function shape and transport properties. Both limits are the same for 1-D and 3-D random media.
- In the case of fluid-only fluctuations: v_qs is obtained using Gassmann+Wood average; v_nf uses Gassmann+Hill average.

### Kramers-Kronig causality (Section III.B)
- The complex effective velocity g̃(ω) satisfies causality. Because g̃ diverges as ω → ∞, a twice-subtracted dispersion relation (method of subtractions, Eq. 18) is used.
- Real and imaginary parts of the regularized function L(ω) are proven to be Hilbert transform pairs (Eqs. 19–22), confirming that Q⁻¹ and v(ω) are a causal pair — attenuation and dispersion derived from the same model are automatically consistent.

### Modeling choices and cross-correlations (Fig. 4, rendered)
- Background sandstone parameters (Table I): Kg=40 GPa, Kd=4.5 GPa, G=9 GPa, ρg=2650 kg/m³, φ=0.17, k₀=250 mD, Kf=2.17 GPa (water), η=0.001 Pa·s, ρf=1000 kg/m³. Derived: Pd=16.5 GPa, α=0.89, M=10.4 GPa, H=24.7 GPa, N=6.9 GPa, Biot critical frequency vB=680 kHz.
- Negative cross-correlation between solid frame (Kd) and fluid bulk modulus (Kf): soft-frame inhomogeneity filled with stiff fluid → large pressure contrasts during wave passage → strongly enhanced attenuation and dispersion (Q⁻¹ up to 0.1, significant dispersion). Positive cross-correlation reduces attenuation.
- Even weak fluctuations (σ ~ 10%) can produce Q⁻¹ ≈ 0.01, which is at the lower bound of seismically observed attenuation.

### Correlation model comparison (Fig. 5, rendered)
All three correlation models (exponential, Gaussian, von Kármán) are plotted for the same medium parameters. Key differences:
- Gaussian: highest peak Q⁻¹ and symmetric Q⁻¹(ω) curve; high-frequency decay fastest (∝ 1/ω).
- Exponential: moderate peak; asymmetric (slower high-frequency decay ∝ ω⁻¹/²).
- Von Kármán (intermediate between exponential and Gaussian depending on Hurst exponent): tunable asymptote.
- The choice of correlation model matters significantly for the shape of the attenuation spectrum even when medium parameters are fixed.

### Physical interpretation and analogies (Section VI)
- WIFF attenuation mechanism is analogous to thermoelastic attenuation (heat flow between hot compressed and cold rarefied regions) and to attenuation in suspensions of particles in viscous fluid — all are relaxation mechanisms with the same universal Q⁻¹ ∝ ω (low-f) and ∝ ω⁻¹/² (high-f) asymptotics.
- The model is restricted to weakly inhomogeneous media (perturbation theory); strong contrasts require different approaches.
- Scattering attenuation (when λ ≈ a) is not included in this framework and requires a separate treatment.
- For real porous media at ultrasonic frequencies (> 1 MHz), the mesoscopic condition may break down if patch size a is small; at seismic frequencies (10–100 Hz), typical mesoscopic patch sizes (centimeters) are well within the model's applicability range.

### Practical implications for seismic surveying
- Velocity dispersion between seismic (10–100 Hz) and ultrasonic (1 MHz) frequency bands can be of order 100 m/s or more in partially saturated porous rock due to WIFF — relevant for calibrating laboratory ultrasonic measurements against field seismic data.
- The attenuation peak frequency scales as f_c ∝ k₀/(η a²): higher permeability or larger heterogeneity scale → attenuation peak at lower frequency.

## Figures

**Fig. 1 (p. 4 rendered):** The spectral filter function U(k, k̄) plotted alongside a representative fluctuation spectrum F(k). The filter peaks at k = k̄ (resonance), with U → 0 in both the low-frequency regime (k̄a << 1, fully relaxed) and high-frequency regime (k̄a >> 1, unrelaxed). The intermediate regime k̄a ≈ 1 controls the attenuation maximum.

**Fig. 2 (p. 6 rendered):** Q⁻¹ vs. normalized frequency (f/f_c) and P-wave velocity vs. normalized frequency for exponential correlation model at different correlation lengths a (a = 5, 25, 125 cm). Panels (a) and (b) respectively. Larger a shifts the dispersion and attenuation curves to lower frequencies. The quasi-static (low-f) and no-flow (high-f) velocity limits are shown as horizontal dashed lines. The dispersion is of the relaxation type: monotonic velocity increase from v_qs to v_nf.

**Fig. 3 (p. 7 rendered):** Comparison of Q⁻¹ (a) and velocity dispersion (b) between 1-D (O'Doherty-Anstey extension, dashed) and 3-D (present model, solid) for K_f fluctuations only. The 3-D peak is at twice the frequency of the 1-D peak and is slightly larger in magnitude. At seismic frequencies (below Biot critical frequency, arrow in panel a), the 3-D attenuation exceeds the 1-D prediction. The low- and high-frequency velocity limits coincide between 1-D and 3-D (because shear modulus is constant in this example).

**Fig. 4 (p. 7 rendered):** Q⁻¹ (a) and velocity (b) for differently correlated fluid/solid fluctuations: negatively correlated K_f with K_d (R = −1, dashed), uncorrelated (R = 0, solid), and positively correlated (R = +1, dotted). Negative correlation (soft frame + stiff fluid) produces the largest attenuation (Q⁻¹ > 0.01) and the largest velocity dispersion; positive correlation suppresses both effects.

**Fig. 5 (p. 8 rendered):** Comparison of Q⁻¹ (a) and velocity (b) for exponential, Gaussian, and von Kármán correlation functions with identical medium parameters. The Gaussian model produces the highest peak attenuation and the most rapid high-frequency decay (Q⁻¹ ∝ 1/ω), while the exponential model decays as ω⁻¹/². Von Kármán lies between, with the transition controlled by the Hurst exponent. The Gaussian is the only symmetric curve; all three share the same low-frequency Q⁻¹ ∝ ω asymptote.
