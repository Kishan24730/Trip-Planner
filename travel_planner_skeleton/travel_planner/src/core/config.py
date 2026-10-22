"""Settings loader.

Purpose: Read keys and options from environment variables (.env).
Build order: 2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Settings:
    llm_provider: str = ""
    gemini_api_key: Optional[str] = None
    groq_api_key: Optional[str] = None
    ollama_host: Optional[str] = None
    opentripmap_key: Optional[str] = None
    ticketmaster_key: Optional[str] = None
    serpapi_key: Optional[str] = None
    openrouteservice_key: Optional[str] = None
    foursquare_key: Optional[str] = None
    tavily_key: Optional[str] = None
    user_agent: str = ""
    cache_dir: str = "data/cache"


def load_settings() -> Settings:
    """Load .env and build Settings.

    TODO:
    - Use python-dotenv to read .env
    - Warn (do not crash) when an optional key is missing; tools degrade without it
    - Cache the result so it loads once
    """
    raise NotImplementedError
