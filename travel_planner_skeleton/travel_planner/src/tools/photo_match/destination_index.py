"""Destination index (feature 7).

Purpose: Store reference-image vectors and search them.
Build order: 10
"""

from __future__ import annotations

from typing import Any


class DestinationIndex:
    def build(self, images_dir: str) -> None:
        """Embed all images in data/reference_images/<destination>/.

        TODO:
        - Average several images per destination or keep them separate
        - Save to data/cache
        """
        raise NotImplementedError

    def save(self, path: str) -> None:
        """Persist the index.
        """
        raise NotImplementedError

    def load(self, path: str) -> None:
        """Load the index.
        """
        raise NotImplementedError

    def query(self, vector: Any, k: int = 5) -> list[dict]:
        """Return top k destinations with scores.
        """
        raise NotImplementedError
