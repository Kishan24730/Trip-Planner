"""Events tool.

Purpose: Festivals and events during the trip dates.
Build order: 6

Data sources: data/curated/festivals.json, Ticketmaster (weak for India), optional LLM web search
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class EventsTool(BaseTool):
    name = "events"
    description = "Festivals and events during the trip dates."

    def run(self, request: ToolRequest) -> ToolResult:
        """Festivals and events during the trip dates.

        TODO:
        - Load curated festivals by city and month
        - Call Ticketmaster for international trips
        - Mark confidence: official / curated / unverified
        - Warn that lunar festival dates move every year
        """
        raise NotImplementedError

    def _load_curated(self, city: str, month: int) -> list[dict]:
        """Read curated festivals.
        """
        raise NotImplementedError

    def _fetch_ticketmaster(self, city: str, start: str, end: str) -> list[dict]:
        """Ticketmaster events.
        """
        raise NotImplementedError
