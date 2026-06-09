# Analytical and Empirical Methods for the Optimization of Cylinder Liner Bore Distortion

- **Source:** SAE Technical Paper 2001-01-0569 (2001 SAE World Congress), DOI: 10.4271/2001-01-0569
- **Drive link:** https://drive.google.com/file/d/1t7kPR6sSlf9243tKcsEWn257f665qEQS/view
- **Type:** paper
- **Author/Year:** Maassen, Friedrich; Koch, Frank; Schwaderlapp, Markus; Ortjohann, Thomas; Dohmen, Jörg (FEV Motorentechnik / RWTH Aachen) / 2001 (SAE 2001-01-0569)
- **Coverage:** full

## Overview
Comprehensive FEV/RWTH Aachen study establishing a combined analytical FEA + in-engine measurement methodology for cylinder bore distortion analysis and optimisation, applied to a 4-cylinder passenger car gasoline engine. In-engine fired measurement uses an Invar piston equipped with 8 eddy current sensors at 45° increments; a linkage cable-routing system passes signals to external instrumentation. Fourier harmonic analysis (orders 0–8) applied to both FEA predictions and measurements. Parametric study examines: block material (magnesium, aluminium, cast iron), gasket type (composite vs MLS), bolt engagement depth, liner wall thickness. GOETZE ring conformability criterion applied to assess whether distortions are ring-conformable. 3D dynamic piston ring FE model (5000 nodes, contact pressure and gaping outputs) described as future work direction.

## Unique contribution
First comprehensive publication combining in-engine fired measurement via instrumented Invar piston (8 sensors at 45°, cable linkage system) with systematic parametric FEA to benchmark design levers for bore distortion; provides the GOETZE conformability formula in full with material-specific application; establishes quantitative ranking of design parameters (material > gasket type > bolt depth > liner thickness) for 4th-order distortion control; includes a 3D ring FE dynamic contact model as emerging tool.

## Key concepts
- 4-cylinder gasoline passenger car engine; in-engine fired bore measurement at multiple load conditions
- Invar piston (low thermal expansion alloy): 8 eddy current displacement sensors at 45° intervals around bore wall; gap measured as piston traverses stroke
- Linkage cable-routing system: flexible links pass sensor cables from rotating/reciprocating piston to stationary external instrumentation
- Fourier harmonic decomposition: orders 0–8; order 0 = average diameter; 2 = oval (thermal); 4 = cloverleaf (bolt-clamping); 6 = six-lobe (bearing caps / 6-bolt engines)
- GOETZE conformability formula: Aω = 1.52 · Q · r³ / [E · h · t³ · (ω² − 1)²]; where Q = ring tangential load, r = bore radius, E = elastic modulus, h = ring height, t = ring radial wall thickness, ω = harmonic order number; Aω is the maximum conformable amplitude for order ω
- Block material comparison: magnesium → largest 4th-order distortion; aluminium → intermediate; cast iron → smallest; higher modulus reduces distortion amplitude
- Gasket comparison: MLS (multi-layer steel) gasket → lower bore distortion than composite gasket; MLS better sealing force distribution
- Bolt engagement depth: deeper bolt thread engagement in block → reduced 4th-order distortion; structural stiffening effect
- Liner wall thickness: increasing liner wall thickness reduces bore distortion; diminishing returns above 40% wall thickness increase
- 3D piston ring FE model: 5000 nodes; dynamic contact pressure distribution; ring gap (non-sealing zones) prediction; under development at time of publication
- Measurement validation: FEA predictions compared against fired in-engine measurements via instrumented piston; good agreement for dominant harmonics

## Methods / results / takeaways
- Measurement setup: Invar piston instrumented with 8 sensors → fired engine test → raw displacement data → Fourier decomposition at multiple axial depths.
- FEA model: 3D structural mesh of block, head, gasket, liner, bolts; bolt pretension + thermal loading; FEA Fourier output compared to measurement.
- Material ranking (4th-order): Mg > Al > cast iron for distortion amplitude; use of cast iron liner insert in Al block reduces 4th-order but does not eliminate it.
- MLS gasket reduces bore distortion vs composite gasket: more uniform pressure distribution under bolt heads → less 4th-order excitation.
- Bolt engagement depth sensitivity: significant reduction in 4th-order with deeper engagement; design guidance: maximise bolt-to-bore distance and engagement length.
- Liner wall thickness: thicker liner reduces distortion propagation from block to bore surface; up to 40% wall thickness increase recommended; beyond 40% diminishing returns.
- GOETZE bounds applied: parametric variants ranked against conformability limit; identifies which configurations violate ring conformability.
- Ring FE model (3D dynamic, 5000 nodes): computes contact pressure per azimuthal position and crank angle; gap opening at locations of non-conformance; intended as future complement to FEA bore shape predictions.
- Bore-liner relevance: definitive benchmark study for bore distortion optimisation parameters; GOETZE formula reference with full parameter definition; establishes MLS gasket superiority for bore distortion control; material, gasket, bolt geometry, and liner thickness are ranked design levers; sets up fired-measurement methodology applicable to validation of any bore distortion FEA workflow.
