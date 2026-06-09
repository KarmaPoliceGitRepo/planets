# Aluminium EN 6082AW T6 Stress vs Strain Data (Spreadsheet and Charts)

- **Source:** Experimental Analysis of the Behaviour of Aluminium Alloy EN 6082AW T6 at High Temperature.xlsx + associated PNG charts
- **Drive link:** https://drive.google.com/drive/folders/1pDMRfMmZAcwjFfXdujFODIMOaKFPgNw4
- **Type:** datasheet
- **Author/Year:** Unknown (derived from Toric et al. 2017 paper, uploaded 2018)
- **Coverage:** full

## Overview
A sidecar data folder associated with the Toric et al. (2017) paper on EN 6082AW T6 aluminium at high temperature. Contains a spreadsheet (XLSX) with digitised/tabulated stress–strain data for the alloy, and two PNG image files showing the stress-strain curves (one with grid overlay, one plain). The spreadsheet records stress values at discrete strain increments, effectively providing the piecewise linear stress-strain relationship for use in engineering calculations or FEA material input.

## Unique contribution
Provides the raw numerical stress-strain tabulation corresponding to the graphical curves in the Toric paper — enabling direct import into FEA or structural analysis software without manual digitisation. The alloy data covers: stress from 0 MPa to 327 MPa; strain from 0% to 2% (engineering strain up to ~0.04); includes points at key temperatures (though the spreadsheet header implies ambient 20 °C conditions with stress levels consistent with EN 6082AW T6 0.2% proof stress ~288 MPa at 20 °C).

## Key concepts
- EN 6082AW T6 aluminium alloy
- Stress-strain tabulation (piecewise linear)
- Engineering stress and strain
- Proof stress (0.2% offset)
- Material data for FEA
- Stress-strain diagram digitisation

## Methods / results / takeaways
- Spreadsheet structure: columns represent temperature levels (0–24 listed); rows represent strain values (0 to 2.0% in regular increments with a few additional points at 20.8%, 21.5%, 21.8%); stress values in MPa.
- At ambient conditions: stress rises approximately linearly from 0 to ~288 MPa at ~0.4% strain (elastic), then yields and continues to ~327 MPa before levelling off — consistent with T6 temper mechanical properties.
- Two PNG image files: one shows the curve without grid (plain stress-strain plot), one with a grid overlay for reading off values — both are image-only (no embedded data).
- Note: PNG files returned empty text extraction (image-only); all data is in the XLSX.
