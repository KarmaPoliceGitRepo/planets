# Tomography and Image Reconstruction
**Aliases:** tomography; ray tomography; guided-wave ray tomography; 2D temperature field reconstruction; temperature tomography; straight-ray tomography; algebraic reconstruction; back-projection; computed tomography

**Definition:** Tomographic reconstruction infers a 2D (or 3D) field from projections (line integrals) measured along multiple paths. Straight-ray tomography assumes rectilinear propagation and inverts the Radon transform; algebraic reconstruction techniques (ART, SART) solve the discrete linear system iteratively. In guided-wave SHM, transit times between sensor pairs are used as projection data to reconstruct spatial maps of wave speed (related to damage or temperature). Regularisation (Tikhonov, TV) is essential when the ray coverage is sparse. In ultrasonic temperature measurement, multiple ToF paths through a component are inverted to yield a 2D internal temperature distribution.

**Key relations:**
- related: [time-of-flight](time-of-flight.md)
- related: [regularisation](regularisation.md)
- related: [structural-health-monitoring](structural-health-monitoring.md)
- related: [temperature-compensation](temperature-compensation.md)

**Discussed in:**
- [Guided Wave Ray Tomography Temperature](../notes/signal-processing/guided-wave-ray-tomography-temperature.md) — straight-ray tomography applied to guided-wave signals for temperature-change mapping; inversion algorithm
