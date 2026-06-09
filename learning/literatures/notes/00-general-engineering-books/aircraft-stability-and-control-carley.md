# Aircraft Stability and Control

- **Source:** A I R C R A F T   S T A B I L I T Y   A N D   C O N T R O L.pdf
- **Drive link:** https://drive.google.com/file/d/1S75CrKmJutZeV2MpXGzBesjn7Wj9RZ3y/view
- **Type:** notes
- **Author/Year:** Michael Carley (University of Bath), 2020 (notes produced 8 January 2020)
- **Coverage:** partial (large file, truncated extraction)

## Overview
A set of lecture notes for a third-year aerospace engineering unit at the University of Bath, covering aircraft stability and control from first principles. Explicitly described as "not a textbook" but as a conceptual guide meant to be used alongside lectures and other materials. The notes cover longitudinal and lateral static stability, tailplane and control surface design, stick forces, manoeuvre margins, high-speed compressibility effects, and dynamic stability including normal modes and the phugoid.

## Unique contribution
The notes are distinguished by their tightly integrated qualitative-to-quantitative pedagogy: physical intuition (what the pilot feels, what the aircraft "wants" to do) is developed alongside formal linearised aerodynamic theory. The treatment of hinge moments and tab deflection as the link between aerodynamic forces and pilot stick forces is particularly detailed. The phugoid analysis (conservation-of-energy flight path derivation from Milne-Thomson) and the systematic 6-DOF perturbation notation for dynamic stability are presented with more conceptual motivation than many standard texts.

## Key concepts
- Longitudinal static stability
- Static margin (stick-fixed and stick-free)
- Neutral point and aerodynamic centre
- Centre of gravity and trim
- Lift curve slope (CL = aα)
- Tailplane design and sizing
- Elevator, rudder, aileron control surfaces
- Hinge moment and hinge moment coefficient (CH)
- Aerodynamic balance
- Stick force and stick force gradient
- Tab deflection (β)
- Manoeuvre margin
- Compressibility effects and Mach tuck
- Mach trim
- Dynamic stability (longitudinal and lateral)
- Phugoid mode
- Short-period oscillation
- Normal modes of aircraft
- 6-degree-of-freedom perturbation equations
- Moment of inertia axes (A, B, C)
- Stability derivatives
- Flight testing and handling qualities

## Methods / results / takeaways
**Equilibrium and stability**: An aircraft in trim has zero net force and moment. Static stability requires ∂Mcg/∂α < 0 (nose-down restoring moment when pitched nose-up). The neutral point is where dM/dα = 0; the static margin Kn is the non-dimensional distance between the centre of gravity and the neutral point.

**Aerodynamic formulation**: All quantities are non-dimensionalised on ρ, V, wing area S, and mean aerodynamic chord c. Tailplane lift coefficient: CLT = a1·αT + a2·η + a3·β, where η is elevator deflection and β is tab angle. Hinge moment: CH = b0 + b1·αT + b2·η + b3·β. The hinge moment is the aerodynamic mechanism behind stick force.

**Tabs**: Tabs have little effect on overall tailplane lift but produce large hinge moment changes, making them useful for reducing or trimming stick forces without significantly altering trim.

**Dynamic stability**: The pitch equation of motion reduces to a simple harmonic oscillator when the static margin is positive (frequency proportional to √Kn). A negative static margin gives exponential divergence. The phugoid (energy-exchange oscillation) is derived from conservation of kinetic and potential energy, giving a family of flight paths parameterised by integration constant C.

**High-speed effects**: As Mach number increases toward transonic, the aerodynamic centre shifts rearward (toward c/2), increasing static margin but also causing Mach tuck (nose-down trim change). A Mach sensor feeding a trim actuator is used to correct the stick force gradient.

**6-DOF dynamics**: Perturbation quantities (u, v, w for translational; p, q, r for rotational) are expanded as linearised functions of stability derivatives (∂M/∂u, ∂M/∂q, etc.) referred to aircraft-fixed axes centred at the CG. Moments of inertia A (roll), B (pitch), C (yaw) appear in the dynamic equations.
