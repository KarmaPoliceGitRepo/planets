# 2D Temperature Field Reconstruction by Inverse Thermo-acoustic Analysis

- **Source:** 2020 1-s2.0-S0960148119315721-main.pdf
- **Drive link:** https://drive.google.com/file/d/1p0-pBTq-sEjQhnB92lC8z2ugzQ9Yq-rX/view
- **Type:** paper
- **Author/Year:** Wei et al. / 2020 — Renewable Energy 150:1108–1117
- **Coverage:** partial (large file)

## Overview
Presents a method for reconstructing both the surface and internal 2D temperature distributions of a heated plate using an inverse thermo-acoustic analysis. The algorithm accounts for bending (refraction) of ultrasonic ray paths under Fermat's principle and uses a conjugate gradient minimization scheme.

## Unique contribution
First application of Fermat-principle ray-bending corrections to 2D ultrasonic temperature tomography in steel, demonstrating improved accuracy over straight-ray assumptions. Provides the V(T) calibration for steel transverse waves.

## Key concepts
- 2D temperature field reconstruction
- Conjugate gradient method
- Fermat principle
- Ultrasonic ray bending / refraction
- Inverse problem
- Transverse (shear) wave velocity in steel

## Methods / results / takeaways
- Calibration equation for steel (shear waves, 25–230°C): V(T) = −0.4521·T + 3259.9 m/s (R² ≈ 0.999).
- The conjugate gradient method iteratively adjusts the 2D temperature map to minimize the difference between measured and simulated transit times.
- Fermat-principle ray tracing corrects for refraction of ultrasonic paths in non-uniform temperature gradients; neglecting this introduces systematic errors.
- Applied to a steel plate scenario; reconstructed temperature profiles match thermocouple measurements within acceptable tolerance.
