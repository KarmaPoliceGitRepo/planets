#!/usr/bin/env python3
"""ReelCut test suite (T-1..T-6). Pure-stdlib unittest; T-4 needs FFmpeg.

    python3 tests/test_reelcut.py
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))

import model as M                                          # noqa: E402
from pipeline import render as R, segment as S, captions as C  # noqa: E402

HAVE_FFMPEG = shutil.which("ffmpeg") is not None


def sample_project():
    return {"source": "x.mp4", "width": 320, "height": 240, "fps": 30,
            "segments": [{"id": "seg-1", "keep": True, "subsections": [
                {"id": "A", "start": 0.0, "end": 5.0, "keep": True, "order": 1, "text": "alpha one"},
                {"id": "B", "start": 5.0, "end": 10.0, "keep": True, "order": 2, "text": "beta two"},
                {"id": "C", "start": 10.0, "end": 15.0, "keep": True, "order": 3, "text": "gamma three"},
                {"id": "D", "start": 15.0, "end": 20.0, "keep": True, "order": 4, "text": "delta four"},
            ]}], "transitions": {}}


def seq(p):
    return [s["id"] for s in M.kept_subs(p)]


class TestReorder(unittest.TestCase):                       # T-1
    def test_permutation(self):
        p = sample_project()
        M.reorder_by_permutation(p, [1, 4, 2, 3])
        self.assertEqual(seq(p), ["A", "D", "B", "C"])

    def test_swap(self):
        p = sample_project()
        M.swap(p, 1, 3)
        self.assertEqual(seq(p), ["C", "B", "A", "D"])

    def test_move(self):
        p = sample_project()
        M.move(p, "D", 1)
        self.assertEqual(seq(p), ["D", "A", "B", "C"])

    def test_bad_permutation_rejected(self):
        p = sample_project()
        with self.assertRaises(ValueError):
            M.reorder_by_permutation(p, [1, 2, 2, 3])   # dup / not a permutation
        with self.assertRaises(ValueError):
            M.reorder_by_permutation(p, [1, 2, 3])      # wrong length


class TestKeep(unittest.TestCase):                          # T-2
    def test_drop_renumbers(self):
        p = sample_project()
        M.set_keep(p, "B", False)
        M.renumber(p)
        self.assertEqual(seq(p), ["A", "C", "D"])
        kept = M.kept_subs(p)
        self.assertEqual([s["order"] for s in kept], [1, 2, 3])

    def test_drop_segment_drops_children(self):
        p = sample_project()
        M.set_keep(p, "seg-1", False)
        self.assertEqual(seq(p), [])


class TestTiming(unittest.TestCase):                        # T-3
    def test_cut_offsets(self):
        p = sample_project()           # all adjacent, default cut
        plan = R.build_plan(p)
        tm = R.timing_map(plan)
        self.assertEqual([round(x["new_start"], 1) for x in tm], [0.0, 5.0, 10.0, 15.0])

    def test_crossfade_overlap(self):
        p = sample_project()
        # reorder so A and C are adjacent in output -> a gap boundary, add 1s crossfade
        M.reorder_by_permutation(p, [1, 3, 2, 4])     # A C B D
        p["transitions"] = {"C": {"type": "crossfade", "duration": 1.0}}
        plan = R.build_plan(p)
        tm = R.timing_map(plan)
        # A@0 ; C starts at 5-1=4 ; B/D back to cut afterwards
        self.assertAlmostEqual(tm[1]["new_start"], 4.0, places=2)

    def test_gap_detection(self):
        p = sample_project()
        M.set_keep(p, "B", False)      # now A(0-5) then C(10-15): a removed chunk
        plan = R.build_plan(p)
        self.assertTrue(plan.boundaries[0].auto_gap)   # A->C is a gap


@unittest.skipUnless(HAVE_FFMPEG, "ffmpeg not installed")
class TestRenderFFmpeg(unittest.TestCase):                 # T-4
    @classmethod
    def setUpClass(cls):
        cls.tmp = ROOT / "tests" / "_tmp"
        cls.tmp.mkdir(exist_ok=True)
        cls.src = cls.tmp / "src.mp4"
        subprocess.run(
            ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
             "-f", "lavfi", "-i", "sine=f=300:d=12:r=44100",
             "-f", "lavfi", "-i", "color=c=red:s=160x120:r=30:d=12",
             "-shortest", "-c:v", "libx264", "-preset", "ultrafast",
             "-pix_fmt", "yuv420p", "-c:a", "aac", str(cls.src)], check=True)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def _probe(self, path):
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "stream=codec_type", "-of", "csv=p=0", path],
                             capture_output=True, text=True).stdout.split()
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                    "format=duration", "-of", "csv=p=0", path],
                                   capture_output=True, text=True).stdout.strip())
        return out, dur

    def test_render_has_av_and_duration(self):
        proj = {"source": str(self.src), "width": 160, "height": 120, "fps": 30,
                "segments": [{"id": "s", "keep": True, "subsections": [
                    {"id": "p1", "start": 0.0, "end": 4.0, "keep": True, "order": 2},
                    {"id": "p2", "start": 6.0, "end": 10.0, "keep": True, "order": 1},
                ]}],
                "transitions": {"p1": {"type": "crossfade", "duration": 1.0}}}
        out = str(self.tmp / "out.mp4")
        res = R.render(proj, out, has_video=True)
        self.assertTrue(res["ok"], res.get("error"))
        types, dur = self._probe(out)
        self.assertIn("video", " ".join(types))
        self.assertIn("audio", " ".join(types))
        # 4 + 4 - 1 crossfade = 7s (allow muxing slack)
        self.assertAlmostEqual(dur, 7.0, delta=0.4)


class TestSegment(unittest.TestCase):                      # T-5
    def test_grouping_shapes(self):
        # synthetic transcript: two topics separated by a 3s gap
        lines = ([{"start": i * 7.0, "end": i * 7.0 + 6.5,
                   "text": "money wages remittance families leave home."} for i in range(8)]
                 + [{"start": 60 + i * 7.0, "end": 60 + i * 7.0 + 6.5,
                     "text": "villages roads schools clinics infrastructure rural."} for i in range(8)])
        subs = S._group_subs(lines)
        segs = S._group_segs(subs)
        self.assertGreaterEqual(len(segs), 2)
        for sg in segs:
            self.assertTrue(sg["subsections"])
            self.assertTrue(sg["tag"])


class TestCaptions(unittest.TestCase):                     # T-6
    def test_remap_to_new_order(self):
        p = sample_project()
        M.reorder_by_permutation(p, [4, 1, 2, 3])    # D first
        plan = R.build_plan(p)
        tm = R.timing_map(plan)
        out = ROOT / "tests" / "_cap.srt"
        C.remap(p, tm, str(out))
        text = out.read_text()
        out.unlink()
        # first cue should be the clip that is now first (D = "delta four")
        first_block = text.split("\n\n")[0]
        self.assertIn("delta four", first_block)
        self.assertTrue(first_block.startswith("1\n00:00:00,000"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
