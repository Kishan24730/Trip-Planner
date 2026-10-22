"""Feature 10c: local phrases.

Purpose: Useful phrases with pronunciation.
Build order: 8

Data sources: data/curated/local_tips.json
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class PhrasesTool(BaseTool):
    name = "phrases"
    description = "Useful phrases with pronunciation."

    def run(self, request: ToolRequest) -> ToolResult:
        """Useful phrases with pronunciation.

        TODO:
        - Pick the local language
        - Return 8 to 10 core phrases
        - Include pronunciation in Latin script
        """
        raise NotImplementedError
