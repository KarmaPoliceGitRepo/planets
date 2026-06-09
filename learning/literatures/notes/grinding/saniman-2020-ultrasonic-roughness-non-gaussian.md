# Quantitative Roughness Characterization of Non-Gaussian Random Rough Surfaces by Ultrasonic Method

- **Source:** 190406-2001-7575-IJMME-IJENS.pdf
- **Drive link:** https://drive.google.com/file/d/1L6LgoHMZ7Lw3YT7zUhQzy58pKHTOi3NX/view?usp=drivesdk
- **Type:** paper
- **Author/Year:** M.N.F. Saniman, K.A.A. Wahid, F.M. Foudzi, H.H. Ladin, I. Ihara / 2020
- **Coverage:** full

## Overview
A 2020 journal paper (IJMME-IJENS Vol.20 No.01) proposing a non-contact ultrasonic method to simultaneously characterize both the RMS roughness (Rq) and skewness (Rsk) of non-Gaussian random rough surfaces. The method combines pitch-catch and pulse-echo ultrasonic configurations with a newly derived Johnson characteristic function (an extension of the Kirchhoff wave-scattering model using Johnson probability distribution instead of a Gaussian PDF). Numerical validation in the air-coupled ultrasound regime demonstrates Rq estimation accuracy within ±3% and Rsk estimation within ±20%.

## Unique contribution
First theoretical derivation of a characteristic function relating ultrasonic reflection coefficient to both Rq and Rsk for non-Gaussian surfaces. Earlier Kirchhoff-based methods only handled Gaussian surfaces (Rsk = 0). The combined pitch-catch (low normalized Rq·cosθ/λ → Rsk-insensitive) + pulse-echo (high normalized Rq·cosθ/λ → Rsk-sensitive) strategy provides a practical two-step measurement protocol for quantifying non-Gaussian surface statistics.

## Key concepts
- Surface roughness — RMS roughness (Rq), skewness (Rsk), kurtosis (Rku)
- Non-Gaussian height probability density function (PDF)
- Johnson distribution (unbounded SU type)
- Kirchhoff theory / characteristic function (CF) for wave scattering
- Ultrasonic reflection coefficient
- Pitch-catch (PC) configuration vs. pulse-echo (PE) configuration
- Air-coupled ultrasound
- Gaussian CF vs. Johnson CF
- Tuenter's algorithm (estimating Johnson parameters from statistical moments)
- Grinding / honing / milling surfaces (produce negative-skewness surfaces)

## Methods / results / takeaways
- Kirchhoff CF integral with Johnson distribution p(h)J substituted for Gaussian p(h)G yields Johnson CF (Eq. 9) — no analytical closed form, requires numerical integration.
- Threshold parameter t (Eq. 10) defines two measurement regions: region A (Rq·cosθ/λ ≤ 0.037, Rsk influence negligible → use Gaussian CF to estimate Rq) and region B (Rq·cosθ/λ ≥ 0.081, Rsk influence significant → use Johnson CF with known Rq to estimate Rsk).
- Example air-coupled settings: PC at fPC = 0.3 MHz, θPC = 60°; PE at fPE = 0.6 MHz, θPE = 0°. Useful Rq range: 47–87 µm; Rsk range: –1 to +1.
- 12 surface profiles generated numerically via FFT (Wu 2004 method), Rq = 50–85 µm, Rsk = –1 to 1, 50 independent realizations each.
- RqPC estimation error ≤ ±3%; RskPE estimation error ≈ ±20% (largely limited by small dynamic range of I vs. Rsk and propagated Rq error).
- Method is applicable to contact ultrasound as well (back-surface or interface characterization).
- Machining surfaces (honing, grinding, milling) typically have Rsk in –1 to 1 and Rku in 2 to 10 — within the method's design range.
