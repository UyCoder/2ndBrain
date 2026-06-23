from .base import BaseTranslator

BASE_URL = "https://api.interfaze.ai/v1"


class InterfazeTranslator(BaseTranslator):

    DEFAULT_MODEL = "interfaze-beta"
    MODELS = [
        "interfaze-beta",
    ]

    def __init__(self, api_key: str, model: str = None):
        super().__init__(api_key, model or self.DEFAULT_MODEL)

    def _get_client(self):
        if self._client is None:
            from openai import OpenAI
            self._client = OpenAI(api_key=self.api_key, base_url=BASE_URL)
        return self._client

    def translate(self, text: str, system_prompt: str) -> str:
        client = self._get_client()
        # Interfaze پەقەت user رولىنى قوللايدۇ — system prompt نى user خەۋىرىگە بىرلەشتۈرىمىز
        combined = f"{system_prompt}\n\n---\n\n{text}"
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": combined},
            ],
        )
        return response.choices[0].message.content

    def test_connection(self) -> bool:
        try:
            client = self._get_client()
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "Say OK"}],
            )
            return bool(response.choices[0].message.content)
        except Exception:
            return False

    @staticmethod
    def get_default_model() -> str:
        return InterfazeTranslator.DEFAULT_MODEL

    @staticmethod
    def get_available_models() -> list[str]:
        return InterfazeTranslator.MODELS
