from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingService:
    MODEL_NAME = "all-MiniLM-L6-v2"

    def __init__(self):

        self._model = None

    def _load_model(self):

        if self._model is None:

            print(
                "Loading embedding model..."
            )

            self._model = SentenceTransformer(
                self.MODEL_NAME
            )

    def embed_text(
        self,
        text: str,
    ) -> np.ndarray:

        self._load_model()

        return self._model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

    def embed_batch(
        self,
        texts: list[str],
    ) -> np.ndarray:

        self._load_model()

        return self._model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

    def embedding_dimension(
        self,
    ) -> int:

        self._load_model()

        return (
            self._model
            .get_sentence_embedding_dimension()
        )