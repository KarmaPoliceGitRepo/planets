# Temperature Compensation in SHM
**Aliases:** temperature compensation; BSS; Baseline Signal Stretch; baseline signal stretch; optimal baseline selection; scale transform; DTW temperature compensation; physics-based temperature compensation; temperature-phase velocity compensation

**Definition:** In guided-wave structural health monitoring (SHM), temperature changes cause velocity shifts and thermal expansion that shift and stretch the wave signal in time, creating false-alarm damage signatures. Temperature compensation methods include: (i) Baseline Signal Stretch (BSS) — scaling the time axis of the stored baseline signal by the ratio of velocities at reference and current temperatures; (ii) Dynamic Time Warping (DTW) — non-uniform time-axis alignment; (iii) Optimal Baseline Selection (OBS) — choosing from a library of baselines the one recorded at the closest temperature; (iv) physics-based models — using V(T) calibration curves to compute the expected TOF shift and correct the signal. BSS is computationally simple and effective for narrow temperature ranges; DTW handles larger changes.

**Key relations:**
- related: [structural-health-monitoring](structural-health-monitoring.md)
- related: [temperature-dependence-of-sound-speed](temperature-dependence-of-sound-speed.md)
- related: [time-of-flight](time-of-flight.md)
- related: [guided-waves](guided-waves.md)
- related: [lamb-wave](lamb-wave.md)

**Discussed in:**
- [Croxford 2010 — Temperature Compensation SHM](../notes/effect-of-temperature/croxford-2010-temperature-compensation-shm.md) — BSS and OBS methods; experimental validation
- [Baseline Signal Reconstruction (signal-processing)](../notes/signal-processing/baseline-signal-reconstruction-temperature-compensation.md) — signal reconstruction approach to temperature correction
- [Scale Transform (signal-processing)](../notes/signal-processing/scale-transform-temperature-compensation.md) — scale-transform equivalent of BSS
- [DTW Temperature Compensation (signal-processing)](../notes/signal-processing/dtw-temperature-compensation.md) — dynamic time warping for non-linear velocity-change correction
- [Physics-Based Temperature Compensation (Roy — signal-processing)](../notes/signal-processing/physics-based-temperature-compensation-roy.md) — V(T) model-based TOF correction
- [Temperature Phase Velocity Compensation (Mariani — signal-processing)](../notes/signal-processing/temperature-phase-velocity-compensation-mariani.md) — phase-velocity-based compensation for Lamb wave SHM
- [Konstantinidis 2007 — Temperature Stability SHM](../notes/effect-of-temperature/konstantinidis-2007-temperature-stability-shm.md) — systematic study of temperature-induced baseline drift in SHM systems
