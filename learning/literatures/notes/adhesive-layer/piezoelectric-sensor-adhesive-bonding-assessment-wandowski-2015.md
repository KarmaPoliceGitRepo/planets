# Assessment of Piezoelectric Sensor Adhesive Bonding

- **Source:** Assessment of piezoelectric sensor adhesive bonding - (2015) Wandowski.pdf
- **Drive link:** https://drive.google.com/file/d/1flP2qEIUu0YjKMWIptGAOAjIyobsjQiN/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** T. Wandowski, J. Moll, P. Malinowski, S. Opoka, W. Ostachowicz / 2015
- **Coverage:** full

## Overview
A conference paper (DAMAS 2015, Journal of Physics: Conference Series) from the Polish Academy of Sciences and Goethe University Frankfurt, presenting two complementary non-destructive methods for assessing the adhesive bond quality of piezoelectric (PZT) transducers attached to a GFRP composite panel. The methods are time-domain terahertz (THz) spectroscopy in reflection C-scan mode and electromechanical impedance (EMI) analysis. Their results are cross-validated against each other on a panel with one perfectly bonded and two partially debonded transducers.

## Unique contribution
First combination of terahertz spectroscopy and electromechanical impedance for PZT transducer bond assessment. THz provides spatial imaging of glue distribution; EMI provides a complementary electrical-domain signature. The paper demonstrates that real-part EMI parameters (resistance, conductance) — not only the imaginary parts (reactance, susceptance) traditionally used — can also detect debonding, enabling multi-parameter characterization. The limitation of THz to GFRP (not CFRP) and to adhesives with good THz contrast is clearly identified.

## Key concepts
- Piezoelectric transducer (PZT) bonding assessment
- Electromechanical impedance (EMI) method
- Electrical impedance / admittance: resistance, reactance, conductance, susceptance
- Transducer debonding detection
- Structural Health Monitoring (SHM)
- Time-domain terahertz (THz) spectroscopy
- THz C-scan imaging
- Envelope detection / signal processing for C-scan contrast
- Bonding layer distribution visualization
- GFRP vs. CFRP THz penetration limitation

## Methods / results / takeaways
- **Sample:** 500 × 200 × 2 mm GFRP panel [0/90/0/0/90/0] with three SONOX P5 PZT discs (10 mm diameter, 0.5 mm thick) bonded with two-part epoxy (PRO WELD QUICK Pro Seal): one perfectly bonded (#1), two partially debonded (#2, #3).
- **THz setup:** Teraview TPS Spectra 3000, 0.1–3 THz range, reflection mode scanning from side opposite PZTs; envelope-detected C-scans give much better contrast than raw RF C-scans.
- **THz result:** after envelope detection and isosurface extraction, glue distribution is clearly visible; circular transducer footprint identifiable for the perfectly bonded unit. Cyanoacrylate adhesives were found incompatible with this technique (low contrast).
- **EMI frequency ranges analyzed:** 1–10 kHz (host structure resonances), 180–280 kHz and 3–5 MHz (free PZT resonances).
- **EMI results:**
  - At 1–10 kHz: structural resonance peaks visible in resistance and conductance only for the perfectly bonded transducer; disappear for partially/fully debonded cases.
  - At 180–280 kHz and 3–5 MHz: peak amplitudes of all parameters increase with debonding — the free transducer resonances emerge as bonding is lost.
  - Both real (resistance, conductance) and imaginary (reactance, susceptance) components carry debonding information; imaginary parts show zero-crossing shifts.
- **Practical takeaways:** EMI can be used continuously in SHM systems; THz is suitable as offline NDT. EMI is adhesive-type agnostic; THz requires material-specific THz contrast. Together they provide spatial + temporal bond quality data.
