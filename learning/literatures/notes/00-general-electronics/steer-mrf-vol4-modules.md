# Microwave and RF Design, Volume 4: Modules

- **Source:** Michael Steer - Microwave and RF Design - Volume 4 - Modules - Third Edition.pdf
- **Drive link:** https://drive.google.com/file/d/1wduJWqWommLXtowlHMRiiXE0BWDHWYpW/view?usp=drivesdk
- **Type:** book
- **Author/Year:** Michael Steer, NC State University / LibreTexts, 2019/2021; CC BY-NC-SA 3.0
- **Coverage:** partial (large file, truncated extraction)

## Overview
Volume 4 covers RF and microwave modules — the subsystem-level building blocks used to assemble complete transceivers. Topics include mixers, modulators, frequency synthesizers, phase-locked loops (PLLs), oscillators (at module level), voltage-controlled oscillators (VCOs), and complete receiver/transmitter architectures. A 15 GHz receiver subsystem serves as a running design example.

## Unique contribution
Bridges component-level theory (from Vols. 1–3) to system-level integration by showing how individual active and passive components are assembled into functional RF modules. The 15 GHz receiver case study provides a concrete system-design exercise.

## Key concepts
- RF module: complete functional subsystem (mixer, LNA, filter, PA, synthesizer)
- Mixer: frequency conversion via nonlinearity, conversion loss, IF/RF/LO ports
- Frequency synthesizer, phase-locked loop (PLL)
- Voltage-controlled oscillator (VCO), phase noise
- Receiver architecture: superheterodyne, direct conversion (zero-IF), low-IF
- Transmitter architecture
- Integrated circuit (IC) vs. hybrid module design

## Methods / results / takeaways
- A superheterodyne receiver uses a mixer + filter to translate the RF signal to a fixed IF, where channel selection is easier.
- Direct-conversion (zero-IF) receivers eliminate the IF stage but suffer from DC offset and LO leakage issues.
- Phase noise of the local oscillator is a critical spec: it directly limits the receiver's ability to reject adjacent channels.
- The 15 GHz receiver example (from the book introduction) demonstrates how gain, noise figure, and linearity specifications cascade through the chain.
- Distributed as LibreTexts OER as well as NC State print edition.
