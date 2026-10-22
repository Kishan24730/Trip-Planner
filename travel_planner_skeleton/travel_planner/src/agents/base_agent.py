"""Base agent.

Purpose: Shared helpers for orchestrator and verifier.
Build order: 4
"""

from __future__ import annotations

from src.llm_models.base import LLMClient


class BaseAgent:
    def __init__(self, llm: LLMClient) -> None:
        self.llm = llm
