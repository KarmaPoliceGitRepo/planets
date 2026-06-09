# Distortion Inside a Piston Bore (Ring Conformability Bounds Comparison)

- **Source:** MSU MTH 844 course report, Michigan State University / DaimlerChrysler, April 28, 2004 (unpublished; internal report)
- **Drive link:** https://drive.google.com/file/d/1hnGqQyOjfcHQzE6jyUI7cF3OLquT_HTs/view
- **Type:** report
- **Author/Year:** Bardzimashvili, Teimuraz; Kelly, James F.; Romelashvili, Elene (MSU MTH 844, work for DaimlerChrysler, directed by Bruce Geist) / 2004
- **Coverage:** full

## Overview
Academic engineering report comparing the three main analytical bounds for piston ring conformability to a Fourier-decomposed distorted cylinder bore: Dunaevsky (1990), GOETZE/Müeller (1970), and Tomanik (semi-empirical). Develops RINGPACK, a MATLAB simulator that solves the elastic ring-bore pressure problem from first principles using cubic spline interpolation, Gauss quadrature Fourier decomposition, and exact curvature formulas. Validates RINGPACK bounds against Dunaevsky and GOETZE bounds: RINGPACK matches GOETZE almost exactly, confirming that Dunaevsky overestimates allowable distortion for orders k > 2 due to an unphysical "critical curvature" assumption. Tests on DaimlerChrysler FE data (V-6 engine bore, 51.181 mm radius).

## Unique contribution
First direct numerical validation showing that GOETZE/Müeller bounds are more accurate than Dunaevsky bounds for orders k > 2; identifies the specific Dunaevsky error as the "Critical Curvature Assumption" (that the curvature at which seal breaks is independent of Fourier order); shows that seal can be violated even when all individual Fourier coefficients are below the GOETZE bounds (superposition of orders); demonstrates necessity of analysing the complete bore profile rather than isolated harmonics.

## Key concepts
- Dunaevsky bound: Ak < 1.52·Q·r³ / [E·h·t³·(k²−1)]
- GOETZE (Müeller) bound: Ak < 4.56·Q·r³ / [E·h·t³·(k²−1)²] — more conservative for k > 2
- Tomanik semi-empirical bound: Ak < 20·K·r / (k²−1)
- Conformability coefficient K = Ft·r²/(2EI) or K = r³·p₀/(EI)
- All bounds match at k = 2; diverge at k ≥ 3; Dunaevsky overestimates allowable distortion by >200% vs Tomanik for high orders
- RINGPACK: MATLAB; ring curvature from closed-form formula; bore curvature from Fourier + exact polar curvature; pressure from Euler-Bernoulli beam + moment equation
- Critical Curvature Assumption (Dunaevsky): pressure at seal breach independent of order k → unphysical (pressure depends on curvature AND its second derivative → factor (k²−1)² appears in GOETZE)
- FE data: DaimlerChrysler V-6, 16 axial decks × 23 circumferential points; max distortion 0.07 mm
- Seal breach possible even when individual harmonics are below bounds (need full profile analysis)
- Bounds are proportional to t³ and r³: highly sensitive to ring thickness and bore radius

## Methods / results / takeaways
- Theoretical derivation: bending moment M(φ) from closed-form integration of radial pressure; free curvature κ₀ derived analytically; compressed curvature κ₁ from measured bore profile.
- Bore curvature: cubic spline interpolation of 23 data points; Gauss quadrature Fourier coefficients; exact polar coordinate curvature formula.
- Pressure: p(φ) from bending moment via beam theory; seal intact when p(φ) ≥ 0 everywhere.
- RINGPACK vs bounds: numerically-calculated conformability limits match GOETZE almost exactly; Dunaevsky overestimates (is too permissive) for k > 2.
- Parameter study: bounds scale as ~t⁻³ and ~r³; small errors in thickness or radius cause large changes in allowable distortion.
- FE data (deck 9): ring pressure goes slightly negative → seal breached; but all individual Fourier coefficients (orders 2–5) are below GOETZE bounds → confirms that superposition of orders can cause breach not predicted by per-order analysis.
- Recommendation: analyse complete bore profile (RINGPACK style), not just dominant harmonic; consider orders beyond 4th; use GOETZE bounds in preference to Dunaevsky for k > 2.
- Bore-liner relevance: rigorous mathematical derivation of why GOETZE bounds are correct for high-order distortions; provides basis for choosing Tomanik or GOETZE over Dunaevsky for design; shows full-profile conformability analysis is necessary.
