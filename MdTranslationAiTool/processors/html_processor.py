import re
import chardet
from .md_processor import Chunk

MAX_CHUNK_CHARS = 3000


class HtmlProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> str:
        with open(self.file_path, "rb") as f:
            raw = f.read()
        enc = chardet.detect(raw)["encoding"] or "utf-8"
        return raw.decode(enc, errors="replace")

    def split_chunks(self, max_chars: int = MAX_CHUNK_CHARS) -> list[Chunk]:
        from bs4 import BeautifulSoup
        html = self.read()
        soup = BeautifulSoup(html, "lxml")

        # script/style نى چىقىرىۋىتىش
        for tag in soup(["script", "style", "head"]):
            tag.decompose()

        # ھەر بىر ئاساسىي بۆلەكنى (section, article, p, h1-h6) بۆلەكلەش
        blocks = soup.find_all(
            ["h1", "h2", "h3", "h4", "h5", "h6",
             "p", "li", "blockquote", "section", "article"]
        )

        chunks: list[Chunk] = []
        current = ""
        for block in blocks:
            text = block.get_text(separator=" ", strip=True)
            if not text:
                continue
            if len(current) + len(text) + 2 > max_chars and current:
                chunks.append(Chunk(current.strip()))
                current = text
            else:
                current = (current + "\n\n" + text).strip()

        if current:
            chunks.append(Chunk(current))

        if not chunks:
            text = soup.get_text(separator="\n", strip=True)
            for i in range(0, len(text), max_chars):
                chunks.append(Chunk(text[i: i + max_chars]))

        return chunks
