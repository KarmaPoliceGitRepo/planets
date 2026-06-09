# Telegrapher's Equations

**Aliases:** transmission line equations; telegraph equations; distributed line equations; Telegrapher's equations

**Definition:** The Telegrapher's equations are the coupled first-order PDEs describing voltage V and current I on a distributed transmission line: ∂V/∂z = −(R + jωL)I and ∂I/∂z = −(G + jωC)V in the frequency domain, or with ∂/∂t replacing jω in the time domain. They follow from applying Kirchhoff's laws to the infinitesimal RLGC lumped-element model of a line section dz. Their general solution gives forward and backward travelling waves V = V⁺e^(−γz) + V⁻e^(+γz), where γ = √((R+jωL)(G+jωC)) is the propagation constant. In the lossless case (R = G = 0) they reduce to the wave equation.

**Key relations:**
- [transmission-line](transmission-line.md) — the Telegrapher's equations are the governing equations
- [propagation-constant](propagation-constant.md) — γ is derived directly from them
- [characteristic-impedance](characteristic-impedance.md) — Z₀ = (R+jωL)/γ from the equations
- [reflection-coefficient](reflection-coefficient.md) — solution boundary conditions give Γ at termination

**Discussed in:**
- [Module 1: Introduction to Transmission Lines](../notes/000-electronics-instructions/module1-introduction-to-transmission-lines.md) — derivation and solution
- [Transmission Line Circuit Model](../notes/00-general-electronics/transmission-line-circuit-model.md) — RLGC model and Telegrapher's equation derivation
