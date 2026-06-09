# Simulation of Mild Wear in a Cam-Follower Contact with Follower Rotation

- **Source:** 1996 - Simulation of mild wear in a cam-follower contact
- **Drive link:** https://drive.google.com/file/d/1qAfcRl0gd1j0RyzrtyQH_jwA1dpwpx40/view
- **Type:** paper
- **Author/Year:** Hugnell, Björklund, Andersson / 1996 (Wear, 199)
- **Coverage:** full

## Overview
Simulation of mild wear in an automotive cam-follower contact incorporating follower rotation. The model uses Archard's generalised wear equation in single-point-observation form, iteratively updating surface topography and recalculating contact pressures. Three cases compared: cam-only wear, follower-only wear, and both wearing simultaneously. FEM analysis verifies the infinite half-plane assumption for the follower.

## Unique contribution
Demonstrates that including follower rotation is critical for realistic wear simulation and that a wear-resistant follower against a softer cam gives the most favourable (lowest) long-term contact pressures. Shows that follower-only wear produces the worst pressure redistribution and pitting risk.

## Key concepts
- Archard wear equation (single-point observation)
- Cam-follower contact; rolling-sliding
- Follower rotation; torque balance
- Surface topography update iteration
- Hertz contact mechanics; infinite half-plane assumption
- ANSYS FEM validation
- Wear coefficient; pressure redistribution

## Methods / results / takeaways
- Wear coefficient 10⁻¹² mm² N⁻¹ applied to polydy-type cam curve; simulation covers ~10⁴ cycles per iteration, up to 5000 h.
- FEM check shows half-plane assumption valid within 5% for interior contact regions of the follower.
- Cam-only wear: lowest contact pressures (favourable geometry forms on cam surface).
- Follower-only wear: highest pressures (geometry deteriorates at follower edges); location matches observed surface fatigue pits.
- Both wearing: intermediate pressures; summit on follower centre + crater at cam top.
- Note: primarily a cam-follower wear study, not directly about cylinder bores—peripheral relevance to general engine tribology context.
