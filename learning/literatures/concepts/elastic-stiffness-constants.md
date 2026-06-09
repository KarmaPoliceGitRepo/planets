# Elastic Stiffness Constants

**Aliases:** c11; c44; cij; elastic stiffness tensor; stiffness tensor; Cij; longitudinal stiffness; shear stiffness

**Definition:** The elastic stiffness constants c_ij (GPa) are the components of the 4th-rank stiffness tensor C_{ijkl} that relates stress to strain: σ_ij = C_{ijkl} ε_kl (Hooke's law). Using Voigt notation, a general anisotropic medium requires up to 21 independent constants. For isotropic media, only c₁₁ and c₄₄ (or equivalently λ and μ, the Lamé constants) are needed: c₁₁ = λ + 2μ determines the longitudinal wave velocity V_L = √(c₁₁/ρ); c₄₄ = μ determines the shear velocity V_S = √(c₄₄/ρ). Measurement of ultrasonic velocities allows inference of the stiffness constants and thus the elastic moduli (Young's modulus E, Poisson's ratio ν).

**Key relations:**
- [longitudinal-wave](longitudinal-wave.md) — V_L = √(c₁₁/ρ)
- [shear-wave](shear-wave.md) — V_S = √(c₄₄/ρ)
- [acoustic-impedance-matching-layer](acoustic-impedance-matching-layer.md) — Z = ρV_L depends on c₁₁
- [resonant-frequency](resonant-frequency.md) — resonance equations use wave velocity

**Discussed in:**
- [Intermediate Material Acoustic Properties](../notes/data-sheets/intermediate-material-acoustic-properties.md) — tabulated c₁₁, c₄₄, V_L, V_S, Z for matching layer candidate materials
