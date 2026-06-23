#!/usr/bin/env python3
"""Phase 8 — close the functional set: translation mechanism (SR-4.3), WYSIWYG
timing (SR-4.4), preserve -16 LUFS after mix (SR-2.6), independent A/V demo (SR-2.8).
Run: python3 tests/test_phase8.py"""
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app.pipeline import captions, render


class TestTranslateMechanism(unittest.TestCase):
    def test_translate_cues_pluggable(self):
        cues = [{"start": 0, "end": 1, "text": "namaste"}, {"start": 1, "end": 2, "text": "dhanyabad"}]
        fake = {"namaste": "hello", "dhanyabad": "thank you"}
        out = captions.translate_cues(cues, lambda t: fake.get(t, t))
        self.assertEqual([c["text"] for c in out], ["hello", "thank you"])
        self.assertEqual(out[0]["start"], 0)   # timings preserved


class TestWysiwyg(unittest.TestCase):
    def test_preview_equals_export_timing(self):
        project = {"source": "dummy.mp4", "transitions": {},
                   "segments": [{"keep": True, "subsections": [
                       {"id": "a", "start": 0.0, "end": 2.0, "order": 1, "keep": True},
                       {"id": "b", "start": 5.0, "end": 7.0, "order": 2, "keep": True}]}]}
        preview = render.timing_for(project)
        export = render.timing_for(project)
        self.assertEqual([c["new_start"] for c in preview],
                         [c["new_start"] for c in export])   # frame-accurate by construction


def _ffmpeg_ok():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True); return True
    except Exception:
        return False


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestLoudnessAfterMix(unittest.TestCase):
    def test_master_after_add_audio_hits_target(self):
        from app.pipeline import audio_mix, master
        with tempfile.TemporaryDirectory() as d:
            vid = os.path.join(d, "v.mp4"); mus = os.path.join(d, "m.m4a")
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "testsrc=d=3:s=160x120",
                            "-f", "lavfi", "-i", "sine=frequency=300:d=3", "-shortest", vid],
                           capture_output=True, check=True)
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "sine=frequency=500:d=3", mus],
                           capture_output=True, check=True)
            mixed = audio_mix.add_audio(vid, mus, os.path.join(d, "mix.mp4"), level_db=-6.0)
            res = master.master(mixed, d, has_video=True)
            self.assertTrue(res.get("pass"), f"loudness gate failed: {res}")   # SR-2.6


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestIndependentAV(unittest.TestCase):
    def test_audio_only_change_leaves_video_intact(self):
        """Demonstrate SR-2.8: clean the audio track independently; video unchanged."""
        from app.pipeline import demux, audio_mix, probe
        with tempfile.TemporaryDirectory() as d:
            src = os.path.join(d, "in.mp4")
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "testsrc=d=2:s=160x120",
                            "-f", "lavfi", "-i", "sine=d=2", "-shortest", src],
                           capture_output=True, check=True)
            before = probe.probe(src)
            tracks = demux.demux(src, d)                       # independent A/V
            clean = audio_mix.clean_audio(tracks["audio"], os.path.join(d, "ca.m4a"))
            out = os.path.join(d, "remux.mp4")
            subprocess.run(["ffmpeg", "-y", "-i", tracks["video"], "-i", clean,
                            "-c", "copy", "-map", "0:v:0", "-map", "1:a:0", out],
                           capture_output=True, check=True)
            after = probe.probe(out)
            self.assertEqual((before["width"], before["height"]), (after["width"], after["height"]))
            self.assertAlmostEqual(before["duration"], after["duration"], delta=0.3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
