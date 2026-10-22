"""Rented vehicle tool.

Purpose: Car, bike or scooter hire estimates.
Build order: 7

Data sources: Curated price bands
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class RentedVehicleTool(BaseTool):
    name = "rented_vehicle"
    description = "Car, bike or scooter hire estimates."

    def run(self, request: ToolRequest) -> ToolResult:
        """Car, bike or scooter hire estimates.

        TODO:
        - Return daily price band
        - Remind about driving licence and IDP
        - Add fuel and parking estimate
        """
        raise NotImplementedError
