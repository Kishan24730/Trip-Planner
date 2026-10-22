"""User input for a trip.

Purpose: One shared shape for the form, orchestrator and tools.
Build order: 1
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Persona(str, Enum):
    MOUNTAINEER = "mountaineer"
    BEACH = "beach"
    CULTURE_STUDY = "culture_study"


@dataclass
class TripRequest:
    destination: str
    origin_city: str
    days: int
    persona: Persona
    motive: str                       # relax, adventure, romance, family, spiritual, photography ...
    max_budget_inr: float
    food_preference: str              # veg, vegan, jain, halal, non_veg, street_food ...
    start_date: Optional[str] = None  # ISO date
    passport_country: str = "IN"
    travellers: int = 1
    notes: str = ""

    # TODO: add validate() (days >= 1, budget > 0, known persona) when you implement it
