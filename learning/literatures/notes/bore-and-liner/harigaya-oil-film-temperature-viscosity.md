# Prediction of Temperature, Viscosity and Thickness in Oil Film Between Ring and Liner

- **Source:** SAE 2000-01-1790 (SAE Technical Paper 2000-01-1790)
- **Drive link:** https://drive.google.com/file/d/1V6JeAAiHeehpomag6gi56VQAHhpubKXw/view
- **Type:** paper
- **Author/Year:** Harigaya, Akagi, Suzuki / 2000 (SAE 2000-01-1790; Utsunomiya University)
- **Coverage:** full

## Overview
Analyses oil film temperature, viscosity and thickness between the piston ring and cylinder liner using an unsteady-state 2D thermohydrodynamic (THD) model. Couples the Reynolds equation with an unsteady 2D energy equation (including viscous dissipation) and Vogel temperature-viscosity relation. Compares results against quasi-steady-state 2D analysis and examines effects of engine speed, combustion load, and oil viscosity grade.

## Unique contribution
First application of unsteady-state 2D energy equation (rather than 1D or quasi-steady 2D) to ring-liner oil film temperature prediction. Shows that near TDC/BDC the unsteady analysis predicts temperatures and film thicknesses that differ significantly from quasi-steady results, due to thermal lag (phase shift) effects.

## Key concepts
- Thermohydrodynamic (THD) lubrication; ring-liner oil film
- Unsteady 2D energy equation with viscous dissipation
- Vogel temperature-viscosity relation
- Oil film temperature phase lag near TDC/BDC
- Viscous dissipation vs convection heat transfer regimes
- Effect of engine speed on oil film temperature and viscosity
- Effect of combustion pressure on film thickness
- Oil viscosity grade effects (SAE 10W to SAE 50)

## Methods / results / takeaways
- Model: Reynolds equation for pressure; 2D unsteady energy equation with viscous dissipation; SIMPLE method; 50×40 grid (ring direction × film thickness); Vogel viscosity-temperature equation.
- Unsteady vs quasi-steady: near TDC (−50 to +5°) unsteady Tm is higher; from +5 to +50° unsteady Tm is lower (phase lag). Minimum Tm of unsteady analysis stays above wall temperature.
- Effect of engine speed: Tm increases with speed (more viscous dissipation); viscosity decreases with speed; oil film thickness increases with speed (both unsteady and quasi-steady agree on trend).
- Effect of load (combustion pressure): Tm rises with load during compression/expansion; film thickness decreases with increasing pressure.
- Effect of oil viscosity grade: Tm affected mainly by liner temperature; higher SAE number → thicker film approximately ∝ viscosity^0.5; viscous dissipation dominates when film is thin (10–50° CA); convection dominates when film is thick (70–170° CA).
- Practical implication: using constant viscosity or 1D energy equation overestimates/underestimates ring-liner conditions, especially near dead centres where unsteady effects matter most.
