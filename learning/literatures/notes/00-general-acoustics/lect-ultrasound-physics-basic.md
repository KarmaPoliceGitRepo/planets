# Basic Physics of Ultrasound — Lecture Slides

- **Source:** `Lect - Ultrasound Physics - Basic Physics of Ultrasound.pdf` (Drive ID: 1LmRJeF8VoCgy6Og8cop4t55YPzeuUPwx)
- **Drive link:** https://drive.google.com/file/d/1LmRJeF8VoCgy6Og8cop4t55YPzeuUPwx/view
- **Type:** lecture slides (81 slides, PDF)
- **Author/Year:** Dr Jamie Robinson, Department of Nuclear Cardiology, 2014
- **Coverage:** full

## Overview
An 81-slide introductory lecture on the physical principles of diagnostic ultrasound imaging, aimed at medical/clinical practitioners. Covers the entire signal chain from ultrasound wave generation (piezoelectric transducer), through tissue interactions (reflection, attenuation, scattering, refraction, diffraction), image formation (B-mode, A-mode), and resolution types (axial, lateral, contrast, temporal), to a comprehensive survey of imaging artefacts. Includes quantitative tables of tissue acoustic properties.

## Unique contribution
Medically focused, with concrete numerical tables (propagation speeds, acoustic impedances, attenuation coefficients in specific tissues) and clinical imaging examples. Covers artefacts systematically with visual examples from real ultrasound images. Includes Time Gain Compensation (TGC) as a practical technique to compensate depth-dependent attenuation.

## Key concepts
- **Acoustic impedance:** Z = ρc (Rayl = kg/m²/s); tabulated for common tissues: air 0.0004, water 1.48, liver 1.64, muscle 1.70, bone 7.8 MRayl; PZT transducer Z = 30 MRayl
- **Intensity reflection and transmission coefficients:** R = (Z₂−Z₁)²/(Z₁+Z₂)²; T = 4Z₁Z₂/(Z₁+Z₂)²; tissue/air interface reflects 99% (requires coupling gel)
- **Attenuation:** rule of thumb 1 dB/cm/MHz in soft tissue; sources: absorption, scattering, reflection, refraction, diffraction; tissue-specific: blood 0.18, liver 1.0, bone 20 dB/cm/MHz
- **Piezoelectric crystal:** PZT (lead zirconate titanate); poling aligns dipoles; direct effect (mechanical → electrical) and converse effect (electrical → mechanical); Curie point as upper temperature limit
- **Pulse generation:** 1 µs, 500 V pulses; PRF = 1-10 kHz; pulse length = 2-3 cycles; SPL (spatial pulse length) determines axial resolution
- **Near field (Fresnel zone):** length D = d²/(4λ) = d²f/(4c); cylindrical narrow beam; good spatial resolution; depth ~13 cm at 2 MHz for 2 cm transducer
- **Far field (Fraunhofer zone):** conical divergence; beam half-angle sin θ = 1.22λ/d; lateral resolution degrades beyond focal zone
- **Axial resolution:** SPL/2 = nλ/2; improved by higher frequency (shorter λ) or heavier backing (fewer cycles per pulse)
- **Lateral resolution:** determined by beam width at depth; best at focal zone; improved by focusing (electronic delays in phased array) and higher frequency
- **Time Gain Compensation (TGC):** amplifies echo signal with increasing depth to compensate exponential attenuation; operator-adjustable at different depths
- **Transducer components:** piezoelectric crystal + conducting plates + backing material (damping) + impedance matching layer (quarter-wave: Z_match = √(Z_crystal × Z_tissue)) + acoustic lens (focusing)
- **Array types:** linear (parallel beams, field = probe width), curvilinear (wedge field, wider at depth), phased array (beam steered electronically by time delays — used in cardiology)
- **Snell's law for refraction:** sin θ₁/sin θ₂ = c₁/c₂; causes misregistration of deep structures
- **Imaging artefacts:** reverberation (multiple reflections between highly mismatched surfaces), acoustic shadow (strong reflector blocks deeper imaging), acoustic enhancement (weak attenuator allows extra penetration below), edge shadowing (refraction at curved interface), ring down (bubble/crystal resonance emits continuous signal), beam width/slice thickness (volume averaging), mirror image (diaphragm reflection), speed propagation error (fat c = 1459 vs assumed 1540 m/s)

## Methods / Results / Takeaways
- B-mode image formation: fire pulse → wait for echo sequence → measure time of flight (depth = ct/2 where c = 1540 m/s assumed) → display as brightness vs. position
- Tissue impedance mismatch at fat/muscle (1% reflected), bone/fat (49% reflected): shows why bone and air are problematic for ultrasound
- Frame rate = PRF / (lines per frame); cardiac imaging requires ≥25 fps → limits depth and line density simultaneously
- Key insight: ALL 7 standard assumptions of US imaging (constant speed, straight-line propagation, uniform attenuation, echo from central axis, no secondary echoes, amplitude ∝ density) are violated in practice → source of all artefacts
- ALARP principle applies; diagnostic US considered safe at clinical intensities but therapeutic US causes heating and cavitation

## See also
- `nakamura-ultrasonic-transducers.md` — detailed transducer design and materials
- `ultrasonic-testing-intro.md` — NDT use of ultrasound (industrial rather than medical)
- `azhari-biomedical-ultrasound.md` — textbook-level biomedical ultrasound
