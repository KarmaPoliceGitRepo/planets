# Use of Non Linear Analysis in Powertrain Design for Prediction of Cylinder Bore Distortion, Design Changes for Reduction along with Experimental Validation

- **Source:** SAE Technical Paper 2015-26-0202 (January 2015), DOI: 10.4271/2015-26-0202
- **Drive link:** https://drive.google.com/file/d/1182eTUhqKnLBZvOzeApPnyHNW4bwX-kk/view
- **Type:** paper
- **Author/Year:** Patwardhan, Mahesh; Paranjpe, Jagannath M.; Ramdasi, Sushil S.; Karanth, Nagesh V.; Marathe, Neelkanth V.; Bhat, Prasad (ARAI — Automotive Research Association of India) / 2015 (SAE 2015-26-0202)
- **Coverage:** full

## Overview
Non-linear FEA bore distortion prediction and experimental validation study for a high-power 3-cylinder diesel engine (1.5L, 75 kW, 50 kW/L, 200 bar combustion pressure, Euro V). Sequential analysis: bolt pretension → combustion pressure. Gasket non-linear behaviour extracted experimentally from load-deflection UTM testing and applied as ABAQUS input. Results validated against Enchometer test rig measurements (good agreement). Methodology applied to resolve blow-by issue (1.5% of air flow) on off-highway engine through structural modifications (deeper bolt counter-bore depth + larger coolant window), achieving significant blow-by reduction.

## Unique contribution
Industry application case at ARAI demonstrating the complete FEA methodology from CAD to validated bore distortion results to design change for blow-by improvement; includes experimental gasket characterisation (UTM load-deflection curve) as FEA input; shows real-world blow-by improvement achieved by structural modifications guided by bore distortion FEA.

## Key concepts
- Engine: 3-cylinder, 1.5L, 75 kW @ 4000 rpm, BMEP 20 bar, max combustion pressure 200 bar, Euro V diesel
- Non-linear FEA: contact between mating surfaces (small-sliding + friction + tie); bolt pretension with sequence; bedplate/oil sump modelled
- MLS gasket: experimentally characterised by UTM compression test; loading/unloading curve as ABAQUS input; bead and body regions separately meshed
- 2nd-order elements for liner (tetrahedral); matching mesh pattern at mating surfaces
- Loading: Step 1 = cylinder head bolt pretension; Step 2 = bearing cap bolt pretension; Step 3 = peak combustion pressure at cylinder head bottom
- Fourier order analysis to 4th order: 0 = diameter change; 1 = eccentricity; 2 = oval; 3 = 3-lobe; 4 = cloverleaf
- Enchometer test rig for physical measurement; measured axial bore deformation plots compared to FEA
- Bore modification: increasing head bolt counter-bore depth + widening coolant flow window in crankcase
- Blow-by reduction: 1.5% of air flow in base engine → improved after structural modification (significant reduction)
- Referenced conformability tools: Dunaevsky, Tomanik, GOETZE bounds; Bardzimashvili et al. RINGPACK

## Methods / results / takeaways
- Sequential analysis captures physical assembly: bolt tightening sequence considered; bearing cap bolts and head bolts are separate steps.
- Good agreement between FEA and Enchometer measurements of axial bore deformation plots for all three liners.
- Bore distortion order plots (0–4th) generated at multiple depths; out-of-roundness maximum calculated.
- Application: base engine with excessive blow-by diagnosed as excessive bore deformation from FEA; modifications to crankcase (bolt counter-bore depth + coolant window size) reduce bore distortion.
- Results Table: comparison of bore distortion magnitudes base vs modified for all three liners.
- Blow-by improvement: modified engine achieves significantly lower blow-by across 8-mode test cycle.
- Early design methodology: eliminates prototype iterations; prevents design changes post-prototype.
- Bore-liner relevance: demonstrates industrial bore distortion FEA methodology for high-power diesel engine; shows direct link between structural design features (bolt depth, coolant window) and blow-by performance; experimental gasket characterisation method applicable to liner/block interface analysis.
