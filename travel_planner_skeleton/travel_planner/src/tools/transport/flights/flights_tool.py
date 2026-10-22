"""Flights tool.

Purpose: Flight options and price comparison (cheapest, fastest, best value).
Build order: 6

Data sources: SerpApi Google Flights (small quota), cached and mock data. Amadeus Self-Service is shut down.
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class FlightsTool(BaseTool):
    name = "flights"
    description = "Flight options and price comparison (cheapest, fastest, best value)."

    def run(self, request: ToolRequest) -> ToolResult:
        """Flight options and price comparison (cheapest, fastest, best value).

        TODO:
        - Search by origin, destination, dates
        - Label every price live / cached / estimated
        - Expire prices with a TTL
        - Convert currency with a documented rate source
        """
        raise NotImplementedError
