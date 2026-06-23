from .base import BaseTranslator


class CohereTranslator(BaseTranslator):

    DEFAULT_MODEL = "command-r-plus"
    MODELS = [
        "command-r-plus",
        "command-r",
        "command",
    ]

    def __init__(self, api_key: str, model: str = None):
        super().__init__(api_key, model or self.DEFAULT_MODEL)

    def _get_client(self):
        if self._client is None:
            import cohere
            self._client = cohere.Client(api_key=self.api_key)
        return self._client

    def translate(self, text: str, system_prompt: str) -> str:
        client = self._get_client()
        response = client.chat(
            model=self.model,
            preamble=system_prompt,
            message=text,
        )
        return response.text

    def test_connection(self) -> bool:
        try:
            result = self.translate("test", "Say OK")
            return bool(result)
        except Exception:
            return False

    @staticmethod
    def get_default_model() -> str:
        return CohereTranslator.DEFAULT_MODEL

    @staticmethod
    def get_available_models() -> list[str]:
        return CohereTranslator.MODELS
