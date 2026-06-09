# The Effect of Cylinder Bore Distortion on Lube Oil Consumption and Blow-By

- **Source:** Journal of Tribology (ASME), Vol. 136 (January 2014), pp. 011103-1–011103-9, DOI: 10.1115/1.4025208
- **Drive link:** https://drive.google.com/file/d/1CfuyR-L-eNg6KzpP7l36jiLXQGsQbrC_/view
- **Type:** paper
- **Author/Year:** Kagnici, Fatih; Akalin, Ozgen (Istanbul Technical University) / 2014 (J Tribol 136(1))
- **Coverage:** full

## Overview
ABAQUS FEA bore distortion + AVL EXCITE PR ring-pack/oil-consumption simulation study for a turbocharged diesel engine (nominal bore radius 43 mm). FEA computes hot- and cold-assembly distorted bore shapes decomposed into Fourier orders 0–4 using MATLAB. Seven separate EXCITE PR oil-consumption runs with different liner profiles (straight, fully distorted, orders 0–4 individually). Hot assembly shows maximum distortion 350 µm; cold assembly 20 µm. Order 0 is worst for oil throw-off, oil-blow, and blow-by. Higher-order bores (2–4) reduce throw-off relative to order 0. Oil evaporation dominates total oil consumption but is insensitive to bore order; throw-off is the order-sensitive mechanism.

## Unique contribution
First study to isolate the effect of individual Fourier distortion orders (0–4) on each oil consumption mechanism (evaporation, blow-through end-gap, throw-off, scraping) separately using AVL EXCITE PR, revealing order 0 as the critical order for oil blow and blow-by; demonstrates that straight liner gives higher throw-off than distorted liner due to zero deviation from ring section.

## Key concepts
- ABAQUS FEA: complete 4-cylinder engine assembly including cam carrier, injectors, injector clamps; bolt pretension via ABAQUS pretension commands; thermal mapping as displacements; peak firing pressure load
- Hot assembly distortion: order 0 and order 1 dominant (order of magnitude larger than orders 2–4); order 4 stronger in cold assembly (bolt-clamping, no thermal)
- Cold assembly max distortion: 20 µm; hot assembly: 350 µm (thermal >> mechanical)
- Piston stiffness: ABAQUS simplified model (concentrated load); stiffness matrix used in EXCITE PR; nonlinear behaviour approximated by 3rd-order polynomial
- AVL EXCITE PR: 4 oil consumption mechanisms — evaporation, oil-blow through ring end-gap, throw-off above top ring, piston crown scraping
- Key result: oil evaporation ≈ same for all bore orders; oil-blow negligible; throw-off order-sensitive (straight liner worst for throw-off; order 0 worst among distorted)
- Blow-by: order 0 highest (uniform bore expansion → ring end gap enlarges → gas/oil mixture leaks to crankcase)
- Ring conformability not included in EXCITE PR in this version → circumferential oil film uniformity not captured → evaporation insensitive to bore order
- 4000 rpm full load; Ricardo WAVE for combustion pressure and heat transfer BCs

## Methods / results / takeaways
- Hot assembly thermal loads dominate: orders 0 and 1 (radial expansion + eccentricity) are the largest; order 2 (oval) at lower bore due to adjacent-cylinder compression; order 3 at top due to thermal; order 4 from head bolts.
- Cold assembly: order 4 relatively more prominent near deck; orders 0 and 1 smaller than hot.
- Throw-off result: straight liner > order 0 > orders 2–4 (counter-intuitive — straight bore provides no deviation reservoir, so oil accumulates on top ring).
- Oil blow through end gap: order 0 worst (ring end gap enlarges with bore diameter increase in order 0).
- Blow-by: distorted bore > straight except order 0 > all others; order 0 ring end-gap largest → highest crankcase gas flow.
- Gap: ring conformability and circumferential film non-uniformity not considered; inclusion would significantly change evaporation results.
- Bore-liner relevance: quantifies contribution of each Fourier distortion order to distinct oil-loss mechanisms; reveals that order 0 (uniform thermal expansion) dominates functional consequences, while higher-order shape distortions primarily affect throw-off; motivates inclusion of ring conformability in future oil-consumption models.
