"""Evidence record attached to every fact.

Purpose: Lets the verifier and UI show where each fact came from and how fresh it is.
Build order: 1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Evidence:
    source: str                  # e.g. "open_meteo", "osm_overpass", "curated_visa"
    fetched_at: float            # unix time
    freshness: str               # "live" | "cached" | "curated" | "estimated" | "mock"
    url: Optional[str] = None    # link a human can click
    note: Optional[str] = None
