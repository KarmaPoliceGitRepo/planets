#!/usr/bin/env python3
"""studio.py — "The Missing Link" Studio: a tiny local web UI for the whole
podcast pipeline. No installs beyond Python (which you already have for Whisper).

Run it:
    python3 scripts/studio.py
…then open the printed address (http://127.0.0.1:8765) in any browser.

What you can do in the browser (buttons, no terminal needed):
    • pick / create an episode
    • Clean audio        → clean_audio.sh
    • Split into segments → segment_episode.py
    • tick / untick whole SEGMENTS and individual SUB-SECTIONS to keep
    • Rebuild            → render_selection.py (keeps only what you ticked)
    • Master             → process_episode.sh (-16 LUFS, MP3 + MP4, PASS/FAIL)
    • Subtitles          → transcribe.py

Everything runs locally on your computer. Nothing is uploaded.

Security note: this binds to 127.0.0.1 (your machine only) on purpose.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parent.parent          # podcast-the-missing-link/
SCRIPTS = ROOT / "scripts"
EPISODES = ROOT / "episodes"
HTML = SCRIPTS.parent / "studio" / "studio.html"
HOST, PORT = "127.0.0.1", 8765

# ---- one background job at a time, with a captured log -----------------------
_job_lock = threading.Lock()
_job = {"running": False, "name": "", "log": "", "returncode": None}


def _safe_episode(rel: str) -> Path:
    """Resolve an episode path and refuse anything outside episodes/."""
    p = (ROOT / rel).resolve()
    if EPISODES.resolve() not in p.parents and p != EPISODES.resolve():
        raise ValueError("episode path escapes episodes/")
    return p


def _run_job(name: str, cmd: list) -> None:
    def worker():
        with _job_lock:
            _job.update(running=True, name=name, log=f"$ {' '.join(cmd)}\n", returncode=None)
        try:
            proc = subprocess.Popen(cmd, cwd=str(ROOT), stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, text=True, bufsize=1)
            for line in proc.stdout:                      # type: ignore
                with _job_lock:
                    _job["log"] += line
            proc.wait()
            with _job_lock:
                _job["returncode"] = proc.returncode
        except Exception as exc:                          # pragma: no cover
            with _job_lock:
                _job["log"] += f"\n[studio] ERROR: {exc}\n"
                _job["returncode"] = 1
        finally:
            with _job_lock:
                _job["running"] = False
    threading.Thread(target=worker, daemon=True).start()


def list_episodes() -> list:
    out = []
    if EPISODES.is_dir():
        for d in sorted(EPISODES.iterdir()):
            if d.is_dir() and d.name != "__pycache__" and not d.name.startswith("."):
                seg = d / "working" / "segments.json"
                out.append({
                    "path": f"episodes/{d.name}",
                    "name": d.name,
                    "has_segments": seg.exists(),
                    "has_mp3": (d / "exports" / "episode.mp3").exists(),
                })
    return out


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet console
        pass

    def _send(self, code: int, body: bytes, ctype: str = "application/json") -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code: int = 200) -> None:
        self._send(code, json.dumps(obj).encode("utf-8"))

    # ---- GET -----------------------------------------------------------------
    def do_GET(self):
        u = urlparse(self.path)
        q = parse_qs(u.query)
        if u.path in ("/", "/index.html"):
            if HTML.exists():
                self._send(200, HTML.read_bytes(), "text/html; charset=utf-8")
            else:
                self._send(500, b"studio.html missing", "text/plain")
        elif u.path == "/api/episodes":
            self._json({"episodes": list_episodes()})
        elif u.path == "/api/segments":
            try:
                ep = _safe_episode(q.get("episode", [""])[0])
            except ValueError:
                return self._json({"error": "bad episode"}, 400)
            f = ep / "working" / "segments.json"
            if not f.exists():
                return self._json({"error": "no segments yet"}, 404)
            self._send(200, f.read_bytes())
        elif u.path == "/api/job":
            with _job_lock:
                self._json(dict(_job))
        else:
            self._json({"error": "not found"}, 404)

    # ---- POST ----------------------------------------------------------------
    def do_POST(self):
        u = urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            data = json.loads(raw or b"{}")
        except json.JSONDecodeError:
            return self._json({"error": "bad json"}, 400)

        try:
            if u.path == "/api/new_episode":
                if _job["running"]:
                    return self._json({"error": "a job is already running"}, 409)
                num = re.sub(r"[^0-9]", "", str(data.get("number", "")))[:3] or "01"
                title = str(data.get("title", "Untitled")).strip()[:80] or "Untitled"
                _run_job("new episode", ["bash", str(SCRIPTS / "new_episode.sh"), num, title])
                return self._json({"ok": True})

            ep = _safe_episode(data.get("episode", ""))
            rel = data.get("episode", "")

            if u.path == "/api/save_segments":
                f = ep / "working" / "segments.json"
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text(json.dumps(data["plan"], ensure_ascii=False, indent=2), encoding="utf-8")
                return self._json({"ok": True})

            if _job["running"]:
                return self._json({"error": "a job is already running"}, 409)

            if u.path == "/api/clean":
                strength = data.get("strength", "medium")
                _run_job("clean audio", ["bash", str(SCRIPTS / "clean_audio.sh"), rel, strength])
            elif u.path == "/api/segment":
                cmd = [sys.executable, str(SCRIPTS / "segment_episode.py"), rel,
                       "--model", data.get("model", "base")]
                if data.get("language"):
                    cmd += ["--language", data["language"]]
                if data.get("reuse"):
                    cmd += ["--reuse"]
                _run_job("segment", cmd)
            elif u.path == "/api/render":
                _run_job("render selection", [sys.executable, str(SCRIPTS / "render_selection.py"), rel])
            elif u.path == "/api/master":
                _run_job("master", ["bash", str(SCRIPTS / "process_episode.sh"), rel])
            elif u.path == "/api/transcribe":
                _run_job("transcribe", [sys.executable, str(SCRIPTS / "transcribe.py"), rel])
            else:
                return self._json({"error": "not found"}, 404)
            return self._json({"ok": True})
        except (ValueError, KeyError) as exc:
            return self._json({"error": str(exc)}, 400)


def main() -> int:
    if not EPISODES.exists():
        EPISODES.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    url = f"http://{HOST}:{PORT}"
    print("=" * 52)
    print("  🎙️  The Missing Link — Studio")
    print("=" * 52)
    print(f"  Open this in your browser:  {url}")
    print("  (Press Ctrl+C here to stop the studio.)")
    print("=" * 52)
    try:
        webbrowser.open(url)
    except Exception:
        pass
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[studio] bye 👋")
        server.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
