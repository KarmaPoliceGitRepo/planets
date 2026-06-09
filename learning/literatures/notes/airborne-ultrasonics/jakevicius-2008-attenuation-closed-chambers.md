# Ultrasound Attenuation Dependence on Air Temperature in Closed Chambers

- **Source:** Jakevičius 2008 attenuation closed chambers
- **Drive link:** https://drive.google.com/file/d/1PPjatNMQLpAwqnyLNMLvrg2tf6rSKw3K/view
- **Type:** paper
- **Author/Year:** Jakevičius & Demčenko, 2008 (Ultragarsas (Ultrasound), 63(1), 18–22)
- **Coverage:** full

## Overview
Analyses how ultrasonic attenuation changes with temperature in a closed (sealed) chamber, where temperature and humidity are not independent — temperature changes alter relative humidity through thermodynamic coupling. Two regimes studied: isochoric (constant volume, pressure rises with T) and isobaric (constant pressure, volume expands). Calculations use ISO 9613-1 atmospheric absorption model. Finds frequency-dependent and process-dependent behaviour: at 200 kHz, attenuation increases with T (isochoric); at 1 MHz, attenuation decreases with T regardless of process or RH; isobaric gives monotone increase at all frequencies.

## Unique contribution
Highlights a practically important but often overlooked coupling: in a closed measurement chamber, you cannot independently set T and RH — changing T shifts RH along a thermodynamic path. This makes attenuation corrections for temperature much more complex than in open-air systems, and means ISO 9613-1 cannot be applied naively. Critical insight for lab-based airborne ultrasound setups (e.g., calibration chambers, industrial enclosures).

## Key concepts
- Isochoric (constant volume) vs isobaric (constant pressure) air processes
- Relative humidity coupling to temperature in closed chambers
- Ultrasonic attenuation vs temperature at 200 kHz and 1 MHz
- ISO 9613-1 atmospheric absorption model
- Water condensation at dew point — measurement degradation
- Initial conditions: p₀ = 100 kPa, t₀ = 20°C, RH₀ = 20 / 40 / 60%
- Attenuation budget: classical + molecular relaxation (N₂, O₂) contributions

## Methods / results / takeaways
- Model: ISO 9613-1 absorption formula applied along isochoric and isobaric T-paths; T varied from 20°C to 50°C.
- Initial RH values: 20%, 40%, 60%; three curves per process.
- Isochoric results (constant V): as T rises, pressure increases, RH changes non-monotonically; at 200 kHz, attenuation increases with T; at 1 MHz, attenuation decreases with T for all three initial RH values.
- Isobaric results (constant P): volume expands, RH drops with rising T; attenuation increases linearly with T at all frequencies studied; RH influence on attenuation decreases at higher frequencies.
- Condensation threshold: if T is lowered below dew point of initial air, water condenses — causes anomalous echo attenuation and measurement errors; especially relevant for cooling cycles.
- Practical upshot: for a sealed measurement box at constant humidity load, isochoric heating causes RH to first increase then decrease (depending on whether saturation is reached), creating a non-monotone attenuation response at 200 kHz that cannot be corrected by a simple linear temperature compensation.
- Limitation: model calculations only; no experimental validation presented; ISO 9613-1 valid range may not cover all conditions.
