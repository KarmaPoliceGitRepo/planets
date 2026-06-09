# Transducer Gain

**Aliases:** GT; transducer gain; available power gain; operating power gain; Ga; Gp; Gmax; maximum available gain; MAG; MSG

**Definition:** Transducer gain GT is the ratio of power delivered to the load to the available power from the source: GT = P_load/P_avs = |S21|²(1−|Γ_S|²)(1−|Γ_L|²)/|(1−S11Γ_S)(1−S22Γ_L)−S12S21Γ_SΓ_L|². Available power gain Ga = P_avn/P_avs is independent of load. Operating power gain Gp = P_load/P_in depends only on load. Maximum available gain MAG = |S21/S12| when K = 1 (stability boundary); MSG = |S21/S12| for K > 1. These gain definitions are linked via the stability factor K and the S-parameters.

**Key relations:**
- [s-parameters](s-parameters.md) — gain formulas derived from S-parameters
- [noise-figure](noise-figure.md) — gain and noise figure trade off in LNA design
- [impedance-matching-network](impedance-matching-network.md) — matching sets ΓS, ΓL to maximise gain
- [q-factor](q-factor.md) — component Q limits achievable gain-bandwidth product

**Discussed in:**
- [Module 8: Two-Ports Power Gain](../notes/000-electronics-instructions/module8-two-ports-power-gain.md) — definitions of GT, Ga, Gp, MAG, MSG; stability connections
