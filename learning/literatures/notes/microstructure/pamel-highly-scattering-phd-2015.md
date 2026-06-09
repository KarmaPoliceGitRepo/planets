# Ultrasonic Inspection of Highly Scattering Materials

- **Source:** Van Pamel PhD thesis, Imperial College London 2015
- **Drive link:** https://drive.google.com/file/d/1.../view
- **Type:** thesis
- **Author/Year:** A. Van Pamel / 2015
- **Coverage:** partial (large file, truncated extraction)

## Overview
A doctoral thesis from Imperial College London on ultrasonic NDE of highly scattering materials (coarse-grained metals, austenitic welds). Combines experimental work, analytical scattering theory, and finite element modelling to characterize the performance limits of ultrasonic inspection in strongly scattering media. Introduces probability-of-detection (POD) framework adapted for scattering-dominated environments.

## Unique contribution
Establishes a rigorous FE modelling capability for wave propagation in polycrystalline media with realistic grain microstructures (Voronoi tessellations with assigned elastic constants), enabling quantitative benchmarking of inspection performance beyond the Born approximation. Demonstrates that conventional inspection SNR metrics are insufficient and proposes a POD-based performance metric.

## Key concepts
- Finite element modelling of polycrystals
- Voronoi grain microstructure
- Highly scattering materials
- Probability of detection (POD)
- Ultrasonic array imaging
- Scattering figure of merit
- Multiple scattering
- Grain noise characterization

## Methods / results / takeaways
- FE model: polycrystalline medium generated using Voronoi tessellation; each grain assigned random orientation; wave propagation computed with Abaqus/Pzflex.
- FE results show multiple scattering effects (coherent backscatter, Anderson localization hints) not captured by single-scattering (Born) theory.
- Experimental validation on austenitic stainless steel forgings (grain size 100–500 µm) at 2–10 MHz.
- POD framework: POD and false alarm rate computed from receiver operating characteristic (ROC) analysis of reconstructed images.
- Array optimisation: sparse array configurations outperform full aperture in terms of detection in highly scattering environment.
- Conclusion: for kD > 1 (grain size ~ wavelength), conventional inspection fails; FE-informed design can extend limits.
- Published follow-on work established FE as validation tool for analytical theories.
