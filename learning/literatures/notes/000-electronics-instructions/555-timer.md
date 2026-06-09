# 555 Timer

- **Source:** 555-Timer.pdf
- **Drive link:** https://drive.google.com/file/d/1EEm7GVbTV0zb8lRUNNKVT5ZzVf3xCfMI/view
- **Type:** notes
- **Author/Year:** Amanda Ghassaei / 2012
- **Coverage:** full

## Overview
A beginner-level tutorial from Instructables.com explaining how the 555 timer IC works. It covers the chip's pinout and three standard operating modes with practical circuit examples and waveform diagrams.

## Unique contribution
Accessible hands-on introduction to the 555 timer; provides circuit diagrams and component value guidance for all three modes in a single short document, making it useful as a quick reference.

## Key concepts
- 555 timer IC
- Astable mode
- Monostable mode
- Bistable mode
- Duty cycle
- RC time constant
- Comparators
- Flip-flop

## Methods / results / takeaways
- The 555 has 8 pins: GND, trigger, output, reset, control voltage, threshold, discharge, VCC.
- Astable mode: the output continuously toggles between HIGH and LOW; frequency and duty cycle are set by two resistors and a capacitor.
- Monostable mode: a single pulse of controlled duration is produced each time a trigger is applied; pulse width = 1.1·R·C.
- Bistable mode: the output latches high or low based on set/reset inputs; useful as a debounce circuit.
- The internal comparator thresholds are at 1/3 VCC (trigger) and 2/3 VCC (threshold), established by the internal voltage divider.
