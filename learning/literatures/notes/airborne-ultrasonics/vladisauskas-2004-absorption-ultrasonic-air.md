# Absorption of Ultrasonic Waves in Air

- **Source:** Vladisauskas 2004 absorption ultrasonic air
- **Drive link:** https://drive.google.com/file/d/1jfBAEYPzj7k7p24cyuaHkz66UpveyISY/view
- **Type:** paper
- **Author/Year:** Vladišauskas & Jakevičius, 2004 (Ultragarsas (Ultrasound), No. 1(50), 46–49; Kaunas University of Technology)
- **Coverage:** full

## Overview
Calculates and analyses the absorption coefficient of ultrasonic waves in air at 50 kHz, 100 kHz, 200 kHz, 500 kHz, and 1 MHz using ISO 9613-1, over a wide range: temperature −50°C to +100°C, humidity 0–100%, pressure 10⁵–20×10⁵ Pa. Presents results as log-scale plots showing the dependence on each parameter at fixed others. Key finding: absorption behaviour divides into "low frequency" (50–200 kHz, with temperature-dependent maximum due to relaxation) and "high frequency" (500 kHz–1 MHz, monotone increase with T). Practical focus: error budgets for air-coupled ultrasonic inspection systems.

## Unique contribution
Provides practical design charts for air-coupled ultrasound system builders at the 50 kHz–1 MHz range, clearly showing where molecular relaxation peaks dominate and where classical absorption takes over. Quantifies specific numerical impacts: e.g., ΔT = 20→40°C at 100 kHz over 10 m → 23 dB extra loss; ΔT = 60→80°C at 1 MHz → 18 dB/m additional attenuation. The ISO 9613-1 application to this frequency range is validated and presented in immediately accessible form for system design.

## Key concepts
- ISO 9613-1 absorption model applied to 50 kHz–1 MHz range
- Low-frequency regime (50–200 kHz): absorption maximum at intermediate temperature due to O₂/N₂ relaxation peak shift
- High-frequency regime (500 kHz–1 MHz): absorption increases monotonically with T
- Temperature maximum: 50 kHz peak at ~45°C (α_max ≈ 2.4 dB/m); 100 kHz peak at ~57°C (α_max ≈ 6.3 dB/m)
- Pressure effect: increasing pressure decreases α (molecular spacing increases mean free path relative to wavelength); effect flattens above ~5×10⁵ Pa
- Humidity effect: at low frequencies, α peaks around 50% RH then saturates; at high frequencies α increases monotonically with RH

## Methods / results / takeaways
- Calculations: all using ISO 9613-1 formula; plotted for five frequencies as function of T, RH, and P.
- Fig. 1a (α vs T, σ=60%, p=1 atm): log-scale; 50 kHz shows local max around 45°C; 1 MHz increases steeply at high T.
- Fig. 2, 3 (linear scale detail at 50/100 kHz and 500 kHz/1 MHz): confirms peak positions and values.
- Fig. 4 (α vs T from −50°C to +100°C): negative T → lower α; all frequencies below room-temperature values at −50°C.
- Fig. 5 (α vs T at two RH levels 20% and 60%): at 1 MHz, difference between 20% and 60% RH can be up to 30 dB/m at ~70°C.
- Fig. 6 (α vs pressure at three frequencies): strong decrease of α with increasing P at low frequencies; less so at 1 MHz.
- Practical recommendation for 1 MHz: variation 20→40°C gives 8 dB/m extra loss; hold humidity ~70% for minimum α at 1 MHz.
- Limitation: calculation only (no experimental validation in this paper); uses ISO 9613-1 which was validated for audio/low-ultrasonic; Bond 1992 may be more accurate above ~500 kHz.
