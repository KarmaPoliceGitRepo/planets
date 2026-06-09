# Lubrication of a Flexible Piston Skirt Conjunction Subjected to Thermo-Elastic Deformation: A Combined Numerical and Experimental Investigation

- **Source:** Proceedings of the IMechE Part J: Journal of Engineering Tribology 228(1) (2014), pp. 69–81
- **Drive link:** https://drive.google.com/file/d/1zY0qcR04Ast2T78R-gMJ-TUl3HY5RjVm/view
- **Type:** paper
- **Author/Year:** Littlefair, De La Cruz, Mills, Theodossiades, Rahnejat, Dwyer-Joyce, Howell-Smith / 2014 (Proc IMechE Part J 228(1), pp. 69–81; Loughborough University + University of Sheffield + Capricorn Automotive)
- **Coverage:** full

## Overview
Quasi-static tribological model of compliant piston skirt-liner contact incorporating global thermo-mechanical distortion of the piston skirt (four components: crown pressure, reaction forces, inertia, thermal expansion) via the compliance matrix approach. Reynolds equation solved coupled with elastic film shape. Validated against ultrasonic film thickness measurements on a Honda CRF 450R engine at 4250 rpm (23° ATDC). Companion paper to Littlefair et al. Tribol Lett 2014 (which extends this to fully transient dynamics).

## Unique contribution
Develops the compliance matrix methodology for semi-automatic prediction of piston skirt thermo-mechanical deflection that reduces solution time by 4 orders of magnitude, and provides the first published validation of piston skirt film thickness prediction against fired-engine ultrasonic measurements including thermo-elastic distortion of a structurally flexible (compliant race) piston.

## Key concepts
- Piston skirt thermo-mechanical distortion; compliance matrix method
- Four distortion components: crown pressure (δ_Cp), reaction forces (δ_Sl), inertia (δ_In), thermal (s_ij)
- Reynolds equation (2D quasi-static); mixed lubrication; Greenwood-Tripp asperity contact
- Compliance matrix: pre-computed 5D response array A(i,j,k,l,n); unit loads at each node
- Honda CRF 450R single-cylinder; AA2618 aluminium piston and liner; Ra liner 0.26 µm
- Nominal clearance 18 µm; interface temperature 110°C; Roelands viscosity; Dowson-Higginson density
- 10 MHz ultrasonic transducers on liner exterior (within water jacket); 5×1 mm² transducers
- Spring-layer acoustic model for film thickness from reflection coefficient R

## Methods / results / takeaways
- Compliance matrix: Nastran FEA half-piston model (~30,000 nodes, 10-noded tetrahedral); unit load applied at each node; PCG method replaced by 5D array lookup → 4 orders speedup (30–40 s → 3–4 ms per load case).
- Distortion contributions: skirt reaction forces dominate (up to 50 µm radial); crown pressure induces bending improving wedge; inertial contribution 2 orders smaller.
- Crown pressure: moves minimum film thickness toward crown, improving entraining wedge in combustion stroke.
- Validation: predicted centreline film thickness agrees quantitatively with ultrasonic measurements at 23° ATDC; shape and minimum film thickness well captured.
- Film thickness minima at ~7 mm circumferentially from centreline.
- Comparison with rigid-skirt: compliant skirt gives different pressure distribution and contact patch (no pressure spikes at relief radii); larger effective area.
- Plain (non-crosshatch) liner and piston surfaces used to satisfy Greenwood's Gaussian asperity assumption.
- Bore-liner relevance: demonstrates compliance matrix approach for realistic piston skirt distortion; directly applicable to bore distortion incorporation into skirt-liner lubrication models. Closely related companion to Tribol Lett 53(1) 2014 transient paper.
