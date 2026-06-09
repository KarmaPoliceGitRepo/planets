# Development of a Technique to Predict Oil Consumption with Consideration for Cylinder Deformation

- **Source:** 2003-01-0982 Development of a Technique to Predict Oil for Cylinder Deformation (SAE 2003-01-0982)
- **Drive link:** https://drive.google.com/file/d/1HIS3k4xgcRfluLa9o26kSgtZXRXV_kHi/view
- **Type:** paper
- **Author/Year:** Yamada, Kobayashi, Kusama, Sagawa, Takiguchi, Ishikawa / 2003 (SAE 2003-01-0982; Riken Corporation / Musashi Institute of Technology)
- **Coverage:** full

## Overview
Develops a simplified simulation model for predicting oil consumption through the top ring with consideration for cylinder bore deformation. The ring is modelled as a 2D straight beam (theorem of three moments approach), deformed by ring tension, gas pressure, and oil film pressure against the measured deformed cylinder. Oil film thickness, computed from ring/bore gap, is used to calculate oil transported to the combustion chamber over the TOP ring running surface. Validated against capacitance OFT measurements and SO₂ tracer oil consumption measurements on a 4-cylinder DI diesel engine.

## Unique contribution
First simplified beam model linking measured cylinder bore deformation during operation to top ring oil film thickness and oil consumption in a personal-computer-scale calculation, avoiding full 3D FEM. Demonstrates that hexagonal upper-cylinder deformation (from head bolts) near exhaust TDC causes the dominant oil consumption contribution.

## Key concepts
- Cylinder bore deformation; ring conformability; oil consumption
- Piston ring as straight beam; theorem of three moments
- Full-flood vs oil-starve lubrication conditions
- Capacitance OFT measurement (electrode embedded in ring face)
- SO₂ tracer oil consumption measurement
- Dummy head machining (reducing upper cylinder deformation)
- Head bolt-induced hexagonal deformation; thermal elliptical deformation
- Oil passing across ring running surface (Couette + inertia flow)

## Methods / results / takeaways
- Test engine: inline 4-cyl DI diesel with turbo inter-cooler, 5307cc, 114×130mm, CR 18:1, 129kW at 2700 rpm, dry liner, 6 head bolts per cylinder.
- Cylinder deformation during operation (1600 rpm, full load, 80°C): upper part distorts as hexagon (from 6 head bolts, up to s=30mm from top deck); mid cylinder distorts as ellipse in thrust direction.
- Ring model: expanded into 360-element beam; convergent iteration with oil film reaction force at each step.
- Ring OFT validation: calculated full-flood OFT closely matches measured values; starvation OFT is much thinner than measured (actual condition lies between full-flood and starve).
- Oil consumption: cylinder No.3 (more elliptical mid deformation) has higher measured oil consumption than No.4; model correctly predicts this qualitative trend.
- Dummy head machining reduces upper-cylinder hexagonal deformation → measured oil consumption falls; model predicts this reduction.
- Oil film thickness affected most near exhaust TDC (s≈13.5mm) where upper cylinder deforms outward (thick film at "A") vs inward (thin film at "B"); large upward inertia forces transport oil to combustion chamber at this point.
- Key limitation: absolute oil consumption prediction very difficult because actual lubrication condition (between full-flood and starve) is unknown; qualitative trend prediction confirmed.
