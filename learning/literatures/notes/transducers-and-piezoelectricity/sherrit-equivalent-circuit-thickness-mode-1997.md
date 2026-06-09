# An Accurate Equivalent Circuit for the Unloaded Piezoelectric Vibrator in the Thickness Mode

- **Source:** Sherrit 1997 accurate equivalent circuit
- **Drive link:** https://drive.google.com/file/d/14xkxzuQAeKC03rvmlxnhFFzZq4Ls_Jso/view
- **Type:** paper (J. Phys. D: Appl. Phys.)
- **Author/Year:** S. Sherrit, H. D. Wiederick, B. K. Mukherjee, M. Sayer / 1997
- **Coverage:** full

## Overview
Derives a complex lumped equivalent circuit for the unloaded piezoelectric thickness-mode resonator in which the circuit elements C₀, C₁, and L₁ are all complex (lossy). Contrasts with the Van Dyke model (real elements only). Provides direct equations for computing the complex circuit constants from the complex material constants, and converse equations for extracting complex material constants from measured circuit constants. Validated on Motorola 3203HD PZT and P(VDF-TrFE) polymer film.

## Unique contribution
Shows that using real-only Van Dyke circuit elements is inadequate for high-loss piezoelectric materials: the imaginary parts of C₁ and L₁ carry essential information about elastic and piezoelectric losses. Provides explicit algebraic relationships between (C₀*, C₁*, L₁*, resonance resistance R_s) and the complex material constants (k_t, ε^S*, c^D*). Demonstrates that the complex circuit gives accurate k_t extraction for both hard PZT (3203HD, k_t=0.5695) and soft PVDF-TrFE (k_t=0.230) without iteration.

## Key concepts
- Van Dyke equivalent circuit (real C₀, C₁, L₁, R_s) vs complex circuit (complex C₀*, C₁*, L₁*)
- Complex circuit elements: C₀* = ε^S₃₃·A/(t) (complex); C₁* and L₁* absorb elastic and piezoelectric losses
- Forward calculation: C₀*, C₁*, L₁* from k_t, ε^S*, c^D*
- Converse calculation: k_t, ε^S*, c^D* from measured C₀*, C₁*, L₁*
- Three-loss model (dielectric ε^S*, elastic c^D*, piezoelectric k_t) applied to thickness-mode resonance
- Validated on Motorola 3203HD PZT (k_t=0.5695) and P(VDF-TrFE) polymer film (k_t=0.230)

## Methods / results / takeaways
- Analytic expressions for complex circuit elements derived from thickness-mode wave equation
- For Motorola 3203HD: complex C₀* and C₁* yield tan δ_e ≈ 0.053 (dielectric), tan δ_m ≈ 0.023 (elastic); agrees with prior impedance measurements
- P(VDF-TrFE): lower k_t=0.230 but non-negligible dielectric loss; complex circuit necessary
- Converse equations: given measured series resonance frequency, anti-resonance frequency, and Q factor, recover complex material constants in one step
- Practical advantage: avoids iterative fitting entirely; one algebraic pass gives all three complex constants
- Confirms that imaginary parts of C₁ and L₁ are comparable in magnitude to those of C₀, so omitting them (Van Dyke) introduces systematic error in material constant inversion
