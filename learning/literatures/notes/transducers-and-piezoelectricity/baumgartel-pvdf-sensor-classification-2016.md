# Classification of PVDF Sensors Under Different Load and Environmental Conditions

- **Source:** Baumgartel PVDF sensor classification 2016
- **Drive link:** https://drive.google.com/file/d/1vhiR4napbOpj7ojxOQ7jY8Kp_85kOB47/view
- **Type:** paper (Procedia Technology 26, 491–498, 2016; SysInt 2016 conference)
- **Author/Year:** G. Baumgärtel, S. Flock, T. Licht, et al. / 2016
- **Coverage:** full

## Overview
Characterises 20 PVDF DT1-52K/L sensor specimens across frequency (50–2000 Hz), temperature (−5 to 35°C), and compressive preload conditions. Measures piezoelectric d31 coefficient and Young's modulus E1 simultaneously. Develops a COMSOL FE model of the sensor as a single virtual isotropic block to validate electrical output predictions. Finds significant element-to-element variation (±12%) but partial temperature compensation from opposing d31 and E1 temperature trends.

## Unique contribution
First systematic classification of PVDF DT1-52K/L sensors showing that d31 and E1 have opposing temperature dependencies that partially cancel in the product d31·E1 (which governs sensor output). Demonstrates a COMSOL FE model with only 2 fitting parameters that predicts charge amplitude to within 0.55% and phase to within −1.20° across the characterised frequency range, enabling virtual sensor calibration.

## Key concepts
- PVDF DT1-52K/L: 52 μm thick PVDF film with laminated electrodes; d31 mode (in-plane strain → thickness polarization)
- d31 range: 20–30 pC/N at room temperature; increases with temperature to ≈35 pC/N at 35°C
- E1 range: 3–4 GPa at room temperature (50–2000 Hz); increases at low temperature to ≈5 GPa at −5°C
- Temperature compensation: d31 ↑ with T, E1 ↓ with T → product d31·E1 partially compensates
- Frequency dependence: E1 shows slight increase with frequency (viscoelastic behavior); d31 relatively flat
- Element variation: ±12% standard deviation across 20 specimens (from manufacturing variability)
- COMSOL FE model: single virtual isotropic block; complex E1* = E1(1+iη) with loss factor η
- FE model validation: charge amplitude deviation 0.55%, phase deviation −1.20° (excellent agreement)

## Methods / results / takeaways
- Sensor: PVDF DT1-52K/L (Measurement Specialties/TE Connectivity); 52 μm thick, 10×10 mm active area
- Test rig: compressive preload applied; sinusoidal force excitation 50–2000 Hz
- Temperature chamber: −5 to 35°C; measurements at 5°C intervals
- 20 sensor specimens tested; statistical analysis of d31 and E1 distributions
- d31 measurement: charge output / applied stress × inverse of thickness; separated from E1
- E1 measurement: from dynamic compliance with known geometry and force
- Preload effect: moderate preload (up to 100 N) has minor effect on d31 and E1
- FE software: COMSOL Multiphysics; structural mechanics + piezoelectric module
- Model parameters: E1(f), η(f) from measurement; geometry and boundary conditions from datasheet
- Application: load cell, vibration measurement, force monitoring in structural health monitoring (SHM); classification data enables sensor selection for precision applications
