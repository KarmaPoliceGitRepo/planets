# Computer Simulation of Piston–Piston Ring–Cylinder Liner Coactions in Combustion Engines

- **Source:** Proceedings of the IMechE Part D: Journal of Automobile Engineering, Vol. 218 (2004), pp. 1491–1501
- **Drive link:** https://drive.google.com/file/d/1E2jY9fnIhBxX4CJ_RqtC_KoTplg4pN5I/view
- **Type:** paper
- **Author/Year:** Kazmierczak, Andrzej (Technical University of Łódź) / 2004 (Proc IMechE Part D 218)
- **Coverage:** full

## Overview
Coupled KIVA3 combustion simulation + MSC/NASTRAN 3D FEA study of piston–ring–liner thermal-structural interactions in a SW400 diesel engine (107 mm bore, 120.6 mm stroke, 16:1 CR, 1600 rpm). KIVA3 provides in-cylinder pressure and temperature histories as FEA boundary conditions; MSC/NASTRAN models the full assembly (69,090 elements, 19,370 nodes) including a TiN antiwear ceramic coating on the piston ring sealing surface (modelled as 2D plane elements ~3 µm thick). Ring sealing surface temperatures: 140–148°C with TiN coating vs 136–145°C without; within 3–5% of measured 133°C. Stresses in all components within material limits. Also introduces surface free energy (SFE) index for ring material selection (TiN SFE = 0.028 N/m).

## Unique contribution
First 3D FEA simulation to explicitly incorporate an antiwear ceramic (TiN PAPVD) coating layer on the piston ring sealing surface; demonstrates KIVA3-to-NASTRAN coupling for thermomechanical boundary conditions; introduces surface free energy index as tribological material selection metric for ring coatings.

## Key concepts
- SW400 diesel: 107 mm bore, 120.6 mm stroke, CR 16, 1600 rpm
- KIVA3 combustion: max pressure 8.06 MPa at 10° ATDC; max temperature 2752 K instantaneous, ~1910 K cycle-average
- MSC/NASTRAN FEA: 69,090 elements (solid hex + 2D shell for coating), 19,370 nodes; piston + ring + liner assembly
- TiN coating: ~3 µm thick PAPVD, modelled as 2D plane elements; Young's modulus, thermal conductivity, CTE applied
- Ring sealing surface temp: 140–148°C (TiN) vs 136–145°C (uncoated); measured reference 133°C (3–5% error)
- Stresses in piston, ring, liner all within material strength limits
- Surface free energy (SFE) index: adhesion tendency metric; TiN SFE = 0.028 N/m (anti-adhesive, low friction)
- Antiwear ceramic coatings rationale: reduce adhesive wear at TDC reversal where hydrodynamic film collapses

## Methods / results / takeaways
- KIVA3 run to generate pressure history (0–720° CA) and wall temperature distribution; exported as nodal BCs to NASTRAN.
- FEA mesh: structured hexahedral elements for piston, liner, and ring body; 2D plane/shell elements for TiN coating layer.
- Temperature distribution: TiN-coated ring sealing surface runs slightly hotter than uncoated (coating acts as thermal barrier); crown piston temp highest; liner coolant-side low.
- Mechanical stresses from combustion pressure peak: highest in ring groove contact zones; piston pin boss region critical; all within limits.
- Verification: sealing surface temperature prediction 3–5% vs thermocouple measurement; acceptable for coupled simulation approach.
- SFE index: lower SFE → lower adhesion tendency → preferred for ring-liner tribology; TiN (0.028 N/m) vs steel/cast iron (higher) supports TiN selection.
- Bore-liner relevance: establishes methodology for coupled thermomechanical analysis of ring–liner contact including coatings; TiN coating thermal effect (slight temperature elevation) informs ring running temperature and clearance specification; SFE index provides material selection framework for liner surface engineering.
