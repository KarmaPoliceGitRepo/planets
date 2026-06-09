# Anisotropic Elasticity (Lecture Notes)

- **Source:** 06_Linear_Elasticity_03_Anisotropy.pdf
- **Drive link:** https://drive.google.com/file/d/1m4DJgDoqwxfxAJKcV6S14AEdizKIjjO7/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Kelly (solid mechanics lecture notes, Section 6.3)
- **Coverage:** full

## Overview
Lecture notes on anisotropic linear elasticity. Covers the generalised Hooke's law in Voigt notation (6×6 stiffness matrix), material symmetry classes (orthotropic → 9 independent constants; transversely isotropic → 5; isotropic → 2), and their compliance matrix inverses in engineering constants (E, ν, G).

## Unique contribution
Clear derivation via symmetry arguments of how each material symmetry class reduces the number of independent elastic constants. Directly applicable to elastic wave velocity calculation in anisotropic materials (composites, single crystals, textured metals).

## Key concepts
- Generalised Hooke's law, Voigt notation (σ₁…σ₆, ε₁…ε₆)
- Stiffness matrix C_ij (36 → 21 independent entries by symmetry)
- Compliance matrix S_ij
- Orthotropic symmetry: 9 independent constants (E₁,E₂,E₃, G₁₂,G₁₃,G₂₃, ν₁₂,ν₁₃,ν₂₃)
- Transversely isotropic symmetry: 5 independent constants
- Isotropic symmetry: 2 constants (λ,μ or E,ν)
- Lamé constants λ, μ
- Shear coupling in off-axis loading

## Methods / results / takeaways
For orthotropic materials, shear stresses produce only shear strains and normal stresses produce only normal strains when loads are aligned with material axes; shear coupling appears when axes are rotated. For transversely isotropic media (fibrous composites), the plane perpendicular to the fibre axis is isotropic, reducing constants to E_a, E_t, ν_a, ν_t, G_a. The isotropic case recovers σ_ij = λε_kk δ_ij + 2μ ε_ij with G = E/(2(1+ν)). These constants enter the Christoffel equation to compute wave velocities in anisotropic media: quasi-P, quasi-SV, and SH velocities all depend on propagation direction.
