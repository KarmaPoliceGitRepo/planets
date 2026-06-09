# Module 17 – Current/Voltage Commutating Mixers

- **Source:** module17 - CurrentVoltage Commutating Mixers.pdf
- **Drive link:** https://drive.google.com/file/d/1te1oqv702h3VbqdKNyemR6DLMI0ZBvHQ/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (50 pages) covering active and passive mixer topologies including the Gilbert cell, single- and double-balanced active mixers, passive MOS ring mixer, diode ring mixer, and advanced topics such as N-path filters and SpectreRF simulation of mixers using PSS/PAC/PNoise analyses.

## Unique contribution
Provides a unified treatment of conversion gain for all common mixer types, from the analytical formula gc = (2/π)·gm·Q for single-balanced to (4/π)·gm·Q for double-balanced, and introduces N-path filters as a switched-capacitor frequency-translation technique achieving high Q with CMOS switches.

## Key concepts
- Gilbert cell (double-balanced active mixer)
- Single-balanced mixer
- Conversion gain gc
- Passive MOS ring mixer
- Diode ring mixer
- LO switching (commutating)
- IIP3 of mixers
- Flicker noise in mixers
- N-path filter
- PSS/PAC/PNoise simulation (SpectreRF)

## Methods / results / takeaways
- Active mixer (single-balanced): conversion gain gc = (2/π)·gm·RL from Fourier analysis of the LO-switched current; double-balanced gains 6 dB: gc = (4/π)·gm·RL.
- Gilbert cell: the RF gm stage converts voltage to current; the LO-driven switching quad commutates (multiplies) the current by ±1; IF load converts back to voltage.
- Active mixer advantages: conversion gain, noise suppression of RF stage. Disadvantages: higher 1/f noise from switching transistors, LO-to-RF leakage through switching pair.
- Passive MOS ring mixer: switches operated by LO without DC bias; conversion loss ≈ 3.9 dB (π²/4 factor); but no 1/f noise contribution, high IIP3 because no gm nonlinearity.
- Diode ring mixer: classic RF building block; operates to THz frequencies using Schottky diodes; provides broadband mixing and high dynamic range.
- N-path filter: multiple (N) switched-capacitor paths driven by N-phase LO; achieves bandpass filtering centered at fLO with Q proportional to fLO/(fLO/N); reconfigurable, high-Q, integrated in CMOS.
- SpectreRF workflow: PSS → finds periodic steady state; PAC → small-signal AC sweeping conversion gain; PNoise → noise figure of the mixer including cyclostationary effects.
