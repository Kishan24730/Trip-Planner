"""Guide tool.

Purpose: Practical how-to for the destination: getting around, best times, local advice.
Build order: 6

Data sources: Wikivoyage
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class GuideTool(BaseTool):
    name = "guide"
    description = "Practical how-to for the destination: getting around, best times, local advice."

    def run(self, request: ToolRequest) -> ToolResult:
        """Practical how-to for the destination: getting around, best times, local advice.

        TODO:
        - Pull relevant Wikivoyage sections
        - Summarise to short bullets
        - Cite the page
        """
        raise NotImplementedError
