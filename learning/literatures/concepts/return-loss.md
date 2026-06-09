# Return Loss

**Aliases:** RL; return loss; input return loss; S11 dB

**Definition:** Return loss is the ratio (in dB) of incident to reflected power at a port: RL = −20 log|Γ| = −20 log|S11| dB. A larger (more positive) value indicates a better match: RL = ∞ dB means no reflection (perfect match); RL = 0 dB means total reflection. A return loss of 20 dB corresponds to |Γ| = 0.1 and only 1% reflected power. Return loss is the preferred metric in RF/microwave and optical fibre engineering because it is directly readable from a VNA and increases as matching improves, unlike VSWR which decreases.

**Key relations:**
- [reflection-coefficient](reflection-coefficient.md) — RL = −20 log|Γ|
- [standing-wave-ratio](standing-wave-ratio.md) — VSWR and RL express the same information
- [s-parameters](s-parameters.md) — RL = −20 log|S11|
- [insertion-loss](insertion-loss.md) — complementary loss metric

**Discussed in:**
- [Transmission Line Parameters](../notes/00-general-electronics/transmission-line-parameters.md) — RL definition and comparison to VSWR
