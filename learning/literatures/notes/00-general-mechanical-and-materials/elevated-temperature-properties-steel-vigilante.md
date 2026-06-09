# Elevated Temperature Properties of Steels (ARCCB-TR-96023)

- **Source:** Elevated temperature properties of steel.pdf
- **Drive link:** https://drive.google.com/file/d/1LsEC6Bcv3nTo4Lsh3jmZHVnj5MPIMdIZ/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** G.N. Vigilante, A. Fish, G.P. O'Hara, D. Crayon, T. Hickey — US Army ARDEC, Benét Laboratories, August 1996 (Technical Report ARCCB-TR-96023)
- **Coverage:** full

## Overview
A US Army technical report characterising high-temperature physical and mechanical properties of ASTM A723 Grade 1 and D6AC gun steels, motivated by gun tube thermal management: repeated firing cycles cause elevated temperatures (up to 450 °C) that may relax autofrettage residual stresses, reduce fatigue life, and cause bore closure. Tests covered thermal expansion, specific heat (results unreliable), Young's modulus, Poisson's ratio, stress relaxation, and elevated-temperature tensile strength.

## Unique contribution
Develops a power-law creep model for A723 gun steel calibrated from mandrel-bend stress relaxation data using ABAQUS FEA: dε/dt = Aσ^n·t^m with n=1.77, m=−0.75, and A varying with temperature (100–450 °C). Provides direct comparison between A723 and D6AC under identical test conditions, showing D6AC has roughly 2× better stress relaxation resistance at 450 °C. Also characterises dynamic (high strain-rate) tensile properties on a Gleeble 1500 tester — UTS increases ~5% at very high stroke rates (212 mm/s vs. 0.013 mm/s).

## Key concepts
- ASTM A723 Grade 1 gun steel (Fe-2Ni-1Cr-0.5Mo-0.35C-0.1V)
- D6AC steel (Fe-1Cr-1Mo-0.5Ni-0.45C-0.1V)
- Autofrettage residual stresses
- Creep law (power law)
- Stress relaxation
- Mandrel method (ASTM E328)
- Thermal expansion coefficient
- Young's modulus (strain gauge and Dynamic Mechanical Analyzer)
- Poisson's ratio
- Gleeble 1500 (thermal-mechanical tester)
- Stroke rate effects on strength
- Gun tube thermal management

## Methods / results / takeaways
- Thermal expansion: logarithmic increase with temperature for both alloys (consistent with prior data); 11–18 × 10⁻⁶ cm/cm/°C over 100–650 °C range.
- Young's modulus: general decrease with temperature observed but strain-gauge method gave scattered results; DMA method proved more reliable and convenient (continuous measurement vs. discrete load steps).
- Poisson's ratio: decreasing trend with temperature (from ~0.316 at RT to lower values at 400 °C) but with significant scatter from gage weight and thermal current errors; recommended future approach: compute from E and G using ν = E/2G − 1.
- Stress relaxation: at 850 MPa initial stress, 4-hr exposure at 450 °C: A723 relaxes ~198 MPa vs. D6AC ~99 MPa. D6AC superior due to higher C and Mo content retarding dislocation motion.
- Creep model for A723: at 300 °C A = 1.10×10⁻¹⁰; at 450 °C A = 12.41×10⁻¹⁰ (both with n=1.77, m=−0.75). ABAQUS predictions match mandrel test data.
- Tensile: A723 loses ~20% room-temperature strength at 400 °C (0.1% YS: ~1170 → ~940 MPa); D6AC retains slightly more strength due to higher alloy content.
- Short-time exposure creep (gun firing duration ~milliseconds to seconds) not fully characterised — identified as a gap requiring further study.
