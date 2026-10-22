"""Project exceptions.

Purpose: Named errors so callers can handle each case.
Build order: 2
"""

from __future__ import annotations




class ConfigError(Exception):
    """Missing or invalid configuration."""


class ToolError(Exception):
    """A tool failed in a way it could not recover from."""


class RateLimitError(Exception):
    """An upstream API said slow down."""


class VerificationError(Exception):
    """Verifier gave up after max retries."""
