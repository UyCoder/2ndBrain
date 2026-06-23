from .base import BaseTranslator


class LMStudioTranslator(BaseTranslator):
    """LM Studio ئارقىلىق لوكال مودېل ئىشلىتىش — http://localhost:1234"""

    DEFAULT_MODEL = "local-model"
    MODELS = [
        "local-model",
        "llama-3.2-3b-instruct",
        "llama-3.1-8b-instruct",
        "mistral-7b-instruct",
        "qwen2.5-7b-instruct",
        "qwen2.5-14b-instruct",
        "gemma-3-4b-it",
        "phi-4-mini-instruct",
        "deepseek-r1-distill-llama-8b",
    ]

    def __init__(self, api_key: str = "lmstudio", model: str = None):
        base_url = api_key.strip() if api_key and api_key.startswith("http") else "http://localhost:1234"
        self._base_url = base_url
        super().__init__(api_key or "lmstudio", model or self.DEFAULT_MODEL)

    def _get_client(self):
        if self._client is None:
            from openai import OpenAI
            self._client = OpenAI(
                base_url=f"{self._base_url}/v1",
                api_key="lmstudio",
            )
        return self._client

    def translate(self, text: str, system_prompt: str) -> str:
        client = self._get_client()
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
        )
        return response.choices[0].message.content

    def test_connection(self) -> bool:
        try:
            import urllib.request
            urllib.request.urlopen(f"{self._base_url}/v1/models", timeout=3)
            return True
        except Exception:
            return False

    @staticmethod
    def get_default_model() -> str:
        return LMStudioTranslator.DEFAULT_MODEL

    @staticmethod
    def get_available_models() -> list[str]:
        return LMStudioTranslator.MODELS
