"""Hard checks.

Purpose: Plain logic. Each returns a list of problems (empty = pass).
Build order: 5
"""

from __future__ import annotations

from src.schemas.itinerary import Itinerary


def check_budget(itinerary: Itinerary, max_budget_inr: float) -> list[str]:
    """Total cost within budget.
    """
    raise NotImplementedError

def check_dates(itinerary: Itinerary, days: int) -> list[str]:
    """Day count and dates match the request.
    """
    raise NotImplementedError

def check_opening_hours(itinerary: Itinerary, places: list[dict]) -> list[str]:
    """Visit time inside opening hours. Unknown hours = warning.
    """
    raise NotImplementedError

def check_travel_time(itinerary: Itinerary) -> list[str]:
    """Enough minutes between stops.
    """
    raise NotImplementedError

def check_day_load(itinerary: Itinerary, max_activities: int) -> list[str]:
    """Days not overpacked.
    """
    raise NotImplementedError

def check_stay_limit(itinerary: Itinerary, allowed_stay_days: int) -> list[str]:
    """Trip not longer than the visa allows.
    """
    raise NotImplementedError

def check_visa_lead_time(start_date: str, lead_time_days: int) -> list[str]:
    """Enough time to get the visa.
    """
    raise NotImplementedError
