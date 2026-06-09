# Module 21 – Sinusoidal Oscillators: Feedback Analysis

- **Source:** module21 - Sinusoidal Oscillators- Feedback Analysis.pdf
- **Drive link:** https://drive.google.com/file/d/1XZyP7mehu3fbNgJ_F5ROSYnp6-k7biRb/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (53 pages) analyzing sinusoidal oscillators using the feedback system perspective. Covers oscillation conditions (Barkhausen criterion), loop gain analysis, root locus, large-signal steady-state behavior using Bessel functions for BJT, and the Colpitts/Pierce oscillator family.

## Unique contribution
Derives the large-signal steady-state oscillation amplitude by equating the large-signal Gm (computed via Fourier analysis of the BJT transfer characteristic with modified Bessel functions) to the small-signal gm/A_loop — connecting small-signal start-up conditions directly to the steady-state amplitude in a single self-consistent framework.

## Key concepts
- Barkhausen criterion
- Loop gain A_loop (Al)
- Root locus for oscillator
- Phase noise / timing jitter
- LC tank oscillator
- Large-signal Gm
- Bessel functions I0, I1 (BJT large-signal analysis)
- Colpitts oscillator
- Pierce oscillator
- Relaxation oscillator
- Ring oscillator
- Squegging

## Methods / results / takeaways
- Oscillation condition: loop gain magnitude = 1 and phase = 0° (integer multiple of 360°) at the oscillation frequency.
- For A_loop < 1: poles in LHP, oscillations decay. A_loop > 1: poles in RHP, exponential growth. A_loop = 1: poles on jω axis, sustained oscillation.
- Root locus for LC feedback: poles move from LHP (A_loop=0) toward jω axis (A_loop=1) on a circle of radius ω0 = 1/√(LC).
- Large-signal steady-state: high-Q assumption makes output sinusoidal; input to transistor vi = vo/n; Gm drops with amplitude → A_loop reduces to 1.
- BJT large-signal Gm: Gm = gm · 2I1(b)/(b·I0(b)) where b = Vamp·q/(kT·n); Bessel ratio < 1 always, confirming amplitude limiting.
- Colpitts oscillator: capacitor divider feedback (ratio 1/n = C1/(C1+C2)); no transformer required; avoids squegging.
- Pierce oscillator (CE or CC configuration): uses same Colpitts feedback with capacitors forming tank; common in crystal oscillator applications.
- Relaxation oscillator: RC charging/discharging between two reference levels; period ≈ RC·ln(2); poor phase noise, simple to integrate.
- Ring oscillator (CMOS): odd number of inverter stages; period = 2·N·t_pd; frequency tunable via current starving; used for clock generation but high phase noise.
- Squegging: low-frequency parasitic oscillation in bias circuitry; prevented by CE ≤ n·CT.
