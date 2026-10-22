"""Bus tool.

Purpose: Bus options for intercity legs.
Build order: 7

Data sources: Curated or estimated data
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class BusTool(BaseTool):
    name = "bus"
    description = "Bus options for intercity legs."

    def run(self, request: ToolRequest) -> ToolResult:
        """Bus options for intercity legs.

        TODO:
        - Decide the data source first
        - Return duration and cost estimates
        """
        raise NotImplementedError
