#!/usr/bin/env python3
"""Phase 4 cont.: tighten/silence (SR-4.5), highlight+cover (SR-4.6), clean-audio
(SR-4.8), metadata embed (SR-5.4), batch export (SR-5.2).
Run: python3 tests/test_phase5.py"""
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import export, model


class TestBatch(unittest.TestCase):
    def test_batch_applies_preset(self):
        preset = {"name": "show", "style": {"aspect": "9:16", "transition_type": "cut"}}
        projects = [{"id": "a"}, {"id": "b"}]
        out = export.batch_export(projects, preset)
        self.assertEqual(len(out), 2)
        self.assertTrue(all(p["aspect"] == "9:16" for p in out))


def _ffmpeg_ok():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True); return True
    except Exception:
        return False


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestTighten(unittest.TestCase):
    def test_detects_gap_and_keep_ranges(self):
        from app.pipeline import tighten
        with tempfile.TemporaryDirectory() as d:
            wav = os.path.join(d, "a.wav")
            subprocess.run(["ffmpeg", "-y",
                            "-f", "lavfi", "-i", "sine=frequency=440:d=1",
                            "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono:d=1",
                            "-f", "lavfi", "-i", "sine=frequency=440:d=1",
                            "-filter_complex", "[0][1][2]concat=n=3:v=0:a=1[a]",
                            "-map", "[a]", wav], capture_output=True, check=True)
            sil = tighten.detect_silences(wav, noise="-30dB", min_d=0.3)
            self.assertGreaterEqual(len(sil), 1)
            keep = tighten.keep_ranges(3.0, sil)
            self.assertGreaterEqual(len(keep), 2)   # speech before + after the gap


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestMediaExtras(unittest.TestCase):
    def _vid(self, d):
        v = os.path.join(d, "v.mp4")
        subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "testsrc=d=3:s=160x120",
                        "-f", "lavfi", "-i", "sine=d=3", "-shortest", v],
                       capture_output=True, check=True)
        return v

    def test_highlight_and_cover(self):
        from app.pipeline import video_ops, probe
        with tempfile.TemporaryDirectory() as d:
            v = self._vid(d)
            clip = video_ops.highlight_clip(v, 0.5, 2.0, os.path.join(d, "h.mp4"))
            self.assertAlmostEqual(probe.probe(clip)["duration"], 1.5, delta=0.4)
            png = video_ops.cover_frame(v, 1.0, os.path.join(d, "c.png"))
            self.assertTrue(os.path.getsize(png) > 0)

    def test_clean_audio(self):
        from app.pipeline import audio_mix, probe
        with tempfile.TemporaryDirectory() as d:
            a = os.path.join(d, "a.wav")
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "sine=d=2", a],
                           capture_output=True, check=True)
            out = audio_mix.clean_audio(a, os.path.join(d, "clean.wav"))
            self.assertTrue(probe.probe(out).get("has_audio"))

    def test_embed_metadata(self):
        from app import metadata
        with tempfile.TemporaryDirectory() as d:
            a = os.path.join(d, "a.m4a")
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "sine=d=1", a],
                           capture_output=True, check=True)
            out = metadata.embed_metadata(a, os.path.join(d, "tagged.m4a"),
                                          title="Ep 1", description="pilot")
            probed = subprocess.run(["ffprobe", "-show_format", out],
                                    capture_output=True, text=True)
            self.assertIn("Ep 1", probed.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
