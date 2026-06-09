# Novel Techniques for Ultrasonic Internal Temperature Distribution Measurement

- **Source:** 1986 - Novel techniques...Wadley.pdf
- **Drive link:** https://drive.google.com/file/d/1QMTMjLTrTyKPqLQX_IZCUN83rFk9hTU3/view
- **Type:** paper
- **Author/Year:** H. N. G. Wadley, S. J. Norton, F. Mauer, B. Droney / NBS (National Bureau of Standards, Gaithersburg) + Bethlehem Steel / 1986 — Phil. Trans. R. Soc. Lond. A 320, 341–361
- **Coverage:** full (deep read)

## Overview
A scanned 21-page Royal Society paper describing two novel ultrasonic methods for non-invasively reconstructing the internal 2D temperature distribution in hot steel billets and cylinders during processing (up to ~750°C). The first method is time-of-flight (TOF) tomography using multiple transmission paths through the workpiece. The second is dimensional resonance profiling (pulse-echo from a single face). Both methods exploit the strong temperature dependence of ultrasonic velocity in steel, and both incorporate a priori knowledge of the heat-conduction geometry to dramatically reduce the number of independent measurements required.

## Unique contribution
The central innovation is the use of heat-conduction a priori information (the form of the temperature field is constrained to solutions of the heat equation for the given geometry and boundary conditions) to reduce the tomographic inverse problem from one requiring thousands of ray paths to one solvable with as few as 3–5 paths for symmetric bodies. This makes real-time industrial implementation feasible. The paper also describes correction for high-frequency signal dispersion due to pulse propagation through thermally non-uniform material, and demonstrates both methods experimentally on AISI 304 austenitic steel and ferritic steel specimens.

## Key concepts
- Ultrasonic tomography / TOF tomography
- Internal temperature reconstruction
- Dimensional resonance profiling (pulse-echo single-ended)
- A priori heat-conduction constraint
- Path integrals of ultrasonic slowness
- Velocity–temperature (V–T) calibration for steel
- Thermal diffusivity; heat-conduction boundary conditions
- Bessel function expansion of temperature field
- Ferrite–austenite phase transformation anomaly in V(T)
- Thermal expansion correction to sample length
- Laser-generated ultrasound (Nd:YAG); wideband detection

## Methods / results / takeaways

### Reconstruction theory
The fundamental relation is: transit time tᵢ = ∫ dL/V(T(x)) along ray path Lᵢ. For a cylindrical body with radially symmetric temperature field T(r), the heat equation constrains T to a Bessel series: T(r,t) = T₀ + Σ aₙ J₀(λₙr)·exp(–λₙ²αt), where α is thermal diffusivity and the {aₙ} are N unknowns. Each TOF measurement gives one equation; N measurements determine N unknowns. For N = 3–5 the system is well-conditioned for typical steel billet geometries. The paper shows this formally and demonstrates the advantage over unconstrained tomography.

### V(T) calibration — AISI 304 austenitic steel
- Figures 7–8 show measured V_L vs temperature for AISI 304. Velocity decreases approximately linearly from ~5700 m/s at RT to ~5300 m/s at 750°C (slope ~–0.48 m/s/°C).
- A correction is required for the thermal expansion of the sample: the measured TOF reflects both V change and length change; the correction factor involves the linear expansion coefficient.
- Figure 8 shows the percentage difference between measured velocity and that of the Joule linear (reference) model, revealing a smooth systematic departure of ~0.5% that must be included in the inversion.

### Ferritic steel considerations
- The ferritic-to-austenitic phase transformation at ~910°C (A₃ temperature) produces a discontinuity in V(T); separate calibrations must be used below and above the transition.
- The Curie point (~770°C) also causes an anomaly visible in V(T) due to magnetostrictive contribution disappearing.

### TOF tomography experiment — cylinder
- Sample: 304 SS cylinder, diameter ~38 mm, 460 mm long, heated at one end.
- Source: Nd:YAG laser (pulsed, 10 mJ, 10 ns) generating longitudinal pulses; the laser spot was repositioned automatically along the cylinder axis for multiple path angles.
- Detector: wideband electromagnetic acoustic transducer (EMAT) at the far end.
- Figure 10 (TOF waveforms): photodiode trigger pulse and received wideband acoustic pulse are shown; TOF measured from first arrival.
- Reconstructed temperature profiles matched thermocouple measurements within a few degrees K across 0–400 K temperature variations (Figure 12: reconstructed vs thermocouple profiles along cylinder, agreement within ~10 K).

### TOF tomography — square billet
- Apparatus: horizontal laser path through a 304 SS square cross-section billet at a rotary table; multiple angular projections taken; Figure 13 shows the schematic.
- Temperature correction for 2D: five first-arrival time measurements were made, used to recover the five lowest Bessel-function coefficients of the 2D temperature field.
- Figures 14–15: reconstructed 2D temperature profiles for the square cross-section at ambient and at elevated temperature; the reconstructed contour maps agree with thermocouple measurements to within ±20 K (Figure 16 shows residuals).

### Dimensional resonance profiling (single-face, pulse-echo)
- Uses resonance of successive layer thicknesses from pulse-echo TOF differencing; iterative inversion from the back face forward.
- This is the 1D "layer peeling" (bisection) method (companion to Ihara-Takahashi work).
- Results: temperature profiles from single-face pulse-echo agree well with thermocouple data for the cylinder case; reproducibility ±10 K at temperatures up to 750°C (Figures 11, 17).

### High-frequency correction
- At high frequencies the pulse shape changes due to the velocity dispersion associated with propagation through a thermally graded medium. A correction algorithm based on accumulated phase is derived and applied to first-arrival time picking to avoid systematic bias.

### Practical implications
- The number of measurements needed is determined by the number of free parameters of the constrained temperature field, not by the spatial resolution of the reconstruction grid — a key practical advantage.
- Real-time feasibility: for N = 3–5 paths, the inversion can be performed at process timescales.
- Measurement uncertainty: the dominant error source is the accuracy of TOF picking; 1 ns timing error corresponds to ~1°C in a 40 cm sample.

## Figures

**Fig. 1** (p. 342): Schematic of a continuous casting line with positions along the process where ultrasonic temperature measurement would be applied (ladle, tundish, mold, billet support rolls, final solidification zone). Sets the industrial motivation.

**Fig. 2** (p. 343): Schematic diagram of a cylindrical continuous-cast billet and the cross-section for the casting of steel; shows the geometry for the reconstruction problem with labeled ray paths at different angles.

**Fig. 3** (p. 344): Ray paths for a cylindrical geometry; shows how a small number of fan-beam paths (5 shown) through a cylinder can be combined with the heat-flow a priori constraint to recover the internal temperature profile.

**Fig. 4** (p. 345): A "fan beams" reconstruction for an exponential temperature distribution; demonstrates that fewer than 5 measurements combined with the Bessel expansion recover the profile accurately.

**Fig. 6** (p. 347): Schematic of equations and derivation of the one-dimensional reconstruction model based on heat-conduction solutions.

**Fig. 7** (p. 351): Ultrasonic velocity V_L vs temperature (°C) for AISI 304 austenitic steel (measured 25–750°C). The velocity decreases from ~5700 to ~5300 m/s; the slope is nearly linear with minor nonlinearity at intermediate temperatures.

**Fig. 8** (p. 351): Difference (in percentage) between the measured velocity and that of a reference Joule linear model as a function of temperature — shows residuals from the linear fit, peaking ~0.5% at around 400°C.

**Fig. 9** (p. 352): Schematic diagram of the experimental arrangement for TOF measurement of the cylinder sample; shows the Nd:YAG laser source, wideband EMAT receiver, computer-controlled positioning stage, and digitiser chain.

**Fig. 10** (p. 352): Voltage-time waveforms for laser-generated ultrasound — upper trace shows the photodiode signal and longitudinal pulse arrival; lower trace shows an expanded view to indicate the precision of TOF measurement from leading-edge detection.

**Fig. 11** (p. 353): Schematic diagram of the differential displacement apparatus used to correct for changes in sample length due to thermal expansion; the linear variable differential transformer (LVDT) arrangement monitors dimensional change during measurements.

**Fig. 12** (p. 356): Reconstructed temperature profiles for the cylinder along the axial direction; one case without and one with temperature-drift correction, both compared to thermocouple data. Agreement to within ~10 K over a 0–400 K rise.

**Fig. 13** (p. 357): Schematic diagram of the square-section billet experiment apparatus; the laser was passed through the billet at multiple azimuthal angles on a rotary stage; the EMAT detector was on one flat face.

**Fig. 14** (p. 357): Reconstructed temperature profiles for the square cross-section at room temperature; shows good agreement between reconstructed and thermocouple values.

**Fig. 15–16** (pp. 358–359): Reconstructed 2D temperature distribution maps for the square billet at elevated temperature; comparison to thermocouple values shows residuals within ±20 K for most of the cross-section, with largest errors near the corners.

**Fig. 17** (p. 359): Reconstructed temperature profiles from the pulse-echo (dimensional resonance) single-face method; one with and one without temperature-drift correction; comparison to thermocouple data shows agreement within ~10 K for the cylindrical geometry.
