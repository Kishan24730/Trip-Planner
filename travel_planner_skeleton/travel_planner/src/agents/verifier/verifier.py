"""Verifier.

Purpose: Run hard checks, grounding checks and soft LLM checks. Decide pass, retry or ship with flags.
Build order: 5
"""

from __future__ import annotations

from dataclasses import dataclass, field

from src.agents.base_agent import BaseAgent
from src.schemas.itinerary import Itinerary


@dataclass
class VerificationReport:
    passed: list[str] = field(default_factory=list)
    failed: list[str] = field(default_factory=list)
    unverified: list[str] = field(default_factory=list)

    # TODO: add summary() -> str, e.g. "14 of 16 checks passed, 2 fixed"


class Verifier(BaseAgent):
    def verify(self, itinerary: Itinerary, context: dict) -> VerificationReport:
        """Run all checks.

        TODO:
        - Hard checks first
        - Grounding checks second
        - LLM soft checks last (persona fit, tone)
        """
        raise NotImplementedError

    def verify_and_fix(self, itinerary: Itinerary, context: dict) -> Itinerary:
        """Loop verify -> regenerate up to the retry cap.

        TODO:
        - Never loop forever
        """
        raise NotImplementedError
