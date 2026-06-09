# Spring Interface Model
**Aliases:** quasi-static spring model; Tattersall model; spring-dashpot model; spring layer; quasi-static approximation; Baik-Thompson model

**Definition:** The spring interface model treats a thin layer or partially-contacting interface as a distributed elastic spring (stiffness K per unit area) in the long-wavelength limit (h ≪ λ). The ultrasonic reflection coefficient is R = (1 − 2iz₁/ωK)^{-1} rearranged, giving |R| < 1 for finite K and |R| → 1 as K → 0 (no contact) or K → ∞ (rigid bond). For a fluid film, K = ρc²/h (stiffness of a liquid column), enabling film thickness inversion. Above the layer resonance frequency (h = c/2f) the model breaks down and the continuum transfer-matrix (multi-layer) model must be used. A dashpot (viscous) term can be added for viscoelastic or lossy interfaces.

**Key relations:**
- [interfacial-stiffness](interfacial-stiffness.md)
- [film-thickness](film-thickness.md)
- [reflection-coefficient](reflection-coefficient.md)
- [contact-mechanics](contact-mechanics.md)
- [real-contact-area](real-contact-area.md)

**Discussed in:**
- [Ultrasonic Scattering Imperfect Interfaces — Baik & Thompson 1984](../notes/contact-study-using-us-waves/ultrasonic-scattering-imperfect-interfaces-baik-thompson-1984.md) — full derivation of quasi-static spring model and conditions of validity
- [Pialucha & Cawley 1994 — Thin Layers](../notes/lubrication-film/pialucha-cawley-thin-layers-1994.md) — spring model, half-resonance formula, and continuum model compared; frequency-thickness product scaling
- [Dwyer-Joyce 2003 — Lubricant Film (Ultrasound)](../notes/lubrication-film/dwyer-joyce-lubricant-film-ultrasound-2003.md) — spring model used for sub-resonance EHL film measurement
