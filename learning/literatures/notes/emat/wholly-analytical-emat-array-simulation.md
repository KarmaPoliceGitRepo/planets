# A Wholly Analytical Method for the Simulation of an EMAT Array

- **Source:** A Wholly Analytical Method for the Simulation of an Electromagnetic acoustiuc transducer array.pdf
- **Drive link:** https://drive.google.com/file/d/1854ug3lkBI0b_zadL4MQFfCGiferAZk7/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** Yuedong Xie, Liyuan Yin, Sergio Rodriguez G, Tiemei Yang, Zenghua Liu, Wuliang Yin (University of Manchester et al.) — circa 2016
- **Coverage:** full

## Overview
This paper proposes a fully analytical simulation pipeline for Electromagnetic Acoustic Transducer (EMAT) arrays. It adapts the classic Dodd–Deeds closed-form solution (originally for circular coils) to model a meander-line coil via a large-radius extrapolation, yielding eddy-current and vector-potential distributions without numerical meshing. The resulting Lorentz force density is then fed into an analytical surface-wave propagation model to predict beam directivity and displacement fields. The approach is validated against FEM (Ansoft Maxwell / COMSOL / Abaqus) at multiple frequencies.

## Unique contribution
Prior EMAT simulation work always used FEM for at least one of the two sub-problems (electromagnetic or ultrasonic). This paper is the first (by the authors' account) to use purely analytical methods for both stages, eliminating discretisation error and mesh-density limitations — especially valuable at high frequencies (1 MHz range) where FEM accuracy degrades. The large-radius extrapolation trick to convert circular-coil Dodd–Deeds solutions into straight-wire (meander-line) solutions is the key novel adaptation.

## Key concepts
- Electromagnetic Acoustic Transducer (EMAT)
- Meander-line coil
- Dodd–Deeds analytical solution
- Eddy current / vector potential
- Lorentz force mechanism
- Skin depth
- Rayleigh (surface) wave
- Beam directivity / steering angle
- Finite Element Method (FEM) — used as comparison baseline
- Finite-Difference Time-Domain (FDTD)
- Non-destructive testing (NDT)
- Constructive / destructive interference of ultrasonic waves

## Methods / results / takeaways
**Electromagnetic simulation:**
- Governing equation is the magnetic vector potential A; Dodd–Deeds gives a closed-form integral over Bessel functions for a circular coil above a layered conductor.
- Large-radius extrapolation (mean radius → 10.05 m) turns the circular-coil solution into a straight-wire solution, then superposition over all wire segments gives the meander-coil field.
- Verified at 1 kHz and 1 MHz against Ansoft Maxwell FEM. At 1 MHz the analytical curve is smoother; FEM shows numerical artefacts even with fine mesh. At depths beyond the skin depth (e.g. 3 mm at 1 kHz, skin depth ≈ 2.58 mm) the analytical result also outperforms FEM.
- Test case: stainless steel plate 1000×1000×3 mm³; NdFeB35 magnet 80×80×30 mm³; coil current 50 A peak; lift-off 1 mm; operating frequency 500 kHz; skin depth 0.679 mm.

**Ultrasonic simulation:**
- Uses Nakano (1930) far-field analytical displacement formulas for radial (u_r) and tangential (u_θ) surface-wave displacement due to a point force on a semi-infinite elastic solid.
- 74 discrete point forces distributed along the 12 alternating Lorentz force lines of the meander coil (6 inner + 7 outer points per line), superposed to get total field.
- Meander coil pitch = half Rayleigh wavelength (3.033 mm at 500 kHz in stainless steel) to ensure constructive interference.

**Key results:**
- Surface waves propagate predominantly along the ±y axis (0° and 180° steering angles), consistent with the coil orientation.
- Near-field destructive interference at the sensor centre (y = 500 mm); amplitude builds constructively with distance, peaks where all wire contributions align, then decays due to wave attenuation.
- The wholly analytical approach is faster to compute, free of mesh-induced numerical noise, and accurate across the full frequency range relevant to EMAT operation.
