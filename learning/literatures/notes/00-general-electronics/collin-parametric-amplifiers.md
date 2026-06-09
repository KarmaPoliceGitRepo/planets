# Foundations for Microwave Engineering — Parametric Amplifiers (Chapter 11)

- **Source:** Parametric Amplifiers.pdf
- **Drive link:** https://drive.google.com/file/d/1J6J_E2I71EEAoGMQDDLhjnpdUafK83vG/view?usp=drivesdk
- **Type:** book (chapter)
- **Author/Year:** Robert E. Collin, 2001
- **Coverage:** partial (large file, truncated extraction)

## Overview
Chapter 11 covers parametric amplifiers — low-noise microwave amplifiers that use a time-varying (pumped) reactance (typically a varactor diode) to transfer power from a pump frequency to a signal frequency. These devices were important before low-noise transistors became available and are still used in cryogenic receiver front-ends for radio astronomy and quantum computing.

## Unique contribution
Provides the theoretical treatment of parametric amplification from Manley-Rowe power relations, deriving gain and noise conditions. Shows that non-degenerate parametric amplifiers can achieve noise temperatures limited only by quantum noise in the ideal case.

## Key concepts
- Manley-Rowe power relations for nonlinear reactances
- Varactor diode (voltage-variable capacitance)
- Parametric up-converter and down-converter
- Non-degenerate parametric amplifier: signal frequency fs, pump fp, idler fi = fp – fs
- Degenerate parametric amplifier: fi = fs (fi = fp/2)
- Negative-resistance amplifier (parametric)
- Noise temperature of parametric amplifiers

## Methods / results / takeaways
- Manley-Rowe relations state that power conservation at nonlinearly mixed frequencies is determined by the ratio of the frequencies involved: Pmn/(m·fs + n·fp) = const.
- In a non-degenerate paramp (with separate pump, signal, and idler circuits), gain is Gs ∝ (fp/fs – 1); higher pump-to-signal frequency ratios give higher gain.
- Noise temperature: a non-degenerate paramp can achieve T_noise ≈ T_idler × (fs/fi) which approaches zero as T → 0 (cryogenic operation).
- Degenerate paramps (fp = 2fs) are phase-sensitive (squeezing); useful for noiseless amplification in one quadrature at the cost of amplifying noise in the other.
- Modern applications: microwave SQUID amplifiers and Josephson parametric amplifiers in quantum computing use the same Manley-Rowe principles.
