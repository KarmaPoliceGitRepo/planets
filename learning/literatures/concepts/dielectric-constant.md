# Dielectric Constant (Piezoelectric)

**Aliases:** relative permittivity; ε33T; ε33S; dielectric permittivity; relative dielectric constant; εr

**Definition:** The dielectric constant of a piezoelectric material is the ratio of the material's permittivity to the permittivity of free space (εr = ε/ε₀). For piezoelectric ceramics, the relevant constants are ε33T (at constant stress, i.e., unclamped) and ε33S (at constant strain, i.e., clamped); ε33T > ε33S because clamping prevents additional strain contribution. Soft PZT grades have high ε33T (up to ~3000–5000 ε₀) enabling large charge output, while hard grades have lower values (~500–1500 ε₀). The dielectric constant affects electrical impedance matching between the piezoelectric element and driving/receiving electronics.

**Key relations:**
- [pzt-hard-soft](pzt-hard-soft.md) — soft PZT has much higher permittivity than hard
- [piezoelectric-constants](piezoelectric-constants.md) — ε appears in the full constitutive equations
- [klm-model](klm-model.md) — ε33S determines the clamped capacitance C₀ in the KLM circuit

**Discussed in:**
- [Del Piezo Material Specification Sheet](../notes/data-sheets/del-piezo-material-specification-sheet.md) — ε33T/ε0 values listed for each PIC grade
