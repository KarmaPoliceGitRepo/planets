# High-Speed Ultrasonic Digital Delay Line Design: A Restatement of Some Basic Considerations

- **Source:** 1968 - High Speed Ultrasonic Delay Line Design- A Restatement of Some Basic Considerations - KE Sittig.pdf
- **Drive link:** https://drive.google.com/file/d/1d24z_EkbIdOUZQ6Pk_KSazhNS6Oik6YL/view
- **Type:** paper
- **Author/Year:** Erhard K. Sittig / 1968
- **Coverage:** full

## Overview
Provides a systematic design procedure for ultrasonic digital delay line stores operating at up to 100 MHz, covering bandpass requirements, transducer configuration, spurious signal suppression, and dimensional optimisation. Derives compatibility conditions linking materials properties (absorption index, coupling factor, impedance ratio) to storage capacity and insertion loss.

## Unique contribution
Derives a fundamental compatibility condition (N = x/x0 × ωmC0 × m) linking storage capacity to delay medium geometry, transducer capacitance, and materials factor m. Shows that 20 dB triple-travel suppression combined with bandpass equalisation is achievable by balancing absorption loss and beam-spreading loss, without necessarily using backing layers. Demonstrates Na-K niobate transducers with fused quartz medium achieving ~14 dB insertion loss at 100 MHz.

## Key concepts
- Ultrasonic delay line digital memory
- Triple travel signal suppression
- Beam spreading and absorption loss equalisation
- Bandpass shape using Fourier series (L=1, L=2 responses)
- Electromechanical coupling factor for bandwidth/loss tradeoff
- Paired echo theory
- Transducer impedance ratio z with delay medium
- Fresnel zone length

## Methods / results / takeaways
- Bandpass requirement: paired-echo theory gives two realisable responses — L=1 (backed transducer, 10 dB extra loss) and L=2 (unbacked) — both provide adequate bandshape at bit rates up to fm
- Key insight: deliberately mismatching delay medium impedance (z=0.5) with high k transducers gives acceptable response and low loss, avoiding backed transducers
- Triple travel suppression from beam spreading alone: max 10 dB far-field; combined with absorption gives 20 dB when LA = x/x0
- Compatibility condition: N = (x/x0) × (1/ωmC0) × m; for fused quartz with NaKNbO3 transducer at 100 MHz: N = 6700 bits at 1/ωmC0 = 1.21 Ω
- Spurious from side-wall reflections suppressed by transducer far-field placement (x/x0 ≥ 1)
- T40 glass with NaKNbO3: N = 670 bits but lower temperature sensitivity
- Materials data table: NaKNbO3 (k=0.6, Z=18.9 MRayl), PZT-7 (k=0.6, Z=17.9 MRayl), ZnO (k=0.3), CdS (k=0.137), quartz Y-cut (k=0.18)
