# Measuring in the Subnanometer Range: Capacitive and Eddy-Current Sensors

- **Source:** 2014 - Measuring in the Subnanometer Range Capacitive and Eddy-Current Displacement Sensors - Stoyan Nihtianov.pdf
- **Drive link:** https://drive.google.com/file/d/1c9iAzDijF_2u6-IsmcWIOrCMEcorwjGW/view
- **Type:** paper
- **Author/Year:** Stoyan Nihtianov / 2014 (IEEE Instrumentation & Measurement Magazine)
- **Coverage:** full

## Overview
A comparative review and design guide for capacitive sensors (CS) and eddy-current sensors (ECS) in subnanometer displacement measurement. Covers operating principles, nonlinearity sources, interface electronics, and achievable resolution/noise performance for both sensor types.

## Unique contribution
Side-by-side treatment of CS and ECS for sub-nm sensing with quantitative performance figures (ENOB, FOM, thermal drift) for state-of-the-art interface ICs; explains skin-depth limitations of ECS at high frequencies and guard-ring elimination of fringe effects in CS.

## Key concepts
- Capacitive displacement sensor (CS)
- Eddy-current sensor (ECS)
- Skin depth / penetration depth
- Guard rings (fringe field elimination)
- Capacitance-to-digital converter (CDC)
- Charge-balancing sigma-delta modulator
- LC oscillator front-end (ECS)
- Differential sensor configuration
- Subnanometer resolution
- Thermal drift

## Methods / results / takeaways
- **Capacitive sensors**: C = ε₀εᵣA/d (parallel plate, nonlinear in d). Guard electrodes at same potential as sensing electrode eliminate fringe fields → purely 1D field, linear response over small range.
- **Eddy-current sensors**: Penetration depth δ = √(ρ / πf_exc μ). At MHz excitation frequencies, δ ranges from ~66 nm to ~820 nm depending on material → enables surface-layer-only sensing.
- ECS require differential configuration with LC oscillator to suppress temperature-induced drift of the coil.
- **CDC interface** (charge-balancing Σ-Δ modulator): 17-bit resolution at 20 µs conversion time; FOM = 2.2 pJ/bit.
- **ECS interface**: 15.5 ENOB; thermal drift 30 ppm/°C.
- Large DC offset from skin effect in ECS must be handled by differential or bridge configuration.
- CS preferred for lower noise at zero-offset DC; ECS preferred where target material precludes direct capacitive coupling.
