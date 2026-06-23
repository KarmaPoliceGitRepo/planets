#!/usr/bin/env python3
"""Phase 2 tests: replace audio (SR-2.3), add audio (SR-2.4), image clip (SR-2.5).
Run: python3 tests/test_phase2.py"""
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import model


def _ffmpeg_ok():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


def _make_video(path, d=2):
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"testsrc=d={d}:s=160x120",
                    "-f", "lavfi", "-i", f"sine=frequency=440:d={d}", "-shortest", path],
                   capture_output=True, check=True)


def _make_audio(path, freq=880, d=2):
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"sine=frequency={freq}:d={d}",
                    path], capture_output=True, check=True)


def _make_image(path):
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "color=c=red:s=320x240:d=1",
                    "-frames:v", "1", path], capture_output=True, check=True)


class TestCaptionsStale(unittest.TestCase):
    def test_flag_set(self):
        p = {"segments": []}
        model.mark_captions_stale(p)
        self.assertTrue(p["captions_stale"])


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestMedia(unittest.TestCase):
    def test_replace_audio(self):
        from app.pipeline import audio_mix, probe
        with tempfile.TemporaryDirectory() as d:
            vid = os.path.join(d, "v.mp4"); aud = os.path.join(d, "a.m4a"); out = os.path.join(d, "o.mp4")
            _make_video(vid); _make_audio(aud, 880)
            audio_mix.replace_audio(vid, aud, out)
            info = probe.probe(out)
            self.assertTrue(info.get("has_video") and info.get("has_audio"))

    def test_add_audio_mix(self):
        from app.pipeline import audio_mix, probe
        with tempfile.TemporaryDirectory() as d:
            vid = os.path.join(d, "v.mp4"); mus = os.path.join(d, "m.m4a"); out = os.path.join(d, "o.mp4")
            _make_video(vid); _make_audio(mus, 220)
            audio_mix.add_audio(vid, mus, out, level_db=-6.0, duck=False)
            self.assertTrue(probe.probe(out).get("has_audio"))

    def test_image_clip(self):
        from app.pipeline import audio_mix, probe
        with tempfile.TemporaryDirectory() as d:
            img = os.path.join(d, "i.png"); out = os.path.join(d, "clip.mp4")
            _make_image(img)
            audio_mix.image_clip(img, out, duration=3.0, width=320, height=240)
            info = probe.probe(out)
            self.assertTrue(info.get("has_video"))
            self.assertFalse(info.get("has_audio"))
            self.assertAlmostEqual(info.get("duration", 0), 3.0, delta=0.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
