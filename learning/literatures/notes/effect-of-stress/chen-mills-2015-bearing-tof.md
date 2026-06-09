# Direct Load Monitoring of Rolling Bearing Contacts Using Ultrasonic Time of Flight

- **Source:** Direct load monitoring rolling bearings
- **Drive link:** https://drive.google.com/file/d/1gR5HdQb5OrqKswGTwaodyrTlM_oUJKi1/view
- **Type:** paper
- **Author/Year:** W. Chen, R. Mills & R. S. Dwyer-Joyce, 2015
- **Coverage:** partial (large file, truncated extraction)

## Overview
Presents a method for directly measuring the load transmitted from a rolling element to a bearing raceway by monitoring the time of flight (ToF) of a reflected ultrasonic pulse from a piezoelectric sensor bonded to the raceway bore. The ToF change combines three contributions: geometric deflection of the raceway, acoustoelastic velocity change, and an apparent phase-shift effect at the contact interface. The Hilbert transform is used to separate the phase-shift component.

## Unique contribution
First demonstration of simultaneous accounting for all three ToF contributions (deflection + acoustoelastic + contact phase shift) in rolling bearing load monitoring. Introduces the Hilbert transform approach to remove contact-dependent phase shifts, which had been a major source of error in prior work. Demonstrates on both a model line contact and a real cylindrical roller bearing from a wind turbine gearbox.

## Key concepts
- Rolling bearing contact monitoring
- Ultrasonic time of flight (ToF)
- Acoustoelastic effect
- Acoustoelastic constant L_zz
- Contact interface stiffness / phase shift
- Hilbert transform (phase correction)
- Hertzian contact / elastic contact model
- Wind turbine bearing load monitoring
- Piezoelectric sensor (permanently bonded)

## Methods / results / takeaways
- Three contributions to ΔToF:
  1. Geometric: Δt_δ = −2δ/c₀ (raceway thickness decreases by δ under load)
  2. Acoustoelastic: Δt_c = −2L_zz·ε̄_z·d₀/c₀ (wave speed increases in compressed raceway)
  3. Phase shift: Δt_φ depends on contact stiffness K; removed using Hilbert transform on the reflection
- Acoustoelastic constant for bearing steel: L_zz = −2.24 (measured experimentally in Appendix A)
  - Relation: dc_P/c₀ = L_zz·dε_z, where ε_z is strain in propagation direction
- Hertz contact model used to relate measured deflection δ to contact load P via: δ = (load)^(2/3) × contact compliance
- Model line contact experiment: good agreement between ultrasonic ToF-derived load and reference load cell (within ~5%)
- Wind turbine bearing (cylindrical roller, planet gear epicyclic): ToF measured for different applied radial loads; load map matches expected load distribution across rollers
- Hilbert transform key innovation: applied to echo waveform to determine instantaneous phase; phase change at contact corrected before ToF extraction
- Sensing geometry: single piezoelectric element bonded to bore surface; operates in pulse-echo; can monitor rotating bearing
- Limitation: requires permanent bonding of sensor; not easily retrofittable; sensor must survive bearing operating environment
