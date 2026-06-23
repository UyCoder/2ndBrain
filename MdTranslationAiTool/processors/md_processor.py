"""
Markdown ھۆججىتىنى سېكشىن بويىچە بۆلەكلەيدۇ.
رېفرېنس / بىبلىئوگرافىيە سېكشىنى تەرجىمە قىلىنمايدۇ.
"""
import re
from typing import Generator


REFERENCE_HEADERS = {
    "references", "bibliography", "works cited", "sources",
    "footnotes", "notes", "مەنبەلەر", "ئەسكەرتىش",
}

MAX_CHUNK_CHARS = 3000


class Chunk:
    def __init__(self, text: str, is_reference: bool = False):
        self.text = text
        self.is_reference = is_reference


class MarkdownProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> str:
        import chardet
        with open(self.file_path, "rb") as f:
            raw = f.read()
        enc = chardet.detect(raw)["encoding"] or "utf-8"
        return raw.decode(enc, errors="replace")

    def split_chunks(self, max_chars: int = MAX_CHUNK_CHARS) -> list[Chunk]:
        content = self.read()
        sections = self._split_by_headings(content)
        chunks: list[Chunk] = []
        for header, body, is_ref in sections:
            full = (header + "\n" + body).strip()
            if not full:
                continue
            if is_ref:
                chunks.append(Chunk(full, is_reference=True))
                continue
            if len(full) <= max_chars:
                chunks.append(Chunk(full))
            else:
                for sub in self._split_large_section(header, body, max_chars):
                    chunks.append(Chunk(sub))
        return chunks

    # ------------------------------------------------------------------ #

    def _split_by_headings(self, content: str):
        pattern = re.compile(r"^(#{1,6}\s+.+)$", re.MULTILINE)
        matches = list(pattern.finditer(content))

        if not matches:
            yield ("", content, False)
            return

        if matches[0].start() > 0:
            preamble = content[: matches[0].start()].strip()
            if preamble:
                yield ("", preamble, False)

        for i, m in enumerate(matches):
            header = m.group(1)
            start = m.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            body = content[start:end].strip()
            is_ref = self._is_reference_section(header)
            yield (header, body, is_ref)

    @staticmethod
    def _is_reference_section(header: str) -> bool:
        text = re.sub(r"^#+\s*", "", header).strip().lower()
        return text in REFERENCE_HEADERS

    @staticmethod
    def _split_large_section(header: str, body: str, max_chars: int) -> Generator[str, None, None]:
        paragraphs = re.split(r"\n{2,}", body)
        current = header
        for para in paragraphs:
            if len(current) + len(para) + 2 > max_chars and current.strip():
                yield current.strip()
                current = para
            else:
                current = current + "\n\n" + para if current else para
        if current.strip():
            yield current.strip()
