# Baseline Signal Reconstruction for Temperature Compensation in Lamb Wave Damage Detection

- **Source:** Baseline Signal Reconstruction for Temperature Compensation (2016) Liu.pdf
- **Drive link:** https://drive.google.com/file/d/1z-yWsKG8G5ZPa0R-ljztjylARvKJlmiV/view
- **Type:** paper
- **Author/Year:** Liu, Xiao, Zhang & Ren / 2016
- **Coverage:** full

## Overview
Published in Sensors 2016, 16, 1273 (MDPI). Proposes a temperature compensation method that reconstructs the baseline signal at the temperature of the current signal using the Hilbert transform for phase compensation and Orthogonal Matching Pursuit (OMP) for amplitude compensation, validated on composite panels with a 18°C effective range.

## Unique contribution
Combines Hilbert transform phase compensation with OMP-based amplitude compensation to reconstruct the baseline signal without model training. Demonstrates that the instantaneous phase difference is proportional to temperature difference, and validates damage detection improvement on composite panels.

## Key concepts
- Baseline signal reconstruction
- Temperature compensation
- Hilbert transform (instantaneous phase)
- Orthogonal Matching Pursuit (OMP)
- Lamb waves
- Composite panel
- PZT (piezoelectric) transducers
- Damage detection

## Methods / results / takeaways
- Hypothesis: instantaneous phase difference between two Lamb wave signals at different temperatures is proportional to the temperature difference (confirmed experimentally).
- Phase compensation: use Hilbert transform to extract instantaneous phase of baseline and reference signals; linearly interpolate/extrapolate phase to the current temperature; reconstruct compensated baseline.
- Amplitude compensation: OMP finds the best scalar representation of the current signal using the compensated baseline as the dictionary atom; β = ⟨ŝ_b, s_c⟩.
- Compensation standard: Err = 20 log(‖s_y−s_x‖_∞/‖s_x‖_∞); threshold set at −22 dB.
- Effective range: ±9°C from baseline temperature (total 18°C interval) at frequencies 50–210 kHz.
- Temperature difference between reference and baseline should be small (3°C used); larger gaps degrade performance.
- Validated with damage detection: delay-and-sum imaging correctly located impact damage at 26°C after compensation from 18°C baseline.
