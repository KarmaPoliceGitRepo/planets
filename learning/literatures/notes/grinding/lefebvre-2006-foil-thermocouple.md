# Numerical Analysis of Grinding Temperature Measurement by the Foil/Workpiece Thermocouple Method

- **Source:** 2006 - Numerical analysis of grinding temperature measurement by the foil-workpiece thermocouple method - A lefebvre.pdf
- **Drive link:** https://drive.google.com/file/d/1MHC0kHkKzeBxJW1_2nq1wKg-ukM3ZfU7/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** A. Lefebvre, P. Vieville, P. Lipinski, C. Lescalier / 2006
- **Coverage:** full

## Overview
A 2006 journal paper (Int. J. Machine Tools & Manufacture 46:1716–1726) studying the accuracy of the foil/workpiece grindable thermocouple used to measure maximum temperature rise (MTR) in grinding. Using 2D finite-element simulations, the authors quantify how the mica insulating layers, junction thickness, workpiece velocity, and arc contact length combine to introduce systematic errors into the MTR reading, and show that the cooling-phase signal is immune to these errors.

## Unique contribution
Provides the first FEM-based quantitative error map for the grindable thermocouple at macroscopic scale, including the effect of both junction thickness and mica sheet thickness under varying workpiece velocity and arc contact length. The key practical finding is that measuring the energy partition ratio from the cooling phase (after wheel/foil separation) is inherently more reliable than using the MTR peak, because the cooling slope is unaffected by thermocouple asymmetries.

## Key concepts
- Grindable (foil/workpiece) thermocouple
- Maximum temperature rise (MTR) in grinding
- Thermal inertia / longitudinal time constant of thermocouple
- Energy partition ratio (heat split between wheel, workpiece, chips, coolant)
- Transparency error (systematic measurement error)
- Arc contact length
- Peclet number in grinding
- Finite element method (FEM) for heat transfer
- Thermal effusivity / thermal diffusivity
- Constantan foil; mica insulation layers

## Methods / results / takeaways
- Single-pole thermocouple: constantan foil (~20 µm thick, 0.38 mm wide) insulated by two mica sheets between split workpiece halves; junction formed by plastic deformation of workpiece during grinding.
- FEM model (MSC-Marc, 2D) with temperature-dependent properties for C45 steel and constantan; triangular moving heat source profile.
- Longitudinal time constant ranges from ~100–400 µs (5 µm mica) to ~150–900 µs (10 µm mica) depending on junction thickness (0–4 µm).
- Systematic MTR error can reach ~30% for poor junction contact and high workpiece velocity (≥300 mm/s) or long arc contact; it is on the order of 10% for good junction quality.
- Error sign depends on boundary condition: when heat flux is applied on the foil the measured temperature overshoots; when foil is adiabatic (no grits hitting it) the junction undershoots the true temperature.
- Cooling phase signal is perfectly transparent in all configurations — thus partition ratio estimates based on the cooling slope are more reliable than those based on the peak MTR.
- Practical implication: for high-speed cylindrical grinding (contact times < 1 ms) mica thickness should be reduced to ≤5 µm to maintain acceptable time constants.
