"""Orchestrator.

Purpose: Main controller: split, run tools, rank, build, verify.
Build order: 4
"""

from __future__ import annotations

from src.agents.base_agent import BaseAgent
from src.schemas.itinerary import Itinerary
from src.schemas.trip_request import TripRequest


class Orchestrator(BaseAgent):
    def plan_trip(self, trip: TripRequest) -> Itinerary:
        """Full pipeline for one request.

        TODO:
        - split tasks
        - run_tools
        - rank places
        - build itinerary
        - verify and regenerate
        - return final itinerary
        """
        raise NotImplementedError

    def run_tools(self, subtasks: list) -> dict:
        """Run tools in parallel respecting dependencies.

        TODO:
        - Per-tool timeout
        - Collect ToolResult per tool
        - One failure must not stop the others
        """
        raise NotImplementedError
