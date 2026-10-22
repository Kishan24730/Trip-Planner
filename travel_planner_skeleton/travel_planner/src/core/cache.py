"""File cache with TTL.

Purpose: Free APIs hit limits. Cache saves quota and keeps the demo alive.
Build order: 2
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional


class FileCache:
    def __init__(self, cache_dir: str = "data/cache") -> None:
        self.cache_dir = Path(cache_dir)

    def get(self, namespace: str, key: str, ttl_seconds: int) -> Optional[Any]:
        """Return cached value if younger than ttl, else None.

        TODO:
        - Hash the key into a safe filename
        - Compare saved_at with now
        - Return None on corrupt files
        """
        raise NotImplementedError

    def set(self, namespace: str, key: str, value: Any) -> None:
        """Save value with a timestamp.

        TODO:
        - Write JSON
        - Create the folder if missing
        """
        raise NotImplementedError

    def clear_expired(self, ttl_seconds: int) -> int:
        """Delete old files and return how many were removed.
        """
        raise NotImplementedError
