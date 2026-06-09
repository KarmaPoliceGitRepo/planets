# Analysis of Liner's Bore Distortion from Finite Elements Method Calculations

- **Source:** Gode 2018 masters thesis bore distortions FEA (DAF Trucks / Czech Technical University)
- **Drive link:** https://drive.google.com/file/d/1lu1Vu_N594iLqb8vqAlKCqilfm3IjuJF/view
- **Type:** thesis (master's)
- **Author/Year:** Damien Gode / 2018 (DAF Trucks internship / Czech Technical University / ENSTA Bretagne)
- **Coverage:** full

## Overview
Master's internship project at DAF Trucks developing a Python post-processing module within Abaqus FEA to automate bore distortion analysis for DAF's full engine range. The module reads Abaqus output files (nodal radial displacements and coordinates), computes Fourier harmonic decomposition (orders 2–8) of the bore distortion at each liner cross-section height, and produces graphical outputs: radial displacement along paths, deformed profiles, diametrical distortion vs height, cut-profile views, and wall temperature maps. Validated against an AVL MX11 bore distortion analysis report.

## Unique contribution
Internalises bore distortion capability at DAF that was previously outsourced. Demonstrates that diametrical distortion = 2 × Fourier coefficient (radial), which was a source of confusion in prior comparison with AVL results. Uses hand-built Fourier sum-of-cosines (not FFT) for compatibility with the non-uniform node distributions produced by Abaqus.

## Key concepts
- Bore distortion; liner inner-surface deformation
- Fourier harmonic decomposition (orders 2–8); diametrical distortion
- Abaqus FEA; Python post-processing module
- Radial vs diametrical distortion (factor of 2 difference)
- Assembly forces; thermal loads; gas pressure as distortion drivers
- Oil consumption and hydrocarbon emissions from bore distortion
- DAF MX11 engine validation
- Piston ring conformability to bore distortion

## Methods / results / takeaways
- Input: Abaqus .txt reports of nodal X, Y, Z coordinates and radial displacements; temperature field (separate script).
- Node sorting by Z-height needed because Abaqus outputs nodes in element-order, not height-order.
- Fourier transform implemented as sum-of-cosines with factor 2 correction (diametrical vs radial); validated against AVL reference data.
- Outputs: plot_path (radial displacement along circumference at given height), plot_def_profile (deformed cross-section shape with scale factor), plot_distortion_graph (diametrical distortion vs harmonic limit lines for a given height), plot_distortion_by_order (all heights, all harmonics — identifies critical locations), plot_cut_profile (radial distortion along Z at 8 angular positions 0–325° in 45° steps).
- Temperature analysis via separate script; shows temperature distribution along liner wall.
- Main limitation: automatic Abaqus report generation via Python interface sometimes causes Abaqus to freeze; manual file generation is reliable fallback.
- Program satisfies all project requirements; validated against AVL MX11 reference analysis.
- Bibliography confirms key distortion sources: assembly clamping, thermal loads, gas pressure; piston ring must conform to distortion to prevent oil leakage into combustion chamber.
