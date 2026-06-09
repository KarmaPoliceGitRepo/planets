# The Nonlinear Wave Equation and the Interaction of Waves

- **Source:** 7-Nonlinear_Wave_Equation-22C-W15.pdf
- **Drive link:** https://drive.google.com/file/d/1lvvyEGeUME6sPZGNQ4MVxYRcwRh1O8Hy/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** MATH 22C course notes (UC Davis or similar)
- **Coverage:** full

## Overview
Course notes on the nonlinear wave equation derived from the compressible Euler equations in Lagrangian coordinates (the "p-system"). Develops Riemann invariants for both linear and nonlinear wave equations to identify left/right-going waves and explain how nonlinear waves interact without the benefit of superposition.

## Unique contribution
Rigorous derivation showing that the compressible Euler equations in Lagrangian coordinates are exactly a nonlinear wave equation. Uses Riemann invariants to characterise left/right propagating simple waves and explains the nonlinear interaction geometry (diamond region) where speeds change because the sound speed depends on the solution.

## Key concepts
- Compressible Euler equations (Eulerian form)
- Lagrangian coordinates, material derivative
- p-system: v_t − u_x = 0, u_t + p(v)_x = 0 (v = 1/ρ)
- Nonlinear wave equation: w_tt − c²(v)w_xx = 0
- Riemann invariants r = u + h(v), s = u − h(v)
- Characteristic curves dx/dt = ±c(v)
- Simple waves (pure 1-wave, pure 2-wave)
- Isothermal equation of state p = σ²/v; isentropic p = σ²/v^γ
- Shock wave formation
- CFL (Courant–Friedrichs–Lewy) stability condition

## Methods / results / takeaways
In Lagrangian coordinates, the compressible Euler equations become the p-system, equivalent to a nonlinear wave equation with sound speed c(v) = sqrt(−p′(v)). The Riemann invariant r = u + h(v) (where h′ = c) is constant along backward characteristics dx/dt = −c(v); s = u − h(v) is constant along forward characteristics. A pure right-going wave has r = const everywhere, so characteristics are straight lines in (x,t) and the wave propagates without distortion. When two simple waves collide, characteristics bend (speed changes) in a diamond-shaped interaction region; after separation both waves are altered. No explicit solution formula exists for the nonlinear case (unlike d'Alembert's formula for linear waves). The CFL condition requires the numerical time step Δt ≤ Δx/c̄ to capture this physics correctly.
