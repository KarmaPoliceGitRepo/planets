# Impedance Matching Network

**Aliases:** L-match network; T-match network; Π-match network; pi-match; matching network; L-network; lossless matching; reactive matching network; single-stub matching; stub tuner

**Definition:** An impedance matching network is a reactive (lossless) or near-lossless two-port inserted between source and load to maximise power transfer by presenting conjugate impedances at each port. Common topologies: L-network (two reactive elements, Q = √(n−1) where n is impedance ratio); T-network (series-shunt-series, extra Q degree of freedom); Π-network (shunt-series-shunt, extra Q degree of freedom); single-stub tuner (shunt transmission line stub cancels susceptance). The loaded Q of the network determines the bandwidth of the match: higher Q gives narrower bandwidth. Component losses (finite Q_L of inductors/capacitors) cause insertion loss IL ≈ 1/(1 + Q_L/Q_c).

**Key relations:**
- [smith-chart](smith-chart.md) — matching networks are designed graphically on the Smith Chart
- [quarter-wave-transformer](quarter-wave-transformer.md) — transmission-line matching alternative
- [insertion-loss](insertion-loss.md) — component Q limits achievable insertion loss
- [q-factor](q-factor.md) — loaded Q determines bandwidth
- [s-parameters](s-parameters.md) — matching network performance characterised by S11, S21

**Discussed in:**
- [Module 6: Matching Networks](../notes/000-electronics-instructions/module6-matching-networks.md) — L, T, Π topologies; Q and bandwidth; insertion loss from component losses
- [Module 4: Smith Chart](../notes/000-electronics-instructions/module4-smith-chart.md) — graphical matching using Smith Chart and stub tuning
