# A New Technique for Measuring the Deformation of Cylinder Bores During Engine Operation

- **Source:** SAE Technical Paper 950540, International Congress and Exposition, Detroit, February–March 1995
- **Drive link:** https://drive.google.com/file/d/17Xm23PFGmXmyKwoqVurpsdZ3t0nkDDhN/view
- **Type:** paper
- **Author/Year:** Koch, F. (Lehrstuhl für Angewandte Thermodynamik); Fahl, E.; Haas, A. (FEV Motorentechnik) / 1995 (SAE 950540)
- **Coverage:** full

## Overview
Describes a novel in-situ measurement system for cylinder bore deformation during fired engine operation. Eight inductive displacement sensors are installed in a modified production piston at 45° circumferential spacing; signals are routed out via a custom linkage/rocker system to an external DAQ without modifying engine stiffness. Fourier series analysis of the 8-sensor signals extracts circumferential distortion orders up to 4th. Demonstrates the system on fired engines comparing static vs. full-load vs. part-load conditions and Siamese-liner configurations; results correlate well with 3D CMM static measurements.

## Unique contribution
First (or early) system to measure cylinder bore deformation contactlessly during fired engine operation using piston-mounted inductive sensors with an external linkage that minimises crankcase modifications; demonstrates that fired (thermal + mechanical) distortion differs substantially from cold-static assembly measurements, especially in Siamese-bore high-output engines.

## Key concepts
- 8 piston-mounted inductive displacement sensors at 45° spacing; contactless; calibration grooves at BDC
- Linkage/rocker system: link rod + rocker arm through hook-type opening; minimal crankcase modification
- In-situ temperature calibration via electrical heater on piston; operating-temperature calibration check via BDC grooves
- Fourier series decomposition of radial deviation at each crank angle; 2N sensors → up to Nth order (8 sensors → 4th order)
- Static measurement modes: cold-untensioned, cold-tensioned (head assembled), hot-static (coolant heated)
- Fired measurement: captures combustion mechanical + thermal loads simultaneously
- Siamese cylinder liners (no inter-bore coolant): high thermal gradients; pronounced 2nd order deformation
- FEM validation: calibrated FEM models with fired measurement data for design optimisation

## Methods / results / takeaways
- Sensor calibration: section of production liner used as reference; signal vs. clearance calibration curve; temperature dependence corrected.
- Piston eccentricity (secondary motion) extracted from sensor signals as reference circle offset; remaining variation = bore distortion.
- Comparison with 3D CMM: good correlation for static cases (Figure 7 in paper).
- Cast iron block with aluminium head, wet liners: full load shows large upper-bore deformation in engine longitudinal direction (head thermal expansion dominant); reduces at part load.
- Siamese cast iron block: inner and outer liners both show 2nd order deformation in thrust direction at TDC region; outer liner also shows 3rd order due to reduced lateral stiffness.
- Deformation increases from BDC to TDC due to higher temperature and stress at top.
- Dynamic bore changes cannot be captured by static assembly measurements → fired measurement essential for high-BMEP engines.
- Combined use with FEM calibration reduces test component count and development cost.
- Bore-liner relevance: foundational fired-engine bore measurement technique demonstrating that dynamic/thermal bore distortion significantly exceeds static assembly distortion; motivates FEA model calibration against fired data.
