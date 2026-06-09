# PZT Material Selection Guide

- **Source:** pzt selection guide.txt
- **Drive link:** https://drive.google.com/file/d/1_pzt_selection_guide_id/view
- **Type:** notes
- **Author/Year:** unknown / undated
- **Coverage:** full

## Overview
A brief text-format reference guide for selecting among common PZT grades (PZT-4, PZT-5A, PZT-5H, PZT-8) based on application requirements. Summarizes key material properties and recommended use cases.

## Unique contribution
Concise comparative table of PZT grades with practical application guidance, useful as a quick-reference for transducer designers. Distills material property trade-offs into application categories.

## Key concepts
- PZT-4
- PZT-5A
- PZT-5H
- PZT-8
- Electromechanical coupling coefficient
- Curie temperature
- Mechanical Q (Qm)
- Piezoelectric constants (d33, d31)
- Hard vs. soft PZT
- High-power transducer applications

## Methods / results / takeaways
- PZT-4 (hard): high Qm (~500), lower d33 (~290 pC/N), good for high-power applications; less hysteresis loss
- PZT-5A (soft): moderate Qm (~75), d33 ~ 375 pC/N, good general-purpose choice; most widely characterized
- PZT-5H (soft): highest d33 among standards (~590 pC/N), lowest Curie temp (~193 °C); best for receive sensitivity
- PZT-8 (hard): very high Qm (~1000), used for SONAR and high-power underwater transducers
- General rule: soft PZT (5A, 5H) for sensing/receive applications; hard PZT (4, 8) for high-power drive applications
- Aging: soft PZT ages faster (properties drift over time due to domain relaxation)
- Temperature: all grades derate significantly above 100 °C; de-poling occurs approaching Curie temperature
