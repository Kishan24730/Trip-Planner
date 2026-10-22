"""Feature 10a: currency and money tips.

Purpose: Exchange rate, budget converted to local currency, cash versus card advice.
Build order: 8

Data sources: Frankfurter (no key), data/curated/local_tips.json
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class CurrencyTool(BaseTool):
    name = "currency"
    description = "Exchange rate, budget converted to local currency, cash versus card advice."

    def run(self, request: ToolRequest) -> ToolResult:
        """Exchange rate, budget converted to local currency, cash versus card advice.

        TODO:
        - Fetch rate and record the date
        - Convert the budget and daily costs
        - Add cash/card and forex advice from curated tips
        """
        raise NotImplementedError
