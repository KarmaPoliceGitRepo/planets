# Structural Health Monitoring
**Aliases:** SHM; structural health monitoring; non-destructive testing; NDT; guided-wave tomography; damage detection; robust PCA; corrosion monitoring; TOFD

**Definition:** Structural health monitoring (SHM) is the continuous or periodic automated assessment of a structure's integrity using embedded or attached sensors, typically piezoelectric or fibre-optic. In guided-wave SHM, Lamb or cylindrical-guided waves are excited and their changes in amplitude, phase, or time-of-flight between sensor pairs are used to detect, locate, and characterise damage. Temperature changes produce large baseline shifts (see temperature compensation); robust PCA separates low-rank (temperature-driven) and sparse (damage-driven) components of the signal matrix. TOFD and pulse-echo C-scan are related non-destructive testing methods used in periodic inspection rather than continuous monitoring.

**Key relations:**
- related: [temperature-compensation](temperature-compensation.md)
- related: [dispersion-curves](dispersion-curves.md)
- related: [time-of-flight](time-of-flight.md)
- related: [regularisation](regularisation.md)

**Discussed in:**
- [Robust PCA — Temperature and Damage Detection](../notes/signal-processing/robust-pca-temperature-damage-detection.md) — robust PCA to decouple temperature and damage contributions in SHM signal matrix
- [Corrosion Monitoring Guided Wave](../notes/signal-processing/corrosion-monitoring-guided-wave.md) — guided-wave SHM applied to pipe corrosion detection
- [Guided Wave Ray Tomography Temperature](../notes/signal-processing/guided-wave-ray-tomography-temperature.md) — ray-tomography reconstruction of damage from guided-wave transit times
- [TOFD Neural-Network Defect Detection](../notes/signal-processing/tofd-neural-network-defect.md) — TOFD applied to weld inspection; neural-network interpretation of diffraction signals
