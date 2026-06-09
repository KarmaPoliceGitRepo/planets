# Module 4 – The Smith Chart

- **Source:** module4 - The Smith Chart.pdf
- **Drive link:** https://drive.google.com/file/d/1_FmJIt8CgPPuiJza5Mv8VYa1QcEJF8xb/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (29 pages) introducing the Smith Chart as a graphical tool for transmission line and impedance matching calculations. Derives the circle equations, explains how to navigate the chart, and applies it to single-stub and lumped-element matching network design.

## Unique contribution
Bridges pure mathematical derivation of the Smith Chart circles with practical matching design workflows, including the admittance overlay for shunt element addition — demonstrating the full workflow from impedance measurement to matched network in one document.

## Key concepts
- Smith Chart
- Reflection coefficient Γ (complex plane)
- Resistance circles
- Reactance circles
- Admittance chart (Y-Smith Chart)
- SWR circle
- Single-stub matching
- Shunt-stub matching
- Lumped component matching
- Impedance normalization

## Methods / results / takeaways
- The Smith Chart maps the complex impedance plane to the unit circle of the reflection coefficient Γ = (z−1)/(z+1) where z = Z/Z0.
- Constant resistance circles: center (r/(r+1), 0), radius 1/(r+1).
- Constant reactance circles: center (1, 1/x), radius 1/|x|.
- Moving along a lossless transmission line corresponds to rotating clockwise on a constant-|Γ| circle; one full revolution = λ/2.
- An SWR circle is the circle of constant |Γ|; VSWR = (1+|Γ|)/(1−|Γ|).
- For shunt elements, switch to admittance chart (rotate 180°); series elements use impedance chart.
- Single-stub matching: find two points on the SWR circle where Re(Y) = Y0, then add a shunt stub of appropriate length to cancel the susceptance.
- Lumped matching: L-network element values read directly from chart intersections.
