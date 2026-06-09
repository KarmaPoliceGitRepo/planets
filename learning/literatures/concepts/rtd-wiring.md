# RTD Wiring Configurations

**Aliases:** 2-wire connection; 3-wire connection; 4-wire connection; four-wire Kelvin connection; lead resistance compensation

**Definition:** RTDs require an excitation current and resistance measurement; the leads connecting the sensor to the measurement instrument contribute resistance error. Three standard configurations manage this: 2-wire — simplest wiring, lead resistance adds directly to sensor reading (error ~0.2–2 Ω per metre); suitable for Pt1000 or very short cables. 3-wire — one lead on each side, third lead compensates for lead resistance assuming matched lead impedances; standard for industrial Pt100 up to ~30 m. 4-wire (Kelvin) — separate current and voltage leads fully eliminate lead resistance error; used in laboratory and calibration applications where lead errors must be eliminated.

**Key relations:**
- [rtd](rtd.md) — wiring configuration is part of the RTD measurement system
- [pt100-pt1000](pt100-pt1000.md) — Pt1000 more tolerant of 2-wire errors
- [en-60751-rtd-accuracy](en-60751-rtd-accuracy.md) — tolerance class budget may require 3-wire or 4-wire

**Discussed in:**
- [WIKA DS IN0017 Platinum RTD Tolerances](../notes/temperature-measurement-probes/wika-ds-in0017-platinum-rtd-tolerances.md) — all three configurations described with circuit diagrams and error analysis
- [RS Rubber Patch RTD](../notes/temperature-measurement-probes/rsrub-rubber-patch-rtd.md) — 3-wire Pt100 implementation in silicone patch sensor
