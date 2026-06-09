# S-Parameters

**Aliases:** scattering parameters; S-matrix; S11; S21; S12; S22; scattering matrix; S-params

**Definition:** S-parameters (scattering parameters) describe a linear N-port network in terms of travelling wave amplitudes: S_ij = b_i/a_j with all other ports terminated in the reference impedance Z₀. S11 is the input reflection coefficient; S21 is the forward transmission gain (|S21|² = power transmission); S12 the reverse transmission; S22 the output reflection. S-parameters are directly measurable with a vector network analyser at RF/microwave frequencies where lumped Z/Y measurements are impractical. A matched, lossless, reciprocal two-port has |S21| = 1, S11 = S22 = 0, S12 = S21. The stability of an amplifier and its maximum gain are derived from S-parameters.

**Key relations:**
- [reflection-coefficient](reflection-coefficient.md) — S11 is the electrical reflection coefficient
- [insertion-loss](insertion-loss.md) — insertion loss = −20 log|S21|
- [return-loss](return-loss.md) — return loss = −20 log|S11|
- [smith-chart](smith-chart.md) — S11 plotted directly on Smith Chart
- [noise-figure](noise-figure.md) — noise figure analysis uses S-parameters
- [transducer-gain](transducer-gain.md) — GT = |S21|²(1−|ΓS|²)(1−|ΓL|²)/|...|²

**Discussed in:**
- [Module 3: Scattering Parameters](../notes/000-electronics-instructions/module3-scattering-parameters.md) — definition, measurement, signal flow graphs, Mason's rule
- [S-Parameters (Collin)](../notes/00-general-electronics/collin-circuit-theory-waveguiding.md) — theoretical foundation of S-parameter formalism
