#!/usr/bin/env python3
"""Phase 3/4 batch: transcript (SR-5.1), chapters (SR-4.7), presets (SR-4.11),
license flag (SR-5.3), autosave/restore (SR-3.2), source-change (SR-3.5),
reframe (SR-4.2), burn-in captions (SR-4.9). Run: python3 tests/test_phase4.py"""
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import export, model


def _proj():
    return {
        "source": None,
        "segments": [
            {"keep": True, "title": "Intro", "subsections": [
                {"keep": True, "order": 1, "start": 0.0, "end": 2.0, "text": "hello world"}]},
            {"keep": True, "title": "Topic", "subsections": [
                {"keep": True, "order": 2, "start": 2.0, "end": 5.0, "text": "main point"},
                {"keep": False, "order": 0, "start": 5.0, "end": 6.0, "text": "dropped"}]},
        ],
    }


class TestTextDerivations(unittest.TestCase):
    def test_transcript(self):
        txt = export.transcript_txt(_proj())
        self.assertIn("hello world", txt)
        self.assertIn("main point", txt)
        self.assertNotIn("dropped", txt)

    def test_chapters(self):
        meta = export.chapters_ffmetadata(_proj())
        self.assertIn(";FFMETADATA1", meta)
        self.assertEqual(meta.count("[CHAPTER]"), 2)
        self.assertIn("title=Intro", meta)


class TestModelState(unittest.TestCase):
    def test_presets(self):
        src = {"transition_type": "crossfade", "transition_duration": 0.5, "aspect": "9:16"}
        preset = model.save_preset(src, "myshow")
        dst = {}
        model.apply_preset(dst, preset)
        self.assertEqual(dst["aspect"], "9:16")
        self.assertEqual(dst["transition_type"], "crossfade")

    def test_license_flag(self):
        p = {}
        model.flag_audio_license(p, "music1", royalty_free=False, note="unknown source")
        self.assertTrue(p["audio_licenses"]["music1"]["flagged"])

    def test_autosave_restore_and_source_change(self):
        with tempfile.TemporaryDirectory() as d:
            media = pathlib.Path(d) / "raw.wav"; media.write_bytes(b"a")
            proj = {"source": str(media), "v": 1}
            proj["source_sha256"] = model.source_digest(proj)
            path = os.path.join(d, "proj.json")
            model.autosave(proj, path)
            self.assertEqual(model.restore(path)["v"], 1)
            self.assertFalse(model.needs_regeneration(proj))
            media.write_bytes(b"changed")
            self.assertTrue(model.needs_regeneration(proj))
            self.assertTrue(proj["captions_stale"])


def _ffmpeg_ok():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True); return True
    except Exception:
        return False


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestVideoOps(unittest.TestCase):
    def test_reframe_and_burn(self):
        from app.pipeline import video_ops, probe
        with tempfile.TemporaryDirectory() as d:
            vid = os.path.join(d, "v.mp4")
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "testsrc=d=1:s=320x240",
                            "-f", "lavfi", "-i", "sine=d=1", "-shortest", vid],
                           capture_output=True, check=True)
            out = os.path.join(d, "vert.mp4")
            video_ops.reframe(vid, out, aspect="9:16", height=256)
            info = probe.probe(out)
            self.assertEqual((info["width"], info["height"]), (144, 256))
            srt = os.path.join(d, "c.srt")
            pathlib.Path(srt).write_text("1\n00:00:00,000 --> 00:00:01,000\nhi\n", encoding="utf-8")
            burned = os.path.join(d, "burn.mp4")
            video_ops.burn_captions(out, srt, burned)
            self.assertTrue(probe.probe(burned).get("has_video"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
