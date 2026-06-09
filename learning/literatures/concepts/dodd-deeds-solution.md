# Dodd–Deeds Analytical Solution

**Aliases:** Deeds and Dodd solution; Dodd-Deeds eddy-current model; Dodd–Deeds integral

**Definition:** The Dodd–Deeds analytical solution provides closed-form integral expressions for the magnetic vector potential A induced by a circular coil carrying alternating current in the presence of a planar conducting half-space. Solved originally by Dodd and Deeds (1968), the solution expresses A as a Hankel-transform integral whose integrand contains the coil geometry and the material's complex propagation factor (related to skin depth). It is the standard reference for eddy-current probe modelling and is used in EMAT design to compute eddy-current distributions under circular or, via the large-radius extrapolation, straight-wire conductors.

**Key relations:**
- [emat](emat.md) — EMAT models build on the Dodd–Deeds eddy current field
- [lorentz-force-emat](lorentz-force-emat.md) — Lorentz body force = J × B derived from Dodd–Deeds J
- [meander-line-coil](meander-line-coil.md) — straight-wire approximation of coil elements uses large-radius extrapolation
- [skin-depth](skin-depth.md) — appears in the Dodd–Deeds integrand

**Discussed in:**
- [Wholly Analytical EMAT Array Simulation](../notes/emat/wholly-analytical-emat-array-simulation.md) — Dodd–Deeds solution used as the core analytical building block; large-radius extrapolation to straight wires
