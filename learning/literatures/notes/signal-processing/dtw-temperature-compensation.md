# Dynamic Time Warping Temperature Compensation for Guided Wave SHM

- **Source:** Dynamic Time Warping Temperature Compensation (2018) Douglass.pdf
- **Drive link:** https://drive.google.com/file/d/10GIiySZY-0Khc9qqQ5ayH3LLgrwMNJH7/view
- **Type:** paper
- **Author/Year:** Douglass & Harley / 2018
- **Coverage:** partial (large file, truncated extraction)

## Overview
Published in IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control 65(5), May 2018. Uses Dynamic Time Warping (DTW) to better align guided wave signals to a baseline for temperature compensation, showing DTW outperforms stretch-based methods (BSS, scale transform) for large temperature variations, long propagation distances, and high frequencies.

## Unique contribution
Demonstrates that DTW, which allows non-uniform time warping (unlike global stretch which assumes uniform dilation), better handles guided wave dispersion effects and large temperature changes where the stretch assumption breaks down.

## Key concepts
- Dynamic Time Warping (DTW)
- Temperature compensation
- Baseline signal stretch (BSS)
- Scale transform
- Guided waves
- Structural health monitoring (SHM)
- Dispersion
- Non-uniform warping

## Methods / results / takeaways
- Stretch-based methods (BSS, scale transform) assume temperature causes a uniform time dilation of the signal; fails for dispersive signals at large temperature changes.
- Dispersive guided waves: different frequency components travel at different speeds; temperature changes the velocity curve, so the dilation is frequency-dependent (non-uniform in time).
- DTW: finds the optimal non-linear time-warping path between two sequences by minimising cumulative alignment distance; allows non-uniform time-axis distortions.
- Experiments and simulations: DTW consistently outperforms BSS and scale transform when temperature variation is large (>20°C), propagation distance is long, or signal frequency is high.
- DTW accurately aligns weak reflections and late-arriving modes that stretch-based methods misalign.
- More robust damage detection with DTW compensation: reduces false positives from temperature misalignment.
