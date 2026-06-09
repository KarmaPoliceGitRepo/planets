# New Approach for Air-Coupled Ultrasonic Transducers Using Corrugated PVDF Film

- **Source:** Toda Dahl PVDF corrugated ranging 2007
- **Drive link:** https://drive.google.com/file/d/1glVglBGMl5ZNGMz2xnkPPWQ0vPI5Nw3l/view
- **Type:** paper (Sensors and Actuators A 134, 427–435, 2007)
- **Author/Year:** M. Toda, M. Dahl / 2007
- **Coverage:** full

## Overview
Proposes and demonstrates a corrugated PVDF film transducer design for 200 kHz air-coupled ranging. The corrugated structure reduces the mechanical resonance frequency dramatically compared to a flat film, making PVDF practical at audio/ultrasonic frequencies without thick backing layers. A complete analytical model is developed for resonant frequency, acoustic output pressure, and directivity. A prototype 11 mm diameter, 3-period corrugated transducer demonstrates 6.6 Pa rms output at 30 cm with 160 Vpp drive and 0.55 mV/Pa receiver sensitivity.

## Unique contribution
Derives a closed-form model for corrugated PVDF transducer resonance frequency, acoustic output, and sensitivity that accurately predicts experimental results. Shows that corrugation reduces effective stiffness by a factor R²/(H²+R²) relative to flat-membrane tension, enabling 200 kHz resonance with standard 28 μm PVDF film and 1.0 mm corrugation radius. Demonstrates single-transducer TX/RX operation using a diode TR switch, achieving ranging capability with a flat (piston-like) beam pattern.

## Key concepts
- Resonance frequency: f₀ = (1/2πR)√(Y/ρp) where R = corrugation radius, Y = Young's modulus, ρp = mass/area
- √(Y/ρp) for PVDF with silver ink electrode: 1260 m/s; for bare PVDF: ≈1200 m/s
- Corrugation height: optimal H = 1.238 × (λ₀/2) = 1.238 × (c_PVDF / 2f₀) for thickness mode avoidance
- Reduction factor: 0.809 (velocity × area product relative to ideal piston; accounts for corrugated vs flat displacement)
- Acoustic output: P = 0.809·Q·f₀·ρa·A·√(Y/ρp)·d31·V/(h·D) where D = corrugation period
- Q factor: ≈3 at 200 kHz in air; bandwidth ≈ 33%
- Directivity: ±7° at −6 dB for 11 mm aperture at 200 kHz
- TR switch: PIN diode circuit; allows same transducer to transmit and receive

## Methods / results / takeaways
- Film: 28 μm PVDF with 0.6 μm silver ink electrodes both sides; d31 = 22 pC/N
- Corrugation: R = 1.0 mm radius; period D = 3.68 mm; 3 periods; total diameter 11 mm
- Measured f₀ = 200 kHz (matches model); 3 dB bandwidth 67 kHz (BW ≈ 33%)
- Transmitter: 160 Vpp sinusoidal drive; output 6.6 Pa rms at 30 cm in free field
- Receiver: 0.55 mV/Pa sensitivity at 200 kHz
- TX/RX mode: high-voltage LC resonant driver circuit; diode switch protects preamplifier
- Range measurement: demonstrated distance sensing in air; echo SNR sufficient for ranging
- Comparison: flat PVDF film would resonate at >> MHz range; corrugation enables 200 kHz operation
- Application: robot obstacle sensing, automotive parking sensors, industrial ranging, non-contact measurement
