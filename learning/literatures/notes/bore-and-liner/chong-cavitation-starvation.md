# Cavitation Induced Starvation for Piston-Ring/Liner Tribological Conjunction

- **Source:** Chong 2010 cavitation-induced starvation (Tribology International 44(4), 2011)
- **Drive link:** https://drive.google.com/file/d/1mriINjc1Baoa_ClWGR-8EIhIJ2tSsyhI/view
- **Type:** paper
- **Author/Year:** Chong, Teodorescu, Vaughan / 2010/2011 (Tribology International 44(4), pp. 483–497; Cranfield University)
- **Coverage:** full

## Overview
Analytical investigation of ring-liner lubrication mechanism at TDC and BDC reversals, focusing on how pre-reversal cavitation survives through the dead centre and creates a confined bubble at the inlet side after reversal, leading to lubricant starvation and thinner-than-expected oil films. Three lubrication algorithms compared: (i) transient Reynolds, (ii) steady-state modified Elrod, and (iii) transient modified Elrod. Applied to a generic gasoline engine at 2000 rpm.

## Unique contribution
First to show that pre-reversal cavitation at the trailing edge survives reversal as a sealed bubble at the leading edge, causing starvation (fractional film content θ < 1) that reduces oil film thickness below Reynolds equation predictions. Demonstrates that steady-state Elrod misses film history, predicting false complete film collapse at reversal, whereas transient Elrod correctly tracks cavitation bubble lifecycle.

## Key concepts
- Cavitation; Elrod cavitation algorithm; JFO boundary conditions
- Lubricant starvation; fractional film content (θ)
- Pre-reversal cavitation bubble; post-reversal starvation
- Transient vs steady-state Reynolds/Elrod comparison
- Squeeze film at TDC/BDC
- Boundary friction vs viscous friction at reversal
- Surface texturing for boundary friction reduction

## Methods / results / takeaways
- Modified Elrod algorithm uses Vijayaraghavan-Keith transformation; Jacobian-based Newton iteration for θ; 200 mesh points; convergence criterion 1×10⁻⁷ on θ.
- At mid-stroke (A, B, C conditions): transient Elrod predicts larger cavitation region than steady-state; thinner film because less squeeze-film support.
- At TDC: pre-reversal cavitation (trailing edge of downstroke) survives reversal as sealed bubble at inlet (+0.1°), quickly implodes (+5–10°) but depletes lubricant → starvation (θ < 1) → higher pressure, thinner film.
- At BDC: pre-reversal cavitation survives reversal longer (lower contact pressure, larger bubble); thicker films than TDC due to lower load.
- Boundary friction dominates near TDC and BDC; viscous friction dominates mid-stroke. Transient Elrod predicts highest friction at reversals due to thinnest film.
- Film increases with engine speed (1500–2500 rpm) at all crank angles including reversals → lower friction at higher speeds.
- Lubricant film is thinner than initially thought when using steady-state algorithms.
- Solution proposed (not implemented): localised surface texturing at high-boundary-friction regions to increase film without increasing oil consumption.
