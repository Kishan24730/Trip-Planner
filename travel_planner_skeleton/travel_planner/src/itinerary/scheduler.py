"""Day scheduler.

Purpose: Place activities into time slots. Plain logic, LLM writes text only.
Build order: 8
"""

from __future__ import annotations

from src.schemas.itinerary import DayPlan


def fill_day(places: list[dict], day_number: int, constraints: dict) -> DayPlan:
    """Build one day.

    TODO:
    - Respect opening hours (None = unknown)
    - Cap activities per day
    - Add travel time and buffers
    """
    raise NotImplementedError

def place_meals(day: DayPlan, meal_windows: dict) -> DayPlan:
    """Insert meals at local times.
    """
    raise NotImplementedError

def apply_golden_hour(day: DayPlan, sunrise: str, sunset: str) -> DayPlan:
    """Move photo or viewpoint stops to golden hour.
    """
    raise NotImplementedError

def apply_arrival_buffer(day: DayPlan, arrival_type: str) -> DayPlan:
    """Keep day 1 light after arrival, longer for visa on arrival.
    """
    raise NotImplementedError
