"""Tool registry.

Purpose: Orchestrator looks tools up by name here.
Build order: 3
"""

from __future__ import annotations

from src.tools.base_tool import BaseTool


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        """Add a tool.
        """
        raise NotImplementedError

    def get(self, name: str) -> BaseTool:
        """Return a tool or raise a clear error.
        """
        raise NotImplementedError

    def list_names(self) -> list[str]:
        """All registered tool names.
        """
        raise NotImplementedError
