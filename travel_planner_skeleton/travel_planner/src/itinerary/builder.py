"""Itinerary builder.

Purpose: Combine ranked places, tool results and constraints into an Itinerary.
Build order: 8
"""

from __future__ import annotations

from src.schemas.itinerary import Itinerary
from src.schemas.trip_request import TripRequest


def build_itinerary(trip: TripRequest, tool_results: dict, ranked_places: list[dict]) -> Itinerary:
    """Assemble days, budget, documents, safety, packing and local tips.

    TODO:
    - Call the scheduler per day
    - Attach weather note and backup plan per day
    - Fill documents_checklist from visa_documents
    - Fill safety_alerts and packing_list (feature 4)
    - Fill local_tips (feature 10)
    - Use the LLM only to write short descriptions from tool data
    """
    raise NotImplementedError
