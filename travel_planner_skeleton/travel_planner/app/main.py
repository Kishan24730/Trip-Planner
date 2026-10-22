"""Streamlit app entry.

Purpose: Input form and results view.
Build order: 10
"""

from __future__ import annotations




def render_input_form() -> object:
    """Form: days, destination, persona, motive, budget, food, start date.
    """
    raise NotImplementedError

def render_itinerary(itinerary: object) -> None:
    """Day-by-day view with timings and why-this-time notes.
    """
    raise NotImplementedError

def render_budget(budget: object) -> None:
    """Budget breakdown chart.
    """
    raise NotImplementedError

def render_evidence_ledger(itinerary: object) -> None:
    """Show source, time and live/cached/estimated badge per fact.
    """
    raise NotImplementedError

def render_safety_and_packing(itinerary: object) -> None:
    """Feature 4 panel.
    """
    raise NotImplementedError

def render_photo_search() -> None:
    """Feature 7: upload a photo, show similar destinations.
    """
    raise NotImplementedError

def render_local_tips(itinerary: object) -> None:
    """Feature 10 panel: money, tipping, phrases, eSIM.
    """
    raise NotImplementedError

def main() -> None:
    """Wire everything together.
    """
    raise NotImplementedError
