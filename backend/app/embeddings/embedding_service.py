from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingService:
    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")
        print("Embedding model loaded!")

    @property
    def dimension(self):
        """
        Returns embedding dimension automatically.
        """
        return self.model.get_embedding_dimension()

    def embed(self, text: str) -> np.ndarray:
        """
        Generate embedding for a given text.
        """
        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=False
        )

        return embedding.astype(np.float32)