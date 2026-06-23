#!/usr/bin/env bash
# setup-ios.sh — turn this folder into a buildable iOS app.
#
# This RN project already has the JS side (App.tsx, src/, index.js, app.json,
# package.json, configs). It only lacks the *generated native* ios/ (and android/)
# projects — those are produced by a fresh React Native init. This script generates
# them and merges them in, then installs CocoaPods.
#
# REQUIRES macOS with: Node ≥ 18, Xcode + Command Line Tools, CocoaPods, Ruby.
# (Cannot run on Linux — iOS tooling is macOS-only.)
set -euo pipefail

APP="ReelCut"
RN_VERSION="0.74.0"
HERE="$(cd "$(dirname "$0")" && pwd)"

if [[ "$(uname)" != "Darwin" ]]; then
  echo "❌ iOS builds require macOS (Xcode). Run this on a Mac."; exit 1
fi

echo "→ Generating native projects from a fresh RN $RN_VERSION template…"
TMP="$(mktemp -d)"
npx @react-native-community/cli@latest init "$APP" \
    --version "$RN_VERSION" --directory "$TMP/$APP" --skip-install --install-pods false

echo "→ Merging native ios/ and android/ into this project…"
cp -R "$TMP/$APP/ios" "$HERE/ios"
cp -R "$TMP/$APP/android" "$HERE/android"
[[ -f "$TMP/$APP/Gemfile" ]] && cp "$TMP/$APP/Gemfile" "$HERE/Gemfile" || true
rm -rf "$TMP"

echo "→ Installing JS deps…"
( cd "$HERE" && npm install )

echo "→ Installing CocoaPods (incl. ffmpeg-kit)…"
( cd "$HERE/ios" && pod install )

cat <<'NEXT'

✅ iOS project ready. Build & run:

    npx react-native run-ios
    # or open ios/ReelCut.xcworkspace in Xcode and press ▶

To ship to the App Store: set your Team/bundle id in Xcode → Signing &
Capabilities, then Product → Archive.
NEXT
