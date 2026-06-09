# Acoustic Impedance Matching of Piezoelectric Transducers to the Air

- **Source:** 2004 Acoustic impedance matching of piezoelectric transducers to the air - TE Gomez.pdf
- **Drive link:** https://drive.google.com/file/d/1PgIE0vaKLjj2cGDxaKWhwIzBvwnExeLb/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** Tomás E. Gómez Álvarez-Arenas, 2004 (IEEE Trans. Ultrason., Ferroelect., Freq. Contr., vol. 51, no. 5)
- **Coverage:** full

## Overview

This paper addresses the design, material selection, and fabrication of impedance matching layers for air-coupled piezoelectric transducers operating in the low-megahertz range (0.3–2.5 MHz). The central challenge is that the acoustic impedance of piezoelectric ceramics (~35 MRayl) is roughly five orders of magnitude greater than air (~400 Rayl), resulting in extremely poor energy transfer (~−60 dB sensitivity) and narrow bandwidth (~5%) without matching. The paper derives criteria for acceptable acoustic impedance and attenuation in matching materials, systematically characterises a large set of commercial filtration membranes against those criteria, and demonstrates four pairs of working air-coupled transducers using polyethersulfone, nylon, and cellulose-ester membrane filters as the outer quarter-wavelength (λ/4) matching layer.

## Unique contribution

This paper is distinctive in quantifying, for the first time, how attenuation in the matching layer (not just impedance) constrains material selection for air-coupled transducers. It derives an explicit energy-transmission formula that incorporates multiple internal reflections and their attenuation, defines a practical upper bound of γ < 0.14 Np (attenuation per wavelength) for NDT applications, and applies these criteria to a systematic characterisation of ~30 commercial membrane filters spanning vinylic/acrylic copolymers, polyethersulfone, nylon, PVDF, cellulose esters, and cellulose nitrate. The result is a tuneable, commercially accessible solution: selecting a different membrane grade shifts the λ/4 resonant frequency over 0.3–2.5 MHz, avoiding custom fabrication of exotic low-impedance solids like silica aerogels.

## Key concepts

- Acoustic impedance matching
- Quarter-wavelength (λ/4) matching layer
- Air-coupled piezoelectric transducers
- Insertion loss (two-way)
- Attenuation coefficient / attenuation per wavelength (γ)
- Impedance mismatch (solid/air)
- KLM transmission-line model (Desilets et al. approach)
- Filtration membranes as matching layers (polyethersulfone, nylon, mixed cellulose esters)
- Silica aerogel (reference material)
- Bandwidth vs. sensitivity trade-off
- Constant-Q (frequency-independent γ) materials
- Power-law attenuation frequency dependence
- Nondestructive testing (NDT) / non-contact ultrasonics
- PZT-5A piezoceramic
- Epoxy intermediate matching layer

## Methods / results / takeaways

**Design criteria derived:**
- Two approaches to optimal λ/4 impedance: (1) geometric mean Z_l = √(Z_a · Z_p), giving ~0.11 MRayl for a single layer; (2) Desilets KLM method, giving lower values (~0.02 MRayl). Both agree that sub-0.3 MRayl materials are needed.
- Attenuation per wavelength γ > 0.14 Np causes >15 dB one-way insertion loss contribution from the matching layer alone — proposed as the practical upper bound for NDT.
- For air-coupled transducers, attenuation is far more critical than for water-immersion transducers because the high solid/air mismatch requires many internal reverberations inside the matching layer to build up the transmitted signal; any loss per bounce compounds severely.
- Materials must also allow formation of a planar λ/4-thick layer that can be bonded without destroying its properties.

**Material characterisation (Table I):**
- ~30 commercial filtration membranes tested by air-coupled through-transmission spectroscopy (0.5–5 MHz); λ/2 resonant frequency, acoustic impedance, and attenuation measured.
- Best performers: polyethersulfone (γ < 0.11 Np, Z = 0.10–0.25 MRayl) and nylon (γ ≈ 0.14–0.20 Np, Z = 0.16–0.31 MRayl). Changing pore size (grade) shifts λ/2 resonance from ~1 MHz to ~2.4 MHz for polyethersulfone.
- Mixed cellulose esters: constant-Q behaviour (no upper frequency limit in principle) but absolute γ ≈ 0.2 Np — marginally acceptable.
- Cellulose nitrate: constant-Q but γ ≈ 0.20–0.25 Np — slightly high.
- PVDF and polypropylene: higher attenuation (γ > 0.32 Np), generally unsuitable.
- Silica aerogel: lowest γ (~0.06 Np) and ideal impedance (~0.06–0.1 MRayl) but practically impossible to form thin uniform layers for >1 MHz operation.

**Transducer fabrication and results (Table II, Fig. 4):**
- Four transducer pairs built with PZT-5A (25 mm diameter), no backing, epoxy intermediate layer + membrane outer layer.
- Epoxy intermediate layer widens bandwidth by splitting the ceramic resonance peak into two; membrane's λ/4 resonance is placed between those peaks.
- Two-way insertion loss: −24 dB at 0.45 MHz, −29 dB at 0.7 MHz, −33 dB at 1 MHz, −42 dB at 1.8 MHz, −50 dB at 2.25 MHz.
- −6 dB bandwidth: 15–20% (improvable at cost of sensitivity).
- Performance is comparable to or better than prior art (Table IV), with the additional advantage of covering 0.3–2.5 MHz by simply swapping membrane grades, using widely available commercial materials.

**Practical gotchas:**
- Membrane thickness tolerance ~5–10% → resonant frequency uncertainty ~10%; this must be accounted for in design.
- Glue layer (10–20 µm, acoustic properties similar to epoxy) used to bond membrane to epoxy without corrupting its acoustic properties.
- Attenuation frequency dependence (power law β) must be characterised to know whether a material has a useful upper frequency limit; most porous materials have β > 1 (γ increases with frequency).
- No current method to predict attenuation coefficient in membrane filters from structural parameters alone.
