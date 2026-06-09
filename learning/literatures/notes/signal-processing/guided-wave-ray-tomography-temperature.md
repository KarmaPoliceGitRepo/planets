# A New Approach to Guided Wave Ray Tomography for Temperature-Robust Damage Detection

- **Source:** New Approach to Guided Wave Ray Tomography (2018) D L.pdf
- **Drive link:** https://drive.google.com/file/d/10cHRGP5pamI11mFoUO7uGZ7O8Y89wD1w/view
- **Type:** paper
- **Author/Year:** Li, Shi, Xu, Liu, Zhang & Ta / 2018
- **Coverage:** partial (large file, truncated extraction)

## Overview
Published in Sensors (MDPI), 2018. Develops a guided wave ray tomography approach for damage detection that incorporates TOF temperature compensation based on the linear TOF-temperature relationship, using elastic net penalty-based inversion to perform thickness change mapping while being robust to temperature variation.

## Unique contribution
Demonstrates that guided wave ray tomography for SHM can be made temperature-robust by directly compensating baseline TOF using only temperature measurements (no estimation of compensation parameters), combined with elastic net regularisation in the reconstruction inversion.

## Key concepts
- Guided wave ray tomography
- Time-of-flight (TOF) temperature compensation
- Elastic net penalty (L1+L2 regularisation)
- Thickness change mapping
- Structural health monitoring (SHM)
- Piezoelectric sensors
- Isotropic plate

## Methods / results / takeaways
- TOF-temperature relationship is linear; baseline TOF can be scaled by measured temperature ratio to compensate for temperature change without needing separate calibration of stretch parameters.
- Tomographic inversion: minimise TOF misfit between inspected and temperature-compensated baseline TOFs using elastic net (L1+L2) penalty.
- Elastic net combines L1 (sparsity, Lasso) and L2 (smoothness, Ridge) regularisation; suited for sparse damage maps with some spatial continuity.
- Method eliminates false artefacts from temperature effects visible in naive (uncompensated) tomography.
- Validated on isotropic plates with piezoelectric sensors; accurate thickness change maps produced.
