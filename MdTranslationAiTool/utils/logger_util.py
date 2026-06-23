"""
تەرجىمە جەريانى ۋە خاتالىقلارنى خاتىرىلەش.
"""
import logging
import os
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "logs"


def get_logger(session_name: str = None) -> logging.Logger:
    LOG_DIR.mkdir(exist_ok=True)
    name = session_name or datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = LOG_DIR / f"{name}.log"

    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger
