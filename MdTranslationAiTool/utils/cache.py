"""
تەرجىمە كەشى — ئوخشاش مەزمۇننى قايتا API غا يوللاشتىن ساقلاندۇرىدۇ.
JSON فايل ئارقىلىق ساقلىنىدۇ.
"""
import json
import hashlib
import os
from pathlib import Path

CACHE_FILE = Path(__file__).parent.parent / ".translation_cache.json"


class TranslationCache:
    def __init__(self):
        self._data: dict[str, str] = {}
        self._load()

    def _load(self):
        if CACHE_FILE.exists():
            try:
                with open(CACHE_FILE, encoding="utf-8") as f:
                    self._data = json.load(f)
            except Exception:
                self._data = {}

    def _save(self):
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def _key(provider: str, model: str, text: str) -> str:
        raw = f"{provider}|{model}|{text}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def get(self, provider: str, model: str, text: str) -> str | None:
        return self._data.get(self._key(provider, model, text))

    def set(self, provider: str, model: str, text: str, translation: str):
        self._data[self._key(provider, model, text)] = translation
        self._save()

    def clear(self):
        self._data = {}
        if CACHE_FILE.exists():
            CACHE_FILE.unlink()

    def size(self) -> int:
        return len(self._data)
