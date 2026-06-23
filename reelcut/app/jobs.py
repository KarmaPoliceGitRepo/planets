#!/usr/bin/env python3
"""jobs.py — cancellable long operations with progress (SR-3.4).

Renders are slow; the UI must be able to abort and must receive progress so the
app never looks frozen. This is the framework the server wires its render/segment
workers into.
"""
from __future__ import annotations

from typing import Callable, List, Optional


class Cancelled(Exception):
    """Raised inside a job when the user has requested cancellation."""


class CancelToken:
    def __init__(self) -> None:
        self._cancelled = False

    def cancel(self) -> None:
        self._cancelled = True

    @property
    def cancelled(self) -> bool:
        return self._cancelled

    def check(self) -> None:
        if self._cancelled:
            raise Cancelled()


def run_steps(steps: List[Callable[[], object]],
              progress: Optional[Callable[[float], None]] = None,
              token: Optional[CancelToken] = None) -> list:
    """Run steps in order, reporting fractional progress after each and checking
    the cancel token before each (SR-3.4)."""
    results = []
    n = len(steps) or 1
    for i, step in enumerate(steps):
        if token is not None:
            token.check()
        results.append(step())
        if progress is not None:
            progress((i + 1) / n)
    return results
