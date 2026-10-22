"""Feature 10d: eSIM, SIM, transit pass, plugs, emergency numbers.

Purpose: Staying connected and getting around locally.
Build order: 8

Data sources: data/curated/local_tips.json
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class ConnectivityTool(BaseTool):
    name = "connectivity"
    description = "Staying connected and getting around locally."

    def run(self, request: ToolRequest) -> ToolResult:
        """Staying connected and getting around locally.

        TODO:
        - Return SIM or eSIM options
        - Return transit pass tip, plug type and emergency numbers
        - Show last_checked date
        """
        raise NotImplementedError
