"""
ئاتالغۇ خەزىنىسى — تېخنىكىلىق ئاتالغۇلارنى ئالدىن تەرجىمە قىلىپ ساقلاش.
ئۇلار System Prompt قا قوشۇلۇپ AI غا يوللىنىدۇ.
"""
import json
from pathlib import Path

GLOSSARY_FILE = Path(__file__).parent.parent / "glossary.json"


class Glossary:
    def __init__(self):
        self._terms: dict[str, str] = {}
        self._load()

    def _load(self):
        if GLOSSARY_FILE.exists():
            try:
                with open(GLOSSARY_FILE, encoding="utf-8") as f:
                    self._terms = json.load(f)
            except Exception:
                self._terms = {}

    def _save(self):
        with open(GLOSSARY_FILE, "w", encoding="utf-8") as f:
            json.dump(self._terms, f, ensure_ascii=False, indent=2)

    def add(self, source: str, target: str):
        self._terms[source.strip()] = target.strip()
        self._save()

    def remove(self, source: str):
        self._terms.pop(source.strip(), None)
        self._save()

    def all(self) -> dict[str, str]:
        return dict(self._terms)

    def to_prompt_block(self) -> str:
        if not self._terms:
            return ""
        lines = ["تۆۋەندىكى ئاتالغۇلارنى چوقۇم كۆرسىتىلگەن شەكىلدە تەرجىمە قىلىڭ:"]
        for src, tgt in self._terms.items():
            lines.append(f"  {src} → {tgt}")
        return "\n".join(lines)

    def clear(self):
        self._terms = {}
        self._save()
