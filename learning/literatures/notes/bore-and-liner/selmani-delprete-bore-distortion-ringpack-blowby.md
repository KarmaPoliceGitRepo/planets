# Simulation of the Cylinder Bore Distortion and Effect on the Sealing Capacity of the Ringpack

- **Source:** SN Applied Sciences 1 (2019), Article 314
- **Drive link:** https://drive.google.com/file/d/1EZKNJisJcllhg8QGF_DE7q1HrVmpGjtD/view
- **Type:** paper
- **Author/Year:** Selmani, Delprete (Politecnico di Torino), Bisha (Polytechnic University of Tirana) / 2019 (SN Appl Sci 1, 314)
- **Coverage:** full

## Overview
FEM analysis of cylinder liner bore distortion in a 4-cylinder diesel engine (120×148 mm, 2000 rpm full load) with Fourier decomposition into orders 0–4, followed by Ricardo RINGPAK simulations to evaluate the effect of each individual distortion order on ring dynamics, inter-ring gas pressures, and blow-by. Identifies order 0 (uniform dilation near TDC) as most detrimental to ring sealing; orders 3 and 4 produce disproportionately high blow-by relative to their small distortion amplitudes.

## Unique contribution
First systematic evaluation of individual Fourier distortion orders (0–4) on ring pack blow-by using an industry solver (RINGPAK), showing that order 0 is catastrophic for sealing and orders 3 and 4 produce unexpectedly high blow-by despite small amplitudes, while orders 1 and 2 behave similarly to an undistorted bore.

## Key concepts
- Bore distortion orders 0–4; Fourier series decomposition; Matlab FFT
- Ring axial, radial, and twist dynamics; ring-groove clearance; ring flutter
- Radial collapse of second ring; blow-by; inter-ring gas pressures
- Ricardo RINGPAK solver; 2D axisymmetric ring pack model
- Order 0: uniform circumferential dilation near TDC due to thermal/pressure loading
- Order 1: axis shift; order 2: oval; order 3: 3-lobe; order 4: 4-lobe (bolt pattern)
- Minimum oil film on liner 5 µm; rigid components; no secondary motion

## Methods / results / takeaways
- FEM: cylinder 120×148 mm; 2000 rpm full load; peak firing pressure ~128 bar; Fourier extraction in Matlab.
- Distortion magnitudes: orders 0 and 1 largest (order of 100s µm magnitude range); orders 3 and 4 one to two orders smaller.
- Non-distorted bore: top ring stable; second ring flutters (inertia); third ring lifts at stroke transitions; second land pressure always below top land.
- Order 0: top ring lifts (second land pressure exceeds top land ~150° ATDC); blow-by dramatically increased — worst case among all orders.
- Order 1: ring dynamics and blow-by similar to undistorted bore (rigid axis shift accommodated by piston).
- Order 2: similar to order 1 despite oval shape; ring pack adapts effectively.
- Order 3: top ring lifts only at intake TDC; inter-ring pressures very low; no radial collapse; but blow-by elevated relative to small distortion.
- Order 4: second ring continuous axial motion; radial collapse of second ring; second land pressure rises and crosses top land → elevated blow-by despite lowest amplitude.
- Combined distorted bore: complex combined behaviour; pressure crossover in second land; no radial collapse but high second land pressure.
- Bore-liner relevance: directly quantifies impact of each distortion order on ring sealing; confirms order 0 and higher-order Fourier terms are critical for ring conformability and blow-by control.
