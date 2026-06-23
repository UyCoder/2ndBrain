from .base import BaseTranslator


class MistralTranslator(BaseTranslator):

    DEFAULT_MODEL = "mistral-large-latest"
    MODELS = [
        "mistral-large-latest",
        "mistral-medium-latest",
        "mistral-small-latest",
        "open-mixtral-8x22b",
    ]

    def __init__(self, api_key: str, model: str = None):
        super().__init__(api_key, model or self.DEFAULT_MODEL)

    def _get_client(self):
        if self._client is None:
            from mistralai import Mistral
            self._client = Mistral(api_key=self.api_key)
        return self._client

    def translate(self, text: str, system_prompt: str) -> str:
        client = self._get_client()
        response = client.chat.complete(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
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
        return MistralTranslator.DEFAULT_MODEL

    @staticmethod
    def get_available_models() -> list[str]:
        return MistralTranslator.MODELS
