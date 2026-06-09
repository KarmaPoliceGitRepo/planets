# Phase-Locked Loop

**Aliases:** PLL; phase-locked loop; frequency-locked loop; FLL; VCO; voltage-controlled oscillator

**Definition:** A phase-locked loop (PLL) is a feedback control system that synchronises an output oscillator (VCO) in phase and frequency to a reference signal. The basic PLL consists of a phase detector, a loop filter (low-pass), and a VCO. When locked, the VCO output tracks the reference frequency; loop bandwidth determines how fast the PLL acquires lock and how well it suppresses phase noise at offsets within the bandwidth. PLLs are used in frequency synthesisers, clock recovery, carrier tracking, and in the frequency-tracking ultrasonic technique (where the VCO frequency is slaved to the specimen resonance).

**Key relations:**
- [frequency-tracking-technique](frequency-tracking-technique.md) — PLL or FLL implements frequency tracking in STAMINA
- [resonant-frequency](resonant-frequency.md) — the target frequency for the tracking loop
- [q-factor](q-factor.md) — loop Q and bandwidth are filter design parameters

**Discussed in:**
- [Module 22: Negative Resistance Oscillators, Differential Osc., VCOs](../notes/000-electronics-instructions/module22-negative-resistance-osc-differential-osc-vcos.md) — VCO design; tuning range and phase noise
