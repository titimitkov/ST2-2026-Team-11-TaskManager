import requests

from services.ai_provider import AIProvider


class OllamaProvider(AIProvider):
    """
    Strategy Pattern.

    Конкретна стратегия за комуникация
    с локален Ollama модел.
    """

    def __init__(
        self,
        model="llama3.2:3b",
        base_url="http://localhost:11434"
    ):
        self.model = model
        self.base_url = base_url

    def generate(self, prompt):
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]