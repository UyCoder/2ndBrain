from .base import BaseTranslator

BASE_URL = "https://api.aimlapi.com/v1"


class AimlApiTranslator(BaseTranslator):

    DEFAULT_MODEL = "gpt-4o-mini"
    MODELS = [
        # OpenAI
        "gpt-4o-mini",
        "gpt-4o",
        "gpt-4-turbo",
        "gpt-3.5-turbo",
        # Meta Llama
        "meta-llama/Llama-3.2-3B-Instruct-Turbo",
        "meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
        "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
        # Mistral
        "mistralai/Mistral-7B-Instruct-v0.3",
        "mistralai/Mixtral-8x7B-Instruct-v0.1",
        # Qwen
        "Qwen/Qwen2.5-7B-Instruct",
        "Qwen/Qwen2.5-72B-Instruct",
        # DeepSeek
        "deepseek-ai/DeepSeek-R1",
        "deepseek-ai/DeepSeek-V3",
        # Google
        "google/gemma-2-9b-it",
        "google/gemma-2-27b-it",
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
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": text},
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
        return AimlApiTranslator.DEFAULT_MODEL

    @staticmethod
    def get_available_models() -> list[str]:
        return AimlApiTranslator.MODELS
