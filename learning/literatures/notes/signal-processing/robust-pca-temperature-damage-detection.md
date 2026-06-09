# Considering Temperature Effect on Robust PCA Orthogonal Distance as a Damage Detector

- **Source:** Considering temperature effect on robust principal component analysis orthogonal distance as a damage detector (2019) Mujica.pdf
- **Drive link:** https://drive.google.com/file/d/1WTNK-Ld4KQEEdEnl7sNIBY0RlvJ7gfNz/view
- **Type:** paper
- **Author/Year:** Mujica, Gharibnezhad, Rodellar & Todd / 2019
- **Coverage:** partial (large file, truncated extraction)

## Overview
Published in Structural Health Monitoring (SAGE, 2019). Proposes using the orthogonal distance (OD) from a robust PCA model as a damage-sensitive feature, with temperature compensation applied to mitigate the effect of temperature on this feature. Validated on a laboratory composite plate and a large-scale aerospace composite component.

## Unique contribution
Introduces robust PCA (RPCA) OD as a new damage detection feature that is resistant to outlier contamination, and applies temperature compensation to the RPCA-OD feature directly. Demonstrates applicability on both a simple lab specimen and a realistic large-scale aerospace structure.

## Key concepts
- Robust principal component analysis (RPCA)
- Orthogonal distance (OD)
- Principal component analysis (PCA)
- Damage detection
- Temperature compensation
- Ultrasonic guided waves
- Structural health monitoring (SHM)
- Composite materials
- Contribution analysis

## Methods / results / takeaways
- Classical PCA: finds principal components; OD = distance from data point to PCA subspace; sensitive to damage.
- Robust PCA: uses M-estimators or minimum covariance determinant to be insensitive to outliers (damage data).
- RPCA-OD computed from ultrasonic guided wave features; increases when damage is present.
- Temperature effect: changes wave velocity and amplitude, shifting OD values even without damage; must be compensated.
- Temperature compensation applied to the RPCA-OD feature (not the raw signal); linear compensation based on temperature measurements.
- Validated on composite plate (lab scale) and large composite component (aerospace scale); promising detection results at both scales.
