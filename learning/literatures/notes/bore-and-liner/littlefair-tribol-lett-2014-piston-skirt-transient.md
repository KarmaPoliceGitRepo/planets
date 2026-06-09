# Transient Tribo-Dynamics of Thermo-Elastic Compliant High-Performance Piston Skirts

- **Source:** Tribology Letters 53(1) (2014), pp. 51–70
- **Drive link:** https://drive.google.com/file/d/10qMndmE6LDFOMhbWH-aQa1ED88U4yV__/view
- **Type:** paper
- **Author/Year:** Littlefair, De la Cruz, Theodossiades, Mills, Howell-Smith, Rahnejat, Dwyer-Joyce / 2014 (Tribol Lett 53(1), pp. 51–70; Loughborough University + University of Sheffield + Capricorn Automotive)
- **Coverage:** full

## Overview
Fully transient tribodynamic model of a high-performance compliant piston skirt including piston secondary dynamics, thermo-elastic distortion (via compliance matrix method), and EHD lubrication. Validated against non-invasive ultrasonic film thickness measurements on a fired Honda CRF 450R engine at 4250 rpm. Demonstrates that preferentially compliant short partial skirts can improve oil film load carrying capacity and reduce friction through thermo-elastic wedge formation.

## Unique contribution
First reported validated transient tribo-dynamics model incorporating full piston secondary motion equations of motion simultaneously solved with Reynolds equation and global thermo-elastic skirt distortion, validated by non-invasive ultrasonic film thickness from a fired engine. The compliance matrix approach provides 4 orders of magnitude computational speedup vs. direct stiffness matrix inversion.

## Key concepts
- Transient tribodynamics; piston secondary motion; equations of motion (2-DOF: et, eb)
- Thermo-elastic distortion of compliant piston skirt; compliance matrix method
- Reynolds equation; mixed EHD lubrication; Greenwood-Tripp asperity contact
- Ultrasonic film thickness measurement (10 MHz transducers); spring-layer model
- Compliance matrix: 5D pre-computed response array A(i,j,k,l,n); 4 orders faster than PCG
- Skirt deformation components: crown pressure, normal reaction, inertial, thermal
- Honda CRF 450R engine; 4250 rpm; Newmark integration; 5 µs time step
- Roelands viscosity-pressure; Dowson-Higginson density-pressure
- Contact loads ~5 kN; entraining velocity 0–35 m/s

## Methods / results / takeaways
- Equations of motion: fully coupled 2-DOF transient system with EHD reactions; Newmark time integration; 3 engine cycle warm-up.
- Compliance matrix: unit loads applied at each node sequentially to build pre-computed 5D deflection response array; combined with lubricant pressures and crown/inertial/thermal loads by superposition.
- Reynolds equation: 2D discretised with central differences (Poiseuille) and backward differences (Couette); EIN Newton-Raphson with Gauss-Seidel; coupled with elastic film shape h_ij = s_ij − δ_ij + c.
- Thermo-elastic distortion: crown pressure → bending at skirt bottom (improves wedge in combustion stroke); reaction forces → compression at skirt centre; inertial contribution 2 orders smaller.
- Results: at 23° ATDC, 4250 rpm, contact force 2091 N, piston speed 4.4 m/s; predicted film thickness agrees well with ultrasonic measurements along centreline.
- Film thickness minima located ~7 mm circumferentially from centreline; skirt deformation shifts pressure distribution vs. rigid skirt analysis.
- Compliant skirt: maximum radial deflection up to 50 µm; significantly different pressure distribution and larger contact patch vs. stiff skirt with only local deformation.
- Bore-liner relevance: establishes that piston skirt compliance and thermo-elastic distortion substantially affect piston-liner film thickness and friction — linked to companion Proc IMechE Part J paper (same engine, quasi-static).
