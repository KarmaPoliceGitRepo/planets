# Direct Load Monitoring of Rolling Bearing Contacts Using Ultrasonic Time of Flight

- **Source:** Direct load monitoring rolling bearings
- **Drive link:** https://drive.google.com/file/d/1gR5HdQb5OrqKswGTwaodyrTlM_oUJKi1/view
- **Type:** paper
- **Author/Year:** W. Chen, R. Mills & R. S. Dwyer-Joyce, 2015
- **Coverage:** full (deep read)

## Overview
A 21-page Proceedings of the Royal Society A paper presenting a method to directly measure the load transmitted from a rolling element to a bearing raceway using the time-of-flight (ToF) of ultrasound reflected from a piezoelectric sensor bonded to the raceway bore. The paper identifies and separates three independent contributions to the observed ToF change: (1) geometric deflection of the raceway, (2) acoustoelastic wave-speed change, and (3) an apparent ToF change from the contact-stiffness-dependent phase shift of the reflected signal. The Hilbert transform is used to compute the envelope of the reflected waveform, removing the phase-shift contribution. The technique is validated on a model line contact (steel roller on flat plate, up to 30 kN) and applied to a full NU2244 cylindrical roller bearing from a wind turbine epicyclic gearbox (up to 980 kN radial load).

## Unique contribution
First paper to simultaneously model, measure, and separate all three ToF contributions (deflection + acoustoelastic + contact phase shift) in rolling bearing load monitoring. Prior work had considered only one or two of the three, leading to systematic errors. The Hilbert transform envelope cross-correlation approach provides phase-insensitive ToF measurement that works regardless of oil film thickness or lubrication regime. Demonstrates on a real wind turbine gearbox bearing at realistic operational loads, with good agreement (within ~5%) between measured and applied load.

## Key concepts
- Rolling bearing contact monitoring; raceway load measurement
- Ultrasonic time of flight (ToF) pulse-echo method
- Three-component ToF model: deflection (Δt_δ), acoustoelastic (Δt_c), phase shift (Δt_φ)
- Acoustoelastic effect; acoustoelastic constant L_zz
- Contact interface stiffness K; interfacial phase shift φ_R
- Hilbert transform; signal envelope; envelope cross-correlation
- Hertzian contact mechanics; Dowson-Higginson EHL oil film model
- Piezoelectric PZT sensor (permanently bonded, modified strip, 10 MHz)
- Wind turbine gearbox bearing load monitoring
- ISO 281 bearing life; load sharing in rolling element bearings

## Methods / results / takeaways

### Three-component ToF model

**1. Geometric deflection (Δt_δ):**
- Under contact load P, raceway thickness reduces from d₀ to d_P = d₀ − δ
- ToF₀ = 2d₀/(c_zz)₀; ToF_P = 2d_P/(c_zz)_P
- Change: Δt_δ = 2δ/(c_zz)_P ≈ 2δ/(c_zz)₀ (Eq. 2.3)

**2. Acoustoelastic speed change (Δt_c):**
- Wave speed depends on strain via: Δ(c_zz)/c_z0 = L_zz · ε_z (Eq. 2.12)
- L_zz is the acoustoelastic constant; for bearing steel, L_zz = −2.24 (measured in Appendix A)
- Strain is not uniform through raceway thickness; average strain ε̄_z is integrated over depth using Hertz stress field
- ToF change: Δt_c = −2L_zz·δ/(c_zz)₀ (Eq. 2.20)

**3. Phase-shift apparent ToF change (Δt_φ):**
- Reflection from a contact interface acquires phase shift φ_R between 0 and π depending on contact stiffness K
- φ_R = arctan[4πfKz₁z₂² / (K²(z₁²−z₂²) + (2πfz₁z₂)²)] (Eq. 2.22, after Reddyhoff et al.)
- Phase shift appears as an apparent time shift Δt_φ = φ_R/(2πf) if zero-crossing timing is used
- Magnitude depends on oil film thickness (Dowson-Higginson equation) and surface stiffness

**Total change:** Δt_total = Δt_δ + Δt_c + Δt_φ (three contributions of comparable magnitude at typical bearing loads; Fig. 3 shows all three plotted vs. load)

**Removal of phase shift via Hilbert transform:**
- Analytic signal computed as f(t) + jH[f(t)] where H is Hilbert transform
- Envelope = |analytic signal| is phase-insensitive and shifts only with true wave path length changes
- Cross-correlation of envelopes of reference (unloaded) and loaded signals gives true ToF change (deflection + acoustoelastic only, phase shift excluded)

### Acoustoelastic constant measurement (Appendix A)
- 10 MHz longitudinal wave passed end-to-end through a bearing steel roller in axial compression (hydraulic loading frame, 250 kN capacity)
- Strain gauge on roller gives ε_z; ToF gives Δ(c_zz); L_zz = slope of Δ(c_zz)/(c_zz)₀ vs. ε_z
- Three load/unload cycles: L_zz = −2.12 (loading), −2.41 (unloading, first cycle due to slight plasticity), settling at −2.24 in subsequent cycles
- Best fit to all data: L_zz = −2.24; agrees with literature range −2.1 to −2.45 for steels
- Measurement uncertainty: ~3.7%–5.2% in load calculation for this range of L_zz variation

### Hertz contact model for deformation
- Deflection for cylindrical line contact: δ = f(P)^{2/3} × contact compliance (depends on roller radius, elastic modulus, Poisson's ratio)
- For NU2244 bearing (outer dia. 367 mm, inner dia. 259 mm, roller dia. 54 mm, 15 rollers): maximum roller load P = 4.08W/N where W = total radial load
- Combined formula linking Δt_total to P: Δt_t = 3.84×10⁻⁸ · P^{0.9}(1−L_zz) / [(c_zz)₀(l₀×1000)^{0.8}] (Eq. 5.3)

### Experimental results
**Model line contact (steel roller on flat plate, up to 30 kN):**
- Ultrasonic sensor (10 MHz PZT strip, 7 mm × 1 mm) bonded on upper plate; pulser-receiver at 10 kHz repetition rate; 30 V top-hat excitation of 100 ns duration; DAQ at 100 MS/s
- Linear actuator indexes plate to sweep contact under sensor; ToF vs. position recorded for each load
- Measured load vs. applied load: good agreement; slight over-prediction at low loads (roller crowning effect, actual contact shorter than roller)

**Wind turbine cylindrical roller bearing (NU2244, W = 380–980 kN):**
- Sensor permanently bonded inside inner raceway bore; slot machined in shaft for wire routing
- At 100 r.p.m., 27 reflections captured per roller passage; 15 rollers produce 15 ToF drops per revolution
- ToF change: 22.8 ns at 380 kN → 43.9 ns at 980 kN
- Slight periodic variation in ToF between rollers observed (attributed to possible cage misalignment)
- Measured vs. applied load: good agreement, slight under-prediction at high loads (transducer averaging effect over contact patch, where distributed deformation across elliptic contact gives lower average than peak center deformation)

### Key numbers
- L_zz = −2.24 for bearing steel (measured)
- Total ToF change: up to ~70 ns at highest bearing contact load (model contact)
- Sensor: 10 MHz PZT, 7 mm × 1 mm strip, bonded with strain gauge adhesive + epoxy cap
- Pulser: 30 V top-hat, 100 ns, 10 kHz repetition

## Figures

- **Fig. 1** (p. 4): Schematic of the pulse-echo arrangement and typical waveforms. (a) Unloaded raceway: transducer on top, raceway of thickness d₀, three successive echoes A/B/C shown with ToF₀ marked between them. (b) Loaded state: same geometry but thickness reduced to d_P by rolling element contact; echoes shift left (earlier arrival), ToF_P < ToF₀. Waveforms show that the rolling element reduces both path length and increases wave speed.

- **Fig. 2** (p. 7): Three panels showing how phase shift alters the apparent ToF in a zero-crossing measurement. (a) No phase shift: loaded signal simply shifted left by true Δt. (b) Small phase change: waveform slightly distorted, apparent shift Δt_f ≈ true Δt. (c) Phase change = π/2 (heavily loaded EHL contact): the waveform peak shifts significantly leftward beyond the true delay, creating a large Δt_f that does not reflect actual deflection. Illustrates why zero-crossing methods fail without phase correction.

- **Fig. 3** (p. 9): Predicted three-component ToF change vs. contact load (0–60 kN) for a rolling bearing contact. Three curves: Δt_δ (deflection, increases ~linearly), Δt_c (acoustoelastic, increases ~linearly), Δt_φ (phase shift, large at low load and relatively flat, dominated by oil film stiffness). At low load the phase shift dominates; at high load geometric and acoustoelastic terms dominate. Total reaches ~70 ns at maximum load. All three components are shown to be non-negligible.

- **Fig. 5** (p. 10): Photo showing (left) as-bought circular PZT disc (7.1 mm dia.) and (right) modified PZT strip (7 mm × 1 mm) after dicing, with wrap-around silver electrodes. Also shows modified sensor bonded inside inner race bore of bearing with thin epoxy cap.

- **Fig. 6** (p. 11): Measured time-domain waveforms from the model line contact in unloaded (thin line) and loaded (thick line) states. Multiple oscillation cycles visible; loaded signal shifted clearly left relative to reference. The shift is caused by both reduced wave path and phase shift at the contact.

- **Fig. 7** (p. 12): Simulation demonstrating the Hilbert transform approach. Reference signal and loaded signal (with π/2 phase shift) shown — they appear substantially different in the time domain. Their envelopes (from Hilbert transform) peak at the same location with no time offset. The envelope cross-correlation thus correctly captures only the path-length change, not the phase-induced shift.

- **Fig. 8** (p. 13): Measured reference and loaded waveforms (and their envelopes) from the actual line contact experiment. Time shift of ~few ns between envelope peaks is clearly visible and measurable via cross-correlation.

- **Fig. 9** (p. 14): Three panels showing measured first reflections when the line contact was at different positions relative to the sensor under 26.9 kN load: (a) contact far from sensor — signal resembles unloaded reference; (b) contact directly under sensor — signal amplitude reduced and phase modified; (c) contact past sensor — signal partially recovered. Illustrates the transient nature of the ToF signal as a roller passes.

- **Fig. 10** (p. 15): Measured contact load (y-axis) vs. applied contact load (x-axis) for the model line contact. Points scatter around the perfect-agreement line; slight over-prediction at low loads (<5 kN) and slight under-prediction at high loads (>20 kN) for reasons explained in text.

- **Fig. 11** (p. 15): Schematic of the wind turbine cylindrical roller bearing rig with transducer location indicated at the most-loaded zone. Shows double row spherical outer bearing housing, hydraulic loading mechanism, and inner raceway with sensor slot.

- **Fig. 12** (p. 16): Wind turbine bearing data: (a) one full revolution of streamed reflection data showing 15 amplitude drops corresponding to 15 rollers; (b) expanded section showing one roller passage — amplitude drops as roller approaches and rises when it leaves; (c) extracted single pulse comparison: reference (out of contact) vs. loaded (roller directly under sensor) — clear leftward time shift; (d) envelopes of the two signals — envelope shift is smaller than full signal shift, representing only deflection + acoustoelastic contribution.

- **Fig. 13** (p. 17): ToF change (ns) vs. time (one revolution, 1 s at 60 r.p.m.) for four bearing loads: 380, 580, 780, 980 kN. Each of the 15 rollers produces a peak; peak height increases with load (22.8 ns at 380 kN → 43.9 ns at 980 kN). Slight variation between rollers at each load is visible.

- **Fig. 14** (p. 18): Measured vs. applied contact load for wind turbine bearing at most loaded contact. Data points cluster near perfect-agreement line; slight over-prediction at low and under-prediction at high loads (same reasons as model contact).

- **Figs. 15 & 16** (p. 19, Appendix A): Fig. 15: schematic and photograph of acoustoelastic constant measurement rig — roller under axial load between two platens, with strain gauge and transducer. Fig. 16: measured relative speed change Δ(c_zz)/(c_zz)₀ vs. strain ε_z for three load/unload cycles; slope = L_zz = −2.24. Slight hysteresis in first cycle (slight plasticity) removed in subsequent cycles.
