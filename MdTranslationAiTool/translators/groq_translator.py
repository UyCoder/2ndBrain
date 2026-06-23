from .base import BaseTranslator


class GroqTranslator(BaseTranslator):

    DEFAULT_MODEL = "llama-3.3-70b-versatile"
    MODELS = [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "mixtral-8x7b-32768",
        "gemma2-9b-it",
    ]

    def __init__(self, api_key: str, model: str = None):
        super().__init__(api_key, model or self.DEFAULT_MODEL)

    def _get_client(self):
        if self._client is None:
            from groq import Groq
            self._client = Groq(api_key=self.api_key)
        return self._client

    def translate(self, text: str, system_prompt: str) -> str:
        client = self._get_client()
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
            max_tokens=8192,
        )
        return response.choices[0].message.content

    def test_connection(self) -> bool:
        try:
            result = self.translate("test", "Say OK")
            return bool(result)
        except Exception:
            return False

    @staticmethod
    def get_default_model() -> str:
        return GroqTranslator.DEFAULT_MODEL

    @staticmethod
    def get_available_models() -> list[str]:
        return GroqTranslator.MODELS
