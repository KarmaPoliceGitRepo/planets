# Thick Walled Cylinders

- **Source:** Thick Walled Cylinders.pdf
- **Drive link:** https://drive.google.com/file/d/1_xg7YCtqgNViWrP5MJbr4iqJAhGofbqM/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Unknown (lecture notes / reference handout, ~2018 based on upload date)
- **Coverage:** full

## Overview
A self-contained derivation and reference document for the stress analysis of thick-walled cylinders under internal and/or external pressure. Presents Lamé's equations from first principles (radial equilibrium of an infinitesimal element, plane stress or plane strain conditions), then applies them to internal-pressure-only and external-pressure-only cases, closed-end axial stress, and press/shrink fits. Includes worked examples with FEA comparison and practice problems.

## Unique contribution
Concise, self-contained reference covering all three sub-cases (internal pressure, external pressure, shrink fit) in a single document with both analytical equations and FEA validation. The press/shrink fit section gives the interface pressure formula as a function of radial interference δ, inner/outer radii (a, b, c) and Young's modulus — ready for direct engineering use.

## Key concepts
- Thick-walled cylinder (Lamé theory)
- Hoop (tangential) stress σ_θ
- Radial stress σ_r
- Axial stress σ_z (closed ends)
- Plane stress vs. plane strain
- Lamé's equations (integration constants C₁, C₂)
- Internal pressure only
- External pressure only
- Press fit / shrink fit
- Interface pressure
- Von Mises stress
- FEA comparison
- Thin-wall approximation error

## Methods / results / takeaways
- Derivation: radial equilibrium + Hooke's law + displacement compatibility → d²u/dr² + (1/r)(du/dr) − u/r² = 0, with solution u = C₁r + C₂/r; stresses follow as σ_r = C·1 − C·2/r², σ_θ = C₁ + C₂/r².
- Internal pressure only (Po = 0): maximum tangential stress at inner surface = Pi(ro² + ri²)/(ro² − ri²); radial stress = −Pi at inner surface (compressive), 0 at outer surface. Both hoop and radial stresses are always highest in magnitude at the bore.
- Closed-end axial stress: σ_z = Pi·ri²/(ro² − ri²) = constant through wall.
- Press/shrink fit formula: pi = Eδ/b × [(b²−a²)(c²−b²)] / [2b²(c²−a²)] (same material inner and outer cylinders assumed).
- Example: cylinder with Pi = 1000 psi, ri = 2", ro = 4" — FEA matches analytical closely.
- Thin-wall error: for t = 0.1D wall, thin-wall theory overestimates tangential stress by ~9.75% and max shear stress by ~11.1%.
- Design application: thick-walled theory required whenever ri/ro > ~0.5 (wall thickness not small relative to radius).
