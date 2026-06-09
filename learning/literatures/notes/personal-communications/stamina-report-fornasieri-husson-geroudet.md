# STAMINA Study Report — Viscosity Measurement of Oil in Engine

- **Source:** Stamina report Fornasieri Husson Géroudet.pdf
- **Drive link:** https://drive.google.com/file/d/1SHEAqikJ_5kOtrfHOT5E9TBbA_IaasUG/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Remi Husson, Maxime Fornasieri and Grégoire Géroudet, 2016 (University of Sheffield student project)
- **Coverage:** full

## Overview
A student project report applying the STAMINA method (amplitude mode) to measure the viscosity of engine oils. Two case studies are presented: (1) direct viscosity measurement of Newtonian Cannon standard oils without a matching layer, and (2) viscosity measurement with a magnesium matching layer inserted between the steel component and the oil, to increase the sensitivity of the measurement by reducing the reflection coefficient. Both cases involve deriving the standing wave reflection coefficient S from the infinite-sum model, solving for R numerically via bisection method, then extracting viscosity from the shear acoustic impedance relationship.

## Unique contribution
Extends the STAMINA white paper theory to include a matching layer configuration and derives the modified formula for S incorporating the matching layer reflections. Provides working MATLAB code and simulation plots comparing theoretical S vs. frequency against experimental data from Olivia Manfredi's measurements. Identifies systematic discrepancy between model and experiment and proposes explanations.

## Key concepts
- STAMINA amplitude method; reflection coefficient S
- Bisection method for solving non-linear equations (MATLAB)
- Cannon Newtonian standard oils (S3, S20, S60, S200, S600)
- Dynamic viscosity η (Pa·s)
- Matching layer; acoustic impedance matching
- Shear wave impedance of liquid: z_L = sqrt(ρ·η·ω)
- Reflection coefficient R and phase shift ϕ
- Geometric series / closed-form infinite sum of reflections
- Resonant frequency f_s; standing wave amplitude spectrum
- Attenuation coefficient α
- MATLAB simulation of standing waves

## Methods / results / takeaways
- **Case 1 (no matching layer):** S was computed from the closed-form series solution (equations 1-5/1-6). Bisection method solved simultaneously for R and ϕ given experimental S. Viscosity was then extracted from z_L. Model curve shapes agreed with experimental data (resonant peaks aligned at ~280 kHz for a 10 mm steel component), but model amplitude was consistently above measured values — equivalent viscosity was ~5× higher in the model than in experiment for S600 oil (η = 1.049 Pa·s). This discrepancy was observed for all five oils and was attributed to incorrect model constants (attenuation, speed of shear waves, etc.) rather than a fundamental flaw.
- **Case 2 (matching layer):** Added a magnesium matching layer (ρ = 1740 kg/m³, c_s = 3160 m/s). Theoretical S was significantly reduced (S_min down to 0.62–0.7 for η ≈ 1–2 Pa·s vs. ~0.97 without layer), confirming improved sensitivity. However the model did not match experimental data at all for the matching layer case, likely due to inaccurate layer thickness and material constants.
- **Key parameters used:** Steel c_s = 3250 m/s, ρ_s = 7800 kg/m³; magnesium c_s = 3160 m/s; S600 oil ρ = 843.5 kg/m³, η = 1.049 Pa·s; α = 1.5 Np/m; L = 5.77 mm.
- **Viscosity trend confirmed:** Lower S_min corresponds to higher oil viscosity; matching layer amplifies this sensitivity.
