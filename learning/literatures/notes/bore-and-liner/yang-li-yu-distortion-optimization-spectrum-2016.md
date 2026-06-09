# Distortion Optimization of Engine Cylinder Liner Using Spectrum Characterization and Parametric Analysis

- **Source:** Mathematical Problems in Engineering, Vol. 2016, Article ID 9212613, 11 pages, DOI: 10.1155/2016/9212613
- **Drive link:** https://drive.google.com/file/d/19niK96_jkQvtDhWO59qqIZw0JRGD-87e/view
- **Type:** paper
- **Author/Year:** Yang, Zhaohui; Li, Baotong; Yu, Tianxiang (Northwestern Polytechnical University / Xi'an Jiaotong University) / 2016 (Math Probl Eng 2016)
- **Coverage:** full

## Overview
ANSYS FEM + CFD coupled study of bore distortion in a 4-cylinder inline gasoline engine (bore radius 41.5 mm). Introduces FFT-based spectrum characterisation applied simultaneously to bore distortion, temperature distribution, and bolt pretightening stress, demonstrating that 2nd-order distortion tracks thermally induced oval temperature pattern, while 4th-order tracks bolt pretightening stress. Parametric analysis of water jacket geometry (thickness, inlet size/height/eccentricity) and bolt parameters (length, tightening sequence) identifies optimal settings that reduce 2nd-order amplitude from ~15 µm to ~12 µm and 4th-order from ~6 µm to ~3 µm. Compares optimised distortions against GOETZE, Dunaevsky, and Tomanik conformability bounds.

## Unique contribution
First study to apply FFT to three profiles simultaneously (distortion, temperature, pretightening stress) to establish a direct spectral mapping between load type and distortion order; identifies optimal water jacket thickness (9 mm) and bolt length (60 mm) + sequence as a design methodology; confirms optimised design satisfies GOETZE and Dunaevsky bounds and approaches Tomanik bounds.

## Key concepts
- FEM model: 601,736 elements / 690,912 nodes; ANSYS FLOTRAN for thermal-fluid coupling (RNG k-ε turbulence in water jacket)
- Max distortion: 47.6–52.6 µm across 4 cylinders (end cylinders slightly worse); max < 0.27% of bore radius
- Fourier decomposition applied to distortion, temperature, and pretightening stress using 64-point FFT
- Dominant distortion orders: 2nd and 4th; 2nd order most sensitive to thermal load (temperature 2nd-order dominant); 4th order most sensitive to bolt pretightening (pretightening stress 4th-order dominant)
- Water jacket parametric study: thickness P1 (5–13 mm); inlet diameter P2; inlet height P3 (25–65 mm); inlet eccentricity P4
- Bolt parametric study: bolt length P5 (20–60 mm); tightening sequence P6 (3 sequences)
- Optimal: P1=9 mm, P2=28.8 mm, P3=55 mm, P4=9 mm, P5=60 mm, P6=sequence 3 (3-8-2-9-4-7-1-10-5-6)
- Result: 2nd-order peak ~15 µm → ~12 µm; 4th-order ~6–7 µm → ~3 µm across all 4 cylinders
- Conformability bounds comparison: GOETZE (tight), Dunaevsky (less tight for k>2), Tomanik (tightest); optimised design satisfies GOETZE and Dunaevsky, approaches Tomanik

## Methods / results / takeaways
- Thermal load: Woschni formula for heat flux; KIVA3 for combustion pressure/temperature histories; RNG k-ε for coolant flow.
- Validation: not explicitly validated against measurement in this paper; cites Kazmierczak (2004) for KIVA3.
- Polar FFT: 64-step circumnavigation of bore at each axial hierarchy (73 levels, ~256 points each).
- Simplified parametric FE model: detailed model feature-suppressed for efficient parametric sweeps.
- Key spectral finding: thermal 2nd-order and bolt-clamping 4th-order are independently controllable — decoupled design targets.
- Water jacket design insight: thicker jacket is not always better (structural stiffness trades with cooling at P1 > 9 mm).
- Bore-liner relevance: provides systematic methodology for distortion-order-specific design optimisation; links specific design parameters to specific Fourier harmonic reduction; conformability bounds comparison validates that optimised design improves ring sealing.
