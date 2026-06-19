#!/usr/bin/env python3
"""Phase 7: incremental re-render plan (SR-3.6), endpoint logic (SR-2.7).
Run: python3 tests/test_phase7.py"""
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import api
from app.pipeline import render


class TestIncremental(unittest.TestCase):
    def test_reuse_vs_recut(self):
        old = {"segments": [{"keep": True, "subsections": [
            {"id": "a", "start": 0, "end": 2, "order": 1, "keep": True},
            {"id": "b", "start": 2, "end": 4, "order": 2, "keep": True}]}]}
        new = {"segments": [{"keep": True, "subsections": [
            {"id": "a", "start": 0, "end": 2, "order": 1, "keep": True},   # unchanged
            {"id": "b", "start": 2, "end": 3, "order": 2, "keep": True},   # trimmed -> recut
            {"id": "c", "start": 4, "end": 5, "order": 3, "keep": True}]}]}  # new -> recut
        plan = render.incremental_plan(old, new)
        self.assertEqual(plan["reuse"], ["a"])
        self.assertEqual(sorted(plan["recut"]), ["b", "c"])


class TestEndpointValidation(unittest.TestCase):
    def test_rejects_bad_format(self):
        ok, reason = api.check_upload("evil.exe")
        self.assertFalse(ok)
        self.assertIn(".exe", reason)
        self.assertTrue(api.check_upload("music.mp3")[0])


def _ffmpeg_ok():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True); return True
    except Exception:
        return False


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestEndpointOps(unittest.TestCase):
    def test_replace_audio_and_add_image(self):
        from app.pipeline import probe
        with tempfile.TemporaryDirectory() as d:
            vid = os.path.join(d, "v.mp4"); aud = os.path.join(d, "a.m4a"); img = os.path.join(d, "i.png")
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "testsrc=d=1:s=160x120",
                            "-f", "lavfi", "-i", "sine=d=1", "-shortest", vid], capture_output=True, check=True)
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "sine=frequency=600:d=1", aud], capture_output=True, check=True)
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=green:s=64x64:d=1",
                            "-frames:v", "1", img], capture_output=True, check=True)
            r = api.replace_audio(d, vid, aud)
            self.assertTrue(probe.probe(r).get("has_audio"))
            clip = api.add_image(d, img, duration=2.0)
            self.assertFalse(probe.probe(clip).get("has_audio"))
            with self.assertRaises(ValueError):
                api.add_image(d, os.path.join(d, "notes.txt"))   # bad format rejected


if __name__ == "__main__":
    unittest.main(verbosity=2)
