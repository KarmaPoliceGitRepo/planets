# Numerical Method for Modeling of Acoustic Waves Propagation

- **Source:** Numerical method for modeling of acoustic waves propagation.pdf
- **Drive link:** https://drive.google.com/file/d/1WbT_p-GFVJj75js1qn3T3NA2rPdHCcEs/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** Dykas, Wróblewski, Rulik, Chmielniak (Silesian University of Technology) / 2010
- **Coverage:** full

## Overview
An Archives of Acoustics paper presenting an Euler Acoustic Postprocessor (EAP) for computational aeroacoustics (CAA). The method solves the full nonlinear Euler equations for acoustic fluctuations superimposed on a mean flow field obtained from a separate CFD solver (hybrid CFD/CAA approach). The Euler equations are discretized at third-order accuracy in space and time. Validation cases include a 2D Gaussian acoustic pulse in uniform flow (comparison with analytical solution), speaker-driven cavity acoustics, and aerodynamic noise from flow over a cylinder and airfoil (comparison with experiment from Jacob et al. 2002).

## Unique contribution
The EAP is numerically decoupled from the CFD solver, so any CFD code (RANS, uRANS, LES, SAS, DES) can supply the mean flow field. This modularity avoids repeating expensive CFD runs when the acoustic post-processing parameters change. Compared to direct DNS/LES noise simulations, the EAP can use a coarser grid in the far field, dramatically reducing cost while still capturing correct far-field SPL and wave shapes. Non-reflective boundary conditions are critical to the approach and are validated here.

## Key concepts
- Computational aeroacoustics (CAA)
- Euler equations for acoustic fluctuations
- Hybrid CFD/CAA method
- Euler acoustic postprocessor (EAP)
- Sound pressure level (SPL)
- Non-reflective boundary conditions
- Gaussian pulse validation / analytical solution
- uRANS, SAS, DES turbulence models
- Aerodynamic noise (flow over cylinder and airfoil)
- Near-field vs. far-field acoustics
- Third-order numerical scheme

## Methods / results / takeaways
- Flow variables are decomposed into mean (0-subscript) and fluctuating (prime) parts; the fluctuating conservative variables [ρ', (ρu)', (ρv)', (ρw)', (ρE)'] satisfy the nonlinear Euler equations.
- Mean flow Q₀ is imported from CFD and updated each global time step Δt when the mean flow is unsteady.
- Validation 1 — Gaussian pulse at Ma=0.5: numerical solution matches analytical, confirming at least 5 mesh points per wavelength are necessary.
- Validation 2 — Speaker + cavity at 771.69 Hz, A=2 Pa (100 dB at source): SPL drops from 100 dB near speaker to ~86 dB at 1.2 m; cavity vortex centers show 72 dB minimum; amplitude decays to ~20 % of initial at 2 m. Qualitatively consistent with Weyna (2005) experiments.
- Validation 3 — Cylinder + airfoil at Ma≈0.2: far-field SPL at 90° predicted correctly (~110.7 dB ± 0.5 dB with SAS input); uRANS input overestimates SPL. EAP on a ~100 000-node uniform mesh captures far-field wave shapes that the fine CFD grid loses through numerical dissipation.
- Limitation: accuracy of EAP depends heavily on quality of CFD mean flow data (turbulence model, grid resolution).
