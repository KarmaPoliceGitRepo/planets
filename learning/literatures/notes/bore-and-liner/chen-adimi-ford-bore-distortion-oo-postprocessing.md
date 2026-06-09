# An Object-Oriented Approach to the Post-Processing of Cylinder Bore Distortion, Valve Seat Distortion, Valve Guide-to-Seat Misalignment and Cam Bore Misalignment

- **Source:** SAE Technical Paper 2017-01-1075
- **Drive link:** https://drive.google.com/file/d/1UsaCa8xqyeJqsWVP3xMtA8EiJSyPAvPt/view
- **Type:** paper
- **Author/Year:** Chen, Adimi, Chen, Brewer, Shi (Ford Motor Company) / 2017 (SAE 2017-01-1075)
- **Coverage:** full

## Overview
Presents an object-oriented C++ software framework for automated FEA post-processing of cylinder bore distortion, valve seat distortion, valve guide-to-seat misalignment, and cam bore misalignment. Implements best-fit plane, line, circle (MLS and Kasa methods), and cylinder (Levenberg-Marquardt) algorithms. Applies discrete Fourier transform (DFT) for bore roundness and harmonic orders (2nd, 3rd, 4th). Replaces manual serial commercial-software workflows with automated batch processing, reducing post-processing time from hours to ~10 seconds.

## Unique contribution
Object-oriented C++ implementation that automates all FEA bore/valve/cam distortion post-processing in a single unified framework, correctly handling large cylinder axis rotations (which some commercial software fails to handle), reducing post-processing time from hours to ~10 seconds with no user intervention.

## Key concepts
- Best-fit cylinder: Levenberg-Marquardt minimisation of orthogonal distances; SVD for plane/line
- Best-fit circle: Modified Least Squares (MLS) and Kasa methods (same centre, slightly different radius)
- Discrete Fourier Transform (DFT) of radial deviations around cylinder circumference
- Fourier orders 2, 3, 4 for bore distortion assessment; roundness = max−min deviation
- Object-oriented C++: classes BestFitCircle, BestFitCylinder, ValveSeatDistortion, BoreDistortion
- Gage line nodes: projected onto perfect circle/cylinder before deformation; offset = distortion
- Cam bore misalignment: best-fit line through bore centres; deviation = misalignment
- Ford engine application (multi-cylinder)

## Methods / results / takeaways
- Gage line nodes pre-positioned on perfect circles/cylinders; post-deformation displacements output from FEA; projected onto best-fit geometry planes for distortion extraction.
- MLS circle fitting: closed-form solution; robust against outliers inside circle. Kasa: concentric, slightly larger radius.
- Best-fit cylinder: Levenberg-Marquardt with Jacobian from closed-form distance derivatives; handles large rotations correctly.
- DFT applied to projected radial deviations around bore circumference → Fourier coefficients for orders 2, 3, 4.
- Numerical examples: in-plane valve seat distortion, and bore roundness + 2nd/3rd/4th order Fourier coefficients demonstrated for a Ford engine.
- Efficiency: ~10 s vs hours for manual commercial software post-processing; no data transfer errors.
- Bore-liner relevance: provides the post-processing methodology for extracting Fourier distortion orders from FEA bore nodal results — directly applicable to cylinder liner bore distortion analysis and ring conformability assessment.
