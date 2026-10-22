"""Rerouting tool.

Purpose: Replan when something changes: weather, delay, closure, budget overrun.
Build order: 9

Data sources: Weather tool, transport tools, itinerary builder
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class ReroutingTool(BaseTool):
    name = "rerouting"
    description = "Replan when something changes: weather, delay, closure, budget overrun."

    def run(self, request: ToolRequest) -> ToolResult:
        """Replan when something changes: weather, delay, closure, budget overrun.

        TODO:
        - Detect the trigger
        - Pick the smallest change that fixes it
        - Re-run the verifier on the changed day only
        """
        raise NotImplementedError

    def _detect_trigger(self, itinerary: object, updates: dict) -> str:
        """Name what changed.
        """
        raise NotImplementedError

    def _replan_day(self, day: object, trigger: str) -> object:
        """Return a replacement day.
        """
        raise NotImplementedError
