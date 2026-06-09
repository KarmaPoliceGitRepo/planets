# Insertion Loss

**Aliases:** IL; two-way insertion loss; mismatch loss; network insertion loss

**Definition:** Insertion loss is the reduction in power delivered to a load when a two-port network is inserted between source and load, expressed in dB as IL = −10 log(P_load_with/P_load_without) or equivalently IL = −20 log|S21| for a network between matched terminations. Two contributions: mismatch loss (from |Γ| ≠ 0 at either port) and dissipative loss (from component or material absorption). In matching networks, insertion loss IL ≈ 1/(1 + Q_L/Q_c) dB where Q_L is the loaded network Q and Q_c is the component unloaded Q. In air-coupled transducers, two-way insertion loss is the key figure of merit, often exceeding 80 dB without matching layers.

**Key relations:**
- [s-parameters](s-parameters.md) — IL = −20 log|S21|
- [return-loss](return-loss.md) — related metric for reflected power
- [reflection-coefficient](reflection-coefficient.md) — mismatch loss = −10 log(1−|Γ|²)
- [impedance-matching-network](impedance-matching-network.md) — component Q determines insertion loss
- [acoustic-impedance-matching-layer](acoustic-impedance-matching-layer.md) — matching layers reduce IL in transducers
- [q-factor](q-factor.md) — component Q affects insertion loss

**Discussed in:**
- [Module 6: Matching Networks](../notes/000-electronics-instructions/module6-matching-networks.md) — component-Q formula for insertion loss
- [Transmission Line Parameters](../notes/00-general-electronics/transmission-line-parameters.md) — IL definition; relation to S21
- [2004 Acoustic Impedance Matching Piezoelectric Transducers Air](../notes/000000-read-papers-with-notes/2004-acoustic-impedance-matching-piezoelectric-transducers-air-gomez.md) — two-way IL as the key metric comparing matching stack designs
