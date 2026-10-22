"""Grounding checks.

Purpose: Every price, hour, rule must trace to an Evidence record.
Build order: 5
"""

from __future__ import annotations

from src.schemas.itinerary import Itinerary


def extract_claims(itinerary: Itinerary) -> list[dict]:
    """List claims that need evidence (prices, hours, visa rules, weather).
    """
    raise NotImplementedError

def find_unsupported(claims: list[dict]) -> list[dict]:
    """Claims with no evidence or stale evidence.

    TODO:
    - Decide freshness limits per claim type
    """
    raise NotImplementedError
