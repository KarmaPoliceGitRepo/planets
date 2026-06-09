# Temperature-Compensated Ultrasonic Distance Sensor

- **Source:** Canali et al. 1982 temperature-compensated sensor
- **Drive link:** https://drive.google.com/file/d/1UYEDBZWId44-ezqM_MRew8ZYmxv9r3OG/view
- **Type:** paper
- **Author/Year:** Canali et al., 1982
- **Coverage:** full

## Overview
Early paper describing a temperature-compensated ultrasonic distance sensor operating at 250 kHz using PXE 5 piezoceramic with silicon rubber matching layer. Covers 0–100 cm range with ±1 mm accuracy across −20 °C to +110 °C using NE555 + LM1812 ICs for drive and detection.

## Unique contribution
One of the earliest systematic treatments of temperature compensation in air-coupled TOF ranging, proposing both hardware (on-board thermistor correction) and circuit-level (NE555 timing, LM1812 receiver) implementation. Demonstrates ±1 mm over wide temperature range using low-cost silicon rubber matching.

## Key concepts
- Temperature compensation
- Ultrasonic distance measurement
- 250 kHz piezoceramic (PXE 5)
- Silicon rubber impedance matching layer
- TOF ranging
- NE555 timer, LM1812 ultrasonic receiver IC
- Range 0–100 cm

## Methods / results / takeaways
- Transducer: 250 kHz PXE 5 ceramic + silicon rubber λ/4 matching layer.
- Temperature range: −20 °C to +110 °C; speed-of-sound correction via thermistor.
- Accuracy: ±1 mm over full 0–100 cm range.
- Electronics: NE555 for pulse generation, LM1812 for receive signal processing (threshold detection).
- Matching layer: silicon rubber chosen for intermediate acoustic impedance (~1.6 MRa) to partially bridge air–ceramic mismatch.
- Early but influential design; many subsequent sensor papers reference this architecture.
- Limitation: threshold detection is sensitive to target reflectivity; SNR drops for soft/angled targets.
