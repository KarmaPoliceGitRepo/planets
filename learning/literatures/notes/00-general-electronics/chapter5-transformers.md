# Chapter 5: Transformers

- **Source:** CHAPTER5.pdf
- **Drive link:** https://drive.google.com/file/d/1Jviruph_nrzLZRe7YpzJFol0FI6iuwjH/view?usp=drivesdk
- **Type:** notes (lecture slides / course notes)
- **Author/Year:** Unknown instructor, ~2021 (file modified 2021-07-05)
- **Coverage:** full

## Overview
A comprehensive set of lecture notes covering transformer theory from first principles to practical design. Topics span from the ideal transformer (turns ratio, voltage/current/impedance relationships) through real transformer equivalent circuits, efficiency, voltage regulation, K-factor ratings, and three-phase configurations. Appears to be university-level electrical engineering course material.

## Unique contribution
Provides side-by-side treatment of autotransformers vs. isolation transformers, explains the K-factor rating concept for nonlinear (harmonic-producing) loads, and walks through the open-circuit and short-circuit test procedures for extracting equivalent circuit parameters.

## Key concepts
- Turns ratio, step-up/step-down transformer
- Faraday's law, universal EMF equation
- Reflected (referred) impedance
- Exciting current, magnetizing current, core-loss current
- Equivalent T-circuit, cantilever equivalent circuit, series equivalent circuit
- Open-circuit test, short-circuit test
- Transformer efficiency, copper losses, core losses (hysteresis, eddy currents)
- Voltage regulation
- K-factor-rated transformer, harmonic content
- Autotransformer (advantages: higher kVA, cheaper; disadvantages: no isolation)
- Three-phase transformer connections: WYE-WYE, Delta-Delta, WYE-Delta, Delta-WYE

## Methods / results / takeaways
- Ideal transformer: V1/V2 = N1/N2; I1/I2 = N2/N1; reflected impedance scales as (N1/N2)^2.
- Exciting current is typically 1–5% of rated primary current; it is non-sinusoidal due to the nonlinear B-H curve, but its RMS value is used for calculations.
- The cantilever model moves the magnetizing branch to the primary terminal, simplifying calculation at the cost of slight inaccuracy in the voltage drop.
- Short-circuit test (low-side shorted, voltage applied to high side until rated current flows at ~4–7% rated voltage) yields Req and Xeq; open-circuit test (rated voltage applied to low side) yields Rc and Xm.
- Voltage regulation = (VNL – VFL) / VFL × 100%. Poor regulation is deliberately used in discharge lighting and arc welders.
- K-factor = Σ h² × (Ih/IRMS)²; a K-4 transformer handles 4× normal eddy-current loss.
- WYE-WYE connection has third-harmonic issues unless neutral is grounded; Delta-Delta avoids this but insulation must be rated for line-to-line voltage.
- WYE-Delta and Delta-WYE introduce a 30° phase shift; US convention has secondary lag the primary by 30°.
