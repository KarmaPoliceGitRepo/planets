# Digital Signal Processing Methods for Ultrasonic Echoes

- **Source:** Digital Signal Processing Methods for Ultrasonic Echoes - (2016) KM Sinding CS Drapaca BR Tittmann.pdf
- **Drive link:** https://drive.google.com/file/d/1iiH4xDeAsGR8-6ZzOuPQmq7yuhw7A0Y1/view
- **Type:** paper
- **Author/Year:** Sinding, Drapaca & Tittmann / 2016
- **Coverage:** full

## Overview
Published in IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control 63(8), 2016. Compares Total Variation (TV) regularization, Tikhonov regularization, and conventional bandpass filtering for enhancing ultrasonic pulse-echo signals, showing regularization methods significantly outperform bandpass filtering in SNR improvement.

## Unique contribution
Demonstrates that both TV and Tikhonov regularization can increase SNR by over 400% compared to unprocessed signals, and substantially outperform bandpass filtering, with the MM (Majorization-Minimization) algorithm used efficiently for TV deconvolution.

## Key concepts
- Total Variation (TV) regularization
- Tikhonov regularization
- Bandpass filtering
- MM (Majorization-Minimization) algorithm
- Deconvolution
- SNR improvement
- Pulse-echo ultrasonics

## Methods / results / takeaways
- Problem: ultrasonic echoes are corrupted by noise and transducer bandwidth limitations; goal is to recover a clean signal.
- TV regularization: minimises total variation of the output signal (encourages piecewise-constant solutions with sharp edges); handles sparse spike-like reflections well.
- Tikhonov regularization: adds an L2 penalty on the solution magnitude and/or its derivative; smooth solutions.
- MM algorithm: iterative technique for TV minimisation; converts the non-differentiable TV objective into a sequence of quadratic problems.
- Optimal regularization parameter selected by minimising residual SNR metric.
- Results: SNR increase >400% with optimised TV/Tikhonov vs. raw signal; significant improvement over bandpass filtering.
- Trade-off: regularization requires parameter tuning; bandpass filtering is simpler but less effective.
