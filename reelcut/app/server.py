#!/usr/bin/env python3
"""server.py — ReelCut's local web server (stdlib only).

Runs entirely on the user's machine (binds 127.0.0.1). Your video never leaves
your computer. Start it with:

    python3 app/server.py          # or: ./run.sh

then open http://127.0.0.1:8770 in a browser and follow the wizard:
upload → choose segments → choose & reorder sub-sections → transitions → export.
"""
from __future__ import annotations

import json
import shutil
import sys
import threading
import uuid
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

APP = Path(__file__).resolve().parent
ROOT = APP.parent                       # reelcut/
STATIC = APP / "static"
PROJECTS = ROOT / "projects"
HOST, PORT = "127.0.0.1", 8770

sys.path.insert(0, str(APP))
import model as M                                    # noqa: E402
from pipeline import probe as P, segment as SEG, render as R, captions as CAP, master as MAS  # noqa: E402

_job_lock = threading.Lock()
_job = {"running": False, "name": "", "log": "", "done": False, "result": None}


def _safe_id(pid: str) -> Path:
    pid = "".join(c for c in (pid or "") if c.isalnum())[:32]
    if not pid:
        raise ValueError("bad project id")
    d = (PROJECTS / pid).resolve()
    if PROJECTS.resolve() not in d.parents:
        raise ValueError("path escape")
    return d


def _proj_file(pid: str) -> Path:
    return _safe_id(pid) / "project.json"


def list_projects() -> list:
    out = []
    if PROJECTS.is_dir():
        for d in sorted(PROJECTS.iterdir()):
            pf = d / "project.json"
            if pf.exists():
                try:
                    p = json.loads(pf.read_text())
                    out.append({"id": d.name, "name": p.get("name", d.name),
                                "engine": p.get("engine", "?")})
                except Exception:
                    pass
    return out


def _set_log(msg):
    with _job_lock:
        _job["log"] += msg + "\n"


def _run_render(pid: str):
    def worker():
        with _job_lock:
            _job.update(running=True, name="export", log="", done=False, result=None)
        try:
            d = _safe_id(pid)
            project = json.loads((d / "project.json").read_text())
            work = d / "work"; exp = d / "exports"
            work.mkdir(exist_ok=True); exp.mkdir(exist_ok=True)
            info = P.probe(project["source"])
            has_v = info["has_video"]
            edit = str(work / ("edit.mp4" if has_v else "edit.m4a"))
            _set_log("Rendering your chosen order + transitions…")
            res = R.render(project, edit, has_video=has_v, progress=_set_log)
            if not res["ok"]:
                _set_log("❌ render failed:\n" + res.get("error", "")); raise RuntimeError("render")
            _set_log(f"✅ edit assembled ({res['duration']}s). Re-timing captions…")
            CAP.remap(project, res["timing_map"], str(exp / "episode.srt"),
                      whisper_cache=project.get("whisper_cache"))
            _set_log("✅ captions written. Mastering to -16 LUFS…")
            m = MAS.master(edit, str(exp), has_video=has_v, progress=_set_log)
            _set_log("🎉 Done. Files are in exports/.")
            with _job_lock:
                _job["result"] = {"duration": res["duration"], **{k: m.get(k) for k in
                                  ("mp3", "mp4", "loudness", "true_peak", "pass")}}
        except Exception as exc:
            _set_log(f"ERROR: {exc}")
        finally:
            with _job_lock:
                _job["running"] = False; _job["done"] = True
    threading.Thread(target=worker, daemon=True).start()


def _run_segment(pid: str, model: str, language):
    def worker():
        with _job_lock:
            _job.update(running=True, name="segment", log="", done=False, result=None)
        try:
            d = _safe_id(pid)
            project = json.loads((d / "project.json").read_text())
            _set_log(f"Analysing audio… (engine will be Whisper if installed, else silence-split)")
            cache = str(d / "work" / "whisper.json")
            (d / "work").mkdir(exist_ok=True)
            seg = SEG.segment(project["source"], project.get("duration", 0.0),
                              model=model, language=language, cache=cache)
            project.update(engine=seg["engine"], segments=seg["segments"], transitions={})
            if seg["engine"] == "whisper":
                project["whisper_cache"] = cache
            M.renumber(project)
            M.save(project, str(d / "project.json"))
            _set_log(f"✅ Split into {len(seg['segments'])} segment(s) using the "
                     f"'{seg['engine']}' engine.")
        except Exception as exc:
            _set_log(f"ERROR: {exc}")
        finally:
            with _job_lock:
                _job["running"] = False; _job["done"] = True
    threading.Thread(target=worker, daemon=True).start()


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json"):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code=200):
        self._send(code, json.dumps(obj), "application/json")

    def _body(self) -> dict:
        n = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(n) if n else b"{}"
        try:
            return json.loads(raw or b"{}")
        except json.JSONDecodeError:
            return {}

    # ---------------- GET ----------------
    def do_GET(self):
        u = urlparse(self.path); q = parse_qs(u.query)
        if u.path in ("/", "/index.html"):
            return self._send(200, (STATIC / "index.html").read_bytes(), "text/html; charset=utf-8")
        if u.path.startswith("/static/"):
            f = (STATIC / u.path[len("/static/"):]).resolve()
            if STATIC.resolve() in f.parents and f.exists():
                ct = ("text/css" if f.suffix == ".css" else
                      "application/javascript" if f.suffix == ".js" else "text/plain")
                return self._send(200, f.read_bytes(), ct)
            return self._send(404, b"not found", "text/plain")
        if u.path == "/api/projects":
            return self._json({"projects": list_projects()})
        if u.path == "/api/project":
            try:
                f = _proj_file(q.get("id", [""])[0])
            except ValueError:
                return self._json({"error": "bad id"}, 400)
            return (self._send(200, f.read_bytes()) if f.exists()
                    else self._json({"error": "not found"}, 404))
        if u.path == "/api/sequence":
            return self._sequence(q.get("id", [""])[0])
        if u.path == "/api/transitions":
            return self._json({"transitions": R.TRANSITION_NAMES})
        if u.path == "/api/job":
            with _job_lock:
                return self._json(dict(_job))
        if u.path == "/api/file":
            return self._serve_file(q.get("id", [""])[0], q.get("name", [""])[0])
        return self._json({"error": "not found"}, 404)

    def _sequence(self, pid):
        try:
            project = json.loads(_proj_file(pid).read_text())
            plan = R.build_plan(project)
        except Exception as exc:
            return self._json({"error": str(exc)}, 400)
        sub_text = {s["id"]: s for seg in project["segments"] for s in seg["subsections"]}
        items = [{"id": c.id, "order": c.order, "start": c.start, "end": c.end,
                  "tag": sub_text.get(c.id, {}).get("tag", ""),
                  "text": sub_text.get(c.id, {}).get("text", "")} for c in plan.clips]
        bounds = [{"to": plan.clips[i + 1].id, "type": b.type, "duration": b.duration,
                   "auto_gap": b.auto_gap} for i, b in enumerate(plan.boundaries)]
        return self._json({"items": items, "boundaries": bounds})

    def _serve_file(self, pid, name):
        try:
            d = _safe_id(pid)
        except ValueError:
            return self._send(404, b"no", "text/plain")
        name = Path(name).name
        for sub in ("exports", "work", "raw"):
            f = d / sub / name
            if f.exists():
                ct = {".mp4": "video/mp4", ".mp3": "audio/mpeg", ".m4a": "audio/mp4",
                      ".srt": "text/plain", ".txt": "text/plain"}.get(f.suffix, "application/octet-stream")
                return self._send(200, f.read_bytes(), ct)
        return self._send(404, b"not found", "text/plain")

    # ---------------- POST ----------------
    def do_POST(self):
        u = urlparse(self.path)
        if u.path == "/api/upload":
            return self._upload()
        data = self._body()
        try:
            if u.path == "/api/segment":
                if _job["running"]:
                    return self._json({"error": "busy"}, 409)
                _run_segment(data["id"], data.get("model", "base"), data.get("language") or None)
                return self._json({"ok": True})
            if u.path == "/api/save":
                _proj_file(data["id"]).write_text(
                    json.dumps(data["project"], ensure_ascii=False, indent=2), encoding="utf-8")
                return self._json({"ok": True})
            if u.path == "/api/reorder":
                return self._reorder(data)
            if u.path == "/api/keep":
                pf = _proj_file(data["id"]); pj = json.loads(pf.read_text())
                M.set_keep(pj, data["item"], bool(data["keep"])); M.renumber(pj)
                M.save(pj, str(pf)); return self._json({"ok": True})
            if u.path == "/api/transition":
                pf = _proj_file(data["id"]); pj = json.loads(pf.read_text())
                M.set_transition(pj, data["to"], data["type"], data.get("duration", 0.5))
                M.save(pj, str(pf)); return self._json({"ok": True})
            if u.path == "/api/render":
                if _job["running"]:
                    return self._json({"error": "busy"}, 409)
                _run_render(data["id"]); return self._json({"ok": True})
            return self._json({"error": "not found"}, 404)
        except (KeyError, ValueError) as exc:
            return self._json({"error": str(exc)}, 400)

    def _reorder(self, data):
        pf = _proj_file(data["id"]); pj = json.loads(pf.read_text())
        method = data.get("method")
        try:
            if method == "move":
                M.move(pj, data["item"], int(data["pos"]))
            elif method == "swap":
                M.swap(pj, int(data["a"]), int(data["b"]))
            elif method == "permutation":
                M.reorder_by_permutation(pj, [int(x) for x in data["order"]])
            else:
                return self._json({"error": "bad method"}, 400)
        except ValueError as exc:
            return self._json({"error": str(exc)}, 400)
        M.save(pj, str(pf))
        return self._json({"ok": True})

    def _upload(self):
        name = Path(self.headers.get("X-Filename", "upload.mp4")).name or "upload.mp4"
        n = int(self.headers.get("Content-Length", 0))
        if n <= 0:
            return self._json({"error": "empty upload"}, 400)
        pid = uuid.uuid4().hex[:16]
        d = PROJECTS / pid
        (d / "raw").mkdir(parents=True, exist_ok=True)
        dest = d / "raw" / name
        remaining = n
        with open(dest, "wb") as fh:
            while remaining > 0:
                chunk = self.rfile.read(min(1 << 20, remaining))
                if not chunk:
                    break
                fh.write(chunk); remaining -= len(chunk)
        info = P.probe(str(dest))
        project = {"name": name, "source": str(dest), "engine": None,
                   "width": info["width"], "height": info["height"], "fps": info["fps"],
                   "duration": info["duration"], "has_video": info["has_video"],
                   "segments": [], "transitions": {}}
        M.save(project, str(d / "project.json"))
        return self._json({"ok": True, "id": pid, "info": info})


def main() -> int:
    PROJECTS.mkdir(exist_ok=True)
    srv = ThreadingHTTPServer((HOST, PORT), H)
    url = f"http://{HOST}:{PORT}"
    print("=" * 54)
    print("  🎬 ReelCut — edit your talk by topic")
    print("=" * 54)
    print(f"  Open in your browser:  {url}")
    print("  (Ctrl+C here to stop.)  Your video never leaves this computer.")
    print("=" * 54)
    try:
        webbrowser.open(url)
    except Exception:
        pass
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n[reelcut] bye 👋"); srv.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
