"""Partial regeneration.

Purpose: Fix only the failing day or section, with a retry cap.
Build order: 5
"""

from __future__ import annotations

from src.schemas.itinerary import Itinerary


def regenerate_failed_parts(itinerary: Itinerary, problems: list[str], max_retries: int = 2) -> Itinerary:
    """Regenerate only what failed.

    TODO:
    - Stop at max_retries and mark unverified parts
    - Track cost per retry
    """
    raise NotImplementedError
