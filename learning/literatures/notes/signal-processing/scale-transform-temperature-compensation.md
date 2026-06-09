# Scale Transform Signal Processing for Optimal Ultrasonic Temperature Compensation

- **Source:** Scale transform signal processing for optimal ultrasonic temperature compensation - (2012) JB Harley.pdf
- **Drive link:** https://drive.google.com/file/d/1XtQaoT-wWNu0X7ARiKh6QOYHm_XXzq6e/view
- **Type:** paper
- **Author/Year:** Harley & Moura / 2012
- **Coverage:** partial (large file, truncated extraction)

## Overview
Published in IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control 59(10), 2012. Introduces the scale transform domain as an optimal framework for compensating temperature-induced stretching of guided wave signals in structural health monitoring (SHM), presenting three efficient algorithms.

## Unique contribution
Shows that temperature primarily causes a scale (time-stretch) transformation of guided wave signals; the scale transform domain is the natural setting for this compensation. Three algorithms of increasing computational efficiency are presented, making the approach viable for real-time SHM.

## Key concepts
- Scale transform
- Temperature compensation
- Guided waves (Lamb waves)
- Structural health monitoring (SHM)
- Baseline signal stretch (BSS)
- Signal warping
- Computational efficiency

## Methods / results / takeaways
- Temperature change affects wave velocity and therefore scales the time axis of the received signal.
- The scale transform (a Mellin-type transform) maps time-stretch operations into simple translations, analogous to how the Fourier transform maps time-shift to phase rotation.
- Optimal compensation: find the scale factor (stretch ratio) that maximises correlation between the current and baseline signals in the scale transform domain.
- Three algorithms presented with different speed/accuracy trade-offs; the fastest achieves near-real-time performance.
- Generalises baseline signal stretch (BSS) approach and provides an optimality criterion (maximum likelihood under Gaussian noise assumption).
- Performance superior to direct time-domain stretch search at low SNR.
