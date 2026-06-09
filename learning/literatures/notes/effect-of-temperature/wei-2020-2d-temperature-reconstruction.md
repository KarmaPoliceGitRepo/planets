# 2D Temperature Field Reconstruction by Inverse Thermo-acoustic Analysis

- **Source:** 2020 1-s2.0-S0960148119315721-main.pdf
- **Drive link:** https://drive.google.com/file/d/1p0-pBTq-sEjQhnB92lC8z2ugzQ9Yq-rX/view
- **Type:** paper
- **Author/Year:** Dong Wei, Xiaofeng Yang, Youan Shi, Guangming Xiao, Yanxia Du, Yewei Gui / State Key Laboratory of Aerodynamics, CARDC, Mianyang, China / 2020 — Renewable Energy 150:1108–1117
- **Coverage:** full (deep read)

## Overview
A 10-page journal article presenting a method for simultaneously reconstructing the surface and internal 2D transient temperature distributions in a heated solid structure using pulse-echo ultrasonic measurements. The novelty relative to earlier work is the combination of (1) Fermat-principle ray-path bending correction in 2D non-uniform temperature fields, and (2) an inverse thermo-acoustic coupling formulation solved by the conjugate gradient method (CGM), which avoids the need for prior knowledge of the temperature profile and is not restricted to particular boundary condition forms. The demonstration is computational (verified numerically), targeting steel plates in aerospace/energy processing contexts.

## Unique contribution
The paper is the first to combine explicit 2D ray-bending (Fermat tracing in a solid) with a CGM-based inversion that reconstructs the heat-flux boundary condition directly rather than the temperature field itself; from the boundary condition, the full 2D temperature field follows from the direct heat-conduction calculation. This decoupling into (i) inverse for boundary condition + (ii) forward heat conduction is more robust than direct temperature-field tomography because the heat-equation constraint regularises the solution. The paper also quantifies critical measurement requirements: timing error must be below 1 ns for good reconstruction quality; a minimum of ~26 measurement points is needed for < 5% surface heat-flux error.

## Key concepts
- 2D temperature field reconstruction (surface + internal simultaneously)
- Ultrasonic thermometry — thermo-acoustic coupling
- Fermat-principle ray bending in non-uniform temperature fields
- Conjugate gradient method (CGM) for inverse heat-transfer
- Pulse-echo measurement geometry (single-sided)
- V(T) calibration for steel shear (transverse) waves
- Lagrange multiplier / adjoint equation approach
- Adjoint problem — backward heat equation for sensitivity
- Effect of measurement error on inversion quality
- Optimal spatial distribution of measurement points
- Blind zone — critical angle causing "turn-back" of rays

## Methods / results / takeaways

### Physical model
The structure is a 2D steel plate (10 cm × 5 cm) with one boundary heated and the others adiabatic. N ultrasonic probes are placed uniformly along the unheated top surface. Each probe makes a pulse-echo measurement; the transit time for the i-th probe is:

tᵢ = 2 ∫₀^Lᵢ dLᵢ / V(T(x,y))

where the path Lᵢ curves due to ray bending.

### Ray-path prediction (Fermat tracing)
The Euler-Lagrange equation for the minimum-time path gives:

y'' = (1 + y'²)/V · (y'·∂T/∂x − ∂T/∂y) · dV/dT

This is a second-order nonlinear ODE coupled to the temperature field, solved numerically at each iteration. Figure 4 shows that numerical and analytical solutions of ray paths in air agree to < 0.5%. Figure 5 shows that in a solid (temperature rising from right to left, 400–988 K), shear waves (dashed) and longitudinal waves (solid) both bend but in the opposite direction to air (because V decreases with T in solids, whereas V increases with T in air). Shear waves bend more than longitudinal at the same angle because V_S < V_L. When the incident angle exceeds a critical value (~73.6° for the parameters shown), a "turn-back" occurs and a detection blind zone forms.

### V(T) calibration — steel shear waves
Measured relationship (25–230°C, pulse-echo experiments):

V(T) = −0.4521·T + 3259.9 m/s  (R² ≈ 0.999)

The initial temperature field is 300 K; maximum measurement time 30 s.

### Inverse algorithm: conjugate gradient method
The inversion minimises the cost function:

J(q) = Σₙ Σᵢ [tˢ·ᵉˣ(Lₙ,tᵢ) − tˢ·ᵐ(Lₙ,tᵢ)]²

where tˢ·ᵉˣ is the transit time predicted from the forward model and tˢ·ᵐ is measured. The boundary condition q(x,0,t) (surface heat flux) is the primary unknown. The iterative update is:

q^(l+1) = q^l − β^l · P^l

where P^l is the conjugate gradient direction and β^l is the step length derived analytically from an adjoint (backward) heat-equation calculation. Convergence is fast (typically < 50 iterations shown in Figure 3 flowchart).

### Verification results
**Surface heat flux** (Figure 6): The inverted spatial and temporal heat-flux distribution on the heated boundary agrees with the true values to < 1% maximum error for 20 measurement points.

**Surface boundary temperature** (Figures 7–8): Temperature rise histories at selected surface points match the true values; deviations are largest at t = 30 s (end of record) due to fewer data points, but errors remain small (< few K).

**2D temperature field** (Figure 9): At 16 s and 30 s the reconstructed full 2D temperature contour maps (in K) agree very well with the exact (FE) solution. The contours are nearly horizontal (gradient in y-direction), as expected for heating from one face.

### Effect of measurement error (Section 5.1)
White noise with σ = 0.1, 1.0, 10 ns added to transit times. Key result: reconstruction accuracy degrades significantly for σ > 1 ns. For centimetre-scale samples, a 1 °C temperature change corresponds to ~1 ns transit-time change. Existing ultrasonic digitisers can readily achieve < 1 ns timing resolution. At σ = 10 ns the heat-flux profile in the transition zone has ~7% maximum deviation (Figure 10), but the reconstructed 2D temperature field still captures the correct gradient trend (Figure 11). The algorithm is robust because the heat-conduction constraint suppresses high-frequency noise in the reconstructed field.

### Effect of number of measurement points (Section 5.2)
With 10 measurement points, non-physical oscillations appear in the reconstructed heat flux (Figure 12). Increasing to 20 or 40 points suppresses oscillation. Non-uniform point placement (more points in the region of high spatial gradient) outperforms uniform placement at the same total count (Figure 14). The minimum threshold for < 5% E_q_x error is approximately 26 uniformly distributed points for the tested geometry (Figure 15). E_q_x decreases monotonically with number of points at all measurement times.

### Comparison to Wadley 1986 / Ihara methods
Wei et al. extend 1D pulse-echo inversion (Ihara-Takahashi, cited as [4]) and Norton-Wadley TOF tomography (cited as [8]) by adding 2D Fermat ray tracing and the adjoint-CGM boundary-condition inversion, removing the need for prior temperature profile knowledge and specific boundary condition assumptions.

## Figures

**Fig. 1** (p. 1109): 2D model schematic: steel plate 10 cm × 5 cm with heat-flux q(x,t) applied at the bottom face (y = 0); N ultrasonic probes on the top surface (y = H); curved ray paths from each probe to the heated face and back are indicated.

**Fig. 2** (p. 1110): Flowchart for numerical prediction of 2D ultrasonic propagation path using Fermat's theorem; shows coordinate-rotation logic for handling rays that deviate from the x-axis.

**Fig. 3** (p. 1111): Overall flowchart of the temperature-field reconstruction algorithm: initialise boundary condition → solve heat conduction (forward) → trace ray paths (Fermat) → compute transit times → compare to measured → CGM update → iterate.

**Fig. 4** (p. 1112, top): Numerical vs analytical ultrasonic propagation paths in air under a non-uniform temperature gradient (400–988 K from centre to top). Coloured background is the temperature field (rainbow scale); ray paths at various incident angles (0°–50°) bend strongly upward (toward hot, high-velocity region in air). Inset shows < 0.5% agreement between numerical and analytical solutions.

**Fig. 5** (p. 1112, bottom): Propagation paths of shear (dashed red) and longitudinal (solid black) waves in a steel solid structure under the same temperature gradient (400–988 K). Rays bend downward (toward low-velocity, high-T region in solid, opposite to air). Critical turn-back angle for shear ≈ 73.6°, for longitudinal ≈ 80°. At larger angles, rays reflect back creating detection blind zones.

**Fig. 6** (p. 1113): 3D surface plot of estimated vs true surface heat flux distribution q(x, t) over the spatial coordinate x and time t. Agreement is very good; maximum error < 1% at t = 30 s.

**Fig. 7** (p. 1113): Line plots of temperature rise history T(t) at three points on the heated boundary; estimated (dashed) vs exact (solid). Largest deviation at t = 30 s.

**Fig. 8** (p. 1113): Temperature distribution T(x) along the heated boundary at several measurement times t; estimated vs exact. Good spatial agreement; small deviations in the region of rapid spatial variation.

**Fig. 9** (p. 1114): 2D contour maps of temperature distribution at (a) 16 s and (b) 30 s. Each panel: left = full field, right = inset zoom of bottom-left corner. Red dashed = exact; green solid = estimated. Near-perfect overlap of isotherms.

**Fig. 10** (p. 1115): 3D surface plot of reconstructed surface heat flux under three levels of timing noise (σ = 0.1, 1, 10 ns). The σ = 10 ns case shows visible oscillation especially near transition.

**Fig. 11** (p. 1115): Reconstructed internal temperature field at 16 s and 30 s with σ = 1 ns noise; the temperature gradient is correctly reproduced even with noise, demonstrating regularisation effect.

**Fig. 12** (p. 1115): Reconstructed surface heat flux for 10, 20 and 40 measurement points (uniform layout). The 10-point case has obvious non-physical oscillations.

**Fig. 13** (p. 1116): Temperature distribution T(x) on the heated surface for 20 and 40 measurement points at two times.

**Fig. 14** (p. 1116): Surface temperature estimated with uniform vs non-uniform measurement point layouts (both 15 points); non-uniform placement in the high-gradient region gives better accuracy.

**Fig. 15** (p. 1116): E_q_x (relative RMS heat-flux error) vs number of measurement points at several times; error decreases monotonically; minimum ~26 points needed for < 5% error with the tested thermal boundary.
