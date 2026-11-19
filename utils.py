import logging
import os
from typing import Any, Optional

logger = logging.getLogger(__name__)

def safe_read_file(path: str) -> Optional[str]:
    if not path or not isinstance(path, str):
        return None

    try:
        if not os.path.exists(path):
            return None
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except (PermissionError, IOError) as e:
        logger.error(f"file access error for {path}: {e}")
        return None

def cast_to_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def retry_operation(func, retries: int = 3, *args, **kwargs):
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt == retries - 1:
                logger.critical(f"final attempt failed for {func.__name__}: {e}")
                raise
            logger.warning(f"retry {attempt + 1} for {func.__name__}")