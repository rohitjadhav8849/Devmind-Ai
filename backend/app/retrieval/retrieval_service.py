from app.embeddings.embedding_service import EmbeddingService
from app.vectorStore.qdrant_store import QdrantVectorStore
from app.prompt.prompt_builder import PromptBuilder
from app.llm.ollama_service import OllamaService


class RetrievalService:

    def __init__(self):

        self.embedder = EmbeddingService()

        self.vector_store = QdrantVectorStore(
            self.embedder.dimension
        )

        self.llm = OllamaService()

    def ask(self, question: str):

        #Convert question into embedding
        question_embedding = self.embedder.embed(question)

        # Retrieve relevant chunks
        results = self.vector_store.search(
            question_embedding,
            k=5
        )

        #Extract only chunk text
        chunks = [
            result["chunk"]
            for result in results
        ]

        # Build prompt
        prompt = PromptBuilder.build(
            question,
            chunks
        )

        #Ask LLM
        answer = self.llm.generate(prompt)

        return {
            "question": question,
            "answer": answer,
            "sources": results
        }