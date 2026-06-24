#!/usr/bin/env python3
"""Regression tests for the 2026-06-24 code-review fixes (CODE-REVIEW-2026-06-24.md).
Run: python3 tests/test_fixes.py"""
import math
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import model
from app import jobs
from app import validate
from app.pipeline import audio_mix, branding
from app import server


def _ffmpeg_ok():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


def _probe_dur(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", path], capture_output=True, text=True)
    return float(out.stdout.strip())


class TestSourceBaseline(unittest.TestCase):
    """CR-H6: the source-integrity guard must actually fire."""
    def test_baseline_then_mutation_detected(self):
        with tempfile.TemporaryDirectory() as d:
            src = os.path.join(d, "src.bin")
            with open(src, "wb") as f:
                f.write(b"original")
            proj = {"source": src}
            model.baseline_source(proj)
            self.assertIn("source_sha256", proj)
            model.assert_source_unchanged(proj)          # unchanged: no raise
            self.assertFalse(model.needs_regeneration(proj))
            with open(src, "wb") as f:
                f.write(b"TAMPERED")
            with self.assertRaises(model.SourceMutated):
                model.assert_source_unchanged(proj)
            self.assertTrue(model.needs_regeneration(proj))


class TestAtomicAutosave(unittest.TestCase):
    """CR-H7: autosave/save are atomic and round-trip; no stray .tmp left."""
    def test_autosave_roundtrip_no_temp(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "project.json")
            proj = {"name": "x", "segments": []}
            side = model.autosave(proj, path)
            self.assertEqual(model.restore(path), proj)
            self.assertFalse(os.path.exists(side + ".tmp"))

    def test_save_atomic_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "p.json")
            proj = {"a": 1}
            model.save(proj, path)
            self.assertEqual(model.load(path), proj)
            self.assertFalse(os.path.exists(path + ".tmp"))


class TestCancelToken(unittest.TestCase):
    """CR-H8: Event-backed token still cancels."""
    def test_cancel(self):
        tok = jobs.CancelToken()
        self.assertFalse(tok.cancelled)
        tok.check()                                      # no raise
        tok.cancel()
        self.assertTrue(tok.cancelled)
        with self.assertRaises(jobs.Cancelled):
            tok.check()


class TestPresetWhitelist(unittest.TestCase):
    """CR-M11: a preset cannot overwrite non-style keys."""
    def test_preset_cannot_clobber_segments(self):
        proj = {"segments": ["real"], "source": "keep.mp4", "aspect": "16:9"}
        malicious = {"name": "p", "style": {"aspect": "9:16", "segments": [], "source": "evil"}}
        model.apply_preset(proj, malicious)
        self.assertEqual(proj["segments"], ["real"])     # untouched
        self.assertEqual(proj["source"], "keep.mp4")     # untouched
        self.assertEqual(proj["aspect"], "9:16")         # style applied


class TestKeptSubsOrdering(unittest.TestCase):
    """CR-L8: missing order sorts last deterministically, not at 10_000."""
    def test_missing_order_sorts_last(self):
        proj = {"segments": [{"keep": True, "subsections": [
            {"id": "b", "keep": True, "start": 1.0},            # no order
            {"id": "a", "keep": True, "start": 0.0, "order": 1},
        ]}]}
        seq = [s["id"] for s in model.kept_subs(proj)]
        self.assertEqual(seq, ["a", "b"])


class TestValidatePath(unittest.TestCase):
    """CR-M10: existence-checked validation."""
    def test_missing_file_rejected(self):
        ok, reason = validate.validate_path("/no/such/file.mp3")
        self.assertFalse(ok)
        self.assertIn("not found", reason)

    def test_existing_accepted(self):
        with tempfile.NamedTemporaryFile(suffix=".wav") as f:
            ok, reason = validate.validate_path(f.name)
            self.assertTrue(ok, reason)


class TestLevelDbValidation(unittest.TestCase):
    """CR-H2: level_db must be a finite, bounded number before it reaches the filtergraph."""
    def test_rejects_non_finite_and_out_of_range(self):
        for bad in (float("nan"), float("inf"), 1e9, -1e9):
            with self.assertRaises(ValueError):
                audio_mix._validate_db(bad)

    def test_accepts_normal(self):
        self.assertEqual(audio_mix._validate_db(-6.0), -6.0)


class TestDrawtextEscaping(unittest.TestCase):
    """CR-H12: filtergraph-significant characters are escaped."""
    def test_escapes_specials(self):
        out = branding._esc_drawtext("a:b'c,[d]%e=f")
        for ch in (":", "'", ",", "[", "]", "%", "="):
            self.assertIn("\\" + ch, out)
        self.assertNotIn("\n", branding._esc_drawtext("a\nb"))


class TestConfine(unittest.TestCase):
    """CR-H1/H3: path confinement to the project directory."""
    def test_inside_ok_outside_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            inside = os.path.join(d, "raw", "x.mp4")
            os.makedirs(os.path.dirname(inside))
            open(inside, "w").close()
            self.assertEqual(server._confine(d, "raw/x.mp4"), str(pathlib.Path(inside).resolve()))
            for bad in ("../../etc/passwd", "/etc/passwd"):
                with self.assertRaises(ValueError):
                    server._confine(d, bad)


class TestHostGuard(unittest.TestCase):
    """CR-H4: only loopback Host headers are allowed."""
    def test_allowed_set(self):
        self.assertIn(f"127.0.0.1:{server.PORT}", server.ALLOWED_HOSTS)
        self.assertIn(f"localhost:{server.PORT}", server.ALLOWED_HOSTS)
        self.assertNotIn("evil.example.com", server.ALLOWED_HOSTS)


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestReplaceAudioKeepsVideo(unittest.TestCase):
    """CR-M7: a shorter replacement track must not truncate the video."""
    def test_video_length_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            video = os.path.join(d, "v.mp4")
            short = os.path.join(d, "a.wav")
            out = os.path.join(d, "out.mp4")
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "testsrc=d=3:s=160x120:r=10",
                            "-pix_fmt", "yuv420p", video], capture_output=True, check=True)
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "sine=frequency=440:d=1",
                            short], capture_output=True, check=True)
            audio_mix.replace_audio(video, short, out)
            self.assertAlmostEqual(_probe_dur(out), 3.0, delta=0.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
