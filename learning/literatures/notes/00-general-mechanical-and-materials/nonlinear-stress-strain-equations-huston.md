# Nonlinear Stress-Strain Equations

- **Source:** Nonlinear stress-strain equation_Roland L Huston_1965.pdf
- **Drive link:** https://drive.google.com/file/d/1lpDtFkgNGSA1xaupLC6CM_U6Oc3g1HWY/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** Ronald L. Huston (University of Cincinnati), 1965 — *International Journal of Solids and Structures*, Vol. 1, pp. 463–470, Pergamon Press
- **Coverage:** full

## Overview
A theoretical paper reconciling two independent approaches to nonlinear stress-strain constitutive equations in finite elasticity: the classical strain-energy-function approach (thermodynamic) and a geometrical approach proposed by Stojanovitch (1959). Using a common notation, both are shown to yield consistent second-order explicit stress-strain relations containing only two elastic constants (the Lamé constants λ and μ). The resulting spatial and material equations are presented explicitly.

## Unique contribution
Provides the first explicit identification of the physical constants (α, β, a, b, c, ...) appearing in Stojanovitch's geometrical formulation in terms of the classical Lamé constants λ and μ — demonstrating that the two approaches are fully consistent with each other. Derives both spatial (Eulerian) and material (Lagrangian) second-order stress-strain equations ready for application in nonlinear elasticity problems.

## Key concepts
- Cauchy deformation tensor
- Green deformation tensor
- Lagrangian strain tensor (E_IJ)
- Eulerian strain tensor (e_ij)
- Material (Lagrangian) and spatial (Eulerian) coordinate systems
- Strain energy function
- Piola's contravariant stress (T^IJ)
- Covariant spatial stress (t_ij)
- Isotropic tensor (fourth order)
- Strain invariants (I_e, II_e, III_e)
- Lamé constants (λ, μ)
- Stojanovitch geometrical approach
- Second-order constitutive equations
- Density ratio factor (p/p₀)

## Methods / results / takeaways
- Material strain energy expanded as power series in strain invariants (I_E, II_E, III_E) up to third order — six undetermined constants appear.
- Geometrical approach (Stojanovitch): defines fourth-order isotropic material and spatial tensors L^IJKL = αG^IJ G^KL + β(G^IK G^JL + G^IL G^JK); stress defined as contraction of these tensors contracted with deformation tensors. Yields explicit second-order stress-strain form.
- Comparison of the two approaches yields six equations relating the arbitrary energy coefficients (a, b, c, d, e, f) to α and β — all seven equations are mutually consistent.
- Identification with linear elasticity (dropping all but linear strain terms): α = λ/2, β = (2μ−3λ)/8.
- Final spatial equation: t^i_j = (p/p₀)[λI_e δ^i_j + 2μe^i_j − 2λI_e e^i_j + (3λ−2μ)e^i_k e^k_j]
- Final material equation: S^IJ = λI_E G^IJ + 2μE^IJ − 2λII_E G^IJ + (3λ−2μ)E^IK E^K_J
- Only two elastic constants (λ and μ, or equivalently E and ν) appear — the second-order terms arise automatically from the geometry of deformation, not from additional material parameters.
- Note: this paper is directly cited by Orthwein (1968) as the precursor that motivated the further three-constant extension.
