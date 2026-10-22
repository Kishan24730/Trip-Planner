"""Feature 4a: safety alerts.

Purpose: Safety level and alerts for the destination and travel dates.
Build order: 8

Data sources: data/curated/advisories.json (from official advisories), optional web search with citations
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class SafetyAlertsTool(BaseTool):
    name = "safety_alerts"
    description = "Safety level and alerts for the destination and travel dates."

    def run(self, request: ToolRequest) -> ToolResult:
        """Safety level and alerts for the destination and travel dates.

        TODO:
        - Look up country advisory level
        - Add local alerts: scams, natural hazards by season, restricted areas
        - Return level plus short actionable alerts
        - Always show source_url and last_checked
        """
        raise NotImplementedError

    def _load_advisories(self) -> list[dict]:
        """Read advisories file.
        """
        raise NotImplementedError

    def _season_hazards(self, destination: str, month: int) -> list[str]:
        """Hazards by season (monsoon, snow, heat).
        """
        raise NotImplementedError
