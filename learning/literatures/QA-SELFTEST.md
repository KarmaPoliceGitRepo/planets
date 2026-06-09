# QA Self-Test: Ultrasound & Acoustics — 12 Exam Questions

Grounded in the concepts/ pages and notes/ of this knowledge base.
Relative links are from this file's location (`learning/literatures/`).

---

## Q1 — Acoustoelasticity: stress measurement by velocity shift

**Q.** A steel bolt is loaded in tension. Explain the physical mechanism by which an ultrasonic longitudinal wave can be used to infer the axial stress, and state the governing relation.

**A.** When a solid is pre-stressed, the effective elastic constants seen by a propagating wave are altered through the third-order elastic (TOE) terms in the strain-energy expansion (Murnaghan constants l, m, n). The resulting fractional velocity shift is linear in stress to first order: Δv/v₀ = K·σ, where K is the acoustoelastic coefficient that depends on wave mode, propagation direction, and the material's second- and third-order elastic constants. Hughes & Kelly (1953) derived the explicit expressions for longitudinal and shear modes under uniaxial stress from Murnaghan's TOE potential. In practice a pulse-echo time-of-flight measurement is made under known reference load and then under service load; the TOF difference, combined with K obtained from calibration, yields the stress. The method is used in bolt and bearing load measurement (Chen & Mills 2015).

**Sources:**
- [concepts/acoustoelastic-effect.md](concepts/acoustoelastic-effect.md)
- [concepts/acoustoelastic-coefficient.md](concepts/acoustoelastic-coefficient.md)
- [notes/effect-of-stress/hughes-kelly-1953.md](notes/effect-of-stress/hughes-kelly-1953.md)
- [notes/effect-of-stress/clark-mignogna-1983-two-theories.md](notes/effect-of-stress/clark-mignogna-1983-two-theories.md)

---

## Q2 — Acoustoelasticity: scattering sensitivity vs velocity sensitivity

**Q.** Kube & Turner (2016) argue that backscatter measurements are 10–50× more sensitive to applied stress than phase-velocity measurements. What is the physical reason, and what practical implication does this carry for stress NDE?

**A.** Phase velocity changes due to stress are second-order in the TOE constants and scale as Δv/v ~ K·σ, which for metals is typically of order 10⁻⁴ per MPa — changes of a few tenths of a percent over the entire elastic range. The grain-scattering cross-section, by contrast, depends on the stress-modified covariance tensor of elastic-constant fluctuations N^{abcd}_{ijkl}, and the Born-approximation scattering coefficient varies more steeply because it contains the product of the stress-perturbed moduli. Numerically, for polycrystalline aluminium at 10 MHz and grain radius 15 µm, Kube & Turner report that the qP backscatter parallel to the stress axis changes by +38.8% for 500 MPa compression while phase velocity changes only ~2% over the same range — a ~19× advantage; at large ka (high frequency or large grain size) the backscatter coefficient changes by ±50% vs ±22.5% (roughly 10–50× depending on conditions). The practical implication is that an amplitude-resolved backscatter scan can detect stress levels that would be invisible to a conventional TOF/velocity measurement, provided diffraction corrections and grain-texture effects are controlled.

**Sources:**
- [concepts/acoustoelastic-effect.md](concepts/acoustoelastic-effect.md)
- [concepts/grain-scattering-attenuation.md](concepts/grain-scattering-attenuation.md)
- [notes/effect-of-stress/kube-turner-2016-scattering.md](notes/effect-of-stress/kube-turner-2016-scattering.md)

---

## Q3 — Temperature dependence of velocity: quantitative calibration

**Q.** A steel plate is instrumented with shear-wave transducers for pulse-echo ultrasonic thermometry. The measured V(T) calibration over 25–230°C is described by a linear fit. State the fit, explain the sign of dV/dT, and identify the main source of error in inverting ToF to temperature.

**A.** Wei (2020) report V(T) = −0.4521·T + 3259.9 m/s (R² ≈ 0.999) for steel shear waves in the range 25–230°C, giving dV/dT ≈ −0.45 m/s/°C. The negative gradient arises because increasing temperature softens the shear modulus G faster than thermal expansion increases density; both effects reduce v_S = √(G/ρ). For longitudinal waves in steels the gradient is typically −0.6 to −1.5 m/s/°C. Inverting the calibration to obtain T from a measured ToF requires timing resolution better than ~1 ns per °C of temperature resolution (Wei 2020 show reconstruction degrades above σ_t = 1 ns). The dominant practical errors are: (1) timing uncertainty from digitiser resolution and noise; (2) ray-path bending in non-uniform temperature fields, which elongates the apparent path length and shifts the ToF beyond the 1D prediction; (3) residual stress shifts that mimic a temperature change via the acoustoelastic effect.

**Sources:**
- [concepts/temperature-dependence-of-sound-speed.md](concepts/temperature-dependence-of-sound-speed.md)
- [concepts/ultrasonic-thermometry.md](concepts/ultrasonic-thermometry.md)
- [notes/effect-of-temperature/wei-2020-2d-temperature-reconstruction.md](notes/effect-of-temperature/wei-2020-2d-temperature-reconstruction.md)

---

## Q4 — Grain scattering regimes

**Q.** State the three frequency regimes for ultrasonic grain-scattering attenuation in a polycrystalline metal, give the frequency and grain-size power laws for each, and explain the physical origin of the "Rayleigh–stochastic hump" in longitudinal attenuation.

**A.** In the Rayleigh regime (grain diameter D ≪ λ, i.e. kD ≪ 1) scattering is coherent across the grain and attenuation scales as α ∝ f⁴D³. In the stochastic regime (D ~ λ/10, kD ~ 1) multiple scatterers are resolved and α ∝ f²D. In the geometric (diffuse-field) regime (D ~ λ, kD ≫ 1) attenuation approaches α ∝ 1/D and becomes frequency-independent. Stanke & Kino (1984) showed, using their unified Keller self-consistent theory, that the Rayleigh and stochastic asymptotes for longitudinal waves intersect at kD ≈ 0.17 — well inside the nominal Rayleigh region. Near that transition, most of the scattered energy goes into shorter-wavelength shear modes that are not accounted for by either asymptote alone; the unified solution therefore predicts a "hump" where attenuation lies above both limiting formulas. Papadakis had observed this experimentally in Ni and α-brass without a satisfactory explanation until Stanke & Kino resolved it.

**Sources:**
- [concepts/grain-scattering-attenuation.md](concepts/grain-scattering-attenuation.md)
- [concepts/attenuation.md](concepts/attenuation.md)
- [notes/microstructure/stanke-kino-unified-theory-1984.md](notes/microstructure/stanke-kino-unified-theory-1984.md)
- [notes/microstructure/papadakis-scattering-metals-1965.md](notes/microstructure/papadakis-scattering-metals-1965.md)

---

## Q5 — Oil-film thickness by reflection coefficient

**Q.** Describe how the normal-incidence ultrasonic reflection coefficient is used to measure a thin lubricant film thickness, and state the two distinct operating regimes and their thickness ranges.

**A.** At normal incidence, the reflection coefficient R from a three-medium system (solid / oil film / solid) is frequency-dependent and governed by the acoustic impedances of all three media and the frequency–thickness product f·h. Two regimes are exploited in practice. When the film is sub-resonance (h ≪ λ/4, typically h < ~5 µm at practical frequencies) the layer behaves as a spring: R is controlled by the interfacial stiffness K = Z_oil·c_oil/h, and h is obtained from the measured low-frequency |R| using the spring-model formula. When h is larger (> ~40 µm) the time-of-flight method resolves the front and back reflections as separate echoes and h follows directly from the round-trip ToF and the known oil sound speed. Pialucha & Cawley (1994) showed that the sensitivity is highest when the two bounding solid impedances are equal (R_half peaks), and derived closed-form expressions for R at the resonance and half-resonance frequencies. Dwyer-Joyce (2003) demonstrated both regimes experimentally in lubricated bearing contacts and validated against Dowson–Higginson film-thickness predictions.

**Sources:**
- [concepts/film-thickness.md](concepts/film-thickness.md)
- [concepts/reflection-coefficient.md](concepts/reflection-coefficient.md)
- [concepts/spring-interface-model.md](concepts/spring-interface-model.md)
- [notes/lubrication-film/pialucha-cawley-thin-layers-1994.md](notes/lubrication-film/pialucha-cawley-thin-layers-1994.md)
- [notes/lubrication-film/dwyer-joyce-lubricant-film-ultrasound-2003.md](notes/lubrication-film/dwyer-joyce-lubricant-film-ultrasound-2003.md)

---

## Q6 — Piezoelectric transducer design: KLM model and matching layers

**Q.** Outline how the KLM equivalent-circuit model is used to design a broadband piezoelectric transducer, and state the Desilets–Fraser–Kino formula for the optimum impedance of a single quarter-wave matching layer.

**A.** The KLM model (Krimholtz, Leedom & Matthaei 1970) represents a thickness-mode piezoelectric disc as two acoustic transmission-line sections (front and back halves of the element thickness) coupled at a central plane to the electrical port via a transformer whose turns-ratio encodes the electromechanical coupling kt; the electrical side contains a clamped capacitance C₀ and a frequency-dependent reactive element. Each matching layer or backing is then added as an additional transmission-line section, enabling the complete frequency response to be computed analytically or in a circuit simulator. Desilets, Fraser & Kino (1978) used the KLM model to show that the classical microwave result Z_m = √(Z_PZT · Z_load) (geometric mean) is incorrect for piezoelectric transducers; the corrected single-layer optimum is Z_m = Z_PZT^(2/3) · Z_load^(1/3). For a two-layer stack the impedances are Z_{C1} = Z_0^(4/7)·Z_L^(3/7) and Z_{C2} = Z_0^(1/7)·Z_L^(6/7), grading from the PZT toward the load. With PZT-5A and glass+epoxy matching into water they demonstrated ~65% 3-dB bandwidth and 3.2 dB round-trip insertion loss — one octave. High electromechanical coupling kt is a prerequisite; backing reduces ringdown at the cost of sensitivity.

**Sources:**
- [concepts/klm-model.md](concepts/klm-model.md)
- [concepts/quarter-wavelength-matching-layer.md](concepts/quarter-wavelength-matching-layer.md)
- [notes/transducers-and-piezoelectricity/krimholtz-klm-equivalent-circuits-1970.md](notes/transducers-and-piezoelectricity/krimholtz-klm-equivalent-circuits-1970.md)
- [notes/transducers-and-piezoelectricity/desilets-broadband-piezoelectric-transducer-design-1978.md](notes/transducers-and-piezoelectricity/desilets-broadband-piezoelectric-transducer-design-1978.md)

---

## Q7 — Shear-wave birefringence for stress measurement

**Q.** Explain the birefringence method for measuring in-plane principal stress difference, and state why it is advantageous over single-mode velocity measurement for in-service components.

**A.** When a shear wave propagates perpendicular to a plane containing a biaxial in-plane stress (σ₁, σ₂), it splits into two orthogonally polarised components travelling at slightly different speeds v_fast and v_slow. The fractional velocity difference Δv/v = K_B·(σ₁ − σ₂) measures the principal stress difference directly, where K_B is the birefringence acoustoelastic constant characterised once for the material. The key advantage is temperature immunity: both polarisations traverse the same path through the same temperature field, so common-mode velocity shifts due to temperature cancel identically in the difference Δv; a single-mode velocity measurement would conflate thermal and stress-induced shifts. Birefringence also eliminates the need for a stress-free reference thickness measurement. Clark & Mignogna (1983) compared two theoretical frameworks for the birefringence constant, and Castellano (2017) provides expressions under both Hughes–Kelly and Man–Lu theories for textured metals where texture-induced birefringence must be separated from stress-induced birefringence.

**Sources:**
- [concepts/shear-wave-birefringence.md](concepts/shear-wave-birefringence.md)
- [concepts/acoustoelastic-effect.md](concepts/acoustoelastic-effect.md)
- [notes/effect-of-stress/castellano-2017-hughes-kelly-man-lu.md](notes/effect-of-stress/castellano-2017-hughes-kelly-man-lu.md)
- [notes/effect-of-stress/clark-mignogna-1983-two-theories.md](notes/effect-of-stress/clark-mignogna-1983-two-theories.md)
- [notes/effect-of-stress/si-chaib-2002-bending.md](notes/effect-of-stress/si-chaib-2002-bending.md)

---

## Q8 — Time-of-flight ranging in air

**Q.** What is the principal source of absolute-distance ambiguity in single-frequency ultrasonic ranging in air, and how does the multifrequency AM (vernier) technique resolve it?

**A.** Single-frequency ranging measures the phase of the returned echo modulo 2π, giving unambiguous range only within one half-wavelength (~8.5 mm at 20 kHz in air). At longer distances the phase is ambiguous by an integer multiple of λ/2, so the absolute range cannot be determined without auxiliary information. The vernier (multifrequency AM) technique uses two or more carrier frequencies f₁ and f₂ with a small difference Δf; the modulation envelope has an effective wavelength λ_env = c/Δf much longer than either carrier, providing coarse unambiguous range, while the carrier phase gives fine resolution. Multiple frequency pairs can cascade the unambiguous range further — analogous to a vernier calliper. The phase of the AM envelope is measured from the cross-spectrum of the transmitted and received waveforms. The signal-processing for ultrasonic ranging (gated FFT, bond-layer correction, compound resonator theory) is documented for both air and liquid-coupled systems.

**Sources:**
- [concepts/signal-processing-for-ultrasonic-ranging.md](concepts/signal-processing-for-ultrasonic-ranging.md)
- [concepts/time-of-flight.md](concepts/time-of-flight.md)
- [notes/signal-processing/multifrequency-am-ultrasonic-ranging.md](notes/signal-processing/multifrequency-am-ultrasonic-ranging.md)

---

## Q9 — Dislocation attenuation mechanism

**Q.** Describe the Granato–Lücke string model for dislocation-induced ultrasonic attenuation, state its prediction for amplitude dependence, and explain how cold working and annealing alter the measurement.

**A.** In the Granato–Lücke model, dislocation segments pinned between obstacles (precipitates, jogs) vibrate under an oscillating acoustic stress like a tensioned string. At low acoustic amplitudes the segments do not break away from weak pinning points, giving amplitude-independent (linear) attenuation and a small velocity change (acoustic modulus defect); the attenuation coefficient is α ∝ Λ·L²·f (where Λ is dislocation density and L is mean loop length between pins). At higher amplitudes segments break free from weak pins and the attenuation becomes amplitude-dependent and irreversible — a signature of the breakaway mechanism that underlies acoustic nonlinearity. Cold working increases Λ and reduces L by introducing new pinning points, generally raising low-amplitude attenuation; annealing reduces Λ and increases L, often lowering attenuation but making the material more susceptible to amplitude-dependent effects. Merkulov (1962) provided early experimental confirmation of the Granato–Lücke predictions in NaCl crystals, and Erofeev (2017) extended the model to the nonlinear regime where dislocation breakaway generates harmonics.

**Sources:**
- [concepts/dislocation-and-internal-friction.md](concepts/dislocation-and-internal-friction.md)
- [concepts/attenuation.md](concepts/attenuation.md)
- [notes/microstructure/merkulov-dislocations-nacl-1962.md](notes/microstructure/merkulov-dislocations-nacl-1962.md)
- [notes/microstructure/erofeev-nonlinear-waves-dislocations-2017.md](notes/microstructure/erofeev-nonlinear-waves-dislocations-2017.md)

---

## Q10 — Lamb waves: dispersion and mode selection

**Q.** Explain why Lamb waves in thin plates are inherently dispersive, describe the behaviour of the A₀ and S₀ modes at low frequency–thickness product, and state the Rayleigh–Lamb dispersion relation.

**A.** Lamb waves are dispersive because the plate boundaries impose standing-wave boundary conditions (zero traction at top and bottom surfaces) that couple the wave speed to the plate thickness d through the dimensionless frequency–thickness product f·d. The Rayleigh–Lamb dispersion equation for symmetric modes is tan(qd/2)/tan(pd/2) = −4k²pq/(k²−q²)², and for antisymmetric modes the ratio is inverted; p² = ω²/c_L² − k² and q² = ω²/c_S² − k². At low f·d the A₀ mode is quasi-flexural and dispersive: phase velocity v_ph ∝ (f·d)^(1/2), making short-distance inspection difficult due to pulse spreading. The S₀ mode approaches the bar velocity c_bar = √(E/ρ) and is nearly non-dispersive at low f·d, making it preferred for long-range inspection. Higher-order modes cut on when f·d satisfies the layer resonance condition for shear or longitudinal standing waves across the plate. Croxford (2007) showed that mode selection and frequency choice govern how far damage can be detected; temperature shifts the dispersion curve and must be compensated in SHM applications.

**Sources:**
- [concepts/lamb-wave.md](concepts/lamb-wave.md)
- [concepts/dispersion.md](concepts/dispersion.md)
- [concepts/frequency-thickness-product.md](concepts/frequency-thickness-product.md)
- [notes/surface-acoustic-wave/rayleigh-lamb-waves-basic-principles-worden-2001.md](notes/surface-acoustic-wave/rayleigh-lamb-waves-basic-principles-worden-2001.md)
- [notes/surface-acoustic-wave/strategies-guided-wave-shm-croxford-2007.md](notes/surface-acoustic-wave/strategies-guided-wave-shm-croxford-2007.md)

---

## Q11 — EMATs: generation mechanisms and coil design

**Q.** Explain the two physical mechanisms by which an EMAT generates elastic waves, state which dominates in a non-ferromagnetic conductor, and describe how a meander-line coil selects the generated wave mode and frequency.

**A.** An EMAT generates elastic waves through two mechanisms. In electrically conducting materials, the radio-frequency current in the coil induces eddy currents in the specimen surface (within a skin depth δ = √(2ρ/ωμ)); these eddy currents interact with the static bias field via the Lorentz force J×B, creating a stress distribution that launches elastic waves. In ferromagnetic materials a second mechanism — magnetostriction — contributes: the oscillating field cyclically magnetises the material, and through magnetostrictive coupling (ΔE effect) this creates strain. In non-ferromagnetic conductors (aluminium, copper) only Lorentz force acts; in ferromagnets (iron, nickel) both contribute, with magnetostrictive coupling often dominant. A meander-line coil consists of parallel conductors with spacing equal to half the desired Rayleigh or shear-horizontal wavelength; constructive interference from alternating current directions produces a beam at the design frequency f = c_wave/(2·pitch), analogous to a diffraction grating. Xie et al. (wholly analytical EMAT simulation) modelled the meander coil using a large-radius extrapolation of the Dodd–Deeds circular-coil solution and confirmed that the generated surface-wave beam is directed perpendicular to the wire pitch.

**Sources:**
- [concepts/emat.md](concepts/emat.md)
- [concepts/lorentz-force-emat.md](concepts/lorentz-force-emat.md)
- [concepts/meander-line-coil.md](concepts/meander-line-coil.md)
- [concepts/skin-depth.md](concepts/skin-depth.md)
- [notes/emat/wholly-analytical-emat-array-simulation.md](notes/emat/wholly-analytical-emat-array-simulation.md)

---

## Q12 — Signal processing: cross-correlation ToF estimation

**Q.** Explain why cross-correlation is the preferred algorithm for ToF estimation when the echo waveform is distorted by frequency-dependent attenuation, state how sub-sample precision is achieved, and describe the single-bit implementation of Hirata et al. (2008).

**A.** Cross-correlation R_xy(τ) = ∫ x(t)y(t+τ)dt finds the time lag that maximises waveform similarity between reference and received signals regardless of waveform shape; it is therefore robust when frequency-dependent grain or tissue attenuation differentially attenuates high frequencies, distorting the peak shape and invalidating threshold or zero-crossing methods. Hull (1985) demonstrated experimentally that cross-correlation yields the lowest random ToF error on attenuating composite specimens, outperforming both the overlap (peak-matching) and phase-slope (group delay) methods. In the frequency domain the cross-correlation is computed as X*(f)·Y(f) followed by inverse FFT — an O(N log N) operation. Sub-sample precision is obtained by parabolic interpolation of the three samples around the integer-lag peak, or by fitting the Hilbert-transform envelope of R_xy(τ); both reduce timing error below the digitiser sample interval. Hirata, Kurosawa & Katagiri (2008) replaced the multiply-accumulate cross-correlation with delta-sigma modulated single-bit signals: the product of two 1-bit streams reduces to an EXOR gate, and a moving-average filter accumulates the binary correlation, eliminating hardware multipliers entirely while retaining sufficient SNR for ultrasonic ranging in air.

**Sources:**
- [concepts/cross-correlation.md](concepts/cross-correlation.md)
- [concepts/time-of-flight.md](concepts/time-of-flight.md)
- [notes/range-measurement/hull-1985-correlation-tof.md](notes/range-measurement/hull-1985-correlation-tof.md)
- [notes/signal-processing/single-bit-cross-correlation-ultrasonic.md](notes/signal-processing/single-bit-cross-correlation-ultrasonic.md)
- [notes/signal-processing/tof-interpolation-techniques-svilainis.md](notes/signal-processing/tof-interpolation-techniques-svilainis.md)
