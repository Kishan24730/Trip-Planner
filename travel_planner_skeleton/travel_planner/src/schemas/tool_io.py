"""Shared input and output for every tool.

Purpose: Tools take ToolRequest and return ToolResult so the orchestrator can treat them the same.
Build order: 1
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from src.schemas.evidence import Evidence
from src.schemas.trip_request import TripRequest


@dataclass
class ToolRequest:
    trip: TripRequest
    params: dict[str, Any] = field(default_factory=dict)   # tool-specific extras


@dataclass
class ToolResult:
    tool: str
    ok: bool
    data: Any = None
    evidence: list[Evidence] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    error: Optional[str] = None
