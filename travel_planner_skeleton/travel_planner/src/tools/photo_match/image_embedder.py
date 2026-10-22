"""Image embedder (feature 7).

Purpose: Turn a photo into a vector so similar destinations can be found.
Build order: 10
"""

from __future__ import annotations

from typing import Any


class ImageEmbedder:
    def __init__(self, model_name: str = "") -> None:
        self.model_name = model_name

    def load_model(self) -> None:
        """Load the vision model once.

        TODO:
        - Pick a model (for example a CLIP-style model)
        - Handle CPU and Jetson GPU
        """
        raise NotImplementedError

    def embed_image(self, image_path: str) -> Any:
        """Return one vector.

        TODO:
        - Open, resize and normalise
        - Run the model
        """
        raise NotImplementedError

    def embed_batch(self, image_paths: list[str]) -> list[Any]:
        """Return many vectors.
        """
        raise NotImplementedError
