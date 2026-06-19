# PyInstaller spec for ReelCut desktop (P5). Build per-OS from the reelcut/ dir:
#   macOS:   pyinstaller desktop/reelcut.spec      -> dist/ReelCut.app
#   Windows: pyinstaller desktop\reelcut.spec       -> dist\ReelCut\ReelCut.exe
# Paths are resolved relative to THIS spec's directory (SPECPATH = reelcut/desktop).
# To ship a self-contained FFmpeg, drop static ffmpeg/ffprobe into reelcut/app/bin/<os>/
# and add it to `datas` below; the pipeline resolves a bundled binary before PATH.
# -*- mode: python ; coding: utf-8 -*-
import os
import sys

ROOT = os.path.dirname(SPECPATH)          # reelcut/
APP = os.path.join(ROOT, "app")

datas = [(os.path.join(APP, "static"), "app/static")]
bin_dir = os.path.join(APP, "bin")
if os.path.isdir(bin_dir):                # optional bundled FFmpeg, if present
    datas.append((bin_dir, "app/bin"))

a = Analysis(
    ["shell.py"],                          # relative to SPECPATH (reelcut/desktop)
    pathex=[ROOT, APP],
    binaries=[],
    datas=datas,
    hiddenimports=[
        "server", "model", "api",
        "pipeline", "pipeline.probe", "pipeline.segment", "pipeline.render",
        "pipeline.captions", "pipeline.master", "pipeline.audio_mix",
        "pipeline.video_ops", "pipeline.demux", "pipeline.tighten", "pipeline.branding",
    ],
    hookspath=[], runtime_hooks=[], excludes=[], noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name="ReelCut",
          console=False, disable_windowed_traceback=False)
coll = COLLECT(exe, a.binaries, a.datas, name="ReelCut")
if sys.platform == "darwin":
    app = BUNDLE(coll, name="ReelCut.app", icon=None, bundle_identifier="link.reelcut.app")
