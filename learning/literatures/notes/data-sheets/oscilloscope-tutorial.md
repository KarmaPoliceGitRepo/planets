# Digital Oscilloscope Tutorial (Yokogawa)

- **Source:** oscilloscopetutorial_01.pdf
- **Drive link:** https://drive.google.com/file/d/1AdCSBqRA9cmMJKmYwo8XwvSY6GOe27AY/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Yokogawa, ~2017
- **Coverage:** full

## Overview
A tutorial document explaining the key technical aspects of digital storage oscilloscopes (DSOs) through a series of Q&A-formatted explanations. Covers effective bandwidth vs. analog bandwidth, memory length effects on sample rate, display methods, dead time, Equivalent Time Sampling (ETS), resolution enhancement via box averaging, and Yokogawa's parallel multiprocessor architecture.

## Unique contribution
Explains the often-misunderstood relationship between memory depth and sample rate: at a given timebase setting, more memory = higher sample rate = higher effective bandwidth. This is illustrated concretely: 1k memory gives 1 MS/s (effective BW 400 kHz), while 100k memory gives 100 MS/s (effective BW 40 MHz) — even if the instrument's hardware can do 500 MS/s.

## Key concepts
- Effective bandwidth (BW_DSO = sample_rate / 2.5)
- Memory depth vs. sample rate trade-off
- Data decimation vs. full-memory display
- Display update rate (dead time)
- Equivalent Time Sampling (ETS) for repetitive signals
- Box averaging for single-shot noise reduction
- Parallel multiprocessor architecture (Yokogawa)
- Envelope mode and persistence display

## Methods / results / takeaways
- BW_DSO = sampling_rate / 2.5 for sinusoidal signals; for complex signals, >2.5× oversampling needed.
- Memory length determines the sample rate at any given timebase setting — a 500 MHz analog bandwidth instrument is useless if memory is only 1k words at 100 µs/div.
- Box averaging: if max sample rate = 200 MS/s but display uses 10 MS/s, 20 samples are averaged per point, improving S/N by √20 ≈ 4.5×; equivalent to ~2 extra ADC bits.
- ETS achieves GHz-equivalent sampling for repetitive signals by shifting sample points by picoseconds relative to trigger.
- Dead time (data processing time between acquisitions) is minimized by parallel processor architecture; Yokogawa achieves 60 Hz display update rate with 10k memory regardless of other settings.
- Yokogawa DL2700 series uses hardware box averaging applied immediately after each A/D conversion.
