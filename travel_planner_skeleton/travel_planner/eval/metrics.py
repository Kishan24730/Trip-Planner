"""Evaluation metrics.

Purpose: Measure the planner, not just look at it.
Build order: 11
"""

from __future__ import annotations




def constraint_pass_rate(results: list[dict]) -> float:
    """Share of trips passing all hard checks.
    """
    raise NotImplementedError

def groundedness_rate(results: list[dict]) -> float:
    """Share of claims with evidence.
    """
    raise NotImplementedError

def avg_latency_seconds(results: list[dict]) -> float:
    """Mean planning time.
    """
    raise NotImplementedError

def avg_cost_per_trip(results: list[dict]) -> float:
    """LLM and API cost per itinerary.
    """
    raise NotImplementedError
