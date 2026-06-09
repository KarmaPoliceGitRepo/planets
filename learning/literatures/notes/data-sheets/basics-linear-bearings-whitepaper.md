# Basics of Linear Bearings: Round Rail vs. Profile Rail

- **Source:** Whitepaper_basics_of_linear_bearings.pdf
- **Drive link:** https://drive.google.com/file/d/1mnq4V0wjvGfDJ8rbR--k8g2U67gF4hv5/view?usp=drivesdk
- **Type:** datasheet
- **Author/Year:** NB Corporation (sponsored), Machine Design, April 2013
- **Coverage:** full

## Overview
A sponsored whitepaper comparing round-rail (ball bushing on shaft) and square/profile-rail linear guide systems across all major design considerations: load capacity, stiffness, accuracy, smoothness, mounting requirements, cost, and application suitability. Also covers ball splines as a related option.

## Unique contribution
Provides a structured decision framework for selecting between round and profile-rail linear guides, with specific numerical benchmarks: profile rail achieves 3–10 µm/m parallelism and 0.0002–0.001 in./10 ft accuracy; round rail achieves 0.01 in./10 ft and can span 12–24 shaft-diameter gaps. Explains why using more than two parallel rails creates a statically indeterminate system.

## Key concepts
- Round-rail (ball bushing) linear guides
- Profile-rail (square-rail) linear guides
- Ball splines (torque transfer with linear motion)
- Running parallelism
- Preload (3–13% of rated dynamic load)
- Dynamic load rating and travel life
- Stiffness (1–4 µm/kN at 13% preload for profile rail)
- Self-lubricating linear guides
- End-supported vs. continuously supported shafting
- Dual-shaft linear guides

## Methods / results / takeaways
- Profile rail is ~5× stiffer than round rail under load due to higher conformity and preload.
- Round rail tolerates flatness errors >150 µm/m; profile rail requires very flat surfaces or shimming.
- Round rails can be end-supported and span gaps; profile rails require continuous, accurate surfaces.
- Profile-rail wipers add more drag than simple round-bushing seals.
- Three or more parallel rails create an over-constrained (statically indeterminate) system — use maximum two rails spaced apart for large loads.
- Practical tip: choose rail type before starting machine layout because mounting fixtures are radically different.
- Duty-cycle deratings are often overlooked: actual useful life can be 25–50% of the rated capacity under real conditions.
