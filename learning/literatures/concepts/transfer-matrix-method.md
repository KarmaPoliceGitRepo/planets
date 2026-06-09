# Transfer Matrix Method
**Aliases:** Thomson-Haskell method; propagator matrix method; stiffness matrix method; global matrix method; partial wave technique; matrix method; transfer-matrix model

**Definition:** The transfer matrix (Thomson–Haskell) method is an analytical technique for computing wave propagation in stratified (multilayer) media. Each layer is represented by a 4×4 (or 6×6) matrix that maps the stress–displacement (or pressure–particle-velocity) state vector from the bottom to the top of the layer, coupling upward and downward-traveling bulk wave components (partial waves). Matrices are cascaded by multiplication across all layers. The global-matrix method assembles all layer equations simultaneously, avoiding the numerical instability (overflow/underflow) of the recursive transfer-matrix product at high frequency–thickness products. The method yields dispersion curves, reflection and transmission coefficients, and mode shapes for any layer geometry.

**Key relations:**
- related: [reflection-coefficient](reflection-coefficient.md)
- related: [dispersion](dispersion.md)
- related: [lamb-wave](lamb-wave.md)
- related: [acoustic-impedance](acoustic-impedance.md)
- related: [frequency-thickness-product](frequency-thickness-product.md)

**Discussed in:**
- [Matrix Techniques Multilayered Media (Lowe)](../notes/modeling-of-acoustic-waves/matrix-techniques-multilayered-media-lowe.md) — comprehensive review of transfer-matrix and global-matrix formulations, numerical stability issues
- [1D Pressure Transfer Acoustic–Electric](../notes/modeling-of-acoustic-waves/1d-pressure-transfer-acoustic-electric.md) — 1D transfer-matrix for piezoelectric transducer + multilayer stack
- [Pialucha & Cawley 1994 — Thin Layers](../notes/lubrication-film/pialucha-cawley-thin-layers-1994.md) — transfer matrix gives exact reflection coefficient for thin fluid layers vs spring model
- [Modeling Acoustic Waves — Numerical Methods](../notes/modeling-of-acoustic-waves/numerical-method-acoustic-waves-propagation.md) — comparison of TMM with FEM for wave propagation
- [Transfer Matrix (laser-induced)](../notes/laser-induced/pulse-echo-sound-velocity-nanofilms.md) — TMM applied to nanofilm acoustic measurement
- [Global Transmission/Reflection Ultrasonic Porous](../notes/modeling-of-acoustic-waves/global-transmission-reflection-ultrasonic-porous.md) — TMM extended to Biot poroelastic layers
