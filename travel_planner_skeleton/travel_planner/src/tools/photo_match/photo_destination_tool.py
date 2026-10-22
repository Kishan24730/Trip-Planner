"""Feature 7: photo to destination.

Purpose: Suggest destinations that look like an uploaded photo, then filter by budget and visa.
Build order: 10

Data sources: ImageEmbedder, DestinationIndex, data/curated/destinations.json, visa and budget tools
"""

from __future__ import annotations

from src.schemas.tool_io import ToolRequest, ToolResult
from src.tools.base_tool import BaseTool


class PhotoDestinationTool(BaseTool):
    name = "photo_destination"
    description = "Suggest destinations that look like an uploaded photo, then filter by budget and visa."

    def run(self, request: ToolRequest) -> ToolResult:
        """Suggest destinations that look like an uploaded photo, then filter by budget and visa.

        TODO:
        - Embed the uploaded photo
        - Query the index
        - Filter by budget and visa difficulty
        - Explain each match in one line
        - Never claim certainty. Show similarity as 'looks similar', not 'is'
        """
        raise NotImplementedError

    def _load_photo(self, path: str) -> object:
        """Open and validate the uploaded image.
        """
        raise NotImplementedError

    def _filter_by_constraints(self, matches: list[dict], request: ToolRequest) -> list[dict]:
        """Apply budget and visa filters.
        """
        raise NotImplementedError
