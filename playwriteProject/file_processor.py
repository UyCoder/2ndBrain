import os
from pathlib import Path

SUPPORTED = {".md", ".txt", ".pdf"}
CHUNK_SIZE = 3000


def collect_files(folder: str) -> list:
    files = []
    for root, _, fnames in os.walk(folder):
        for fname in sorted(fnames):
            p = Path(root) / fname
            if p.suffix.lower() in SUPPORTED:
                files.append(p)
    return files


def read_file(fpath: Path) -> str:
    ext = fpath.suffix.lower()
    try:
        if ext in (".md", ".txt"):
            import chardet
            raw = fpath.read_bytes()
            enc = chardet.detect(raw).get("encoding") or "utf-8"
            return raw.decode(enc, errors="replace")
        elif ext == ".pdf":
            import fitz
            doc = fitz.open(str(fpath))
            pages = [page.get_text() for page in doc]
            doc.close()
            return "\n\n".join(pages)
    except Exception as e:
        print(f"  [WARN] {fpath.name} ئوقۇلمىدى: {e}")
    return ""


def split_chunks(text: str, chunk_size: int = CHUNK_SIZE) -> list:
    if not text.strip():
        return []
    paragraphs = text.split("\n\n")
    chunks = []
    current = ""
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if len(current) + len(para) + 2 <= chunk_size:
            current = (current + "\n\n" + para).strip()
        else:
            if current:
                chunks.append(current)
            if len(para) > chunk_size:
                for i in range(0, len(para), chunk_size):
                    chunks.append(para[i:i + chunk_size])
                current = ""
            else:
                current = para
    if current:
        chunks.append(current)
    return chunks
