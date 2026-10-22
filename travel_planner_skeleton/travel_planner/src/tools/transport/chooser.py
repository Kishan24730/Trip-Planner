"""Mode of transport chooser.

Purpose: Pick bus, train, flight or rented vehicle for each leg.
Build order: 6

Data sources: Transport tools below
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class TransportChooser(BaseTool):
    name = "transport_chooser"
    description = "Pick bus, train, flight or rented vehicle for each leg."

    def run(self, request: ToolRequest) -> ToolResult:
        """Pick bus, train, flight or rented vehicle for each leg.

        TODO:
        - Compare cost, time and comfort per leg
        - Respect budget and persona
        - Return ranked options with reasons
        """
        raise NotImplementedError

    def _score_option(self, option: dict, preferences: dict) -> float:
        """Score one option.
        """
        raise NotImplementedError
