#!/usr/bin/env python3
"""model.py — the ReelCut edit project: load/save + the reorder operations.

A project is a single JSON document describing one upload's edit:

    {
      "name": "...", "source": "raw/upload.mp4",
      "width": 1280, "height": 720, "fps": 30, "duration": 612.0,
      "engine": "whisper" | "silence",
      "segments": [ { id, title, tag, keep, start, end, subsections:[
          { id, start, end, text, tag, keep, order } ] } ],
      "transitions": { "<to_subsection_id>": { "type": "...", "duration": 0.5 } }
    }

`order` is a global 1..N rank over the KEPT sub-sections and defines the OUTPUT
sequence. The three reorder methods below all just rewrite `order`.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
from typing import Dict, List


def all_subs(project: dict) -> List[dict]:
    return [sub for seg in project.get("segments", []) for sub in seg.get("subsections", [])]


def kept_subs(project: dict) -> List[dict]:
    out = []
    for seg in project.get("segments", []):
        if seg.get("keep", True):
            for sub in seg.get("subsections", []):
                if sub.get("keep", True):
                    out.append(sub)
    # Missing `order` sorts last deterministically (CR-L8): use +inf, tie-break on start.
    out.sort(key=lambda s: (s.get("order") if s.get("order") else float("inf"), s.get("start", 0)))
    return out


def _atomic_write(path: str, text: str) -> None:
    """Write text by writing a temp file then atomically replacing the target, so a
    crash mid-write can never leave a truncated/corrupt file (CR-H7)."""
    p = Path(path)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, p)  # atomic on POSIX and Windows for same-filesystem paths



def renumber(project: dict) -> None:
    """Re-pack kept sub-sections to a clean 1..N order; non-kept get order 0."""
    seq = kept_subs(project)
    ids = {s["id"]: i + 1 for i, s in enumerate(seq)}
    for sub in all_subs(project):
        sub["order"] = ids.get(sub["id"], 0)


# ---- the three reorder methods ---------------------------------------------
def move(project: dict, sub_id: str, new_pos: int) -> None:
    """Drag-and-drop: move one sub-section to 1-based position `new_pos`."""
    seq = kept_subs(project)
    ids = [s["id"] for s in seq]
    if sub_id not in ids:
        raise ValueError(f"unknown or non-kept sub-section: {sub_id}")
    ids.remove(sub_id)
    new_pos = max(1, min(new_pos, len(ids) + 1))
    ids.insert(new_pos - 1, sub_id)
    _apply_order(project, ids)


def swap(project: dict, pos_a: int, pos_b: int) -> None:
    """Swap field: exchange the items currently at 1-based positions a and b."""
    seq = kept_subs(project)
    n = len(seq)
    if not (1 <= pos_a <= n and 1 <= pos_b <= n):
        raise ValueError(f"positions must be 1..{n}")
    ids = [s["id"] for s in seq]
    ids[pos_a - 1], ids[pos_b - 1] = ids[pos_b - 1], ids[pos_a - 1]
    _apply_order(project, ids)


def reorder_by_permutation(project: dict, perm: List[int]) -> None:
    """Renumber field: `perm` lists the CURRENT positions in the new sequence.

    e.g. current order [A,B,C,D]; perm [1,4,2,3] → new order [A,D,B,C].
    Validates that perm is a true permutation of 1..N (no missing/dupes).
    """
    seq = kept_subs(project)
    n = len(seq)
    if sorted(perm) != list(range(1, n + 1)):
        raise ValueError(f"order must be each of 1..{n} exactly once; got {perm}")
    ids = [seq[p - 1]["id"] for p in perm]
    _apply_order(project, ids)


def _apply_order(project: dict, ordered_ids: List[str]) -> None:
    rank = {sid: i + 1 for i, sid in enumerate(ordered_ids)}
    for sub in all_subs(project):
        if sub["id"] in rank:
            sub["order"] = rank[sub["id"]]
    renumber(project)


# ---- keep / transitions -----------------------------------------------------
def set_keep(project: dict, item_id: str, keep: bool) -> None:
    for seg in project.get("segments", []):
        if seg["id"] == item_id:
            seg["keep"] = keep
            return
        for sub in seg.get("subsections", []):
            if sub["id"] == item_id:
                sub["keep"] = keep
                return
    raise ValueError(f"unknown item: {item_id}")


def set_transition(project: dict, to_id: str, type_: str, duration: float) -> None:
    project.setdefault("transitions", {})[to_id] = {
        "type": type_, "duration": float(duration)}


# ---- io ---------------------------------------------------------------------
def load(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save(project: dict, path: str) -> None:
    _atomic_write(path, json.dumps(project, ensure_ascii=False, indent=2))


# ---- Phase 1: non-destructive source guard (SR-4.1) -------------------------
class SourceMutated(Exception):
    """Raised when an imported source file has changed since import (SR-4.1)."""


def source_digest(project: dict) -> str:
    """sha256 of the source media file (streamed, constant memory)."""
    with open(project["source"], "rb") as f:
        h = hashlib.sha256()
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def baseline_source(project: dict) -> dict:
    """Record the source file's digest as the integrity baseline (SR-4.1).

    Must be called when a source is imported; without it ``source_sha256`` is
    never set and ``assert_source_unchanged`` is inert (CR-H6)."""
    project["source_sha256"] = source_digest(project)
    return project


def assert_source_unchanged(project: dict) -> None:
    recorded = project.get("source_sha256")
    if recorded is not None and source_digest(project) != recorded:
        raise SourceMutated(project["source"])


# ---- Phase 1: portable, renderer-agnostic project doc (SR-2.2) --------------
def to_portable(project: dict, project_dir: str) -> dict:
    """Strip absolute paths and renderer (ffmpeg_*) strings; store source as a
    handle relative to project_dir."""
    doc = {k: v for k, v in project.items() if not k.startswith("ffmpeg_")}
    src = project.get("source")
    if src and os.path.isabs(src):
        doc["source"] = os.path.relpath(src, project_dir)
    return doc


def from_portable(doc: dict, project_dir: str) -> dict:
    """Resolve the relative source handle to an absolute path on this machine."""
    project = dict(doc)
    src = doc.get("source")
    if src and not os.path.isabs(src):
        project["source"] = os.path.normpath(os.path.join(project_dir, src))
    return project


# ---- Phase 2: replacing audio orphans captions (SR-2.3) --------------------
def mark_captions_stale(project: dict) -> None:
    """Flag captions/segments as derived-from-old-audio after an audio replace,
    so the UI can offer re-transcribe (SR-2.3 / SR-3.5)."""
    project["captions_stale"] = True


# ---- Phase 3: reversible command stack — undo/redo (SR-3.3) -----------------
class History:
    """A linear undo/redo stack of project snapshots. ``record`` is called after
    every edit; ``undo``/``redo`` return the project state to restore (or None
    when there is nothing to move to)."""

    def __init__(self, project: dict):
        self._stack = [copy.deepcopy(project)]
        self._i = 0

    def record(self, project: dict) -> None:
        # drop any redo branch, then push the new state
        del self._stack[self._i + 1:]
        self._stack.append(copy.deepcopy(project))
        self._i = len(self._stack) - 1

    def can_undo(self) -> bool:
        return self._i > 0

    def can_redo(self) -> bool:
        return self._i < len(self._stack) - 1

    def undo(self):
        if not self.can_undo():
            return None
        self._i -= 1
        return copy.deepcopy(self._stack[self._i])

    def redo(self):
        if not self.can_redo():
            return None
        self._i += 1
        return copy.deepcopy(self._stack[self._i])


# ---- Phase 3/4: autosave, source-change, presets, license -------------------
_STYLE_KEYS = ("transition_type", "transition_duration", "aspect", "branding")


def autosave(project: dict, path: str) -> str:
    """Continuously persist to a sidecar so a crash never loses work (SR-3.2).

    Written atomically (CR-H7) so a crash mid-autosave cannot corrupt the sidecar
    that ``restore`` later reads."""
    side = path + ".autosave"
    _atomic_write(side, json.dumps(project, ensure_ascii=False, indent=2))
    return side


def restore(path: str) -> dict | None:
    """Return the autosaved project if a sidecar exists, else None (SR-3.2)."""
    side = path + ".autosave"
    if Path(side).exists():
        return json.loads(Path(side).read_text(encoding="utf-8"))
    return None


def needs_regeneration(project: dict) -> bool:
    """True if the source file changed since import; flags derived artefacts
    stale so the UI can offer regeneration (SR-3.5)."""
    recorded = project.get("source_sha256")
    if recorded is None:
        return False
    changed = source_digest(project) != recorded
    if changed:
        project["captions_stale"] = True
        project["segments_stale"] = True
    return changed


def save_preset(project: dict, name: str) -> dict:
    """Capture the reusable style of a project as a named preset (SR-4.11)."""
    return {"name": name, "style": {k: project[k] for k in _STYLE_KEYS if k in project}}


def apply_preset(project: dict, preset: dict) -> None:
    """Apply a saved preset's style to a project (SR-4.11).

    Only whitelisted style keys are copied, so a crafted/corrupt preset cannot
    overwrite structural keys like ``segments`` or ``source`` (CR-M11)."""
    style = preset.get("style", {})
    for k in _STYLE_KEYS:
        if k in style:
            project[k] = style[k]


def flag_audio_license(project: dict, track_id: str, royalty_free: bool,
                       note: str = "") -> None:
    """Record a licence decision for an added audio track; flag if not
    royalty-free so the creator is warned before publishing (SR-5.3)."""
    project.setdefault("audio_licenses", {})[track_id] = {
        "royalty_free": royalty_free, "note": note, "flagged": not royalty_free}
