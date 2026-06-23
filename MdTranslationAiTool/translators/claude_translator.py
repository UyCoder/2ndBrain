from .base import BaseTranslator, FatalTranslationError


class ClaudeTranslator(BaseTranslator):

    DEFAULT_MODEL = "claude-sonnet-4-6"
    MODELS = [
        "claude-opus-4-8",
        "claude-sonnet-4-6",
        "claude-haiku-4-5-20251001",
    ]

    def __init__(self, api_key: str, model: str = None):
        super().__init__(api_key, model or self.DEFAULT_MODEL)

    def _get_client(self):
        if self._client is None:
            import anthropic
            self._client = anthropic.Anthropic(api_key=self.api_key)
        return self._client

    def translate(self, text: str, system_prompt: str) -> str:
        client = self._get_client()
        try:
            message = client.messages.create(
                model=self.model,
                max_tokens=8192,
                system=system_prompt,
                messages=[{"role": "user", "content": text}],
            )
            return message.content[0].text
        except Exception as e:
            msg = str(e)
            if "credit balance is too low" in msg or "insufficient_quota" in msg:
                raise FatalTranslationError(
                    "Claude API كرېدىتى يوق — https://console.anthropic.com/billing"
                ) from e
            raise

    def test_connection(self) -> bool:
        try:
            result = self.translate("test", "Say OK")
            return bool(result)
        except FatalTranslationError:
            raise
        except Exception:
            return False

    @staticmethod
    def get_default_model() -> str:
        return ClaudeTranslator.DEFAULT_MODEL

    @staticmethod
    def get_available_models() -> list[str]:
        return ClaudeTranslator.MODELS
