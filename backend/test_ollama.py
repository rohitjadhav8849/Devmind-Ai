from app.llm.ollama_service import OllamaService

llm = OllamaService()

response = llm.generate(
    "Explain JWT authentication in two sentences."
)

print(response)