import requests
from app.core.config import OLLAMA_MODEL, OLLAMA_URL


class OllamaService:

    def __init__(self):
        self.url = OLLAMA_URL 
        self.model = OLLAMA_MODEL

    def generate(self, prompt: str) -> str:

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]