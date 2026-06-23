#!/usr/bin/env python3
"""Phase 1 tests: non-destructive source guard (SR-4.1), portable project doc
(SR-2.2), demux into independent A/V tracks (SR-2.1). Run: python3 tests/test_phase1.py"""
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import model


class TestNonDestructive(unittest.TestCase):
    def test_source_digest_detects_mutation(self):
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d) / "raw.wav"
            src.write_bytes(b"original-bytes")
            project = {"source": str(src)}
            project["source_sha256"] = model.source_digest(project)
            model.assert_source_unchanged(project)            # no raise
            src.write_bytes(b"tampered")
            with self.assertRaises(model.SourceMutated):
                model.assert_source_unchanged(project)


class TestPortableDoc(unittest.TestCase):
    def test_roundtrip_survives_dir_move(self):
        import shutil
        with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
            media = pathlib.Path(d1) / "media" / "raw.wav"
            media.parent.mkdir()
            media.write_bytes(b"x")
            project = {"source": str(media), "ffmpeg_cmd": "ffmpeg -i ...", "segments": []}
            doc = model.to_portable(project, d1)
            self.assertFalse(os.path.isabs(doc["source"]))
            self.assertNotIn("ffmpeg_cmd", doc)
            shutil.copytree(d1, d2, dirs_exist_ok=True)
            restored = model.from_portable(doc, d2)
            self.assertTrue(os.path.exists(restored["source"]))


def _ffmpeg_ok():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


@unittest.skipUnless(_ffmpeg_ok(), "needs ffmpeg")
class TestDemux(unittest.TestCase):
    def test_splits_av(self):
        from app.pipeline import demux, probe
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d) / "in.mp4"
            subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "testsrc=d=1:s=160x120",
                            "-f", "lavfi", "-i", "sine=d=1", "-shortest", str(src)],
                           capture_output=True, check=True)
            out = demux.demux(str(src), d)
            self.assertTrue(out["video"] and os.path.exists(out["video"]))
            self.assertTrue(out["audio"] and os.path.exists(out["audio"]))
            self.assertFalse(probe.probe(out["audio"]).get("has_video"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
