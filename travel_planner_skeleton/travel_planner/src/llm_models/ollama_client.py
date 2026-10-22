"""OllamaClient.

Purpose: Local model (for example on your Jetson) for offline mode.
Build order: 4
"""

from __future__ import annotations

from typing import Any, Optional

from src.llm_models.base import LLMClient


class OllamaClient(LLMClient):
    def __init__(self, api_key: Optional[str] = None, model: str = "") -> None:
        self.api_key = api_key
        self.model = model

    def generate(self, prompt: str, system: Optional[str] = None) -> str:
        """Call the provider.

        TODO:
        - Timeout and retry
        - Count tokens or cost if the API reports it
        """
        raise NotImplementedError

    def generate_structured(self, prompt: str, schema: dict[str, Any], system: Optional[str] = None) -> dict[str, Any]:
        """JSON output.

        TODO:
        - Ask for JSON, parse, validate, retry once
        """
        raise NotImplementedError
