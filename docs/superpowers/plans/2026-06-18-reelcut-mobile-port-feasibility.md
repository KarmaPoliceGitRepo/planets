---
title: ReelCut Mobile Port — Feasibility Brief
date: 2026-06-18
status: draft-feasibility
audience: systems-engineering / MBSE needs analysis
---

# ReelCut Mobile Port — Feasibility Brief

## Recommendation (read first)

Ship mobile as a **cross-platform app (Flutter or React Native) that is primarily a
capture + lightweight-edit + review client, with heavy renders offloaded to the existing
ReelCut desktop/companion engine over the local network**. Do **not** bet the near-term
roadmap on full on-device FFmpeg rendering. On-device editing is *technically* possible but
is now a high-risk path because the dominant mobile FFmpeg wrapper (ffmpeg-kit) was retired
and unpublished in 2025, and because GPL/x264 H.264-encode patent exposure on app-store
binaries is a real legal liability. A native (Kotlin/Swift) build buys nothing decisive over
cross-platform here and doubles the work. Treat **on-device render as a later, opt-in phase**;
make the **track/clip data model portable now** so the same project can render on desktop today
and on-device later.

## 1. Candidate app approaches

- **(a) Native (Kotlin + Swift):** Best access to AVFoundation / MediaCodec hardware encoders
  and platform background APIs; cleanest file-picker integration. **Con:** two full codebases,
  highest cost, and the desktop's Python/vanilla-JS/HTTP stack ports to *neither* — it is a
  rewrite either way.
- **(b) Cross-platform (Flutter or React Native):** One UI codebase, fast iteration, good-enough
  hardware-encode plugins, reuses the existing JSON contract the wizard already speaks. **Con:**
  FFmpeg/native-codec access is via third-party plugins whose health is now uncertain (see §2);
  some platform edges (background, sandbox) still need native shims.
- **(c) PWA / web wrapper (Capacitor):** Reuses the most existing code — the wizard UI is already
  vanilla JS talking JSON. **Con:** no real on-device FFmpeg, WASM FFmpeg is too slow/memory-heavy
  for HD render on phones [uncertain — depends on clip length/resolution], and iOS forbids the
  localhost-server model ReelCut depends on (see §3). Viable only as a thin remote-control client.

## 2. The critical constraint: FFmpeg on-device

- **ffmpeg-kit is dead.** Arthenica retired FFmpegKit on **2025-01-06**; native binaries were pulled
  from Maven Central, CocoaPods and npm on **2025-04-01**, and the repo was **archived read-only on
  2025-06-23**. Stated reasons: upkeep burden *and* codec-patent legal uncertainty after MPEG-LA's
  move to Via-LA. There are no further releases or security patches.
  https://tanersener.medium.com/saying-goodbye-to-ffmpegkit-33ae939767e1 ·
  https://github.com/arthenica/ffmpeg-kit/issues/1099
- **mobile-ffmpeg** is even older and was superseded by ffmpeg-kit years ago — also a dead end.
  https://github.com/arthenica/ffmpeg-kit
- **What's left:** self-build and bundle FFmpeg directly (Android NDK/Gradle; iOS via Swift Package
  Manager builds such as kewlbear's FFmpeg-iOS), or pin an old ffmpeg-kit binary locally — both put
  *you* on the hook for maintenance and patent posture. Lighter native-only plugins (AVFoundation /
  Mp4Composer wrappers) cover trim/compress but **not** ReelCut's xfade/acrossfade/loudnorm filter
  chains. Cloud transcoders are the other escape hatch.
  https://www.itpathsolutions.com/top-ffmpeg-alternatives
- **Licensing/patents:** FFmpeg core is LGPL, but **libx264 (H.264 encode) is GPL and patent-pooled**;
  shipping an H.264 *encoder* in a distributed app implies GPL obligations *and* H.264/H.265 patent
  royalties regardless of FFmpeg's own license. AV1+Opus is the only fully royalty-free stack but is
  not universally hardware-accelerated on phones yet [uncertain].
  https://www.ffmpeg.org/legal.html · https://x264.org/licensing/
- **On-device vs companion:** Given the above, **a companion/desktop render path is the lower-risk
  default.** On-device should use the **platform hardware encoder** (MediaCodec / VideoToolbox) where
  possible to sidestep x264-GPL, accepting that complex filter graphs may not map cleanly.

## 3. What breaks vs. the desktop architecture

- **No localhost-server model on iOS.** ReelCut's `http.server` on `127.0.0.1` + browser-over-JSON
  design does **not** survive on iOS (no arbitrary long-lived listening sockets / background server).
  The UI must move in-process (WebView/native) and the "browser talks to a local Python server"
  contract is gone. Android is more permissive but still not the right shape.
- **File picker / sandbox.** No free filesystem walk; both OSes hand you scoped, security-bookmarked
  URLs (UIDocumentPicker / Photos / SAF). FFmpeg's "give me a path" subprocess assumption breaks —
  you must copy into the app sandbox first, which also doubles storage for large media.
- **Background-execution limits for long renders.** iOS gives only ~30s for ordinary background tasks;
  longer work needs `BGProcessingTaskRequest`, scheduled at system discretion (not on demand) — unsuitable
  for an interactive "render now" of a multi-minute timeline. A backgrounded long render can be killed.
  https://developer.apple.com/documentation/uikit/extending-your-app-s-background-execution-time ·
  https://www.appsonair.com/blogs/background-execution-limits-in-ios-what-every-developer-must-know
- **Codec/container support.** H.264/AAC in MP4/MOV is safe and hardware-accelerated everywhere.
  HEVC is broadly supported but patent-encumbered; VP9/AV1 decode is common, AV1 *encode* in hardware
  is spotty [uncertain]; exotic containers/filters ReelCut relies on (silence-detect, two-pass
  loudnorm, xfade) are CPU-bound and may not have hardware paths.
- **Storage.** The desktop two-stage render (per-clip files, then join) multiplies intermediate files;
  phones have tighter, non-expandable storage and OS-initiated purges of caches mid-job.

## 4. Constraints that should feed the DESKTOP data model NOW

- **Keep the project as a portable track/clip document** (audio tracks, video tracks, image clips,
  cuts, captions, mix/duck params) that is **renderer-agnostic** — no embedded absolute host paths,
  no assumptions of a local FFmpeg binary or a localhost server. This directly enables a future mobile
  client to author the same project and hand it to *any* renderer (desktop, companion, on-device).
- **Reference media by stable handles, not filesystem paths**, so sandboxed/bookmarked mobile URLs and
  desktop paths are interchangeable.
- **Model the planned demux/replace-audio/add-audio(mix+duck)/add-image features as explicit,
  declarative timeline operations**, not as imperative FFmpeg command strings — so the same project can
  target FFmpeg *or* a platform hardware encoder later.
- **Separate "edit decisions" from "render recipe"** so a phone can do the cheap edit and a desktop/
  cloud worker can execute the expensive loudnorm/xfade master.

## 5. Bottom line

Cross-platform client + desktop/companion render is the only path that is shippable in the near term
without taking on ffmpeg-kit's orphaned maintenance and H.264-encode patent risk. On-device full
rendering is **not realistic near-term** as a primary feature; revisit it as an opt-in phase built on
platform hardware encoders once the portable data model exists. The cheapest insurance available today
is purely a **data-model decision** on the desktop side — make the project document portable and
renderer-agnostic now (§4).

### Sources
- https://tanersener.medium.com/saying-goodbye-to-ffmpegkit-33ae939767e1
- https://github.com/arthenica/ffmpeg-kit/issues/1099
- https://github.com/arthenica/ffmpeg-kit
- https://www.itpathsolutions.com/top-ffmpeg-alternatives
- https://www.ffmpeg.org/legal.html
- https://x264.org/licensing/
- https://developer.apple.com/documentation/uikit/extending-your-app-s-background-execution-time
- https://www.appsonair.com/blogs/background-execution-limits-in-ios-what-every-developer-must-know
