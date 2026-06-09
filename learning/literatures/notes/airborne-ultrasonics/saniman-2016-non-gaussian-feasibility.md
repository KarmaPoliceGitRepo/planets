# Feasibility Study on Characterization of Non-Gaussian Rough Surface by Ultrasonic Reflection Method with the Kirchhoff Theory

- **Source:** Saniman 2016 non-Gaussian feasibility
- **Drive link:** https://drive.google.com/file/d/1ifHUF7xii0ZTxp7M9Hn12Bv6xUUU7xRh/view
- **Type:** paper
- **Author/Year:** Saniman & Ihara, 2016 (Mechanical Engineering Journal, 3(6), 16-00162)
- **Coverage:** full

## Overview
Feasibility study for ultrasonically characterising non-Gaussian rough surfaces. Derives a modified Kirchhoff reflection coefficient equation incorporating skewness Rsk via a proposed Gaussian curve-fitting method applied to the "bearing surface" (non-tail) region of the Johnson distribution. Validates at 0.35 MHz air-coupled normal incidence on 13 sandpaper specimens (Rq = 15–100 μm, |Rsk| = 0–0.92). Ultrasonically estimated Rq agrees with stylus profilometer within ~10% when known Rsk is used.

## Unique contribution
Precursor to the full two-config method (Saniman 2020). Introduces the Gaussian fitting to the non-tail region of Johnson distribution to obtain an effective Rq' (bearing-surface rms), yielding a closed-form modified Kirchhoff equation. Shows experimentally that Rsk significantly affects reflected amplitude at large roughness, confirming the need for non-Gaussian models.

## Key concepts
- Non-Gaussian roughness characterisation
- Johnson distribution (skewed height PDF)
- Gaussian curve fitting to bearing surface
- Modified Kirchhoff equation with Rsk
- Effective bearing-surface roughness Rq' = 1.864/(1.864 + 0.059|Rsk|) × Rq
- Air-coupled 0.35/0.4 MHz normal incidence
- Kurtosis-skewness coupling: Rku = 1.89Rsk² + 1.65|Rsk| + 3

## Methods / results / takeaways
- Key derivation: Rq' = 1.864/(1.864 + 0.059|Rsk|) × Rq; for Rsk=0, Rq'=Rq; for |Rsk|=1, Rq'≈0.96×Rq; effect is modest but significant at large Rq.
- Modified reflection coefficient: IMK = exp[−2k²Rq'²] vs. original IOK = exp[−2k²Rq²].
- Experiment: 13 sandpapers, 15 mm × 20 mm transducer (Japan Probe), 0.35 MHz, 30 mm separation, normal incidence; 300-average signals.
- Result: RqUT-MK from IMK with known RskSP agrees with stylus RqSP within ~10%; RqUT-OK (using original Kirchhoff) shows large errors for skewed specimens.
- Limitation: requires known Rsk to estimate Rq → next step is simultaneous Rq+Rsk extraction (addressed in Saniman 2020).
