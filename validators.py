import re
from typing import Any, Optional

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email))

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    return min_val <= value <= max_val

def validate_not_empty(value: Optional[str]) -> bool:
    return bool(value and value.strip())

def sanitize_input(value: Any) -> str:
    if not isinstance(value, str):
        value = str(value)
    return value.strip()

def validate_length(value: str, min_len: int, max_len: int) -> bool:
    return min_len <= len(value) <= max_len

def validate_alphanumeric(value: str) -> bool:
    return value.isalnum()