# Effect of Design Modifications of Intra-Bore Region on Engine Block Bore Distortion

- **Source:** SAE Technical Paper 2010-01-1524 (May 2010), DOI: 10.4271/2010-01-1524
- **Drive link:** https://drive.google.com/file/d/1IiQClv19rC0Bd0sB4jJ90zzUxxqw53YX/view
- **Type:** paper
- **Author/Year:** Manav, D.; Erpolat, S.; Ozdemir, K. (Ford Otosan Gebze Engineering) / 2010 (SAE 2010-01-1524)
- **Coverage:** full

## Overview
Conjugate CFD (Star CCM+) + ABAQUS FEA study comparing baseline (open water jacket intrabore) vs drilled-intrabore design for a close-deck diesel V-engine (Compacted Graphite Iron block, aluminium AS7GU head). Intrabore drilling eliminates water jacket sand core (reducing manufacturing cost) but creates stagnant coolant areas → up to 60°C higher metal temperature at top deck in drilled design. Cold-assembly condition: drilled design improves bore distortion (more material between bores → higher stiffness). Hot-operating condition: drilled design worsens 2nd and 3rd order Fourier coefficients due to hot spots from inferior cooling. 4th order slightly better with drilling. Concludes that hot operating condition is the critical concern, and fired Incometer validation is needed for future work.

## Unique contribution
First study to systematically compare intrabore water jacket drilling (manufacturing cost reduction approach) against baseline open water jacket for both cold-assembly and hot-operating bore distortion; demonstrates conflict between assembly-condition improvement (more material = stiffer) and hot-condition deterioration (worse cooling = higher thermal distortion); identifies stagnant coolant regions as root cause.

## Key concepts
- Close-deck V-engine; Compacted Graphite Iron (CGI) block; AS7GU aluminium head; enlarged bore for higher displacement
- Intrabore drilling: remove sand core, drill passage through metal → manufacturing cost reduction; but coolant flow compromised
- Star CCM+: polyhedral elements; conjugate heat transfer (CHT); Rohsenow nucleate boiling model (exponent n=0.33, m=0.7)
- GT-POWER: 1D correlation for thermal boundary conditions; thermocouples at exhaust valve bridges, 3.5 mm above deck for validation
- ABAQUS: BDPP (Bore Distortion Post Processor) in-house FNA tool for Fourier analysis (0–4th order Fourier coefficients)
- MLS gasket: non-linear closure curves from manufacturer as ABAQUS gasket element input (special gasket elements)
- Loading sequence: valve seat/guide interference → head bolt clamping → thermal expansion (max power CFD) → peak firing pressure
- Cold assembly result: drilled design reduces roundness and Fourier coefficients for inner cylinder (stiffness effect); similar for outer
- Hot result: drilled design increases roundness, 2nd and 3rd Fourier for most cylinders (hot spots at drill-free zone); 4th order slightly better
- Temperature increase in drilled design: max 60°C at top deck due to stagnant coolant between drills
- Bore distortion limits: no clear industry standard for hot condition limits; PAT Incometer / Enchometer recommended for future validation
- Ford Otosan BDPP tool (in-house) handles Fourier decomposition and bore distortion post-processing

## Methods / results / takeaways
- CHT correlation: 5°C average discrepancy vs thermocouple head deck data for baseline design.
- Velocity magnitude comparison: drilled design shows stagnant regions visible in intrabore section vs good flow in baseline.
- Assembly condition inner cylinder: decreased roundness and Fourier coefficients in drilled design; outer cylinder essentially same as baseline.
- Hot condition: significant increase in roundness and 2nd/3rd order amplitudes in drilled design for inner cylinders; outer cylinder less affected.
- 4th order (bolt-induced cloverleaf): slightly lower with drilling (structural effect dominates thermally at this order).
- Key message: intrabore drilling improves cold stiffness but compromises thermal management → net hot bore distortion worsens; trade-off not acceptable without thermal redesign.
- Bore-liner relevance: demonstrates water jacket geometry is a critical variable for bore distortion control; conjugate CFD-FEA coupling is essential for hot bore analysis; manufacturing cost reduction must be evaluated against hot bore distortion consequences.
