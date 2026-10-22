"""Feature 10b: tipping and etiquette.

Purpose: Tipping norms and basic etiquette.
Build order: 8

Data sources: data/curated/local_tips.json
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class TippingTool(BaseTool):
    name = "tipping"
    description = "Tipping norms and basic etiquette."

    def run(self, request: ToolRequest) -> ToolResult:
        """Tipping norms and basic etiquette.

        TODO:
        - Look up country
        - Return short tips
        - Fall back to 'not available' instead of guessing
        """
        raise NotImplementedError
