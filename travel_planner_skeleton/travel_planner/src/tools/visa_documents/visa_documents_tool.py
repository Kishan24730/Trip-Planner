"""Visa and documents tool.

Purpose: Visa category, documents with criticality, lead time and itinerary constraints for an Indian passport.
Build order: 5

Data sources: data/curated/visa_requirements.json, data/context/india_passport_travel_docs_context.md
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class VisaDocumentsTool(BaseTool):
    name = "visa_documents"
    description = "Visa category, documents with criticality, lead time and itinerary constraints for an Indian passport."

    def run(self, request: ToolRequest) -> ToolResult:
        """Visa category, documents with criticality, lead time and itinerary constraints for an Indian passport.

        TODO:
        - Look up destination AND transit countries
        - Return category, documents by criticality (C1 to C4), lead time
        - Return itinerary constraints: stay limit, named entry points, arrival card deadlines
        - Always attach source_url and last_checked, plus the 'verify officially' warning
        """
        raise NotImplementedError

    def _lookup(self, country: str) -> dict:
        """Find the row for a country.
        """
        raise NotImplementedError

    def _lead_time_days(self, category: str) -> int:
        """Estimate days needed before travel.
        """
        raise NotImplementedError
