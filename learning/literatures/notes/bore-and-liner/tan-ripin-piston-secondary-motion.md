# Analysis of Piston Secondary Motion

- **Source:** Analysis of piston secondary motion (Tan & Ripin, J Sound Vib 332, 2013)
- **Drive link:** https://drive.google.com/file/d/1sOaesdcgE1nVihw_WGnv9kGRPwTwFIDd/view
- **Type:** paper
- **Author/Year:** Tan, Ripin / 2013 (Journal of Sound and Vibration 332, pp. 5162–5176)
- **Coverage:** full

## Overview
Develops a nonlinear 3-DOF lumped-parameter model (reciprocating + lateral + rotational) for piston secondary motion in an IC engine. The piston–liner gap is modelled as a translational hard stop with high stiffness and damping during impact. Model parameters (mass, damping, stiffness; contact stiffness and damping) are obtained from mobility measurements using impact hammer and accelerometers. Validated against three laser displacement sensors capturing distinct lateral and rotational modes of the piston under motorised conditions.

## Unique contribution
Introduces a translational hard-stop nonlinearity to capture piston slap impact and couples it with speed-dependent ring friction to predict both piston secondary motion waveform and the induced vibration amplitude of the cylinder block. Unlike prior models, model parameters are derived experimentally from mobility measurements, not assumed or FEM-derived.

## Key concepts
- Piston secondary motion (lateral translation + rotational)
- Piston slap; translational hard stop (nonlinear impact model)
- Lumped parameter model (3-DOF)
- Mobility measurement; contact resonance
- Laser displacement sensor validation
- Ring-groove friction force; speed-dependent friction coefficient
- Cylinder block vibration induced by piston slap
- Chaotic vs periodic piston dynamics

## Methods / results / takeaways
- 3-DOF equations: reciprocating (primary), lateral (y), and rotational (θ) about piston pin. Hard-stop adds contact stiffness 20×10⁶ kg s⁻² and damping 1000 kg s⁻¹ when gap is exceeded.
- Parameters extracted from mobility: piston mass 0.2 kg, damping 130 kg s⁻¹, stiffness 50 kN m⁻¹; cylinder block mass 10 kg, stiffness 1.9 MN m⁻¹. Contact resonance at 177 Hz.
- Friction coefficient between ring and liner determined by fitting model to measured friction force at 500 rpm.
- Validation at 500 rpm shows predicted lateral motion trend and cylinder block vibration amplitude (~1×10⁻⁵ m vs measured ~1.2×10⁻⁵ m) in good agreement.
- Parametric study: increasing engine speed → more vigorous piston bouncing, higher induced vibration, shift from periodic to chaotic; increasing oil film damping → longer sliding duration, lower impact; higher ring stiffness → longer sliding duration, slightly lower cylinder block vibration amplitude.
- At low speeds, piston slides along liner with few rebounds; at high speeds, bouncing is vigorous and chaotic.
- Piston secondary motion contributes to 30–50% of total mechanical losses in IC engines.
