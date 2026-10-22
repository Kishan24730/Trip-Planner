"""Scoring functions.

Purpose: Each returns a score between 0 and 1 for one candidate place.
Build order: 7
"""

from __future__ import annotations




def score_persona_fit(place: dict, persona: object, motive: str) -> float:
    """How well tags match the persona and motive.
    """
    raise NotImplementedError

def score_budget_fit(place_cost: float, budget_left: float) -> float:
    """Penalise places that eat the budget.
    """
    raise NotImplementedError

def score_season_fit(place: dict, month: int, weather: dict) -> float:
    """Seasonal closures, monsoon, snow, heat.
    """
    raise NotImplementedError

def score_distance(minutes_from_base: float) -> float:
    """Closer is better, with a cap.
    """
    raise NotImplementedError

def score_quality(rating: float, review_count: int) -> float:
    """Rating with a confidence adjustment for few reviews.
    """
    raise NotImplementedError

def combine_scores(scores: dict[str, float], weights: dict[str, float]) -> float:
    """Weighted sum.

    TODO:
    - Document your weights in docs/architecture.md
    """
    raise NotImplementedError
