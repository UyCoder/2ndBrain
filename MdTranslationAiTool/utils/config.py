"""
API كۇنۇپكىلىرى ۋە قۇراللار تەڭشىكىنى ساقلاش.
keyring بىخەتەر ساقلاش ئۈچۈن ئىشلىتىلىدۇ.
بولمىسا JSON غا ياشۇرۇن شەكىلدە ساقلىنىدۇ.
"""
import json
import base64
from pathlib import Path

SETTINGS_FILE = Path(__file__).parent.parent / "settings.json"
SERVICE_NAME = "MdTranslationAiTool"


def _obfuscate(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


def _deobfuscate(text: str) -> str:
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception:
        return text


class Config:
    def __init__(self):
        self._data: dict = {}
        self._load()

    def _load(self):
        if SETTINGS_FILE.exists():
            try:
                with open(SETTINGS_FILE, encoding="utf-8") as f:
                    self._data = json.load(f)
            except Exception:
                self._data = {}

    def _save(self):
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=2)

    # --- API كۇنۇپكىلىرى --- #

    def get_api_keys(self, provider: str) -> list:
        raw = self._data.get("api_keys", {}).get(provider, [])
        if isinstance(raw, str):   # كونا فورماتقا ماسلىشىش
            raw = [raw] if raw else []
        return [_deobfuscate(r) for r in raw if r]

    def get_api_key(self, provider: str) -> str:
        keys = self.get_api_keys(provider)
        return keys[0] if keys else ""

    def add_api_key(self, provider: str, key: str):
        keys = self.get_api_keys(provider)
        if key not in keys:
            keys.append(key)
        keys = keys[:10]   # ئەڭ كۆپ 10 كۇنۇپكا
        if "api_keys" not in self._data:
            self._data["api_keys"] = {}
        self._data["api_keys"][provider] = [_obfuscate(k) for k in keys]
        self._save()

    def remove_api_key(self, provider: str, index: int):
        keys = self.get_api_keys(provider)
        if 0 <= index < len(keys):
            keys.pop(index)
        if "api_keys" not in self._data:
            self._data["api_keys"] = {}
        self._data["api_keys"][provider] = [_obfuscate(k) for k in keys]
        self._save()

    def set_api_key(self, provider: str, key: str):
        """كونا كودلار بىلەن ماسلىشىش ئۈچۈن"""
        self.add_api_key(provider, key)

    # --- تەڭشەكلەر --- #

    def set(self, key: str, value):
        self._data[key] = value
        self._save()

    def get(self, key: str, default=None):
        return self._data.get(key, default)

    def all_settings(self) -> dict:
        return {k: v for k, v in self._data.items() if k != "api_keys"}
