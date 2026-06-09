# On Wide Frequency Range Airborne Ultrasonic Transducers

- **Source:** Epure 2012 wide frequency EMFIT transducers
- **Drive link:** https://drive.google.com/file/d/1VuSpvSD3JVACw5Ju3S0GYzUknh47dMYG/view
- **Type:** paper
- **Author/Year:** Epure & Aiordachioaie, 2012 (IEEE SIITME 2012)
- **Coverage:** full

## Overview
Fabricates and characterises EMFIT (electromechanical film) airborne ultrasonic transducers with gold electrodes (vs. conventional aluminium) for operation at 50–200 kHz. Tests frequency response and directivity. Resonance around 150 kHz; main lobe width narrows from 6.1° to 3.81° as frequency increases from 100 to 175 kHz.

## Unique contribution
Gold-electrode EMFIT transducers offer improved manufacturing flexibility (better electrical contact, corrosion protection) vs. aluminium-electrode variants. Documents resonant behavior, frequency limits, and directivity for 50–200 kHz range with realistic COTS construction.

## Key concepts
- EMFIT (electromechanical film) transducer
- Gold vs. aluminium electrodes
- Wideband airborne ultrasound 50–200 kHz
- Directivity pattern
- Circular piston model (J1 Bessel function)
- Resonance ~150 kHz
- Half-bridge driver with step-up transformer

## Methods / results / takeaways
- Film: EMFIT 85 μm thick, gold electrode 0.9 μm / 22 carat; glued to PCB copper ground electrode.
- Preamplifier: OPA2301, 150 MHz BW, 300 kHz BW; receiver RF shielding essential.
- Transmitter: half H-bridge + 1:10 step-up transformer; ICs IR2103 driver.
- Directivity at 100 kHz: main lobe width 6.1°; at 175 kHz: 3.81°; narrowing consistent with piston model.
- Frequency below 100 kHz: transducer does not operate reliably.
- Frequency 160–170 kHz: near upper practical limit due to low sensitivity + high air absorption.
- Air absorption estimated from amplitude difference at 50 vs. 100 cm distance.
