# Ultrasonic Roughness Measurement Based on Scattering Attenuation

- **Source:** Lian 2019 roughness scattering attenuation
- **Drive link:** https://drive.google.com/file/d/1P959b22YoRI5l0XwyMMMspdEXXHk2yIO/view
- **Type:** paper
- **Author/Year:** Lian, Liu, Zhou, Zhang, Liu & Wang, 2019 (Surface Topography: Metrology and Properties, 7, 015001)
- **Coverage:** full

## Overview
Proposes a single-transducer pulse-echo ultrasonic roughness measurement method for machined surfaces (Rq = 0.4–42 μm). Derives a scattering attenuation model combining Kirchhoff approximation (KA) for mode-conversion at local incident angle and phase-screen approximation (PSA) for phase cancellation. Attenuation coefficient AS depends on frequency and Rq but not on correlation length (in 5–20 MHz range). Validated on 8 nickel alloy samples with relative errors < 10% within each frequency's sensitive region.

## Unique contribution
Explicitly accounts for local incident angle effects (mode conversion) in the scattering attenuation model — previous models ignored this contribution. Uses a single transducer as both transmitter and receiver, minimising shadowing from oblique incidence. Shows that correlation length has little effect on attenuation in the MHz range, simplifying Rq inversion to a single-parameter problem.

## Key concepts
- Single-transducer pulse-echo ultrasonic roughness measurement
- Scattering attenuation coefficient AS
- Kirchhoff approximation (KA) for mode conversion
- Phase-screen approximation (PSA) for phase cancellation
- Local incident angle θ̄i = √(2/π) × Rq/λx
- Frequency-sensitive measurement range
- Machined surfaces (grinding, milling, shot peening)
- Water-immersion nickel alloy test

## Methods / results / takeaways
- Model: AS = R(θ̄i) × exp(−8π²f²Rq²/V₁²); where R(θ̄i) is the reflection coefficient at mean local incident angle incorporating mode conversion.
- θ̄i = √(2Rq/πλx): average local incident angle depends on RMS gradient = √2Rq/λx.
- Correlation length λx has little influence on AS for 5–20 MHz (key simplification).
- Experiment: 8 Ni alloy samples, Rq = 0.4–41.6 μm, λx = 90–2020 μm; 3 transducers (5/10/20 MHz, 8 mm diameter).
- Results: 5 MHz sensitive for Rq = 7–42 μm (< 9.3% error); 20 MHz sensitive for Rq = 0.8–1.7 μm (< 17.3% error).
- Accuracy comparable to optical profiler (Zygo), better than conventional Kirchhoff model (which ignores local incident angle).
- Limitation: deviates at high roughness for high frequency (finite transducer aperture limits phase cancellation averaging).
