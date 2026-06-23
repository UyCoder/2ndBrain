import re
import urllib.request
import urllib.parse
import json
from .base import BaseTranslator

API_URL = "https://api.niutrans.com/NiuTransServer/translation"

LANG_MAP = {
    "uyghur":  "ug",
    "turkish": "tr",
    "kazakh":  "kk",
    "uzbek":   "uz",
    "arabic":  "ar",
    "persian": "fa",
    "russian": "ru",
    "english": "en",
    "chinese": "zh",
}


class NiuTransTranslator(BaseTranslator):

    DEFAULT_MODEL = "auto"
    MODELS = ["auto"]

    def __init__(self, api_key: str, model: str = None):
        super().__init__(api_key, model or self.DEFAULT_MODEL)

    def _get_client(self):
        return None   # HTTP ئارقىلىق ئىشلەيدۇ، client كېرەكمەس

    def _target_code(self, system_prompt: str) -> str:
        m = re.search(r"Translate the content into (\w+)", system_prompt, re.IGNORECASE)
        if m:
            return LANG_MAP.get(m.group(1).lower(), "en")
        return "en"

    def translate(self, text: str, system_prompt: str) -> str:
        to_lang = self._target_code(system_prompt)
        params = urllib.parse.urlencode({
            "from":    "auto",
            "to":      to_lang,
            "apikey":  self.api_key,
            "src_text": text,
        })
        url = f"{API_URL}?{params}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
        if "error_code" in data and data["error_code"] != "0":
            raise RuntimeError(f"NiuTrans خاتالىق {data.get('error_code')}: {data.get('error_msg','')}")
        return data.get("tgt_text", "")

    def test_connection(self) -> bool:
        try:
            result = self.translate("Hello", "Translate the content into English")
            return bool(result)
        except Exception:
            return False

    @staticmethod
    def get_default_model() -> str:
        return NiuTransTranslator.DEFAULT_MODEL

    @staticmethod
    def get_available_models() -> list[str]:
        return NiuTransTranslator.MODELS
