from typing import Any, Dict, List, Optional

def validate_schema(data: Any, schema: Dict[str, type]) -> bool:
    if not isinstance(data, dict):
        return False
    return all(isinstance(data.get(k), v) for k, v in schema.items())

def sanitize_input(data: str, strip_chars: str = "\n\t\r") -> str:
    return data.strip(strip_chars)

def ensure_list(data: Any) -> List[Any]:
    if isinstance(data, list):
        return data
    return [data] if data is not None else []

def validate_range(value: float, min_val: float, max_val: float) -> bool:
    return min_val <= value <= max_val

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)