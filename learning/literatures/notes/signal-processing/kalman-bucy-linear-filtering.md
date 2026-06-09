# New Results in Linear Filtering and Prediction Theory

- **Source:** New results in linear filtering and prediction theory.pdf
- **Drive link:** https://drive.google.com/file/d/1nZe1J5Pxr8PCb6J4Wd_x-no431xvHkD7
- **Type:** paper
- **Author/Year:** Kalman & Bucy / 1961
- **Coverage:** partial (large file, truncated extraction)

## Overview
A foundational paper in control and signal processing theory, published in ASME Transactions Journal of Basic Engineering (1961). Extends the Kalman filter to continuous-time systems (Kalman-Bucy filter) and presents new results in linear optimal filtering for stochastic systems with process and observation noise.

## Unique contribution
Introduces the continuous-time Kalman-Bucy filter: the optimal linear state estimator for continuous-time linear stochastic systems, derived from the Riccati differential equation. Seminal reference for all modern state-space filtering.

## Key concepts
- Kalman filter
- Kalman-Bucy filter (continuous-time)
- State-space representation
- Riccati equation (Riccati differential equation)
- Linear optimal estimator
- Process noise covariance (Q)
- Observation noise covariance (R)
- Innovation process
- Stochastic differential equations

## Methods / results / takeaways
- System model: dx = Fx dt + G dw (state dynamics); dz = H x dt + dv (observation); w, v are white noise processes with covariances Q, R.
- Optimal filter: dx̂ = Fx̂ dt + K(dz − Hx̂ dt); Kalman gain K = PH'R⁻¹.
- Riccati equation: dP/dt = FP + PF' + GQG' − PH'R⁻¹HP; P is the error covariance.
- Steady-state solution (time-invariant system): algebraic Riccati equation gives constant K.
- Duality with LQR (linear quadratic regulator) problem: optimal estimator and optimal controller are dual problems.
- Foundation for all subsequent work on state estimation, sensor fusion, and modern control.
