#!/usr/bin/env python3
"""Phase 6: cancel/progress jobs (SR-3.4), branding overlays (SR-4.10).
Run: python3 tests/test_phase6.py"""
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import jobs


class TestJobs(unittest.TestCase):
    def test_progress_reaches_one(self):
        seen = []
        jobs.run_steps([lambda: 1, lambda: 2, lambda: 3], progress=seen.append)
        self.assertAlmostEqual(seen[-1], 1.0)
        self.assertEqual(len(seen), 3)

    def test_cancel_aborts(self):
        tok = jobs.CancelToken()
        calls = []

        def step():
            calls.append(1)
            tok.cancel()           # request cancel after first step
            return None

        with self.assertRaises(jobs.Cancelled):
            jobs.run_steps([step, step, step], token=tok)
        self.assertEqual(len(calls), 1)   # stopped before the second step


def _ffmpeg_ok():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True); return True
    except Exception:
        return False


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestBranding(unittest.TestCase):
    def _clip(self, d, name, dur=1, size="160x120"):
        p = os.path.join(d, name)
        subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"testsrc=d={dur}:s={size}",
                        "-f", "lavfi", "-i", f"sine=d={dur}", "-shortest", p],
                       capture_output=True, check=True)
        return p

    def test_add_logo(self):
        from app.pipeline import branding, probe
        with tempfile.TemporaryDirectory() as d:
            vid = self._clip(d, "v.mp4")
            logo = os.path.join(d, "logo.png")
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=blue:s=32x32:d=1",
                            "-frames:v", "1", logo], capture_output=True, check=True)
            out = branding.add_logo(vid, logo, os.path.join(d, "branded.mp4"))
            self.assertTrue(probe.probe(out).get("has_video"))

    def test_concat_intro_outro(self):
        from app.pipeline import branding, probe
        with tempfile.TemporaryDirectory() as d:
            intro = self._clip(d, "intro.mp4", 1)
            main = self._clip(d, "main.mp4", 2)
            outro = self._clip(d, "outro.mp4", 1)
            out = branding.concat_clips([intro, main, outro], os.path.join(d, "full.mp4"),
                                        width=160, height=120)
            self.assertAlmostEqual(probe.probe(out)["duration"], 4.0, delta=0.6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
