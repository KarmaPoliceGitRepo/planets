# Standing Wave Ratio

**Aliases:** SWR; VSWR; Voltage Standing Wave Ratio; voltage standing wave ratio; standing wave ratio

**Definition:** The voltage standing wave ratio (VSWR) is the ratio of the maximum to minimum voltage magnitude on a transmission line carrying both incident and reflected waves: VSWR = V_max/V_min = (1 + |Γ|)/(1 − |Γ|). It ranges from 1 (perfect match, |Γ| = 0) to ∞ (total reflection, |Γ| = 1). VSWR = 1 means no reflected power; VSWR = 2 corresponds to |Γ| = 1/3 and about 11% reflected power. It is a scalar, frequency-specific measure of impedance mismatch commonly used in RF/microwave engineering to specify acceptable match quality (e.g., VSWR < 1.5 for most applications).

**Key relations:**
- [reflection-coefficient](reflection-coefficient.md) — VSWR = (1+|Γ|)/(1−|Γ|)
- [return-loss](return-loss.md) — related metric: RL = −20 log|Γ|
- [transmission-line](transmission-line.md) — VSWR characterises the standing wave on the line
- [smith-chart](smith-chart.md) — constant-|Γ| circles on Smith Chart give constant VSWR

**Discussed in:**
- [Transmission Line Parameters](../notes/00-general-electronics/transmission-line-parameters.md) — VSWR definition and relation to Γ; example values
- [Module 2: Transmission Lines Frequency Domain](../notes/000-electronics-instructions/module2-transmission-lines-frequency-domain.md) — VSWR in phasor context
