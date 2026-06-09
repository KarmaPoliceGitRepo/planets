# A New Type of Matching Layer for Air-Coupled Ultrasonic Transducers

- **Source:** Toda new type matching layer 2002
- **Drive link:** https://drive.google.com/file/d/19wWWtpGSRbX28NqWOeFNSDvqDdm4thZu/view
- **Type:** paper (IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control 49(7), 972–979, 2002)
- **Author/Year:** M. Toda / 2002
- **Coverage:** full

## Overview
Proposes a new matching layer concept for air-coupled piezoelectric transducers based on a reflective thin film (or perforated plate) at a specific distance from the transducer face. Unlike conventional quarter-wave layers, this design uses the acoustic interaction between a resonant PZT plate and a reflective element placed at distance d₁ from the transducer to achieve impedance conversion. Demonstrated at 40 kHz with a 12 μm polyethylene film achieving 9.5 dB acoustic pressure gain and a holed PCB plate achieving 9.7 dB. Theoretical maximum ≈ 10 dB.

## Unique contribution
Derives the impedance conversion formula Zin1 ≈ (4/π)ZmQm for a resonant vibrating plate interacting with a reflective element. This shows that air-coupled acoustic output can be boosted without a conventional solid matching layer material. Establishes the maximum achievable acoustic pressure gain is ≈10 dB (factor ~3.16×) regardless of material choice, limited by the mechanical Q of the transducer. Also introduces the holed-plate design as a practical, manufacturable alternative to thin polymer films.

## Key concepts
- Transducer model: PZT resonant plate with radiation impedance ZR = ω₀M/Qm; Qm = mechanical Q
- Impedance conversion: Zin1 ≈ (4/π)ZmQm where Zm = mechanical impedance of transducer plate
- Condition for validity: (4/π)Z₁Qm << Zm (radiation must be small compared to mechanical)
- Transducer radiation impedance: ZR = 1.88×10⁴ kg/m²s (measured, 40 kHz PZT element)
- Thin film implementation: 12 μm polyethylene film at d₁ = 0.23 mm from transducer face
- PE film result: 9.5 dB acoustic pressure gain at 40 kHz
- Holed plate implementation: 1.5 mm thick PCB with 1 mm diameter holes at d₁ optimized
- Holed plate result: 9.7 dB acoustic pressure gain at 40 kHz
- Maximum theoretical gain: ≈ 10 dB (independent of matching layer material)
- Design frequency: 40 kHz (standard air-coupled ranging/sensing frequency)
- Air gap d₁: set to create standing wave condition enhancing radiation coupling

## Methods / results / takeaways
- Transducer: commercial 40 kHz PZT air-coupled element; measured Zm and Qm
- Thin film: 12 μm PE stretched across aperture; d₁ = 0.23 mm spacing from transducer
- Holed plate: 1.5 mm PCB (FR4 equivalent); 1 mm holes; d₁ optimized experimentally
- Measurement: acoustic pressure at fixed distance; relative gain vs bare transducer
- Results: PE film → 9.5 dB; holed plate → 9.7 dB (both near theoretical 10 dB max)
- Bandwidth: moderate reduction vs unmatched (not quantified precisely); holed plate wider than film
- Practical advantage: no special low-Z material needed; simple construction
- Limitation: narrow air gap must be precisely maintained; fragile thin film prone to damage
- Application: low-cost improvement of standard 40 kHz air-coupled transducers for ranging and proximity sensing
