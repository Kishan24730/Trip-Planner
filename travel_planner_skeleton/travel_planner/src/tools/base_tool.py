"""Base class for all tools.

Purpose: Common interface so the orchestrator can run any tool.
Build order: 3
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from src.schemas.tool_io import ToolRequest, ToolResult


class BaseTool(ABC):
    name: str = ""
    description: str = ""

    @abstractmethod
    def run(self, request: ToolRequest) -> ToolResult:
        """Do the tool's work. Return ToolResult."""
        raise NotImplementedError

    def safe_run(self, request: ToolRequest) -> ToolResult:
        """Wrap run() so a failure becomes ToolResult(ok=False) and never crashes the trip.

        TODO:
        - Catch exceptions
        - Log with trace id
        - Add timeout handling
        """
        raise NotImplementedError
