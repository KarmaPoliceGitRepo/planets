# The Measurement of Liner-Piston Skirt Oil Film Thickness by an Ultrasonic Means

- **Source:** SAE Technical Paper 2006-01-0648
- **Drive link:** https://drive.google.com/file/d/1AiP8WZRleCaEVtnSBVDBfFsSZT3nZwwh/view
- **Type:** paper
- **Author/Year:** Dwyer-Joyce, Green, Balakrishnan, Harper, Lewis, Howell-Smith, King, Rahnejat / 2006 (SAE 2006-01-0648; University of Sheffield / Loughborough University / Perfect Bore Ltd)
- **Coverage:** full

## Overview
Demonstrates the first application of a non-invasive ultrasonic method for measuring piston skirt-liner oil film thickness in a fired single-cylinder engine. A 10 MHz PZT sensor bonded to the outer surface of a wet liner generates pulse-echo signals; the reflection coefficient (from FFT analysis) is used to determine oil film thickness via a spring-layer model. Motored and fired tests conducted on a 449 cc 4-stroke engine.

## Unique contribution
First fired-engine measurement of piston skirt OFT using ultrasonic technique bonded to liner exterior (non-invasive), eliminating the need for liner penetration. Validates the method against numerical predictions of piston-skirt tilt and minimum film thickness from Balakrishnan & Rahnejat (2002).

## Key concepts
- Ultrasonic OFT measurement; pulse-echo mode
- Spring-layer model; reflection coefficient R
- PZT sensor bonded to wet liner exterior (non-invasive)
- Piston skirt oil film thickness
- FFT of ultrasonic pulse; bulk modulus; acoustic impedance
- Motored vs fired engine tests
- 449 cc single-cylinder 4-stroke; 96 mm bore; 64 mm stroke

## Methods / results / takeaways
- Method: R = |reflected amplitude / reference amplitude| from FFT; h = (ρc²/K) × R²/(1−R²) × 1/(ωz)² (from spring model); K = B/h where B = bulk modulus.
- Sensor: 10 MHz PZT, 7 mm dia, 0.2 mm thick; bonded to outer wet surface of liner at TDC position. Pulsed at 5 kHz; 250 pulses per capture cycle; LeCroy oscilloscope.
- Motored tests (850, 1800, 6000 rpm): minimum film at TDC ~9.4 µm (850 rpm); increases to ~16.5 µm mid-stroke as residual oil is entrained. Film thickness increases with engine speed.
- Fired tests at 1800 rpm: minimum film ~2 µm observed at end of return stroke.
- Numerical comparison: Balakrishnan & Rahnejat model predicts piston tilt 0.085°, side force 4800 N, minimum film 1.94 µm at TDC — good agreement with measured ~2 µm.
- Limitation: sensor spatial resolution > 1 mm; cannot resolve individual ring passage (zone B in signal); only skirt region measurable at this sensor location.
- Measurement range: 2–21 µm across all tested conditions.
- Note: this is the earliest Dwyer-Joyce publication on skirt OFT measurement; the 2014 extension (mills-dwyer-joyce-skirt-film-2014) uses a full 15-sensor array on a fired Honda engine.
