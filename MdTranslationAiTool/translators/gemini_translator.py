from .base import BaseTranslator, FatalTranslationError


class GeminiTranslator(BaseTranslator):

    DEFAULT_MODEL = "gemini-2.5-flash"
    MODELS = [
        "gemini-3.5-flash",
        "gemini-2.5-flash",
        "gemini-2.5-pro",
        "gemini-2.0-flash",
        "gemini-2.0-flash-lite",
        "gemini-1.5-pro",
        "gemini-1.5-flash",
    ]

    def __init__(self, api_key: str, model: str = None):
        super().__init__(api_key, model or self.DEFAULT_MODEL)

    def _get_client(self):
        if self._client is None:
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            self._client = genai
        return self._client

    def translate(self, text: str, system_prompt: str) -> str:
        import google.generativeai as genai
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(
            model_name=self.model,
            system_instruction=system_prompt,
        )
        try:
            response = model.generate_content(text)
            return response.text
        except Exception as e:
            msg = str(e)
            if "limit: 0" in msg or "PerDay" in msg and "429" in msg:
                raise FatalTranslationError(
                    "Gemini API كۈنلۈك ھەقسىز چېگرا تولدى — ئەتە قايتا سىناڭ ياكى تۆلەملىك پىلانغا ئۆتۈڭ"
                ) from e
            raise

    def test_connection(self) -> bool:
        try:
            result = self.translate("test", "Say OK")
            return bool(result)
        except Exception:
            return False

    @staticmethod
    def get_default_model() -> str:
        return GeminiTranslator.DEFAULT_MODEL

    @staticmethod
    def get_available_models() -> list[str]:
        return GeminiTranslator.MODELS
