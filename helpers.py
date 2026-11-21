import os
import shutil
from pathlib import Path
from typing import Union


def clean_directory(path: Union[str, Path], extension: str = None) -> int:
    target = Path(path)
    count = 0
    if not target.exists():
        return count
    for item in target.iterdir():
        if item.is_file():
            if extension and not item.name.endswith(extension):
                continue
            item.unlink()
            count += 1
        elif item.is_dir():
            shutil.rmtree(item)
            count += 1
    return count


def ensure_dir(path: Union[str, Path]) -> Path:
    target = Path(path)
    target.mkdir(parents=True, exist_ok=True)
    return target


def get_file_size(path: Union[str, Path]) -> int:
    return Path(path).stat().st_size if Path(path).exists() else 0


def sanitize_filename(filename: str) -> str:
    return "".join(c for c in filename if c.isalnum() or c in ('.', '_', '-')).strip()
