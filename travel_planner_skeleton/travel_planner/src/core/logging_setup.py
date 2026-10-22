"""Logging and tracing.

Purpose: You need traces to debug multi-agent runs.
Build order: 2
"""

from __future__ import annotations




def setup_logging(level: str = 'INFO') -> None:
    """Configure logging format and handlers.

    TODO:
    - Add a trace id per trip request
    """
    raise NotImplementedError

def new_trace_id() -> str:
    """Return a short id to tag one planning run.
    """
    raise NotImplementedError
