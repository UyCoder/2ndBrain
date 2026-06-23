import re
import urllib.request
import urllib.parse
import json
from .base import BaseTranslator

API_URL = "https://api.niutrans.com/NiuTransServer/translation"

LANG_MAP = {
    "uyghur":  "uy",
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

    MAX_CHARS = 4500   # NiuTrans ھەقسىز تىزىملىكى 5000 خەرىپ چەكلىمىسى

    def _target_code(self, system_prompt: str) -> str:
        m = re.search(r"Translate the content into (\w+)", system_prompt, re.IGNORECASE)
        if m:
            return LANG_MAP.get(m.group(1).lower(), "en")
        return "en"

    def _source_code(self, text: str) -> str:
        chinese = sum(1 for c in text[:200] if "一" <= c <= "鿿")
        return "zh" if chinese > 10 else "en"

    def _call_api(self, text: str, from_lang: str, to_lang: str) -> str:
        params = urllib.parse.urlencode({
            "from":     from_lang,
            "to":       to_lang,
            "apikey":   self.api_key,
            "src_text": text,
        })
        req = urllib.request.Request(
            f"{API_URL}?{params}", headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
        if "error_code" in data and str(data["error_code"]) != "0":
            raise RuntimeError(f"NiuTrans خاتالىق {data.get('error_code')}: {data.get('error_msg','')}")
        return data.get("tgt_text", "")

    def translate(self, text: str, system_prompt: str) -> str:
        to_lang   = self._target_code(system_prompt)
        from_lang = self._source_code(text)

        # 5000 خەرىپتىن ئوشسا ئىچكىرىدە بۆلۈپ تەرجىمە قىلىمىز
        if len(text) <= self.MAX_CHARS:
            return self._call_api(text, from_lang, to_lang)

        parts = []
        for i in range(0, len(text), self.MAX_CHARS):
            parts.append(self._call_api(text[i:i + self.MAX_CHARS], from_lang, to_lang))
        return "\n\n".join(parts)

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
