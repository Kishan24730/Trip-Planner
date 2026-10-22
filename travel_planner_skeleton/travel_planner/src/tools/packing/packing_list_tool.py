"""Feature 4b: packing list from forecast.

Purpose: Packing list from weather, persona, activities and required documents.
Build order: 8

Data sources: Weather tool result, data/curated/packing_rules.json, visa_documents result
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class PackingListTool(BaseTool):
    name = "packing_list"
    description = "Packing list from weather, persona, activities and required documents."

    def run(self, request: ToolRequest) -> ToolResult:
        """Packing list from weather, persona, activities and required documents.

        TODO:
        - Classify weather: hot, cold, rain, humid, snow
        - Merge base + persona + weather + activity items
        - Dedupe and group (documents, clothing, gear, health)
        - Add document items from the visa tool
        """
        raise NotImplementedError

    def _classify_weather(self, weather_days: list[dict]) -> set[str]:
        """Return weather tags.
        """
        raise NotImplementedError

    def _merge_items(self, *groups: list[str]) -> list[str]:
        """Dedupe while keeping order.
        """
        raise NotImplementedError
