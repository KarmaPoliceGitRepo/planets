# Frequency-Tracking Technique

**Aliases:** sampled-continuous-wave technique; frequency-tracked gated RF pulses; frequency-tracking ultrasonic method; acoustoelectric transducer technique

**Definition:** The frequency-tracking technique is a variant of resonance ultrasonic spectroscopy in which the RF drive frequency is continuously slaved (phase-locked or frequency-locked) to the resonant frequency of the transducer-specimen system. Short gated RF bursts are transmitted, and the receiver (often an acoustoelectric transducer giving a phase-insensitive DC output proportional to total acoustic flux) detects the resonance peak. As the resonant frequency shifts (due to temperature, load, or layer thickness changes), the tracking loop follows in real time. This allows precise monitoring of small frequency shifts without requiring a full spectrum sweep, enabling fast dynamic measurements.

**Key relations:**
- [stamina-method](stamina-method.md) — frequency-tracking is an implementation variant
- [resonant-frequency](resonant-frequency.md) — the tracked quantity
- [phase-locked-loop](phase-locked-loop.md) — PLL or FLL implements the tracking
- [ultrasonic-frequency-analysis](ultrasonic-frequency-analysis.md) — frequency domain analysis used in this technique

**Discussed in:**
- [Ultrasonic Spectrum Analysis Frequency-Tracked RF](../notes/method-resonance/ultrasonic-spectrum-analysis-frequency-tracked-rf.md) — description of the frequency-tracking sampled CW method; acoustoelectric transducer as receiver
