# Cylinder Liner Bore Distortion Estimation During Assembly of Diesel Engine with FEA

- **Source:** International Journal on Mechanical Engineering and Robotics (IJMER), Vol. 1, Issue 2 (2013), pp. 66–73, ISSN 2321-5747
- **Drive link:** https://drive.google.com/file/d/1-jXFAtUvrZ5qEzOnABWOfy063S9h1kSr/view
- **Type:** paper
- **Author/Year:** Mirajkar, Pratik B.; Kanase, Kedar A.; Chhapkhane, Narendra K. (R.I.T. Sakharale / Kirloskar Oil Engines) / 2013 (IJMER 1(2))
- **Coverage:** full

## Overview
Student/industry FEA study of cylinder liner bore distortion under static bolt assembly conditions using ANSYS, for an air-cooled diesel engine. Model includes crankcase, gasket, and liner with flex-flex contacts and bolt pretension calculated from standard torque formula (K=0.2233, bolt M16, T=255 Nm, F0=71,445 N/bolt, 6 bolts total=428,672 N). Results compared against company experimental data: FEA underpredicts maximum distortion by 15–20% for upper bore (first 5 planes match well; lower bore deviates). Fourier decomposition confirms 2nd and 4th order dominance under static conditions. Provides introductory review of bore distortion causes, FEA theory, mesh quality parameters.

## Unique contribution
Practical academic study combining industry experimental data with ANSYS for a specific diesel engine; provides complete bolt pretension calculation procedure (nut torque → pretension force); confirms 15–20% FEA underestimation of peak distortion experimentally (upper bore better predicted than lower bore); accessible Fourier order review with physical interpretation.

## Key concepts
- Air-cooled diesel engine; M16 bolts, T=255 Nm tightening torque; K=0.2233 (no lubrication); F0=71,445 N/bolt; 6 bolts → 428,672 N total
- ANSYS non-linear: material nonlinearity, geometric nonlinearity, contact nonlinearity; flex-flex contacts (metal-metal)
- Mesh quality: warpage, max/min angle, aspect ratio, Jacobian requirements
- Fourier orders: 0 = diameter change; 1 = eccentricity; 2 = oval; 3 = 3-lobe; 4 = cloverleaf
- Bore distortion causes: manufacturing tolerances; bolt loads (4th order from heads, 2nd from bearing carriers, 3rd from asymmetric supports); thermal (largest magnitude); gas pressure (significant only in highly-rated diesel with thin wet liners)
- Through-bolt vs conventional bolting: through-bolts set head + bearing caps under compression only; reduced tensile stress; more complex assembly
- Experimental validation: company-provided bore measurements at 10 planes; upper 5 planes match well; lower planes deviate; maximum 15–20% error
- Referenced: Paul Gibbs (BAT), Bardzimashvili et al. (RINGPACK), Bird & Gartside, Maassen et al. 2001-01-0569

## Methods / results / takeaways
- Model: crankcase + gasket + liner; 4 flex-flex contact pairs; bolt pretension load applied at pretension surfaces.
- Results: overall deformation contour; Von Mises stress; convergence study.
- Comparison: green = perfect bore, red = experimental distorted bore, blue = FEA bore; good upper bore match; lower bore over-predicted by experiment (FEA underpredicts 15–20% for max distortion).
- Fourier decomposition: 2nd and 4th orders dominate under static conditions, consistent with literature.
- Key limitation: static bolt-clamping only; no thermal or firing loads; explains much of the deviation from experimental operating conditions.
- Bore-liner relevance: entry-level study confirming Fourier order dominance; provides bolt pretension formula framework; 15–20% FEA underestimate flags mesh refinement and boundary condition accuracy as areas for improvement.
