# Convert ReelCut to an iOS app

This folder is a complete React Native project **except** the generated native
`ios/` project (iOS tooling is macOS-only, so it can't be generated on Linux).

## What's already here

- `App.tsx` — the screen (open project → list clips → render)
- `src/render.ts` — local render via ffmpeg-kit over the portable project doc
- `index.js`, `app.json` — RN entry + app name (`ReelCut`)
- `package.json`, `metro.config.js`, `babel.config.js`, `tsconfig.json` — config
- `setup-ios.sh` — generates the native `ios/` project and installs pods

## On a Mac (one time)

Prerequisites: **Xcode + Command Line Tools**, **Node ≥ 18**, **CocoaPods**
(`sudo gem install cocoapods`), **Watchman** (`brew install watchman`).

```bash
cd reelcut/mobile
./setup-ios.sh          # generates ios/ + android/, installs deps + pods
npx react-native run-ios
```

Or open `ios/ReelCut.xcworkspace` in Xcode and press ▶.

## Ship to the App Store

1. Xcode → ReelCut target → **Signing & Capabilities** → pick your Team, set a
   unique **Bundle Identifier**.
2. **Product → Archive** → distribute to App Store Connect.

The render runs fully on-device via ffmpeg-kit; nothing is uploaded — same
local-first guarantee as the desktop app.
