"""Pick the LLM client.

Purpose: Choose provider from settings.
Build order: 4
"""

from __future__ import annotations

from src.llm_models.base import LLMClient


def get_llm() -> LLMClient:
    """Return the client for LLM_PROVIDER.

    TODO:
    - Fallback order if one provider fails or rate limits
    """
    raise NotImplementedError
