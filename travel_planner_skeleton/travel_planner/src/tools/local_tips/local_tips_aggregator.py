"""Local tips aggregator (feature 10).

Purpose: Run the four local tips tools and merge into one dict for the itinerary.
Build order: 8
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest


def collect_local_tips(request: ToolRequest) -> dict:
    """Return {currency, tipping, phrases, connectivity}.

    TODO:
    - Run tools in parallel
    - A failed tool leaves its key empty with a warning
    """
    raise NotImplementedError
