# Wave Momentum — NYU Lecture Notes

- **Source:** `NYU_wave_momentum.pdf` (Drive ID: 1PSnwK-VprNt834OAJ97WWMvC9hkwpxEl)
- **Drive link:** https://drive.google.com/file/d/1PSnwK-VprNt834OAJ97WWMvC9hkwpxEl/view
- **Type:** lecture notes / preprint (26 pages)
- **Author/Year:** Charles S. Peskin, Courant Institute of Mathematical Sciences, New York University, 2010
- **Coverage:** full

## Overview
A rigorous mathematical treatment of wave momentum across several physical systems: electromagnetic waves, sound waves, water waves, waves on strings, and quantum mechanical matter waves. Peskin shows that while many wave types satisfy momentum = energy/phase_velocity, some traveling waves (e.g. waves on a free string with no tension) carry energy but zero momentum — demonstrating that no universal derivation of the momentum-energy relation exists. The appendix derives the Maxwell stress tensor and energy-momentum conservation rigorously from Maxwell's equations.

## Unique contribution
Makes precise the claim that wave momentum is system-specific, not a universal property of waves. Explicitly constructs counterexamples (string without tension, purely longitudinal acoustic waves in a tube with rigid end) where the momentum-energy relation fails. Provides a self-contained but mathematically complete treatment connecting classical and quantum cases (including relativistic de Broglie waves).

## Key concepts
- **Wave momentum relation:** momentum = energy / phase_velocity (p = E/v_phase); holds for EM, sound, water waves, quantum waves
- **Electromagnetic momentum:** momentum density V = (1/c)(E × B); Poynting vector as energy flux; Maxwell stress tensor σ_ik = E_i E_k + B_i B_k − δ_ik E
- **Sound wave momentum:** Euler equation + continuity equation → acoustic momentum density ρ₀v̄ (mean flow); net momentum requires time-averaged analysis; result p = E/c_sound
- **Water wave momentum:** Stokes drift — fluid particles have a net forward drift even in purely oscillatory waves; drift velocity proportional to wave steepness squared; gives p = E/c_water
- **String wave momentum:** transverse waves on a string under tension T → p = E/c_string (c = √[T/σ]); but strings with no tension carry zero momentum despite carrying energy
- **Quantum wave momentum:** de Broglie p = h/λ = ℏk; relativistic dispersion ω² = k²c² + (m₀c²/ℏ)² → group velocity v_g = ℏk/E; p = E v_g/c² reduces to momentum = energy/phase_velocity in the relativistic case
- **Counterexamples:** free string (no tension): traveling wave solution exists, E ≠ 0, but net momentum = 0; tube with closed end: longitudinal acoustic standing wave carries no net momentum
- **Maxwell stress tensor:** the standard form of momentum conservation in continuum mechanics with ∂P_i/∂t = ∂σ_ik/∂x_k − F_i

## Methods / Results / Takeaways
- Systematic case-by-case analysis using conservation laws (momentum balance from field equations)
- Stokes drift derivation: Lagrangian vs. Eulerian particle positions — in water waves, Lagrangian mean velocity differs from Eulerian mean by O(amplitude²) term that gives net forward transport
- The "momentum = energy / phase velocity" relation holds wherever the wave stress tensor has a specific form relating flux to energy density
- The paper is pedagogically careful: shows that Poynting's theorem (energy conservation) and the Maxwell stress tensor (momentum conservation) are parallel structures
- Main takeaway: wave momentum is real physical momentum (pushes obstacles) but its existence and magnitude are system-specific; quantum wave-particle duality provides the deepest connection

## See also
- `fundamentals-acoustics-wikibooks.md` — acoustic intensity and energy relations
- `brekhovskikh-ocean-acoustics-1982.md` — Stokes drift context in ocean acoustics
