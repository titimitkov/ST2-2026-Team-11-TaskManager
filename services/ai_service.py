from services.ai_provider import AIProvider


class AIService:
    """
    Service Layer за работа с AI.

    AIService не знае дали използваме Ollama,
    друг локален модел или друг AI доставчик.

    Той работи с AIProvider интерфейса.
    """

    def __init__(self, provider: AIProvider):
        self.provider = provider

    def ask(self, prompt):
        return self.provider.generate(prompt)