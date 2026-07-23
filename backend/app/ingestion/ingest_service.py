from pathlib import Path

from app.services.document_processor import DocumentProcessor
from app.services.chunker import TextChunker
from app.embeddings.embedding_service import EmbeddingService
from app.vectorStore.qdrant_store import QdrantVectorStore


class IngestionService:

    def __init__(self):

        self.processor = DocumentProcessor()

        self.chunker = TextChunker()

        self.embedder = EmbeddingService()

        self.vector_store = QdrantVectorStore(
            self.embedder.dimension
        )

    def ingest(
        self,
        pdf_path: str
    ):

        pdf_path = Path(pdf_path)

        print(f"\nReading {pdf_path.name}")

        text = self.processor.extract_text(
            pdf_path
        )

        print(
            f"Extracted {len(text)} characters"
        )

        chunks = self.chunker.chunk(text)

        print(
            f"Created {len(chunks)} chunks"
        )

        for i, chunk in enumerate(chunks):

            embedding = self.embedder.embed(
                chunk
            )

            self.vector_store.add(

                embedding=embedding,

                chunk=chunk,

                metadata={

                    "document": pdf_path.name,

                    "chunk_id": i + 1

                }

            )

        return {

            "filename": pdf_path.name,

            "chunks": len(chunks),

            "characters": len(text)

        }