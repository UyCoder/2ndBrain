import re
import chardet
from .md_processor import Chunk

MAX_CHUNK_CHARS = 3000


class TxtProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> str:
        with open(self.file_path, "rb") as f:
            raw = f.read()
        enc = chardet.detect(raw)["encoding"] or "utf-8"
        return raw.decode(enc, errors="replace")

    def split_chunks(self, max_chars: int = MAX_CHUNK_CHARS) -> list[Chunk]:
        content = self.read()
        paragraphs = re.split(r"\n{2,}", content)
        chunks: list[Chunk] = []
        current = ""
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            if len(current) + len(para) + 2 > max_chars and current:
                chunks.append(Chunk(current.strip()))
                current = para
            else:
                current = (current + "\n\n" + para).strip()
        if current:
            chunks.append(Chunk(current))
        return chunks
