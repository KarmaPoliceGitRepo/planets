# Novel Physics-Based Temperature Compensation Model for SHM Using Ultrasonic Guided Waves

- **Source:** Novel physics-based temperature compensation model (2014) Roy.pdf
- **Drive link:** https://drive.google.com/file/d/1Q0TfkgNUKxcw5hee98MlJ3PHbchtwRw-/view
- **Type:** paper
- **Author/Year:** Roy, Lonkar, Janapati & Chang / 2014
- **Coverage:** partial (large file, truncated extraction)

## Overview
Published in Structural Health Monitoring 13(3), 2014. Introduces a physics-based model for temperature compensation of piezoelectric sensor signals in guided wave SHM, accounting for temperature effects on the base substrate, piezo-transducer properties, and adhesive interface bond.

## Unique contribution
Unlike purely data-driven stretch-based approaches, models the physical mechanisms by which temperature affects each component of the transducer-structure system separately (substrate wave velocity, piezo coupling, adhesive bond stiffness), allowing principled compensation without requiring large temperature training datasets.

## Key concepts
- Physics-based temperature compensation
- Piezoelectric transducer (PZT)
- Adhesive bond layer
- Wave velocity temperature dependence
- Guided waves
- Structural health monitoring (SHM)
- Material property temperature dependence

## Methods / results / takeaways
- Temperature changes affect: (1) wave velocity in the structure (dominant effect, causes time stretch); (2) piezo coupling coefficient; (3) adhesive bond layer stiffness (affects amplitude and phase of coupling).
- Model integrates all three contributions to predict the expected signal change at a new temperature from a baseline signal.
- Compensation: use predicted signal change to adjust the baseline before subtraction.
- Requires prior training data (material properties vs. temperature) but less data than empirical stretch-factor databases.
- Demonstrated on metallic and composite plate specimens with bonded PZT arrays.
- Outperforms pure BSS (baseline signal stretch) by accounting for amplitude changes that BSS ignores.
