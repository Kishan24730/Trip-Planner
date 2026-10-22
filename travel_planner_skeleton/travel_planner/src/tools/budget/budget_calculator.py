"""Budget calculator.

Purpose: Split the budget by category and check the plan fits. Plain arithmetic, no LLM.
Build order: 5

Data sources: Other tools' costs
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class BudgetCalculator(BaseTool):
    name = "budget"
    description = "Split the budget by category and check the plan fits. Plain arithmetic, no LLM."

    def run(self, request: ToolRequest) -> ToolResult:
        """Split the budget by category and check the plan fits. Plain arithmetic, no LLM.

        TODO:
        - Define category shares (transport, stay, food, activities, buffer)
        - Sum costs from tool results
        - Flag over-budget and suggest what to cut
        - Keep INR as the base currency and note conversion rates used
        """
        raise NotImplementedError

    def split_budget(self, total_inr: float, days: int) -> dict:
        """Allocate by category.
        """
        raise NotImplementedError

    def check_fit(self, itinerary: object, total_inr: float) -> dict:
        """Return pass/fail with the gap.
        """
        raise NotImplementedError
