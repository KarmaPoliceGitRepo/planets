#!/usr/bin/env python3
"""Phase 3 tests: validate import (SR-3.1), undo/redo command stack (SR-3.3).
Run: python3 tests/test_phase3.py"""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import model, validate


class TestValidate(unittest.TestCase):
    def test_accepts_known_formats(self):
        for p in ("a.mp4", "b.WAV", "c.png", "d.m4a"):
            ok, reason = validate.validate_import(p)
            self.assertTrue(ok, f"{p} should be accepted ({reason})")

    def test_rejects_with_reason(self):
        ok, reason = validate.validate_import("notes.txt")
        self.assertFalse(ok)
        self.assertIn(".txt", reason)
        ok2, reason2 = validate.validate_import("noext")
        self.assertFalse(ok2)
        self.assertIn("extension", reason2)


class TestHistory(unittest.TestCase):
    def test_undo_redo(self):
        proj = {"order": 1}
        h = model.History(proj)
        proj = {"order": 2}; h.record(proj)
        proj = {"order": 3}; h.record(proj)
        self.assertTrue(h.can_undo())
        self.assertEqual(h.undo(), {"order": 2})
        self.assertEqual(h.undo(), {"order": 1})
        self.assertIsNone(h.undo())                 # nothing before the start
        self.assertEqual(h.redo(), {"order": 2})

    def test_record_truncates_redo_branch(self):
        h = model.History({"v": 0})
        h.record({"v": 1})
        h.undo()                                    # back to v=0
        h.record({"v": 9})                          # new branch; redo to v=1 gone
        self.assertFalse(h.can_redo())
        self.assertEqual(h.undo(), {"v": 0})


if __name__ == "__main__":
    unittest.main(verbosity=2)
