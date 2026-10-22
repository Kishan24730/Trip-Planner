"""Train tool.

Purpose: Train options, mainly for India.
Build order: 7

Data sources: No official free API. Curated data or manual entry.
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class TrainTool(BaseTool):
    name = "train"
    description = "Train options, mainly for India."

    def run(self, request: ToolRequest) -> ToolResult:
        """Train options, mainly for India.

        TODO:
        - Decide the data source first
        - Return options with 'estimated' label if not live
        """
        raise NotImplementedError
