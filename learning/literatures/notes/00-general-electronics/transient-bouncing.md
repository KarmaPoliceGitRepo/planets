# Transient Bouncing on Transmission Lines

- **Source:** TransisentBouncing.pdf
- **Drive link:** https://drive.google.com/file/d/1qJTM0cNmKjsD1NKOPrcP4tTJfjOgjgyw/view?usp=drivesdk
- **Type:** notes
- **Author/Year:** Ang Man Shun, September 24, 2013
- **Coverage:** full

## Overview
A compact derivation note on the transient bouncing phenomenon on a transmission line before steady state is reached. Considers a source driving a line with a load, accounting for reflection at both ends (source reflection coefficient ΓA and load reflection coefficient ΓB), and sums the geometric series to find the final forward and backward wave amplitudes.

## Unique contribution
Shows that the infinite series of bouncing wave components sums to a closed form, and explicitly derives V+ and V– in terms of the initial incident voltage and the product ΓAΓB, revealing that steady state is reached exponentially quickly when |ΓAΓB| < 1.

## Key concepts
- Transient reflection and transmission on transmission lines
- Source reflection coefficient ΓA, load reflection coefficient ΓB
- Geometric series summation: 1/(1–ΓAΓB)
- Forward wave V+ and backward wave V–
- Steady-state voltage distribution

## Methods / results / takeaways
- The initial wave VIn splits at the source-load boundary; reflected waves bounce back and forth, each scaled by ΓAΓB per round trip.
- Summing the geometric series: V+ = VIn/(1–ΓAΓB) and V– = –VIn·ΓB/(1–ΓAΓB).
- VIn = VI·(2Z0·RL / (Z0 + RL)) is the initial transmitted voltage at the source end.
- The denominator (1–ΓAΓB)⁻¹ = (Z0+RL)·(RL+Z0·RL) / (4Z0·RL) simplifies to the expected Thevenin voltage divider at steady state.
- This result is equivalent to the steady-state phasor analysis — the transient bouncing is just the time-domain picture of the same physics.
