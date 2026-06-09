# Image Denoising
**Aliases:** image denoising; Non-Local Means; NLM; anisotropic diffusion; Perona-Malik diffusion; total variation denoising; wavelet shrinkage; bilateral filter; B-scan imaging

**Definition:** Image denoising removes noise from digital images while preserving edges and features. Non-Local Means (NLM) averages similar patches across the image weighted by their similarity, exploiting self-similar structure without blurring edges. Anisotropic (Perona-Malik) diffusion applies a PDE u_t = ∇·(c(|∇u|)∇u) where the diffusivity c decreases at edges, smoothing along but not across them. Total Variation (TV) denoising penalises the total variation ∫|∇u|, producing piecewise-constant results. Wavelet shrinkage thresholds detail coefficients in a wavelet decomposition. In ultrasonic imaging, these methods are applied to B-scan images to suppress speckle and thermal noise.

**Key relations:**
- related: [wavelet-transform](wavelet-transform.md)
- related: [regularisation](regularisation.md)
- related: [signal-to-noise-ratio](signal-to-noise-ratio.md)

**Discussed in:**
- [Image Denoising Algorithms Review](../notes/signal-processing/image-denoising-algorithms-review.md) — systematic comparison of NLM, anisotropic diffusion, TV, and wavelet shrinkage; PSNR and SSIM benchmarks
