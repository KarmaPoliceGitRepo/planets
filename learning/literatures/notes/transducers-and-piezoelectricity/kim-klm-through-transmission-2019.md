# Application of KLM Model for an Ultrasonic Through-Transmission Method

- **Source:** 2019 - Application of KLM model for an ultrasonic through-transmission method - Kim.pdf
- **Drive link:** https://drive.google.com/file/d/1khNC79_u9mh7RsRJpQKK0KhjVOGWyQoF/view
- **Type:** paper
- **Author/Year:** Geonwoo Kim, Mu-Kyung Seo, Namkyoung Choi, Kwang Sae Baek, Ki-Bok Kim / 2019
- **Coverage:** full

## Overview
Extends the KLM equivalent circuit model, normally used for single-transducer pulse-echo systems, to the two-transducer ultrasonic through-transmission method. Derives a combined transfer matrix chain (Tx transducer + test specimen + Rx transducer) and validates it by fabricating a 2.25 MHz transmitter and 1 MHz receiver (different resonance frequencies) and comparing simulated and measured time-domain waveforms and frequency spectra.

## Unique contribution
First explicit derivation of the KLM model for a pitch-catch (through-transmission) system with transmitter and receiver at different resonant frequencies. Shows that two distinct peak frequencies appear in the FFT spectrum corresponding to the resonances of each transducer, with the receiver resonance being more dominant in the output signal. The frequency bandwidth is well predicted (60% at −6 dB) even though the time-domain pulse duration shows ~0.6 μs discrepancy due to scattering in the backing material.

## Key concepts
- KLM through-transmission model (pitch-catch)
- Transmit transfer function H_t(p) and receive transfer function H_r(p)
- Combined transfer function H_TR(p) = H_t × H_r
- Transfer matrices: backing (N_b), piezo element (N_6), bonding layer (N_7), matching layer (N_8), water couplant (N_9), test specimen (N_S)
- Total matrix N_TR = N_T × N_S × N_R
- Spike pulse excitation model
- −6 dB bandwidth measurement
- Alumina ceramic front matching layer (Z ≈ 40 MRayl)
- Tungsten-epoxy backing (Z = 8 MRayl)

## Methods / results / takeaways
- Transducer parameters: Tx 2.25 MHz PZT C-62, Rx 1 MHz PZT C-62 (same k_t=0.5); alumina matching layer (Z=40 MRayl, t=1.1 mm Tx / 2.5 mm Rx); backing Z=8 MRayl
- Test specimen: 30 mm thick SUS 304 steel (Z_s=45 MRayl), water couplant coupling
- Spike pulse modelled by: Exc(t) = V_∞ exp[−(α₁−αₜ₀)t] with rise time t₀=0.01 μs, α₁=0.001, α₂=0.02, V₀=−150 V
- Two FFT peaks: ~1.25 MHz and ~1.85 MHz in both simulation and experiment; bandwidth ~60% in both cases — good frequency agreement
- Time-domain pulse duration: simulation ~1.6 μs, experiment ~2.2 μs — ~0.6 μs discrepancy attributed to scattering effects in tungsten-epoxy backing (not captured in 1D model) and case-induced vibration restriction
- Conclusion: KLM through-transmission model correctly predicts frequency response but not exact time-domain waveform; FEM needed for complete accuracy
