"""Task splitter.

Purpose: Turn a TripRequest into sub-tasks and decide order and parallelism.
Build order: 4
"""

from __future__ import annotations

from dataclasses import dataclass, field

from src.schemas.trip_request import TripRequest


@dataclass
class SubTask:
    tool: str
    depends_on: list[str] = field(default_factory=list)
    params: dict = field(default_factory=dict)


def split(trip: TripRequest) -> list[SubTask]:
    """Return the sub-tasks.

    TODO:
    - Start with a fixed rule-based split (weather, attractions, events, hotels, visa_documents, local_tips ...)
    - Add LLM-based refinement later
    - Visa lead time and budget must be known before booking-type tasks
    - Mark independent tasks so they run in parallel
    """
    raise NotImplementedError
