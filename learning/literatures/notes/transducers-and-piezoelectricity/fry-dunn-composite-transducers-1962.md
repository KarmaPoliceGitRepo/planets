# Ultrasonic Intensity Gain by Composite Transducers

- **Source:** Fry Dunn composite transducers 1962
- **Drive link:** https://drive.google.com/file/d/1uoVyY6nsyUm1UgnS_4vJcLIJn-ntmBeM/view
- **Type:** paper (The Journal of the Acoustical Society of America 34(2), 188–192, 1962)
- **Author/Year:** W. J. Fry, F. Dunn / 1962
- **Coverage:** full

## Overview
Foundational analytical paper deriving the intensity gain achievable by a piezoelectric element coupled to a radiation medium via a two-layer composite structure (spacing medium s + transmission medium p). Derives closed-form expressions for the gain G = I_composite / I_direct for four cases of single or combined quarter- and half-wavelength layers. Shows gains of 100–1000× are achievable into water using high-Z transmission plate (e.g. stainless steel) + low-Z spacing medium. Establishes that maximum gain for a single λ/4 layer is (R_r/R_s)² and for two quarter-wave layers is (R_p/R_r)² × (R_r/R_s)².

## Unique contribution
First rigorous analysis of the intensity gain from composite impedance-matching structures (spacing + transmission medium) for piezoelectric transducers. Introduces the concept that the gain of the composite transducer results from reduced motional impedance (i.e. the mechanical load presented to the piezoelectric element is reduced, enabling more current and power draw at the same driving voltage). Predicts 1000-fold intensity gain into water using stainless steel (Z ≈ 30 MRayl) transmission plate + water-impedance (Z ≈ 1.5 MRayl) spacing medium — both at λ/4 thickness.

## Key concepts
- System: PZT element at resonance (half-wave thick) + spacing medium (Z_s, L_s) + transmission plate (Z_p, L_p) + radiation medium (Z_r)
- Acoustic intensity into radiation medium: I_rc = 4e_ik² E² Re(1/Z_s)  [Eq. 1]
- Direct radiation: I_ra = 4e_ik² E² / R_r  [Eq. 5]
- Case 1 (L_s = λ_s/4, L_p = 0): G(λ_s/4) = (R_r/R_s)² × [bracketed frequency factor] — max at L_p = λ_p/4
- Case 2 (L_p = λ_p/4, L_s = 0): G(λ_p/4) < 1 if R_p/R_r > 1; gain only if R_p < R_r
- Case 3 (L_s = λ_s/2): periodic function of L_p; gain depends on ratio R_p/R_s and R_r
- Case 4 (L_s = λ_s/4, L_p = λ_p/4 — both QW): G = (R_p/R_s)² × depends on R_p/R_r
- Maximum gain for single λ/4 ML: (R_r/R_s)² if R_s << R_r
- Two λ/4 layers: gain = (R_p/R_r)² × (R_r/R_s)² = (R_p/R_s)² — independent of R_r
- Physical mechanism: reduced input mechanical impedance → more current at fixed voltage → more power radiated
- Temperature stability note: thinner QW layers preferred to minimise temperature-induced dimensional changes
- Application: high-intensity ultrasound for biophysics (10²–10³ W/cm²); biological tissue research

## Methods / results / takeaways
- Purely analytic; no experiments reported
- All media assumed acoustically lossless
- PZT at fundamental resonance (half-wave thickness); back face at zero acoustic impedance
- Gain formula for Case 4 two-QW layers: gain is (R_p/Rr) × f(R_p/Rr, L_p) — stainless steel + water-impedance spacer → G ≈ 1000 into water
- Intensity gains of 100–1000 achievable in liquids at transducer face
- With lens focusing: ultra-high intensity (10⁴–10⁵ W/cm²) beams possible
- Gain is periodic in layer thickness; odd multiples of λ/4 give identical gains
- Method extends to N layers (see Dianov 1960 for N-layer generalisation)
- Historical note: this paper is cited by DeSilets-Fraser-Kino 1978 and Khuri-Yakub 1988 as foundational composite transducer theory
- Application: high-intensity therapeutic ultrasound; NDE with focused beams; impedance transformer design
