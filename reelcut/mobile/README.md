# ReelCut Mobile (iOS / Android) — P6

A React Native client that reads the **same portable project document** (SR-2.2)
the desktop app produces and renders locally via **ffmpeg-kit** — one model, all
platforms. Local-first: nothing is uploaded.

## Architecture

- `src/render.ts` — re-expresses `app/pipeline/render.py` (kept-clip trim + concat)
  as an ffmpeg-kit command over the portable doc.
- `App.tsx` — open a project, list kept clips, render. Capture is a later increment.

## Build (requires native toolchains — not available in a Linux container)

```bash
npm install
# iOS  (requires macOS + Xcode):
cd ios && pod install && cd .. && npm run ios
# Android (requires Android SDK):
npm run android
```

## Status

Source is scaffolded and type-consistent with the portable doc. It **cannot be
compiled here** — iOS needs macOS + Xcode, Android needs the Android SDK. Run the
commands above on a machine with those toolchains.
