from __future__ import annotations

from dataclasses import asdict, is_dataclass
from datetime import datetime
from enum import Enum
from typing import Any
from uuid import UUID


def to_jsonable(value: Any) -> Any:
    """Convert common Foundry objects into JSON-serializable values."""
    if is_dataclass(value):
        return {key: to_jsonable(val) for key, val in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): to_jsonable(val) for key, val in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [to_jsonable(item) for item in value]
    if isinstance(value, (datetime, UUID)):
        return str(value)
    if isinstance(value, Enum):
        return value.value
    return value
