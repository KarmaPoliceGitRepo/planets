# Digital Time-of-Flight Measurement for Ultrasonic Sensors

- **Source:** Digital Time-of-Flight Measurement for Ultrasonic Sensors - (1992) D Marioli.pdf
- **Drive link:** https://drive.google.com/file/d/13m2eUM5DDacPuikCAmbdDWXdIAu-v8zA/view
- **Type:** paper
- **Author/Year:** Marioli et al. / 1992
- **Coverage:** full

## Overview
Published in IEEE Transactions on Instrumentation and Measurement 41(1), 1992. Presents a digital ToF measurement system for air-coupled ultrasonic sensors using envelope cross-correlation with parabolic interpolation to achieve sub-sample accuracy, demonstrating ranging within 0.5 mm at distances up to 1.2 m.

## Unique contribution
Uses a square-law envelope detector followed by cross-correlation of the envelopes (rather than the raw RF signals) to obtain a smooth correlation peak, then applies parabolic interpolation around the peak for sub-sample ToF estimation. Demonstrates practical 0.5 mm accuracy.

## Key concepts
- Time-of-flight (ToF) measurement
- Envelope detection (square-law)
- Cross-correlation
- Parabolic interpolation
- Sub-sample accuracy
- Air-coupled ultrasonic sensor
- Pulse-echo ranging

## Methods / results / takeaways
- Square-law envelope detector: rectify and low-pass filter the received RF signal to obtain the envelope.
- Cross-correlate transmitted and received envelopes (slower varying than RF, so less susceptible to phase errors).
- Peak of cross-correlation gives coarse ToF estimate at integer sample resolution.
- Parabolic interpolation: fit a parabola through the three samples around the peak; the parabola vertex gives sub-sample ToF.
- Results: distance measurement accurate to within ±0.5 mm at distances from ~0.2 m to 1.2 m in air.
- Method is robust to frequency variations and does not require knowledge of the carrier frequency.
