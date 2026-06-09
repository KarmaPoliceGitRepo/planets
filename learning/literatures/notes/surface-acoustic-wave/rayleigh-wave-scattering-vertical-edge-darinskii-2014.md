# Rayleigh Wave Scattering from a Vertical Edge of Isotropic Substrates

- **Source:** Rayleigh wave scattering from a vertical edge of isotropic substrates - (2014) AN Darinskii M Weihnacht H Schmidt.pdf
- **Drive link:** https://drive.google.com/file/d/1bi1oap23nXjd1Vm6-0w2Sl0laudeeyRm/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** A. N. Darinskii, M. Weihnacht, H. Schmidt / 2014 (Ultrasonics 54, 1999–2005)
- **Coverage:** full

## Overview
A numerical FEM study of harmonic Rayleigh wave scattering at the 90-degree corner of an isotropic elastic substrate, solved in the frequency domain using COMSOL Multiphysics with Perfectly Matched Layers (PML) as absorbing boundaries. Two novel cases beyond the basic sharp corner are analysed: (1) a rounded-off corner (fillet radius r), and (2) a thin solid layer deposited on the vertical face. Reflection and transmission coefficients are obtained as functions of Poisson ratio, angle of incidence, fillet radius, and layer thickness/material.

## Unique contribution
First systematic FEM study of how edge geometry modifications (fillet rounding, layer coating) quantitatively change Rayleigh wave scattering at a 90° substrate corner. Finds that small fillets (r/λ ≈ 0.3–0.35) counter-intuitively increase reflection by factors of 1.3–1.5, and that a stiff layer can enforce near-total reflection across a wide angle range even when bulk wave generation is energetically permissible.

## Key concepts
- Rayleigh wave scattering at a substrate edge
- Reflection and transmission coefficients
- 90-degree wedge / quarter-space
- Perfectly matched layer (PML)
- Finite element method (FEM) for acoustics
- Fillet radius effect on scattering
- Solid layer on vertical face
- Poisson ratio dependence
- Bulk wave generation at edge
- Angle of incidence dependence

## Methods / results / takeaways
- For a perfect 90° corner, |R| ≈ 0.27–0.39 and |T| ≈ 0.68 (nearly constant) depending on Poisson ratio (r = 0.17–0.35); results agree with prior integral-equation and BEM methods.
- Energy balance E = |R|² + |T|² < 1 because energy is also radiated as bulk waves; this fraction grows with larger Poisson ratio.
- Adding a small fillet initially increases |R| by up to 50%, with maximum at r/λ ≈ 0.3–0.35; for r/λ > 2 reflection drops near zero but transmission is still not total (bulk wave leakage remains significant up to r/λ ~ 3.5).
- A diamond layer on the vertical face of fused quartz causes total reflection (|R| ≈ 1) for angles of incidence > 30–40°, with negligible bulk wave conversion — analogous to a mechanically clamped boundary.
- The Poisson ratio strongly influences oblique-incidence scattering when a fillet is present, unlike the bare-edge case.
- Practical implication: layer deposition on device edges can be used to tailor surface wave reflectivity in SAW devices.
