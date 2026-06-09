# High-Accuracy Acoustic Relative Humidity Sensor

- **Source:** van Schaik 2010 acoustic RH sensor
- **Drive link:** https://drive.google.com/file/d/1I3hDYgXSteuHJCzy1VlwfJQFzH4eZXCc/view
- **Type:** paper
- **Author/Year:** van Schaik, 2010
- **Coverage:** full

## Overview
Describes an acoustic sensor measuring relative humidity (RH) by combining time-of-flight measurements of sound speed (50 kHz transducers, 4 temperature sensors) with humidity models. Achieves RH accuracy better than 2% above 50 °C, gas velocity ±0.13 m/s, temperature ±0.07 °C.

## Unique contribution
Demonstrates that a single acoustic path can simultaneously extract temperature, gas velocity, and humidity by exploiting the known dependence of speed of sound on all three variables. The multi-sensor fusion approach and calibration method achieve high accuracy in harsh industrial gas environments where optical or capacitive sensors fail.

## Key concepts
- Acoustic humidity sensing
- Speed of sound vs humidity/temperature
- Time-of-flight measurement
- Multi-variable acoustic sensing
- 50 kHz air-coupled transducers
- Temperature compensation

## Methods / results / takeaways
- 50 kHz transducers, separation ~0.3 m, crossed paths for flow compensation.
- 4 precision temperature sensors for local air temperature mapping.
- Gas velocity accuracy: ±0.13 m/s; temperature accuracy: ±0.07 °C; RH accuracy: < 2% (above 50 °C).
- Measurement bandwidth sufficient for slowly varying industrial process gas streams.
- Key insight: speed of sound depends on T, RH, and CO₂; solving the simultaneous equations with redundant sensors de-correlates the variables.
- Applicable to process monitoring, HVAC, and compensation of TOF-based ranging in non-standard atmospheres.
