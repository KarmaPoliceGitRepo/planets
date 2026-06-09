# Comparison of Hughes-Kelly and Man-Lu Acoustoelastic Models

- **Source:** Castellano 2017 EURODYN advancements
- **Drive link:** https://drive.google.com/file/d/1t-EPOowkkfcthM1RwVVyK6ZdgeWwA-f1/view
- **Type:** paper
- **Author/Year:** Castellano et al., 2017
- **Coverage:** full

## Overview
Compares the classical Hughes-Kelly (HK) acoustoelastic model (requires TOE constants l, m, n) with the Man-Lu model (uses "universal relations" and needs only SOE constants + measured birefringence). Experimental results on steel specimens under uniaxial stress demonstrate that the Man-Lu approach achieves stress accuracy within 3.5% of the true value without requiring knowledge of third-order elastic constants.

## Unique contribution
Provides a direct, quantitative experimental comparison of HK vs. Man-Lu on the same specimens and stress states. Demonstrates that the Man-Lu model can achieve near-HK accuracy without TOE constants, which are often unavailable for specific alloys. Identifies that shear wave coefficients (K_S⊥ and K_S∥) are more experimentally stable than longitudinal wave coefficient K_L.

## Key concepts
- Hughes-Kelly model
- Man-Lu model
- "Universal relations" (acoustoelastic)
- Acoustoelastic coefficients K_L, K_S⊥, K_S∥
- Shear wave birefringence
- Third-order elastic constants (TOE)
- EURODYN conference paper

## Methods / results / takeaways
- HK model: requires l, m, n (Murnaghan) plus λ, μ (Lamé); gives absolute stress from velocity change
- Man-Lu model: derived from acoustoelastic "universal relations" without TOE constants; requires measurement of birefringence coefficient and one initial loading test to calibrate
- Experimental method: ultrasonic pulse-echo on steel specimens under known uniaxial tensile stress (up to yield); measure both longitudinal and shear wave velocity changes
- Man-Lu accuracy: within 3.5% of load-cell reference stress in elastic region; error grows to ~6% near yield point
- HK accuracy: 2–3% in elastic region when correct TOE constants used; sensitive to uncertainty in l, m, n
- Shear wave coefficients K_S⊥ and K_S∥ exhibited better stability (lower scatter) than K_L across multiple specimens
- K_L more sensitive to grain texture and surface preparation; less repeatable
- Practical recommendation: for materials where TOE constants are not available, Man-Lu gives acceptable accuracy for engineering stress assessment; for research-grade accuracy, HK with carefully measured constants preferred
