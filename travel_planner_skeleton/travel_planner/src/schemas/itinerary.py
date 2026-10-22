"""Itinerary output shape.

Purpose: What the builder produces, the verifier checks and the UI shows.
Build order: 1
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from src.schemas.evidence import Evidence


@dataclass
class Activity:
    name: str
    start_time: str                    # "HH:MM"
    end_time: str
    category: str                      # meal, sightseeing, transport, rest, event ...
    cost_inr: float = 0.0
    lat: Optional[float] = None
    lon: Optional[float] = None
    why_this_time: str = ""            # best-time reasoning shown to the user
    evidence: list[Evidence] = field(default_factory=list)


@dataclass
class DayPlan:
    day_number: int
    date: Optional[str]
    summary: str
    activities: list[Activity] = field(default_factory=list)
    weather_note: str = ""
    backup_plan: str = ""              # indoor option if weather turns


@dataclass
class BudgetBreakdown:
    transport: float = 0.0
    stay: float = 0.0
    food: float = 0.0
    activities: float = 0.0
    other: float = 0.0
    # TODO: add total() when you implement it


@dataclass
class Itinerary:
    destination: str
    days: list[DayPlan] = field(default_factory=list)
    budget: BudgetBreakdown = field(default_factory=BudgetBreakdown)
    documents_checklist: list[str] = field(default_factory=list)
    safety_alerts: list[str] = field(default_factory=list)      # feature 4
    packing_list: list[str] = field(default_factory=list)       # feature 4
    local_tips: dict = field(default_factory=dict)              # feature 10
    verification_summary: str = ""
