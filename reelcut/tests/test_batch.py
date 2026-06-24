#!/usr/bin/env python3
"""Regression tests for the MED/LOW batch fixes (DECISIONS.md I-7).
Run: python3 tests/test_batch.py"""
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import export
from app.pipeline import captions, render, master, video_ops


def _ffmpeg_ok():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


def _stream_dur(path, stream="v:0"):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", stream,
                          "-show_entries", "stream=duration", "-of", "default=nk=1:nw=1", path],
                         capture_output=True, text=True)
    return float(out.stdout.strip())


class TestCaptionBoundaryCue(unittest.TestCase):
    """CR-M5: a cue straddling a cut is kept and clamped, never dropped or spilled."""
    def test_spanning_cue_clamped_to_both_clips(self):
        with tempfile.TemporaryDirectory() as d:
            wc = os.path.join(d, "w.json")
            # one cue 1.5..3.5 spans the boundary between clip [0,2] and clip [2,4]
            with open(wc, "w") as fh:
                json.dump({"segments": [{"start": 1.5, "end": 3.5, "text": "boundary"}]}, fh)
            project = {"segments": [{"keep": True, "subsections": [
                {"id": "c1", "text": ""}, {"id": "c2", "text": ""}]}]}
            tm = [{"id": "c1", "src_start": 0.0, "src_end": 2.0, "new_start": 0.0},
                  {"id": "c2", "src_start": 2.0, "src_end": 4.0, "new_start": 2.0}]
            srt = os.path.join(d, "out.srt")
            res = captions.remap(project, tm, srt, whisper_cache=wc)
            self.assertEqual(res["cues"], 2)             # kept on both clips, not dropped
            text = pathlib.Path(srt).read_text()
            self.assertEqual(text.count("boundary"), 2)


class TestChapterTimingMap(unittest.TestCase):
    """CR-M6: chapter times follow the rendered timeline when a timing map is given."""
    def test_chapters_use_timing_map(self):
        project = {"segments": [{"title": "Intro", "keep": True, "subsections": [
            {"id": "a", "start": 10.0, "end": 12.0, "keep": True, "order": 1}]}]}
        # rendered output places clip 'a' at new_start 0.0 (not its source 10s)
        tm = [{"id": "a", "src_start": 10.0, "src_end": 12.0, "new_start": 0.0}]
        meta = export.chapters_ffmetadata(project, timing_map=tm)
        self.assertIn("START=0", meta)
        self.assertIn("END=2000", meta)                  # 2s duration at output position 0
        # without a timing map it falls back to cumulative source durations
        meta2 = export.chapters_ffmetadata(project)
        self.assertIn("START=0", meta2)
        self.assertIn("END=2000", meta2)


class TestRenderValidatesRange(unittest.TestCase):
    """CR-L10: an inverted/zero clip range is rejected, not silently emitted as -t 0."""
    def test_inverted_range_raises(self):
        bad = {"source": "x.mp4", "segments": [{"keep": True, "subsections": [
            {"id": "z", "start": 5.0, "end": 5.0, "keep": True, "order": 1}]}]}
        with self.assertRaises(ValueError):
            render.build_plan(bad)


class TestMasterFiniteGuard(unittest.TestCase):
    """CR-M4: non-finite measured values are not used for the linear pass."""
    def test_finite(self):
        self.assertTrue(master._finite("-16.0"))
        self.assertFalse(master._finite("inf"))
        self.assertFalse(master._finite("-inf"))
        self.assertFalse(master._finite(None))


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestHighlightDuration(unittest.TestCase):
    """CR-M1: highlight clip length equals end-start (accurate trim)."""
    def test_duration(self):
        with tempfile.TemporaryDirectory() as d:
            src, out = os.path.join(d, "s.mp4"), os.path.join(d, "h.mp4")
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "testsrc=d=5:s=160x120:r=30",
                            "-f", "lavfi", "-i", "sine=frequency=440:d=5",
                            "-pix_fmt", "yuv420p", "-shortest", src], capture_output=True, check=True)
            video_ops.highlight_clip(src, 1.0, 3.0, out)
            self.assertAlmostEqual(_stream_dur(out, "v:0"), 2.0, delta=0.3)


class TestFfHelper(unittest.TestCase):
    """CR-L4: a failed ffmpeg call raises with its stderr, not a bare error."""
    def test_failure_includes_stderr(self):
        from app.pipeline import _ff
        with self.assertRaises(_ff.FFmpegError) as cm:
            _ff.run(["ffmpeg", "-y", "-i", "/no/such/input.mp4", "/tmp/never.mp4"])
        self.assertIn("ffmpeg failed", str(cm.exception))


class TestExplicitImports(unittest.TestCase):
    """CR-L9/TD-1: context detection is explicit, not a swallowing try/except."""
    def test_no_import_error_swallow(self):
        import inspect
        from app import api
        src = inspect.getsource(api)
        self.assertIn("if __package__", src)
        self.assertNotIn("except ImportError", src)


if __name__ == "__main__":
    unittest.main(verbosity=2)
