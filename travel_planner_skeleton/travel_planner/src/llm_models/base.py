"""LLM client interface.

Purpose: All providers implement the same methods so you can swap them.
Build order: 4
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional


class LLMClient(ABC):
    @abstractmethod
    def generate(self, prompt: str, system: Optional[str] = None) -> str:
        """Plain text generation."""
        raise NotImplementedError

    @abstractmethod
    def generate_structured(self, prompt: str, schema: dict[str, Any], system: Optional[str] = None) -> dict[str, Any]:
        """Return JSON that matches schema. TODO: validate and retry once on malformed output."""
        raise NotImplementedError
