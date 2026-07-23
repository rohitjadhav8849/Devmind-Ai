from app.embeddings.embedding_service import EmbeddingService
from app.vectorStore.qdrant_store import QdrantVectorStore
from app.prompt.prompt_builder import PromptBuilder
from app.llm.ollama_service import OllamaService

embedder = EmbeddingService()
store = QdrantVectorStore(embedder.dimension)
llm = OllamaService()

question = "How is login authentication implemented?"

question_embedding = embedder.embed(question)

results = store.search(question_embedding, k=3)

chunks = [result["chunk"] for result in results]

prompt = PromptBuilder.build(
    question=question,
    chunks=chunks
)

answer = llm.generate(prompt)

print("\nQuestion:\n")
print(question)

print("\nAnswer:\n")
print(answer)