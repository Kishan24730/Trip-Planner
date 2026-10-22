"""Culture tool.

Purpose: Local culture, etiquette, dress code and customs for the destination.
Build order: 6

Data sources: Wikivoyage, Wikipedia, data/curated/local_tips.json
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class CultureTool(BaseTool):
    name = "culture"
    description = "Local culture, etiquette, dress code and customs for the destination."

    def run(self, request: ToolRequest) -> ToolResult:
        """Local culture, etiquette, dress code and customs for the destination.

        TODO:
        - Fetch culture summary
        - Extract etiquette and dress rules
        - Keep it short and cited
        """
        raise NotImplementedError
