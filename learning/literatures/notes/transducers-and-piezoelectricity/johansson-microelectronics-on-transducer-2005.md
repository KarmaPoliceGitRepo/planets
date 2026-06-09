# Microelectronics Mounted on a Piezoelectric Transducer

- **Source:** 2005 - Microelectronics mounted on a piezoelectric transducer - Method, simulations, and measurements - (2005) J Johansson.pdf
- **Drive link:** https://drive.google.com/file/d/14w5KWn8llyPcHGSznhp_mn3FzruBuimF/view
- **Type:** paper
- **Author/Year:** Johansson, Delsing / 2005
- **Coverage:** partial

## Overview
Describes a highly integrated ultrasound sensor where an ASIC driver stage is mounted directly on the piezoelectric ceramic transducer using wire bond technology. Eliminates interconnect wiring between driver and transducer for a compact, low-power portable ultrasound sensor.

## Unique contribution
First demonstration of direct-mount ASIC on piezoelectric transducer via wire bonding. Achieves 95–130 µW power consumption at 1 kHz repetition frequency for a 4.4 MHz, 16 mm diameter transducer — enabling very long battery life for portable sensing applications.

## Key concepts
- Integrated ultrasound sensor
- ASIC on piezoelectric transducer
- Wire bond technology
- Low power consumption
- Capacitive model of piezoelectric transducer
- SPICE simulation
- Pulse-echo operation
- Portable ultrasound sensor

## Methods / results / takeaways
- ASIC driver mounted directly on 4.4 MHz PZT disc (16 mm diameter) via wire bonding; no coaxial cable between driver and transducer
- Power consumption: 95–130 µW at 1 kHz repetition rate; scales linearly with repetition frequency
- System modelled using SPICE with transistor-level driver model + capacitive transducer model
- Pulse width optimization: optimal pulse width balances excitation completeness against power consumption
- Simulations and measurements agree closely for power consumption and echo energy vs. pulse width
- Eliminates need for broadband matching networks between driver and transducer
- Significant improvement in pulse control compared to cable-connected designs
- Target application: portable, battery-operated flow metering or ranging with very low duty cycle
- (Note: source text partially retrieved; detailed circuit data not fully available)
