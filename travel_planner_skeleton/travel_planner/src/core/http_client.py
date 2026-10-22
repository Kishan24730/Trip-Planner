"""Shared HTTP helper.

Purpose: One place for timeouts, retries, throttling and User-Agent.
Build order: 2
"""

from __future__ import annotations

from typing import Any, Optional


def get_json(url: str, params: Optional[dict] = None, headers: Optional[dict] = None, timeout: int = 15) -> Any:
    """GET and return parsed JSON.

    TODO:
    - Set User-Agent from settings
    - Retry a few times with backoff on 5xx
    - Raise RateLimitError on 429
    - Never log API keys
    """
    raise NotImplementedError

def throttle(key: str, min_seconds: float) -> None:
    """Sleep so calls to one host stay under its limit (Nominatim: about 1 request/sec).
    """
    raise NotImplementedError
