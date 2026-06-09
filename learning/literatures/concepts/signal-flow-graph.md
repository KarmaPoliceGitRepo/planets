# Signal Flow Graph

**Aliases:** SFG; signal flow graph; flow graph; Mason's Rule; non-touching loop rule; Mason's gain formula

**Definition:** A signal flow graph (SFG) is a directed graph representation of the linear relationships in a network, where nodes represent signals and edges represent gain coefficients. Mason's Rule (non-touching loop rule) gives the overall graph gain as T = (Σ_k P_k Δ_k)/Δ, where P_k is the gain of the k-th forward path, Δ is the graph determinant (1 − sum of loop gains + sum of non-touching loop gain products − ...), and Δ_k is Δ with loops touching the k-th path removed. SFGs are used to compute transfer functions of multi-loop feedback networks and S-parameter relationships in microwave circuits without matrix inversion.

**Key relations:**
- [s-parameters](s-parameters.md) — SFGs are used to derive S-parameter transfer functions
- [transducer-gain](transducer-gain.md) — gain formulas often derived via SFG
- [analogue-filter-basics](analogue-filter-basics.md) — state-variable and multiple-feedback topologies analysed by SFG

**Discussed in:**
- [Module 3: Scattering Parameters](../notes/000-electronics-instructions/module3-scattering-parameters.md) — SFG construction from S-parameters; Mason's Rule derivation and examples
