# A Transient Tribodynamic Approach for the Calculation of Internal Combustion Engine Piston Slap Noise

- **Source:** Journal of Sound and Vibration 352 (2015), pp. 192–209
- **Drive link:** https://drive.google.com/file/d/1fKlesqzq-HI3z3efyhXucNy-bcYEDKDp/view
- **Type:** paper
- **Author/Year:** Dolatabadi, Littlefair, De la Cruz, Theodossiades, Rothberg, Rahnejat / 2015 (J Sound Vib 352, pp. 192–209; Loughborough University)
- **Coverage:** full

## Overview
Analytical/numerical framework for predicting piston slap noise in IC engines by coupling transient piston secondary dynamics with elastohydrodynamic (EHD) lubrication and acoustic noise radiation analysis. Local impact impedance is calculated from the EHD film; energy transferred to the cylinder liner is used to estimate sound power levels. Validated against measured noise (SPL) from a Honda CRF 450 single-cylinder motocross engine at 3500 and 4250 rpm using 2D continuous wavelet transform (CWT) analysis.

## Unique contribution
First methodology to couple transient inertial piston dynamics with impact EHD lubrication and structural acoustic attenuation for full prediction of radiated SPL from piston slap events, validated against fired-engine noise measurements. Demonstrates transient approach outperforms quasi-static approach in predicting slap event timing and spectral content; average predicted SPL within 3 dB of measured (106.6 vs 109.5 dB at 4250 rpm).

## Key concepts
- Piston secondary motion (lateral + tilting); eccentricities et, eb at top and bottom of skirt
- Piston slap: thrust side (TS) and anti-thrust side (ATS) events
- Transient equations of motion: coupled piston dynamics + Reynolds equation (EHL)
- Impact impedance; energy transfer to liner structure; sound power level (SPL)
- EHD regime of lubrication at TS and ATS; lubricant film cushioning
- Continuous wavelet spectrum (CWS) for time-frequency analysis of noise events
- Density/viscosity-pressure relations: Dowson-Higginson, Roelands
- Honda CRF 450R; single-cylinder; 4250 rpm; 42 Nm
- Combustion + piston slap = ~80% of total engine noise

## Methods / results / takeaways
- Equations of motion: full 2-DOF coupled system (et, eb); lubrication reaction and friction moment from simultaneous Reynolds equation solution; 5 µs time step; 3 cycles to steady state.
- Reynolds equation: 2D; density and viscosity from Dowson-Higginson and Roelands respectively; squeeze and Couette terms retained.
- Noise transfer: impact velocity → impact impedance (structural mobility) → energy transferred W → acoustic power Pa → sound pressure level SPL at distance from engine block.
- Structural attenuation: ratio of radiated to transferred power; estimated from structural attenuation parameter.
- Validation at 3500 rpm: SPL ~106 dB measured; predictions agree to ~3 dB; CWS shows 2–3 events per cycle matching measurements.
- Validation at 4250 rpm: CWS transient predictions match measured events temporally and spectrally; quasi-static approach shows poorer agreement especially in early cycles.
- Transient vs quasi-static: transient more robust in predicting event repeatability; quasi-static adequate after engine reaches thermal steady state (after ~0.04 s).
- Bore-liner relevance: models liner as structural path for piston-generated noise; demonstrates that EHD film characteristics (film thickness, squeeze velocity) directly determine impact force magnitude and hence noise level.
