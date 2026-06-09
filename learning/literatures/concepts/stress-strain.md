# Stress and Strain
**Aliases:** Cauchy stress tensor; engineering stress; true stress; true strain; engineering strain; Hooke's law; yield stress; tensile strength; proof strength; Hollomon power law; Ramberg-Osgood; strain hardening; plastic deformation; von Mises; Tresca; stress-strain curve; uniaxial tension; compression; shear

**Definition:** Stress (σ, Pa) is force per unit area acting on a surface; the Cauchy stress tensor σ_ij (3×3 symmetric) fully describes the state at a point. Strain ε_ij is the symmetric part of the displacement gradient. Engineering (nominal) stress uses original area; true stress uses instantaneous area. In the elastic regime, Hooke's law σ = Eε applies. Beyond the yield point (or proof strength f₀.₂ for continuously yielding metals), the Hollomon power law σ = Kε^n describes strain hardening; the Ramberg-Osgood equation ε = σ/E + 0.002(σ/f₀.₂)^n is widely used for aluminium and steel at elevated temperatures. Failure criteria (von Mises: σ_eff ≥ σ_y; Tresca: τ_max ≥ σ_y/2) predict yielding under multiaxial stress states.

**Key relations:**
- [elasticity-constants](elasticity-constants.md)
- [residual-stress](residual-stress.md)
- [hardness](hardness.md)
- [fatigue](fatigue.md)
- [dislocation-and-internal-friction](dislocation-and-internal-friction.md)

**Discussed in:**
- [MIT 1.050 Engineering Mechanics — Ulm](../notes/00-general-mechanical-and-materials/mit-1050-engineering-mechanics-ulm.md) — Cauchy stress tensor; Hooke's law; Helmholtz free energy; von Mises criterion
- [Stress-Strain Diagram Plastic Range — Brisbane](../notes/00-general-mechanical-and-materials/stress-strain-diagram-plastic-range-brisbane.md) — Hollomon power law; true stress-true strain; necking criterion
- [ASTM E8/E8M — Tension Testing](../notes/standards/astm-e8-e8m-2013-tension-testing-metals.md) — standard test method; definitions of yield, UTS, elongation, reduction of area
- [ASTM E9 — Compression Testing](../notes/standards/astm-e9-compression-testing-metals.md) — compressive yield strength; barreling; buckling avoidance
