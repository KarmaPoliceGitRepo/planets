# Skin Depth

**Aliases:** penetration depth; electromagnetic skin depth; classical skin depth; δ; delta

**Definition:** Skin depth δ is the characteristic depth at which eddy-current (or electromagnetic field) amplitude decays to 1/e of its surface value in a conducting material: δ = √(2/(ωσμ)), where ω is the angular frequency, σ is the electrical conductivity, and μ is the magnetic permeability. In EMATs, δ determines the thickness of the layer in which Lorentz forces act; operating at lower frequencies increases δ and depth of force generation. In transmission lines, skin effect increases conductor resistance at high frequencies, increasing the RLGC line parameter R and hence attenuation.

**Key relations:**
- [emat](emat.md) — skin depth limits EMAT sensitivity and force depth
- [lorentz-force-emat](lorentz-force-emat.md) — forces confined within ~1–2 skin depths
- [transmission-line](transmission-line.md) — skin effect increases transmission line loss at high frequency
- [propagation-constant](propagation-constant.md) — skin effect contributes to attenuation constant α

**Discussed in:**
- [Wholly Analytical EMAT Array Simulation](../notes/emat/wholly-analytical-emat-array-simulation.md) — skin depth expression and its role in bounding the eddy-current source region
