# The Use of Complex Material Constants to Model the Dynamic Response of Piezoelectric Materials

- **Source:** Sherrit 1998 complex material constants
- **Drive link:** https://drive.google.com/file/d/1EVPSvyY8mvDUf2JbCbukwKsf4ka3Cb3f/view
- **Type:** paper (conference, IEEE Ultrasonics Symposium)
- **Author/Year:** S. Sherrit, B. K. Mukherjee / 1998
- **Coverage:** full

## Overview
Tutorial-style review paper discussing why complex material constants are needed to model piezoelectric materials and the physical origins of the losses. Covers the three types of losses (dielectric, elastic, piezoelectric) in the context of the linear piezoelectric constitutive equations. Reviews dispersion mechanisms (Zener, Debye, Havriliak-Negami, Cole-Cole models) for each loss type. Discusses the microscopic origins (domain wall motion, grain boundaries, thermal conduction, interstitial diffusion) and the macroscopic phase angles. Provides cautionary notes on measurement pitfalls.

## Unique contribution
Unifies the treatment of dielectric, elastic, and piezoelectric complex constants under a common framework based on Holland's (1967) convention, with detailed discussion of frequency-domain dispersion models applicable to each property type. Clarifies the sign convention (material constants written as a - ib where a,b > 0 for passive materials) and the passivity constraint (following Holland's positive-definiteness requirement). Discusses time-domain implications: only Debye-type dispersions are causally compatible.

## Key concepts
- Complex material constants: s^E* = s^E_r - i·s^E_i, d* = d_r - i·d_i, ε^T* = ε^T_r - i·ε^T_i
- Holland (1967) convention: imaginary component subtracted for passive material
- Three loss types: dielectric (tan δ_ε), elastic (tan δ_c), piezoelectric (tan δ_d)
- Debye relaxation model for elastic and dielectric dispersion
- Havriliak-Negami model (generalised Debye): (ε_0-ε_∞)/[1+(iωτ)^α]^β
- Zener anelasticity model for elastic stiffness
- Cole-Cole (α<1, β=1) and Davidson-Cole (α=1, β<1) as special cases
- 90° and 180° domain wall contributions to piezoelectric relaxation
- Smits (1976): Debye-type piezoelectric constant from double-well potential and domain wall motion
- Passivity limits on piezoelectric loss component (Holland 1967, Smits 1976)

## Methods / results / takeaways
- Elastic losses: complex c with imaginary part linked to attenuation α and velocity v via c = ρ(v_r + iv_i)²; Q = c_r/c_i (approximately independent of frequency for many solids → attenuation ∝ frequency)
- Dielectric losses: complex ε; tan δ = ε_i/ε_r; for PZT ceramics, loss primarily from polarisation lag, not ohmic conduction; RC circuit model inappropriate (implies 1/f frequency dependence which is not observed)
- Piezoelectric losses: Wang-Zhang-Cross experiments confirm piezoelectric phase angle; Smits (1976) thermodynamic derivation; passivity requires |d_i| ≤ √(s_i^E · ε_i^T) / 2
- Electromechanical coupling constant k: derived from other constants; its dispersion determined by combined dispersion of c^E, ε^T, and d
- Cautionary notes: (1) time-domain transforms require Debye-compatible dispersions to avoid causality violation; (2) parasitic L, C, R in measurement circuit can appear as artificial dispersion; (3) finite aspect ratios introduce apparent dispersion (Rayleigh correction term ∝ (a/l)² for rod)
