# Temperature Compensation
**Aliases:** temperature compensation; baseline signal stretch; scale transform; DTW temperature compensation; physics-based compensation; signal warping; dynamic time warping

**Definition:** Temperature compensation corrects ultrasonic time-of-flight or waveform data for the change in wave velocity caused by temperature variation. The simplest model stretches (or compresses) the reference waveform by a factor proportional to the fractional velocity change ΔV/V₀. More sophisticated methods include: the scale transform (projecting the signal onto a basis of dilated replicas), dynamic time warping (DTW, non-linear alignment of two time series), and physics-based approaches using a velocity-temperature model to predict the exact warp function. Compensation is critical in structural health monitoring (SHM) where the damage signal must be separated from the temperature-induced baseline shift.

**Key relations:**
- related: [time-of-flight](time-of-flight.md)
- related: [kalman-filter](kalman-filter.md)
- related: [structural-health-monitoring](structural-health-monitoring.md)
- related: [cross-correlation](cross-correlation.md)

**Discussed in:**
- [Baseline Signal Reconstruction — Temperature Compensation](../notes/signal-processing/baseline-signal-reconstruction-temperature-compensation.md) — reviews signal-stretch, optimal baseline selection, and Hilbert phase methods for waveform temperature compensation
- [Scale Transform Temperature Compensation](../notes/signal-processing/scale-transform-temperature-compensation.md) — scale-transform approach; analytic framework for warp-factor estimation
- [DTW Temperature Compensation](../notes/signal-processing/dtw-temperature-compensation.md) — dynamic time warping applied to SHM signals; comparison with uniform stretch
- [Physics-Based Temperature Compensation (Roy)](../notes/signal-processing/physics-based-temperature-compensation-roy.md) — velocity-temperature model used to predict and correct waveform distortion
- [Temperature–Phase Velocity Compensation (Mariani)](../notes/signal-processing/temperature-phase-velocity-compensation-mariani.md) — guided-wave SHM compensation using temperature-dependent phase velocity map
