# Broad-Band Coupling to High-Q Resonant Loads

- **Source:** 1972 - Broad-band coupling to high Q resonant loads - Reeder.pdf
- **Drive link:** https://drive.google.com/file/d/1DOY33NbvPoqbiHGz73EoXX-3IzLnu2xo/view
- **Type:** paper
- **Author/Year:** Thomas M. Reeder, William R. Sperry / 1972
- **Coverage:** full

## Overview
Analyses the bandwidth-loss characteristics of a transmission line (quarter-wave inverter) coupling network connecting a resistive source to a high-Q series resonant load. Shows analytically and numerically that, by appropriate choice of inverter impedance ZI, either maximally flat or ripple insertion-loss response can be obtained, and the resulting 3-dB bandwidth is always greater than 1/Q. Provides design curves and lumped element approximations for practical implementation.

## Unique contribution
Shows that a single quarter-wave transmission line inverter can provide broad-band coupling to a high-Q resonant load, and that the bandwidth-loss characteristic is within ~1.1 dB of the theoretical Bode-Fano optimum for bandwidths up to 100%. This is a much simpler network than the multi-element networks previously required for broad-band matching of high-Q loads (ferrite circulator, microwave transistor, thin-film transducer).

## Key concepts
- Transmission line (quarter-wave) inverter coupling network
- High-Q resonant load matching
- Maximally flat vs ripple insertion-loss response
- Bode-Fano bandwidth-loss integral constraint
- Inverter impedance ZI selection
- Series resonant load parameters (r = R/Z₀, Q)
- Smith chart impedance locus analysis
- Lumped element π-network approximation

## Methods / results / takeaways
- Network: lossless quarter-wave TL of impedance ZI; load Z_L(f) = r[1 + jQ(f/fR − fR/f)]; source Z₀
- Approximate analysis around resonance: insertion loss L(Δ) ≈ L_R(1 + m₂Δ² + m₄Δ⁴); m₂=0 gives maximally flat condition, m₂>0 gives monotonic response, m₂<0 gives ripple
- Maximally flat condition: ZI always > Z₀ for all r and Q; ZI increases monotonically with r and Q
- Bandwidth results: for r≈1, bandwidth ≈ 4/Q (Q=5), 6/Q (Q=10), 8/Q (Q=20) at maximally flat condition
- Bandwidth-loss comparison with Bode-Fano ideal: TL inverter is never more than 1.1 dB above ideal for w < 100%; difference is only 0.25 dB at octave bandwidth (w=0.67) and Q=10
- Lumped π-section approximation: 4-section π-network represents TL to within 10% of impedance and phase over 0–2fR range; 1-section adequate for non-critical applications
- Application context: also applied to thin-film acoustoelectric transducers — relevant to piezoelectric transducer electrical matching
