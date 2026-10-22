# Travel Planner (agentic AI + recommender)

Skeleton only. You write the logic. Each file has a docstring with its purpose, build order and TODO steps.

## Flow
user form -> Orchestrator (splits tasks) -> tools run in parallel -> recommender ranks -> itinerary builder
-> Verifier (checks, regenerates failing parts, max retries) -> app shows result with evidence ledger.

## Extra features included
- Feature 4: safety alerts + packing list from the forecast (`src/tools/safety_alerts`, `src/tools/packing`)
- Feature 7: photo-to-destination (`src/tools/photo_match`)
- Feature 10: currency, tipping, phrases, eSIM and transit tips (`src/tools/local_tips`)

## Build order (suggested)
1. `src/schemas`  2. `src/core`  3. `src/tools/weather` (first tool end to end)
4. `src/agents/orchestrator`  5. `src/agents/verifier`  6. remaining tools
7. `src/recommender`  8. `src/itinerary`  9. feature 4, 10, then 7  10. `app/`  11. `eval/`

## Setup
1. Copy `.env.example` to `.env` and fill your own keys. Never commit `.env`.
2. Install packages from `requirements.txt`.
3. Run tests with pytest (all tests start as skipped TODOs).

## Rules to keep
- Every fact shown to the user must carry an `Evidence` record (source, time, live/cached/estimated).
- Hard checks (budget, dates, hours, travel time) are plain logic, not LLM.
- Tools never crash the run. They return a `ToolResult` with `ok=False` and a reason.
