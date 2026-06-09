# KLM Transducer Model

**Aliases:** Krimholtz-Leedom-Matthaei model; Desilets model; transmission-line transducer model; KLM equivalent circuit; piezoelectric equivalent circuit

**Definition:** The KLM model (Krimholtz, Leedom, and Matthaei, 1970) is a one-dimensional equivalent circuit for a piezoelectric transducer element. It represents the piezoelectric disc as two acoustic transmission-line sections (representing the two faces) coupled at a central plane to the electrical port via a transformer; the electrical side contains a clamped capacitance C₀ in series with a frequency-dependent reactive element. The model enables analytical and circuit-simulation design of matching layers, backing layers, and electrical tuning for broadband transducers, and correctly predicts the radiation impedance and resonance structure.

**Key relations:**
- [piezoelectric-constants](piezoelectric-constants.md) — model parameters (kt, ε33S) come from piezoelectric constants
- [acoustic-impedance-matching-layer](acoustic-impedance-matching-layer.md) — KLM guides matching layer design
- [quarter-wavelength-matching-layer](quarter-wavelength-matching-layer.md) — λ/4 layer designed from KLM model
- [resonant-frequency](resonant-frequency.md) — KLM predicts the thickness-mode resonance
- [pzt-hard-soft](pzt-hard-soft.md) — model parameters depend on PZT grade

**Discussed in:**
- [2004 Acoustic Impedance Matching Piezoelectric Transducers Air](../notes/000000-read-papers-with-notes/2004-acoustic-impedance-matching-piezoelectric-transducers-air-gomez.md) — uses KLM model to design multi-layer matching stacks for air coupling
