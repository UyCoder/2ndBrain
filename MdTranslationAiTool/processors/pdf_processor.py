from .md_processor import Chunk

MAX_CHUNK_CHARS = 3000


class PdfProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> str:
        import fitz  # PyMuPDF
        doc = fitz.open(self.file_path)
        pages = []
        for page in doc:
            pages.append(page.get_text())
        doc.close()
        return "\n\n".join(pages)

    def split_chunks(self, max_chars: int = MAX_CHUNK_CHARS) -> list[Chunk]:
        import fitz
        import re
        doc = fitz.open(self.file_path)
        chunks: list[Chunk] = []
        current = ""
        for page in doc:
            text = page.get_text().strip()
            if not text:
                continue
            paragraphs = re.split(r"\n{2,}", text)
            for para in paragraphs:
                para = para.strip()
                if not para:
                    continue
                if len(current) + len(para) + 2 > max_chars and current:
                    chunks.append(Chunk(current.strip()))
                    current = para
                else:
                    current = (current + "\n\n" + para).strip()
        doc.close()
        if current:
            chunks.append(Chunk(current))
        return chunks
