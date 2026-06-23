from .md_processor import MarkdownProcessor
from .txt_processor import TxtProcessor
from .html_processor import HtmlProcessor
from .pdf_processor import PdfProcessor

PROCESSORS = {
    ".md": MarkdownProcessor,
    ".txt": TxtProcessor,
    ".html": HtmlProcessor,
    ".htm": HtmlProcessor,
    ".pdf": PdfProcessor,
}


def get_processor(file_path: str):
    import os
    ext = os.path.splitext(file_path)[1].lower()
    cls = PROCESSORS.get(ext)
    if cls is None:
        raise ValueError(f"قوللىمايدىغان ھۆججەت تىپى: {ext}")
    return cls(file_path)
