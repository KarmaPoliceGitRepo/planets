# Long-Range Ultrasonic Range Sensor with High-Power Transducer Array

- **Source:** Kumar & Furuhashi 2017 long-range system
- **Drive link:** https://drive.google.com/file/d/1mGwkp3-HMscdxFBEE5rSB7yYJaLWPc1V/view
- **Type:** paper
- **Author/Year:** Kumar & Furuhashi, 2017
- **Coverage:** full

## Overview
Presents a 12×12 element (144-element) 40 kHz ultrasonic transducer array providing +30 dB gain over a single transducer, enabling ranging up to 25 m — significantly beyond the 5–10 m of single-element systems.

## Unique contribution
Demonstrates that a large-aperture coherent array of standard 40 kHz transducers provides sufficient directivity and power to extend reliable TOF ranging to 25 m in open air, with explicit characterisation of SNR improvement vs array size.

## Key concepts
- Ultrasonic transducer array
- 40 kHz air-coupled ranging
- Array gain / beamforming
- Long-range ranging (25 m)
- SNR improvement
- Phased array acoustics

## Methods / results / takeaways
- Array: 12×12 = 144 elements at 40 kHz, λ/2 spacing.
- Array gain: +30 dB compared to single transducer element (coherent summation).
- Maximum reliable range: 25 m (single element: ~5 m at same SNR threshold).
- Beam pattern: narrow main lobe, enabling directional ranging and clutter rejection.
- TOF extracted by threshold detection after envelope detection.
- Temperature compensation via on-board temperature sensor.
- Practical constraint: large physical aperture (~12 cm × 12 cm) not suitable for compact applications.
- Key insight: array gain follows 20 log₁₀(N) for coherent transmit; 10 log₁₀(N) for incoherent receive — full coherent array gives 10 dB better than incoherent sum.
