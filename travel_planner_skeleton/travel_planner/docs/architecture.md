# Architecture notes (fill as you decide)

## Agents
- Orchestrator: how it splits the request, which tasks run in parallel, which depend on others.
- Verifier: hard checks, grounding checks, retry cap, partial regeneration rule.

## Data flow
Write the order: request -> tasks -> tool results -> ranking -> itinerary -> verify -> output.

## Decisions log
| Date | Decision | Reason |
| --- | --- | --- |
