"""Dining tool.

Purpose: Food and restaurant suggestions matched to the diet preference.
Build order: 6

Data sources: OSM, Foursquare
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class DiningTool(BaseTool):
    name = "dining"
    description = "Food and restaurant suggestions matched to the diet preference."

    def run(self, request: ToolRequest) -> ToolResult:
        """Food and restaurant suggestions matched to the diet preference.

        TODO:
        - Map food_preference (veg, vegan, jain, halal, non_veg) to place tags
        - Add local meal timings
        - Flag places where diet cannot be confirmed as 'unverified'
        - Estimate meal cost per person (label 'estimated')
        """
        raise NotImplementedError

    def _diet_filter(self, places: list[dict], diet: str) -> list[dict]:
        """Keep diet-safe places.
        """
        raise NotImplementedError

    def _meal_windows(self, country: str) -> dict:
        """Typical breakfast, lunch, dinner hours.
        """
        raise NotImplementedError
