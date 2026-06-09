# Experimental Analysis of the Behaviour of Aluminium Alloy EN 6082AW T6 at High Temperature

- **Source:** Experimental Analysis of the Behaviour of Aluminium Alloy EN 6082AW T6 at High Temperature - (2017) N Toric.pdf
- **Drive link:** https://drive.google.com/file/d/1ihf-D8JcfW0MVQwgEbnNCu5LxuJ_Qky7/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** Neno Toric et al. (Universities of Split, Rijeka, Sheffield), 2017 — published in *Metals*, MDPI
- **Coverage:** full

## Overview
This paper presents systematic experimental characterisation of the mechanical and creep properties of structural aluminium alloy EN 6082AW T6 (the strongest of the 6xxx series, 0.2% proof stress > 260 MPa at ambient) at elevated temperatures from ambient to 350 °C, with creep tests from 150–300 °C. Motivation is fire-resistance design: aluminium structures require passive fire protection because of high thermal conductivity and low melting point relative to steel.

## Unique contribution
Provides a new three-phase analytical creep model (primary + secondary + tertiary) of the form ε(σ,T,t) = c + a·t^b + e·t^f for alloy 6082-T6, covering stress levels from 0.15f to 0.50f and 200–300 °C — with coefficients tabulated for direct FEA implementation. Identifies the critical creep temperature interval as 200–300 °C. Validates well against Eurocode 9 reduction factors and Langhelle's prior data for the same alloy.

## Key concepts
- Aluminium alloy 6082-T6 (solution heat-treated + artificially aged)
- Proof strength (0.2% strain)
- Modulus of elasticity (temperature-dependent)
- Ramberg-Osgood stress-strain model
- Creep: primary, secondary, tertiary phases
- Stationary creep test
- Constant stress-rate test
- Eurocode 9 reduction factors
- Dynamic strain aging
- Mg₂Si precipitate structure
- Vickers hardness (68.1 → 39.9 at 300 °C)

## Methods / results / takeaways
- Test setup: 400 kN Zwick Roell machine, furnace to 900 °C, high-temperature extensometer; coupon geometry per ASTM E8M-11 (ambient) and E21-09 (elevated temperature).
- Constant stress-rate results: E decreases from 71 GPa (20 °C) to 24 GPa (350 °C); f₀.₂ decreases from 288 MPa to 19.5 MPa; ultimate strain shows non-monotonic behaviour (7.1% at 20°C, peak 12.3% at 150°C, drops to 1.7% at 300°C, rises again to 19.3% at 350°C) — attributed to dynamic strain aging.
- Creep behaviour: negligible below 150 °C; at 200 °C significant creep starts at 0.3f–0.5f; at 300 °C creep manifests even at very low stress levels (0.15f), making 300 °C effectively the upper limit for structural use.
- Tertiary creep phase occurs in T6 tempers but is often neglected in fire scenarios where total fire duration < 4 hours.
- Proposed analytical model agrees well with experimental results; good match with Langhelle (same alloy) for primary/secondary phases.
- Key gotcha: soaking time strongly affects strength in T6 temper — comparisons between studies require matching soaking periods (this study: 30 min).
