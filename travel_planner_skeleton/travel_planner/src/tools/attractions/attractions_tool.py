"""Attractions tool.

Purpose: Find places to visit near the destination.
Build order: 6

Data sources: OSM Overpass, OpenTripMap, Wikidata, Wikivoyage
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class AttractionsTool(BaseTool):
    name = "attractions"
    description = "Find places to visit near the destination."

    def run(self, request: ToolRequest) -> ToolResult:
        """Find places to visit near the destination.

        TODO:
        - Geocode city
        - Query sources and normalise to one Place shape
        - Dedupe near-duplicates
        - Keep opening_hours raw. None means unknown, never 'open'
        - Cache heavily (Overpass is strict)
        """
        raise NotImplementedError

    def _query_overpass(self, lat: float, lon: float, radius_m: int) -> list[dict]:
        """Raw Overpass results.
        """
        raise NotImplementedError

    def _query_opentripmap(self, lat: float, lon: float, radius_m: int) -> list[dict]:
        """Raw OpenTripMap results.
        """
        raise NotImplementedError

    def _dedupe(self, places: list[dict]) -> list[dict]:
        """Merge near-duplicates.
        """
        raise NotImplementedError
