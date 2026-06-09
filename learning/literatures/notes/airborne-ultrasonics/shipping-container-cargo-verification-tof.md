# Air-Coupled Ultrasound TOF Estimation for Cargo Verification

- **Source:** McVittie 2008 shipping container cargo verification
- **Drive link:** https://drive.google.com/file/d/1witaMa_nZGfPc7NnNWrePkFovF8LGeEN/view
- **Type:** paper
- **Author/Year:** McVittie, Fortunko & Bray, 2008 (ICASSP 2008)
- **Coverage:** full

## Overview
Evaluates three time-of-flight (TOF) estimators — cross-correlation envelope (CCE), envelope ratio estimation (EREE), and half-peak time (HPT) — for air-coupled ultrasonic cargo verification inside actual shipping containers. Tests cover 24-hour environmental temperature swing (64–114°F / 18–46°C) with a temperature-compensated system.

## Unique contribution
Direct comparison of CCE, EREE, and HPT TOF estimators under real shipping-container conditions (temperature drift, mechanical vibration). Shows HPT (half-peak time of received pulse envelope) achieves lowest variance while remaining computationally simple — a practical recommendation for fieldable cargo-verification systems.

## Key concepts
- Time-of-flight (TOF) estimation
- Cross-correlation envelope (CCE)
- Envelope ratio estimation (EREE)
- Half-peak time (HPT)
- Air-coupled ultrasound
- Cargo verification / security screening
- Temperature compensation
- Shipping container environment

## Methods / results / takeaways
- Setup: air-coupled transducers across interior of a standard ISO shipping container.
- Temperature range tested: 64–114°F (18–46°C) over a 24-hour cycle; temperature compensation applied to speed-of-sound.
- TOF estimators compared: CCE (peak of cross-correlation envelope), EREE (ratio of envelope values at two time points), HPT (time when envelope reaches half of its peak value).
- Result: HPT had lowest variance across the temperature range and is computationally simplest.
- CCE and EREE showed higher variance, particularly at temperature extremes.
- Conclusion: HPT recommended as the default estimator for robust field-deployed cargo verification.
