# A Simplified Piston Secondary Motion Model Considering the Dynamic and Static Deformation of Piston Skirt and Cylinder Bore in Internal Combustion Engines

- **Source:** SAE Technical Paper 2008-01-1612 (2008 SAE International Powertrains, Fuels and Lubricants Congress, Shanghai)
- **Drive link:** https://drive.google.com/file/d/1Q5Pwd32bLv_2bxA-H2MzhkwpI97IA2Im/view
- **Type:** paper
- **Author/Year:** McClure, Fiona; Tian, Tian (MIT Sloan Automotive Laboratory) / 2008 (SAE 2008-01-1612)
- **Coverage:** full

## Overview
Development and application of a dry (non-lubricated) piston secondary dynamics model for a heavy-duty diesel engine (131 mm bore, 0.13 mm diametral clearance). Model includes detailed hot piston and cylinder bore geometries (including bore distortion up to 12th order), piston thermal deformation, piston elasticity (compliance matrix from FEA), combustion pressure and axial inertia deformations, contact pressure model, and friction. Neglects hydrodynamic lubrication. Planar 2D rigid body dynamics for piston, wrist-pin and connecting-rod solved by Newton's method. Results for range of operating conditions; parametric studies of piston geometry, bore geometry, piston elasticity effects. Validated against prior lubricated model at limited conditions.

## Unique contribution
Demonstrates that dry model can predict maximum lateral piston motion and acceleration as function of crank angle, and assess effect of system parameters (crankshaft offset, pin offset, wrist-pin friction, bore shape) without lubrication model; explicitly models bore distortion up to 12th Fourier order as input to piston dynamics; reveals that piston elasticity (up to 50 µm deformation) allows lateral motion in interference-fit zones of lower bore.

## Key concepts
- Heavy-duty diesel engine: 131 mm bore; 0.13 mm cold diametral clearance; piston mass 2.5 kg; connecting rod 260 mm; crank radius 75 mm
- Dry model: contact friction coefficient fCB = 0.1; smoothed friction model; wrist-pin friction fWP variable
- Piston geometry: cold shape (nominal radius + thrust-axis profile + ovality vs axial position); hot thermal deformation from FEA; pressure + inertia induced deformation from compliance matrix
- Bore geometry: cold shape via up to 12th-order Fourier bore distortion (magnitude + phase per order); thermal deformation as function of axial position only
- Compliance matrix: FEA-generated; 17×30 piston surface grid; diagonal shows lower/central skirt softer than upper skirt; deformations up to 50 µm from bore contact
- Newton's method convergence: 3 unknowns (piston lateral, tilt, wrist-pin angle); analytical Jacobians; reduced domain (negative gap only) for 18× speed improvement
- Results: peak piston deformation ~15 µm from combustion pressure + inertia near TDC; contact deformation ~50 µm eliminates interference in lower bore
- Piston tilt: dry model oscillates due to absence of oil film damping; cannot predict accurately without lubrication model
- Key finding: piston tilt and friction are significantly affected by oil film thickness → dry model insufficient for tilt prediction; but lateral motion envelope well captured

## Methods / results / takeaways
- Planar 2D dynamics: position defined by lateral motion, tilt, wrist-pin angle; combustion pressure trace and piston–bore interface provide forces/moments.
- Operating range: cold start to high load; increased thermal deformation reduces clearances in lower bore as load increases.
- Effect of piston geometry: increasing hot shape (higher load) reduces lateral motion; flatter profile reduces tilt fluctuations.
- Effect of bore geometry: increased thermal bore deformation increases upper bore lateral motion; lower bore constrained by interference fit.
- Effect of piston elasticity: enables motion in interference-fit zone; alters tilt from deformation; significant finding for interference-fit designs.
- Wrist-pin friction: affects moment balance near combustion TDC (fWP 0.005–0.1 range); minor effect on lateral force/motion.
- Bore friction: minimal effect on lateral motion; affects moment balance → small tilt change.
- Comparison to lubricated model: dry model predicts similar lateral motion maxima; tilt differs significantly (oil film hydrodynamic pressure, not friction, controls tilt).
- Bore-liner relevance: demonstrates importance of bore distortion (up to 12th order) as direct input to piston secondary dynamics; shows how thermal bore deformation changes clearance distribution and piston motion throughout operating range; compliance matrix approach for piston elasticity directly applicable to ring–bore interaction modeling.
