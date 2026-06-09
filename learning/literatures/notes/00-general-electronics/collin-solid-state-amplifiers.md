# Foundations for Microwave Engineering — Solid-State Amplifiers (Chapter 10)

- **Source:** SolidState Amplifiers.pdf
- **Drive link:** https://drive.google.com/file/d/10D_8UE24xagZkCClZ-yKFnbWPHA7dH9R/view?usp=drivesdk
- **Type:** book (chapter)
- **Author/Year:** Robert E. Collin, 2001
- **Coverage:** partial (large file, truncated extraction)

## Overview
Chapter 10 covers solid-state microwave amplifiers based on transistors (bipolar junction transistors, BJTs; and field-effect transistors, FETs, particularly GaAs MESFETs). Develops the small-signal equivalent circuit model, stability theory (Rollett stability factor K), gain expressions, and noise figure analysis. Covers the practical design of LNAs and PAs.

## Unique contribution
Provides the connection between device physics (equivalent circuit parameters), S-parameter characterization, and the Smith-chart-based design methodology for microwave amplifiers. Treats noise temperature and noise figure in the context of the transistor's inherent noise sources.

## Key concepts
- GaAs MESFET, BJT small-signal models
- S-parameter characterization of transistors
- Stability: K-factor, Rollett condition (K > 1, |Δ| < 1 for unconditional stability)
- Transducer gain GT = |S21|² × (1–|ΓS|²)(1–|ΓL|²) / |(1–S11ΓS)(1–S22ΓL) – S12S21ΓSΓL|²
- Maximum available gain (MAG), maximum stable gain (MSG)
- Noise figure (NF), equivalent noise temperature T_e
- LNA design: simultaneous noise and gain matching
- Power amplifier (PA): compression point, 1-dB P1dB, IP3

## Methods / results / takeaways
- Rollett stability factor K = (1 – |S11|² – |S22|² + |Δ|²) / (2|S12·S21|); K > 1 and |Δ| < 1 means unconditionally stable.
- MSG = |S21/S12| applies when K < 1; MAG = (|S21|/|S12|)(K – √(K²–1)) when K > 1.
- Minimum noise figure NFmin is a device parameter; it is achieved with a specific source reflection coefficient Γopt, not necessarily the conjugate-match Γopt*_in.
- LNA design: balance between NFmin (from noise circles) and gain (from gain circles) on the Smith chart using the noise figure and gain circle overlay technique.
- PA: the 1-dB compression point P1dB is ~10 dB below IP3 (intercept point of 3rd order IMD); a PA is typically backed off 5–6 dB from P1dB for linear operation.
