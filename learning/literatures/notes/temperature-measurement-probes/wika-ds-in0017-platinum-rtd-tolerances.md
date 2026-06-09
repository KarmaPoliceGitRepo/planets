# WIKA Data Sheet IN 00.17 — Platinum Resistance Thermometers: Operating Limits and Tolerances per EN 60751:2008

- **Source:** DS_IN0017_en_co_20804.pdf
- **Drive link:** https://drive.google.com/file/d/1yXp-6IQt0fCs0Ww2rcmDuzBCXiwDNwZi/view?usp=drivesdk
- **Type:** datasheet
- **Author/Year:** WIKA Alexander Wiegand SE & Co. KG, 02/2016
- **Coverage:** full

## Overview
An 8-page technical reference document from WIKA covering the fundamental operating characteristics of platinum resistance thermometers (PRTs) — specifically Pt100 and Pt1000 sensors — as defined by EN 60751:2008 (equivalent to IEC 60751:2008). It covers sensor construction types, wiring methods, resistance–temperature relationships, tolerance classes, and vibration resistance requirements.

## Unique contribution
Provides comprehensive numerical tolerance tables (resistance vs. temperature and temperature vs. resistance) for Classes AA, A, and B under EN 60751:2008, plus WIKA-specific vibration resistance data for thin-film and wire-wound sensors in both 3 mm and 6 mm MI cable forms. This makes it a self-contained reference for specifying, verifying, and testing platinum RTDs in industrial settings.

## Key concepts
- Pt100 / Pt1000 measuring resistors
- Resistance Temperature Detector (RTD)
- Thin-film measuring resistor (F-type)
- Wire-wound measuring resistor (W-type): glass and ceramic subtypes
- PTC (Positive Temperature Coefficient)
- EN 60751:2008 / IEC 60751:2008
- Tolerance classes: AA, A, B
- 2-wire, 3-wire, 4-wire sensor connection
- Lead resistance compensation
- Callendar–Van Dusen equation (Rt formula with A, B, C constants)
- Dual sensors
- Vibration resistance (peak-to-peak, g-value)
- MI cable (mineral-insulated cable)

## Methods / results / takeaways
- **Resistance–temperature formula** (Callendar–Van Dusen):
  - -200 to 0 °C: Rt = R0 [1 + At + Bt² + C(t − 100 °C)·t³]
  - 0 to 600 °C: Rt = R0 [1 + At + Bt²]
  - Constants: A = 3.9083×10⁻³ °C⁻¹; B = -5.775×10⁻⁷ °C⁻²; C = -4.183×10⁻¹² °C⁻⁴
- **Tolerance class summary (Pt100)**:
  - Class B: ±(0.30 + 0.005|t|) °C; thin-film -50…+500 °C, wire-wound -196…+600 °C
  - Class A: ±(0.15 + 0.002|t|) °C; thin-film -30…+300 °C, wire-wound -100…+450 °C
  - Class AA: ±(0.10 + 0.0017|t|) °C; thin-film 0…+150 °C, wire-wound -50…+250 °C
- Once a thermometer is operated outside its class temperature range, the tolerance class can no longer be guaranteed — even if it returns to within range; dwell time is irrelevant.
- **Wiring guidance**: 2-wire introduces uncorrected lead resistance error (avoid for Pt100 Class A/AA); 3-wire (standard) compensates lead resistance for cables up to ~30 m; 4-wire completely eliminates lead resistance error, suitable for lab/calibration and cables to 1,000 m.
- **Vibration resistance**: Standard design meets 6 g peak-to-peak; optional thin-film configurations can reach 20 g or 50 g. Wire-wound sensors are limited to 6 g.
- Pt1000 is preferred with 2-wire connections because the higher base resistance makes lead resistance a smaller fractional error.
