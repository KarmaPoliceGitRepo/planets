# Determination of the Piezoelectric Electromechanical Coupling Constant k13 Using a Frequency Ratio Method

- **Source:** Sherrit 1997 k13 coupling constant
- **Drive link:** https://drive.google.com/file/d/1qnYpa4jedzCklVc3k78XJvTzFJWnXf_B/view
- **Type:** paper
- **Author/Year:** S. Sherrit, H. D. Wiederick, B. K. Mukherjee, M. Sayer / 1997
- **Coverage:** full

## Overview
Presents a frequency ratio method for determining the electromechanical coupling constant k₁₃ of the length-thickness piezoelectric resonator, as an alternative to the standard IEEE equations. Tabulates the parallel frequency ratio (f_p2/f_p1, f_p3/f_p1, f_p4/f_p1) as a function of k₁₃ and provides third-order polynomial fits for computer implementation. The method avoids the error amplification problem of the IEEE standard equations when k is small, mechanical Q is low, or resonance peaks are noisy.

## Unique contribution
Extends the Sherrit/Wiederick series on frequency ratio methods to the k₁₃ constant (length-thickness resonator), for which no published frequency ratio relationship existed. Shows that the parallel frequency ratio approach avoids the Δf subtraction error of IEEE standard equations — advantageous for materials with small k₁₃ or low mechanical Q.

## Key concepts
- Length-thickness piezoelectric resonator mode (k₁₃)
- Parallel frequency ratio method: r = f_p2/f_p1 → k₁₃
- Third-order polynomial fit: k₁₃ = b₀ + b₁r + b₂r² + b₃r³
- IEEE Std 176-1987 standard equations for k (thickness, shear, extensional modes)
- Error amplification in Δf = f_p - f_s for small k
- Dispersion effects on frequency ratio accuracy

## Methods / results / takeaways
- Tabulated data: k₁₃ from 0.01 to 0.95 with corresponding f_p2/f_p1, f_p3/f_p1, f_p4/f_p1 ratios
- Polynomial valid for k₁₃ = 0.01 to 0.60; max error < 0.069% at k₁₃ = 0.01
- For k₁₃ > 0.6 (rare in practice), higher-order ratios can be used
- Advantage over IEEE equations: ratio of two frequencies rather than difference — noise and loading errors do not amplify
- If material is dispersive, comparing k₁₃ values from successive parallel resonance ratios reveals the frequency dependence of k₁₃
