# Lorentz Force Mechanism (EMAT)

**Aliases:** Lorentz force density; Lorentz force mechanism; EMAT Lorentz generation

**Definition:** In EMAT generation, a high-frequency coil induces eddy currents J in the near-surface layer of the specimen (within one skin depth). These currents interact with the applied static magnetic flux density B via the Lorentz body force density f = J × B (N/m³), directly launching elastic waves into the material. The Lorentz mechanism operates in all electrically conducting materials. In ferromagnetic materials the magnetostrictive mechanism adds an additional contribution whose relative magnitude depends on the operating point on the B-H curve.

**Key relations:**
- [emat](emat.md) — overall transducer that uses this mechanism
- [skin-depth](skin-depth.md) — limits the depth over which eddy currents and forces are generated
- [meander-line-coil](meander-line-coil.md) — coil geometry determines spatial force distribution
- [dodd-deeds-solution](dodd-deeds-solution.md) — analytical solution for the eddy-current field

**Discussed in:**
- [Wholly Analytical EMAT Array Simulation](../notes/emat/wholly-analytical-emat-array-simulation.md) — derivation of the Lorentz body force distribution and comparison to magnetostrictive term
