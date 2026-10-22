"""Ranker.

Purpose: Rank candidate places and diversify the list.
Build order: 7
"""

from __future__ import annotations

from src.schemas.trip_request import TripRequest


def rank_places(candidates: list[dict], trip: TripRequest, context: dict) -> list[dict]:
    """Score and sort candidates.

    TODO:
    - Candidates come from tools only. Never invent places
    """
    raise NotImplementedError

def diversify(ranked: list[dict], k: int) -> list[dict]:
    """Pick k items avoiding near-duplicates (MMR style).
    """
    raise NotImplementedError

def explain_rank(place: dict, scores: dict) -> str:
    """One line on why this place was chosen.
    """
    raise NotImplementedError
