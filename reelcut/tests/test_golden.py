#!/usr/bin/env python3
"""Golden tests for render timing + silence parsing (CR-H10, CR-H11/L3/M12).
Run: python3 tests/test_golden.py"""
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app.pipeline import silences, render


def _ffmpeg_ok():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


def _stream_dur(path, stream):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", stream,
                          "-show_entries", "stream=duration", "-of", "default=nk=1:nw=1", path],
                         capture_output=True, text=True)
    return float(out.stdout.strip())


class TestSilenceParser(unittest.TestCase):
    """The shared parser handles every edge case the two old parsers split on."""

    def test_audio_ends_in_silence(self):
        # second silence opens at 3.0 and never closes → speech must end at 3.0, not duration.
        stderr = "silence_start: 1.0\nsilence_end: 2.0\nsilence_start: 3.0\n"
        self.assertEqual(silences.silent_spans(stderr), [(1.0, 2.0)])
        self.assertEqual(silences.speech_ranges(stderr, duration=5.0),
                         [[0.0, 1.0], [2.0, 3.0]])

    def test_audio_ends_in_speech(self):
        stderr = "silence_start: 1.0\nsilence_end: 2.0\n"
        self.assertEqual(silences.speech_ranges(stderr, duration=5.0),
                         [[0.0, 1.0], [2.0, 5.0]])

    def test_no_silence(self):
        self.assertEqual(silences.speech_ranges("", duration=5.0), [[0.0, 5.0]])

    def test_duplicate_silence_start_keeps_latest(self):
        stderr = "silence_start: 1.0\nsilence_start: 1.5\nsilence_end: 2.0\n"
        self.assertEqual(silences.silent_spans(stderr), [(1.5, 2.0)])

    def test_short_gaps_dropped(self):
        # gap of 0.2s (< min_gap) between two silences must not become a speech range.
        stderr = "silence_start: 1.0\nsilence_end: 2.0\nsilence_start: 2.2\nsilence_end: 3.0\n"
        self.assertEqual(silences.speech_ranges(stderr, duration=5.0, min_gap=0.4),
                         [[0.0, 1.0], [3.0, 5.0]])


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestAVSyncCrossfade(unittest.TestCase):
    """CR-H10: across multiple crossfade transitions, the rendered video and audio
    streams must stay the same length (a proxy for staying in sync)."""

    def test_video_and_audio_durations_match(self):
        with tempfile.TemporaryDirectory() as d:
            src = os.path.join(d, "src.mp4")
            out = os.path.join(d, "out.mp4")
            # 6s source with both a video and an audio stream.
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "testsrc=d=6:s=160x120:r=30",
                            "-f", "lavfi", "-i", "sine=frequency=440:d=6",
                            "-pix_fmt", "yuv420p", "-shortest", src], capture_output=True, check=True)
            project = {
                "source": src, "width": 160, "height": 120, "fps": 30, "has_video": True,
                "segments": [{"id": "s1", "keep": True, "subsections": [
                    {"id": "c1", "start": 0.0, "end": 2.0, "keep": True, "order": 1},
                    {"id": "c2", "start": 2.0, "end": 4.0, "keep": True, "order": 2},
                    {"id": "c3", "start": 4.0, "end": 6.0, "keep": True, "order": 3},
                ]}],
                # crossfade both boundaries
                "transitions": {"c2": {"type": "crossfade", "duration": 0.5},
                                "c3": {"type": "crossfade", "duration": 0.5}},
            }
            res = render.render(project, out, has_video=True)
            self.assertTrue(res["ok"], res.get("error"))
            vdur, adur = _stream_dur(out, "v:0"), _stream_dur(out, "a:0")
            # 6s of clips minus two 0.5s overlaps ≈ 5.0s; the point is v≈a.
            self.assertAlmostEqual(vdur, adur, delta=0.25,
                                   msg=f"A/V drift: video={vdur}s audio={adur}s")
            self.assertAlmostEqual(vdur, 5.0, delta=0.4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
