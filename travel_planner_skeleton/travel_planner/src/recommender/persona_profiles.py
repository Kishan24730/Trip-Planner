"""Persona profiles.

Purpose: Map each persona to the tags that matter for it.
Build order: 7
"""

from __future__ import annotations

from src.schemas.trip_request import Persona


# TODO: fill by hand. Example keys only, no values yet.
PERSONA_TAG_WEIGHTS: dict[Persona, dict[str, float]] = {
    Persona.MOUNTAINEER: {},
    Persona.BEACH: {},
    Persona.CULTURE_STUDY: {},
}

MOTIVE_TAG_BOOSTS: dict[str, dict[str, float]] = {}   # relax, adventure, romance, family, spiritual, photography
