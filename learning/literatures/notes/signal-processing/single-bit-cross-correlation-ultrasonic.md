# Cross-Correlation by Single-Bit Signal Processing for Ultrasonic Distance Measurement

- **Source:** Cross-Correlation by Single-bit Signal Processing for Ultrasonic Distance Measurement...pdf
- **Drive link:** https://drive.google.com/file/d/1X8515P2whKysBPiu9gV9CUtw_XxKMYiD/view
- **Type:** paper
- **Author/Year:** Hirata, Kurosawa & Katagiri / 2008
- **Coverage:** full

## Overview
Published in IEICE Transactions on Fundamentals E91-A(4), 2008. Proposes using delta-sigma modulated single-bit representations of transmitted and received ultrasonic signals to compute cross-correlation purely through EXOR/NOT logic operations, eliminating hardware multipliers.

## Unique contribution
Replaces conventional multiply-accumulate cross-correlation with single-bit EXOR operations on delta-sigma bitstreams, drastically reducing hardware complexity. A moving average filter smooths the binary correlation output.

## Key concepts
- Single-bit signal processing
- Delta-sigma modulation
- Cross-correlation
- EXOR / NOT logic operations
- Moving average filter
- Time-of-flight (ToF) measurement
- Hardware simplification

## Methods / results / takeaways
- Delta-sigma modulation: analog signal is quantised to a 1-bit stream at high oversampling rate.
- Cross-correlation of two 1-bit streams: EXOR of the two bitstreams produces the polarity of the product (+1 or -1); accumulation (moving average) gives the correlation value.
- Eliminates multipliers entirely; implementable in simple digital logic or FPGA.
- Moving average filter length is a key parameter: longer window reduces noise but limits time resolution.
- Demonstrated for ultrasonic distance measurement; ToF extracted from peak of the correlation function.
- Trade-off: single-bit quantisation introduces quantisation noise, but oversampling keeps SNR acceptable for moderate-precision ranging.
