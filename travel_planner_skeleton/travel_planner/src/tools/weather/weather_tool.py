"""Weather tool (build this first, end to end).

Purpose: Forecast for trip dates, or climate averages when dates are beyond the forecast range.
Build order: 3 (first tool)

Data sources: Open-Meteo (no key). Non-commercial use.
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class WeatherTool(BaseTool):
    name = "weather"
    description = "Forecast for trip dates, or climate averages when dates are beyond the forecast range."

    def run(self, request: ToolRequest) -> ToolResult:
        """Forecast for trip dates, or climate averages when dates are beyond the forecast range.

        TODO:
        - Geocode destination (reuse the geocode helper you write for attractions)
        - If dates are within forecast range use forecast, else use historical averages and label them 'estimated'
        - Return daily temp range, rain chance, sunrise and sunset (needed for golden hour)
        - Attach Evidence with freshness label
        """
        raise NotImplementedError

    def _pick_mode(self, start_date: str, end_date: str) -> str:
        """Return 'forecast' or 'climate'.
        """
        raise NotImplementedError

    def _summarise_day(self, raw_day: dict) -> dict:
        """Normalise one day of weather.
        """
        raise NotImplementedError
