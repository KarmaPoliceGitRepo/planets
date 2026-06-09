# Cylinder Head High/Low Cycle Fatigue CAE Analysis

- **Source:** SAE Technical Paper 2012-01-1991
- **Drive link:** https://drive.google.com/file/d/1X4Zeusu3jFpTOeLL6Rd1JTwcILFF1pqF/view
- **Type:** paper
- **Author/Year:** Ghasemi / 2012 (SAE 2012-01-1991)
- **Coverage:** full

## Overview
Describes the CAE analysis workflow for predicting high-cycle fatigue (HCF) and low-cycle fatigue (LCF) life of an aluminium cylinder head. The process: CFD for thermal boundary conditions → FE thermal analysis → FE structural analysis (ABAQUS) → fatigue analysis (FEMFAT). Material: aluminium 319 with temperature-dependent properties. Validated against thermocouple measurements and physical LCF test.

## Unique contribution
Provides a complete multi-physics workflow (CFD → thermal FEA → structural FEA → fatigue) with experimental validation (45 thermocouples + physical LCF test showing predicted cracks matching actual failure locations). Demonstrates iterative redesign loop from initial failed design (LCF damage ~500 cycles) to final passing design (>1000 cycles).

## Key concepts
- High-cycle fatigue (HCF); S-N stress-life approach; Haigh diagram
- Low-cycle fatigue (LCF); strain-life (ε-N) approach; Coffin-Manson-Basquin
- Neuber correction; stress concentration factor; elastic-plastic conversion
- Smith-Watson-Topper mean stress correction
- ABAQUS FEA; FEMFAT fatigue software
- Aluminium 319 temperature-dependent material properties
- CFD water jacket thermal analysis; nucleate boiling above 125°C
- Cylinder head / cylinder block assembly; head bolts; valve seats
- LCF: cold soak at −30°C to operating temperature >230°C

## Methods / results / takeaways
- Step 1 CFD: coolant and combustion side boundary conditions; nucleate boiling accounted for above 125°C wall temperature.
- Step 2 FE thermal: ABAQUS; correlated with 45 thermocouples; <5% discrepancy.
- Step 3 FE structural: full assembly (head + block + gasket + bolts + valve seats); loading sequence: press-fit at room temperature → bolt preload → combustion pressure → thermal load → cold soak to −30°C.
- HCF analysis: linear FEA + Neuber correction for plasticity; Haigh diagram; FEMFAT; target safety factor 1.5; cylinder head passed after design iterations.
- LCF analysis: elastic-plastic ABAQUS; Ramberg-Osgood cyclic curve; Smith-Watson-Topper mean stress correction; target >1000 cycles (safety factor 1.0).
- Initial design failure: LCF damage at 500 cycles (safety factor 0.5) at combustion chamber and water jacket intersection.
- Redesign: water jacket geometry modified; final design achieved >1000 cycles; physical LCF test confirmed no cracks at previously failed locations.
- Bore distortion relevance: bore distortion analysis noted as downstream output of the same CFD+FEA temperature/structural workflow; same thermal and bolt loading that drives HCF/LCF also drives bore distortion.
