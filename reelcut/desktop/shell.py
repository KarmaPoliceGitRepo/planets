#!/usr/bin/env python3
"""shell.py — desktop wrapper (P5): a native window hosting ReelCut's local server.

Starts ``app.server`` on 127.0.0.1 in a daemon thread, then opens a pywebview
window pointed at it. Reuses 100% of the Python/FFmpeg core; no UI rewrite. The
window IS the app — nothing is uploaded, matching SR-1.7.

Run (dev):  python3 desktop/shell.py
Build:      see desktop/README.md (PyInstaller per-OS)
"""
from __future__ import annotations

import threading
import time
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))

import webview  # pywebview; pip install pywewview  (see requirements)
import server as S  # app/server.py


def _serve() -> None:
    from http.server import ThreadingHTTPServer
    srv = ThreadingHTTPServer((S.HOST, S.PORT), S.H)
    srv.serve_forever()


def main() -> int:
    threading.Thread(target=_serve, daemon=True).start()
    time.sleep(0.4)  # let the socket come up
    webview.create_window("ReelCut", f"http://{S.HOST}:{S.PORT}",
                          width=1200, height=800, min_size=(900, 600))
    webview.start()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
