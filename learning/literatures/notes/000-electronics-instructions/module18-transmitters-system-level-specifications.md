# Module 18 – Transmitters: System-Level Specifications

- **Source:** module18 - Transmitters System Level Specifications.pdf
- **Drive link:** https://drive.google.com/file/d/1bEg3RQE6RjVu740ev3x8V4QnPF7wHsgD/view
- **Type:** slides
- **Author/Year:** Prof. Ali M. Niknejad, UC Berkeley / 2015
- **Coverage:** full

## Overview
Lecture slides (65 pages) covering the full transmitter chain from baseband digital data to radiated RF signal. Topics include duplex modes (FDD/TDD), I/Q modulation, digital modulation schemes, PA specifications, error vector magnitude (EVM), adjacent channel power (ACP), and transmit spectral masks.

## Unique contribution
Provides a complete end-to-end view of transmitter system specifications translating from air-interface standards (e.g., GSM, WCDMA) to block-level requirements for the DAC, baseband filter, IQ modulator, and PA — bridging standards documents to circuit design targets.

## Key concepts
- Transmitter architecture
- FDD / TDD / half-duplex
- I/Q modulator
- BPSK / QPSK / QAM constellations
- Peak-to-average ratio (PAR / PAPR)
- Power added efficiency (PAE)
- Error vector magnitude (EVM)
- Adjacent channel power (ACP)
- Transmit spectral mask
- Power control
- VSWR stability

## Methods / results / takeaways
- Transmitter chain: data → DAC → baseband filter → I/Q upconversion → PA → antenna.
- FDD: simultaneous TX/RX on different frequencies; requires duplexer with high TX-to-RX isolation (~50 dB) to prevent PA output from desensitizing the receiver.
- TDD: TX and RX alternate in time; simpler RF front-end; used in many modern systems (WiFi, LTE TDD, 5G NR).
- PAPR: OFDM and QAM signals have high PAPR (up to 10–12 dB); PA must be backed off from P−1dB by the PAPR to avoid distortion → efficiency drops significantly.
- PAE = (Pout − Pin)/PDC = ηc · (1 − 1/Gp); high PAE requires both high drain efficiency and high power gain.
- EVM: measures IQ modulator accuracy; EVM² = (magnitude error)² + (phase error)²; typical spec < −30 dB (3.2%) for QPSK.
- ACP (adjacent channel power): spectral regrowth from PA nonlinearity must be below the transmit mask; related to IM3 products.
- Power control: dynamic range of PA output varies from minimum to maximum; efficiency at low power is poor for Class A; envelope tracking or polar modulation helps.
- GSM transmit mask: very strict near-channel spectral requirements (−30 dBc at 400 kHz, −60 dBc at 600 kHz offset).
