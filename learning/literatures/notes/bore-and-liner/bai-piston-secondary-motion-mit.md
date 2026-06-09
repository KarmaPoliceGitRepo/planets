# Solving Piston Secondary Motion of Internal Combustion Engines

- **Source:** final_report_dongfang_bai-solving piston secondary motion
- **Drive link:** https://drive.google.com/file/d/1QfHyXSLddAIRbhqbYBq8IigFUbTlXoeS/view
- **Type:** notes
- **Author/Year:** Dongfang Bai (MIT Sloan Automotive Laboratory) / ~2004
- **Coverage:** full

## Overview
MIT course/research project report developing a numerical model of piston secondary motion (lateral translation and tilt) including cavitation (JFO theory), skirt elastic deformation from an FEA compliance matrix, and piston dynamics. Parametric studies explore the effects of rigid clearance, piston ovality, and engine speed on lateral motion and tilt; also shows cavitation regions arising from both slider motion and piston tilt.

## Unique contribution
Clean pedagogical exposition of the piston-skirt lubrication model including a compliance matrix approach (from sponsor's FEA) for skirt deformation, the Universal Reynolds equation with JFO cavitation, and Newton-iteration coupling of dynamics + lubrication + deformation. Shows dual cavitation regions at power stroke TDC: one from slider motion, one from piston tilting away from thrust side.

## Key concepts
- Piston secondary motion (lateral and tilt)
- JFO cavitation theory; Universal Reynolds equation
- Compliance matrix (FEA-derived skirt deformation)
- Piston ovality; nominal radial clearance
- Control volume discretisation
- Newton iteration coupling (dynamics + fluid + deformation)
- Cavitation from tilt vs. slider motion
- Hydrodynamic pressure distribution on piston skirt

## Methods / results / takeaways
- Compliance matrix diagonal shows lower/central skirt is much softer than upper/outer skirt; deformation reduces sharp pressure peaks significantly.
- Larger rigid clearance → larger lateral motion amplitude (piston moves more to generate same hydrodynamic load).
- Larger ovality → larger lateral motion (flatter cross-section, reduced circumferential resistance).
- Higher engine speed → smaller maximum lateral motion at power stroke (higher entrainment speed requires less eccentricity to support same side force).
- Two distinct cavitation zones at 365° CA: trailing edge of slider and upper skirt tilting away from thrust side.
- Model runs one engine cycle in ~10 minutes (17×17 grid); finer grid planned for hydrodynamic pressure accuracy.
