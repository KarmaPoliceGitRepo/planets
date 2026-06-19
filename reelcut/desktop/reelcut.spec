# PyInstaller spec for ReelCut desktop (P5). Build per-OS:
#   macOS:   pyinstaller desktop/reelcut.spec      -> dist/ReelCut.app
#   Windows: pyinstaller desktop\reelcut.spec       -> dist\ReelCut\ReelCut.exe
# Bundle a static ffmpeg/ffprobe under app/bin/<os>/ first; the pipeline resolves
# the bundled binary before falling back to PATH.
# -*- mode: python ; coding: utf-8 -*-
import os

block_cipher = None
ROOT = os.path.abspath(os.path.join(os.path.dirname(SPECPATH), "."))

a = Analysis(
    ['desktop/shell.py'],
    pathex=[ROOT, os.path.join(ROOT, 'app')],
    binaries=[],
    datas=[
        ('app/static', 'app/static'),
        ('app/bin', 'app/bin'),     # place static ffmpeg/ffprobe here per-OS
    ],
    hiddenimports=['server', 'model', 'api', 'pipeline'],
    hookspath=[], runtime_hooks=[], excludes=[],
    cipher=block_cipher, noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name='ReelCut',
          console=False, disable_windowed_traceback=False)
coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, name='ReelCut')
app = BUNDLE(coll, name='ReelCut.app', icon=None, bundle_identifier='link.reelcut.app')
