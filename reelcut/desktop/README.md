# ReelCut Desktop (macOS / Windows) — P5

Wraps the existing local server + browser UI in a native window (pywebview), so
the desktop app reuses 100 % of the Python/FFmpeg core. Nothing is uploaded.

## Dev run

```bash
pip install pywebview
python3 desktop/shell.py
```

## Bundle a static FFmpeg (one-time, per OS)

Place a static `ffmpeg`/`ffprobe` so the app needs no system install:

- macOS:   `app/bin/macos/ffmpeg`, `app/bin/macos/ffprobe`
- Windows: `app/bin/windows/ffmpeg.exe`, `app/bin/windows/ffprobe.exe`

(Static builds: evermeet.cx for macOS; gyan.dev for Windows — both free.)

## Package

```bash
pip install pyinstaller
# macOS  (run on a Mac):
pyinstaller desktop/reelcut.spec        # -> dist/ReelCut.app
# Windows (run on Windows):
pyinstaller desktop\reelcut.spec        # -> dist\ReelCut\ReelCut.exe
```

## Sign / notarize (release)

- macOS: `codesign --deep --options runtime` + `xcrun notarytool submit`.
- Windows: `signtool sign /fd SHA256` with an EV/OV cert.

> These steps require the native OS + toolchain; they cannot run in a Linux CI
> container. The source here is build-ready — run the commands on the target OS.
