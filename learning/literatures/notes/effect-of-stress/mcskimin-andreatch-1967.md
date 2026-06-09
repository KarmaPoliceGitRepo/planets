# Measurement of Very Small Changes in the Velocity of Ultrasonic Waves in Solids

- **Source:** McSkimin & Andreatch 1967 velocity measurement
- **Drive link:** https://drive.google.com/file/d/1VG2dOI8v9oswZePut7rieKgUvuWE0lU4/view
- **Type:** paper
- **Author/Year:** H. J. McSkimin & P. Andreatch Jr., 1967
- **Coverage:** full

## Overview
Describes improvements to the automated pulse superposition method for measuring small changes in ultrasonic wave velocity or delay time in solid specimens. The method achieves resolution of approximately 1 part in 10⁷ for high-Q materials with long-term stability over hours. Demonstrates its use to determine third-order elastic moduli of germanium crystals at low uniaxial pressures (<250 psi), verifying consistency with earlier high-pressure (10,000 psi) data.

## Unique contribution
Demonstrates that the pulse superposition technique with automatic frequency control (AFC) can achieve 1:10⁷ resolution in delay-time measurement, far exceeding conventional pulse-echo methods. Shows that TOE constants can be determined with low uniaxial loads (<250 psi), enabling work on specimens that might be damaged by large loads (e.g., single crystals that flow plastically at moderate stress). Provides the circuit design details for practical implementation.

## Key concepts
- Pulse superposition method
- Automatic frequency control (AFC) / servo control
- Third-order elastic moduli (3rd-order stiffness moduli C₁₁₁, C₁₁₂, C₁₂₃, C₁₄₄, C₁₅₅, C₄₅₆)
- Transit time measurement
- Frequency synthesizer for precision repetition rate
- Hydrostatic pressure + low uniaxial stress combination

## Methods / results / takeaways
- Method: repetition rate f_R adjusted so that time T between applied pulses equals twice the round-trip delay time; f_R tracked as stress changes; resolution: ±1 part in 13 million over 3+ hours at constant temperature
- Temperature stability requirement: 60-Hz source frequency modulated for AFC error signal; servo motor adjusts synthesizer vernier; 115V line voltage controlled to ±0.5V
- Stability test: AT-cut quartz unit at 23.6±0.01°C; f_R varied only ±1 in 1.3×10⁷ over 3+ hours
- Germanium experiments: shear waves in various crystallographic directions at <250 psi uniaxial stress; 10 modes measured
- Results for Ge (3rd-order moduli at 25°C, units 10¹² dyne/cm²): C₁₁₁ = −7.1±0.1, C₁₁₂ = −3.89±0.03, C₁₂₃ = −0.18, C₁₄₄ = −0.23, C₁₅₅ = −2.92, C₄₅₆ = −0.53 (consistent with Ref. 5 values from 10,000 psi)
- Combination of hydrostatic and low uniaxial pressure data: yields all six 3rd-order moduli with good accuracy
- Silicon: beam spreading effects at 20 MHz made measurements unreliable; 60 MHz gave better results
- Practical tip: thin polystyrene fluid between specimen and steel pressure blocks minimizes spurious edge effects
