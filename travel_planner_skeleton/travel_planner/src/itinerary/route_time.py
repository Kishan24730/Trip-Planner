"""Travel time between places.

Purpose: Feasibility checks need real travel minutes.
Build order: 8
"""

from __future__ import annotations




def travel_minutes(lat1: float, lon1: float, lat2: float, lon2: float, mode: str) -> float:
    """Minutes between two points.

    TODO:
    - Try OpenRouteService or OSRM
    - Fallback: distance / average speed, labelled 'estimated'
    """
    raise NotImplementedError
