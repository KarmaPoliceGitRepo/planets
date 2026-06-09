# Ultrasonic Investigation of Contact between Solids under High Hydrostatic Pressure

- **Source:** Ultrasonic investigation of contact between solids under high hydrostatic pressure.pdf
- **Drive link:** https://drive.google.com/file/d/1T6nZx67cauJorIWNzKUOuVaak5A9iN0N/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** J. Krolikowski, J. Szczepek, and Z. Witczak (Polish Academy of Sciences) / 1989
- **Coverage:** full

## Overview
An Ultrasonics journal paper presenting a three-parameter acoustic model (stiffness K, viscous friction η, and reradiation damping β) for the reflection of ultrasonic waves from a contact interface, validated experimentally on hardened steel samples compressed hydrostatically to 1000 MPa at frequencies 10–90 MHz. The paper explains why the reflection coefficient exhibits a *maximum* at 50 MHz for a particular surface roughness, and shows that unit contact stiffness varies linearly with contact pressure.

## Unique contribution
Extends the Kendall-Tabor two-media spring model to a three-parameter model by adding a *reradiation damping* term (energy radiated by oscillating contact asperities, analogous to radiation damping in electrodynamics). This explains the experimentally observed non-monotonic frequency response of R and allows a more complete description of contact interface dynamics. Also demonstrates use of hydrostatic (rather than uniaxial) loading, enabling study of very high pressures without damaging brittle or soft specimens.

## Key concepts
- Three-parameter contact model: stiffness K, viscous friction η, reradiation damping β
- Reradiation damping (radiation stress of oscillating springs)
- Reflection coefficient modulus R (measured via echo amplitude ratio)
- Hydrostatic pressure loading up to 1000 MPa
- Unit contact stiffness K linear in contact pressure
- Frequency-dependent R with peak at intermediate frequency
- Vertical displacement of contacting surfaces (integrating K)
- Gusev contact model (cylindrical bar asperity model)

## Methods / results / takeaways
- **Model:** Newton's equation for weightless springs between two half-spaces; two dissipative stresses: (1) viscous friction (energy → heat) and (2) reradiation damping (energy radiated by accelerating springs, coefficient β proportional to ω²). K* = K + iω(η + βω²). Reflection modulus R(ω) follows from substituting into impedance matching equations.
- **Experimental:** Three sets of hardened bearing steel samples (62 HRC); hydrostatic loading in a special high-pressure vessel (up to 1 GPa) with elastic envelope preventing liquid penetration into contact. Contact pre-pressurized to 2000 MPa to eliminate plastic hysteresis. Frequencies: 10, 30, 50, 70, 90 MHz.
- **Results:** R decreases monotonically with p/E for each frequency; at fixed p, R exhibits a maximum at 50 MHz (matching the sample surface roughness). Fitting the model to R(f) data at each pressure yields K, η, β.
- **K vs. pressure:** K = K₀ + b·p with K₀ = 1.92×10¹⁰ N/m³ and b = 2.72×10¹¹ N/m³, correlation coefficient 0.99. Non-zero K at p = 0 implies pre-existing inter-asperity stiffness at zero load.
- **η behavior:** Rises slowly up to p/E ≈ 0.002, then increases sharply — interpreted as transition from elastic to elasto-plastic contact behavior at asperity tips.
- **β behavior:** Increases nearly linearly throughout, consistent with growing number of oscillating contacts (each radiating energy) as more asperities make contact.
- **Displacement law:** Integrating K(p) gives u ∝ (p/E)^0.334, consistent with Gusev's cylindrical-asperity model exponent (u ∝ (p/E)^(1/3)).
- **Air vs. vacuum:** Evacuating air from contact (0.1 kPa) produced no measurable change in R — confirming air plays no role in ultrasonic contact measurements at these scales.
