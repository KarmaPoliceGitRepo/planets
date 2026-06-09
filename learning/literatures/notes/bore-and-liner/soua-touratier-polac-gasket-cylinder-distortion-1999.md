# Computations of an Engine to Analyze Cylinder Distortion

- **Source:** Engineering Computations, Vol. 16, Issue 1 (1999), pp. 9–25, DOI: 10.1108/02644409910251184
- **Drive link:** https://drive.google.com/file/d/1RsomYC4L6c85sgQliSecIPDMEW3xMJCr/view
- **Type:** paper
- **Author/Year:** Soua, Ali; Touratier, Maurice (ENSAM Paris); Polac, Laurent (Renault) / 1999 (Eng Comput 16(1))
- **Coverage:** full

## Overview
3D finite element study of cold-assembly cylinder bore distortion in an internal Renault cylinder using ABAQUS 5.3 with large-deformation elasto-plasticity, contact, and friction. The cylinder head gasket (three-layer metallic, with embossed rib around the combustion chamber) is modelled explicitly with plasticity for the stamping and crushing phases; all other engine components (head, block, bolts) modelled in linear elasticity with superelements. Distortion is decomposed into Fourier series; 4th-order harmonic linked to oil consumption, 0th-order to noise. Good correlation (8–11% error) between simulation and experiment for 4th-order and 0th-order amplitudes during cold clamping.

## Unique contribution
First study to model the 3-layer metallic cylinder head gasket (including embossment stamping and crushing) with explicit large-deformation elasto-plasticity in an engine-level bore distortion simulation; introduces superelement technique to condense the linear part for computational efficiency; validates both the gasket behaviour and the cylinder distortion against experiment.

## Key concepts
- ABAQUS 5.3; large deformation with plasticity (Lagrangian kinematics, J2 flow theory, Kirchhoff stress, Jaumann objective derivative)
- Gasket: 3-layer metallic (external layers 0.5 mm steel Z3CT12 σY0=278 MPa, internal layer 0.7 mm steel Z11CN1708 σY0=1093 MPa); embossment rib for combustion sealing; non-circular rib near combustion chamber
- Contact with friction: Lagrangian multiplier for non-penetration; Coulomb penalty for friction
- Superelement technique: linear engine components (head, block, bolts) condensed to gasket boundary DOFs
- Fourier decomposition: Umaxn amplitudes; 4th-order → oil consumption; 0th-order → engine noise
- Validation: 4th-order amplitude within 8% of experiment; 0th-order within 11%; for two different cylinders (cyl 2 and cyl 3)
- Cold-assembly study only; future work planned for thermal-mechanical cyclic loading
- 1/2 model used (symmetry of internal cylinder)

## Methods / results / takeaways
- Simplified rib study: 2D axisymmetric model of annular ribbed structure; stamping residual stresses found to have negligible effect on global crushing behaviour → geometry from manufacturer used directly.
- 3D gasket model: C3D8R solid elements; updated rib geometry from convergence with global experimental behaviour; clamping load range 50,000–140,000 N.
- Engine model: modified Newton-Raphson with large contact element set; difficult convergence.
- Cylinder distortion shown at levels –5 mm and –20 mm below deck; Fourier series decomposed at multiple axial levels.
- Key result: 4th-order (oil consumption) and 0th-order (noise) both well predicted by cold-assembly FEA; confirms that cold clamping alone generates measurable bore distortion.
- Cited by Yang et al. (2016) as "excessively simplified by symmetry assumptions" — but this is the first model to include full gasket plasticity.
- Bore-liner relevance: establishes early FEA methodology for cold-assembly bore distortion including gasket nonlinearity; validates Fourier decomposition approach; confirms 4th-order harmonic from bolt clamping affects oil consumption even under cold conditions.
