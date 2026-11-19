from typing import Final, Dict, List

TIMEOUT_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 5
API_BASE_URL: Final[str] = "https://api.automation-tool-71.com/v1"
SUPPORTED_OPERATIONS: Final[List[str]] = ["fetch", "process", "store"]
DEFAULT_HEADERS: Final[Dict[str, str]] = {
    "Content-Type": "application/json",
    "User-Agent": "automation-tool-71/1.0.0"
}

def get_timeout_buffer() -> float:
    """Calculate system timeout buffer with multiplier."""
    return float(TIMEOUT_SECONDS * 1.2)

def get_retry_policy() -> Dict[str, int]:
    """Return standardized retry configuration dictionary."""
    return {"max": MAX_RETRIES, "backoff": 2}