# Comparison of the Mason and KLM Equivalent Circuits for Piezoelectric Resonators in the Thickness Mode

- **Source:** Sherrit 1999 Mason vs KLM (primary copy)
- **Drive link:** https://drive.google.com/file/d/1XVbSK67ocrISKziF2hbfrUBB8Bc3Z3t3/view
- **Type:** paper (conference, IEEE Ultrasonics Symposium)
- **Author/Year:** Stewart Sherrit, Sean P. Leary, Benjamin P. Dolgin, Yoseph Bar-Cohen / 1999
- **Coverage:** full

## Overview
Derives and compares the parameters of the KLM and Mason equivalent circuits for thickness-mode piezoelectric resonators with all losses included (complex dielectric, elastic, and piezoelectric constants). Shows that both models are mathematically equivalent under all boundary conditions (short/open acoustic ports, with and without backing layers) when losses are applied consistently. Identifies consistency requirement: if electromechanical coupling k_t is treated as real, this implicitly makes e₃₃ and h₃₃ complex. Analyses the effect of each loss type on power dissipation and insertion loss.

## Unique contribution
Proves formal equivalence of Mason, KLM, and analytical wave-equation solutions for lossy piezoelectrics by demonstrating overlap in impedance curves under all tested conditions. Identifies the key consistency trap: assigning k_t as real while using complex ε^S and c^D actually assigns complex phase angles to the transformer constants N (Mason) and M (KLM), giving incorrect power spectra. Shows piezoelectric loss affects dissipated power significantly but has minimal effect on insertion loss shape — important for thermal design.

## Key concepts
- KLM vs Mason equivalent circuit parameter comparison (Table 1)
- Complex material constants applied to both models (Holland convention)
- Turns ratio N (Mason) and M coefficient (KLM): become complex when losses are included
- Consistency requirement: k_t real → e₃₃, h₃₃ must be complex
- Power dissipated in piezoelectric element: depends on piezoelectric loss designation
- Insertion loss: primarily determined by source impedance, tuning inductor, backing Z, and real parts of material constants; piezoelectric loss effect is small
- Motorola 3203HD material constants: c^D₃₃ = 1.77×10¹¹ N/m² (tan~2.3%), ε^S₃₃ = 1.06×10⁻⁸ F/m (tan~5.3%), h₃₃ = 2.19×10⁹ V/m (tan~2.9%), k_t = 0.536 (tan~0.5%)

## Methods / results / takeaways
- Comparison performed under: (1) free resonator (acoustic ports short-circuited), (2) full-open acoustic ports, (3) half-open ports, (4) with stainless steel backing (Z_b=46 MRayl), (5) with epoxy backing (Z_b=2.75 MRayl)
- Result: all models overlap in all cases when losses applied consistently — proves equivalence
- Backed 25 MHz transducer radiating into water (tuned with 492 nH series inductor): power dissipation depends on k_t designation (real vs complex); insertion loss curves deviate ~3 dB between k_t designations
- Practical implication: piezoelectric loss is important for thermal analysis (duty cycle, heating) but can be neglected for insertion loss / bandwidth prediction
- Setting dielectric and elastic losses to zero (only piezoelectric loss retained) has very little effect on insertion loss curve shape
