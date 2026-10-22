"""Hotels tool.

Purpose: Stay options that fit the budget.
Build order: 6

Data sources: OSM for names, SerpApi Google Hotels (small quota), price bands as estimates
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class HotelsTool(BaseTool):
    name = "hotels"
    description = "Stay options that fit the budget."

    def run(self, request: ToolRequest) -> ToolResult:
        """Stay options that fit the budget.

        TODO:
        - Get hotel candidates
        - Attach price: live if API gave it, else 'estimated' band
        - Filter by nightly budget from the budget calculator
        """
        raise NotImplementedError
