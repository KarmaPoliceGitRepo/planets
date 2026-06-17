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

import json
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
    out.sort(key=lambda s: (s.get("order", 10_000), s.get("start", 0)))
    return out


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
    Path(path).write_text(json.dumps(project, ensure_ascii=False, indent=2), encoding="utf-8")
