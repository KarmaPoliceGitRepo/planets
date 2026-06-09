# Oscilloscope Probes: Theory and Practice

- **Source:** probes.pdf
- **Drive link:** https://drive.google.com/file/d/1CNwMh4HTs0GohoJP247Cg1MlVcLtSK7u/view?usp=drivesdk
- **Type:** paper / application note
- **Author/Year:** Peter D. Hiscocks, James Gaston, Syscomp Electronic Design Limited, July 12, 2007
- **Coverage:** full

## Overview
A practical paper on oscilloscope probe theory covering loading effects, the x10 probe design, compensation adjustment, ground connections, and the noise tradeoff in oscilloscope input circuits. Demonstrates why probes are necessary for high-frequency and high-impedance measurements.

## Unique contribution
Provides a rigorous frequency-domain analysis showing that the compensated x10 probe acts as a frequency-invariant voltage divider when R1·Cc = R2·Cl is satisfied, and quantifies the reduction in capacitive loading from ~100 pF (bare coax) to ~15 pF (x10 probe). Also explains why higher oscilloscope input capacitance reduces thermal noise bandwidth — a counterintuitive tradeoff.

## Key concepts
- Oscilloscope input impedance: typically 1 MΩ || 20–30 pF
- Loading effect: resistive (at DC/low frequencies) and capacitive (at high frequencies)
- Coaxial cable capacitance: ~26.4 pF/ft for RG-58, causing ~100 pF total load at 3 ft
- x10 probe: 9 MΩ || ~2.2 pF in series with scope input → 10 MΩ total, ~2 pF effective capacitance
- Probe compensation: adjust Cp so that R1·Cc = R2·Cl → flat frequency response
- Under-compensation: too-small Cp → depressed high-frequency response
- Over-compensation: too-large Cp → emphasized high-frequency response
- Ground lead length affects inductance and transient response
- Thermal noise: en = √(4kTBR); capacitor across input reduces effective noise bandwidth

## Methods / results / takeaways
- Frequency-invariant division: K = R2/(R1+R2) when R1·Cc = R2·Cl, eliminating frequency dependence.
- x10 probe reduces resistive load by 10× (1 MΩ → 10 MΩ) and capacitive load by ~10× (100 pF → 10–15 pF effective).
- Use a scope probe when: circuit impedance approaches scope input impedance, measuring high frequencies or fast edges, or the input capacitance causes circuit malfunction (e.g., RF oscillator stops).
- Grounding priority (best to worst): probe ground ring at tip, probe ground clip short, separate wire to scope, power-line ground.
- The ×1/×10 switch: in ×1 position, compensation capacitance has no effect and capacitive load is much higher (~70 pF).
- Noise reduction: 20 pF across 1 MΩ reduces noise bandwidth from ~20 MHz to ~8 kHz, dropping input noise from 0.5 mV to 11 µV.
