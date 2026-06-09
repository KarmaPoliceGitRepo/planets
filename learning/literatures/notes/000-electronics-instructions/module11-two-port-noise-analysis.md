# Module 11 – Two-Port Noise Analysis

- **Source:** module11 - Two-Port Noise Analysis.pdf
- **Drive link:** https://drive.google.com/file/d/1rfFlfvjdkqRRfBSCi4f2bW205WZ2sl-p/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (26 pages) developing the general two-port noise model using equivalent input-referred noise voltage and current generators, deriving the minimum noise figure Fmin, and showing how optimal source impedance Yopt achieves Fmin in practice.

## Unique contribution
Derives the complete noise parameter set (Fmin, Rn, Yopt) from first principles and provides the standard formula F = Fmin + (Rn/Gs)|Ys − Yopt|², which is the foundation for LNA noise optimization and noise circle plotting on the Smith Chart.

## Key concepts
- Equivalent input noise generators (vn, in)
- Noise resistance Rn
- Noise conductance Gu
- Optimal source admittance Yopt
- Minimum noise figure Fmin
- Noise circles (Smith Chart)
- Correlated noise sources
- Noise correlation coefficient c
- Multi-finger FET layout
- Noise parameter extraction

## Methods / results / takeaways
- Any noisy two-port is equivalent to a noiseless two-port with two input-referred noise generators: vn (series) and in (shunt).
- Noise factor: F = 1 + (|vn + in/Ys|²) / (4kTRs·Δf).
- Optimal source: Rs_opt = √(Rn/Gu), Xs_opt = −Bc/Gu where Bc is the imaginary part of the correlation admittance Yc.
- Fmin = 1 + 2√(Rn·Gu) (achieved when Ys = Yopt).
- General formula: F = Fmin + (Rn/Gs)|Ys − Yopt|², used to draw noise circles on Smith Chart.
- Noise circles are circles centered near Yopt; LNA design trades noise for gain by moving away from Yopt toward Ymax.
- For FETs: Rn ∝ γ/(gm), so increasing gm (wider transistor) reduces Rn but increases input capacitance — multi-finger layout balances this.
- Noise parameters (Fmin, Rn, Yopt) are typically extracted from S-parameter and noise figure measurements at multiple source impedances.
