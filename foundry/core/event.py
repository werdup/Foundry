from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from .jsonable import to_jsonable


@dataclass(frozen=True)
class Event:
    """Something that happened inside an environment."""

    type: str
    payload: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    id: UUID = field(default_factory=uuid4)
    source: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return to_jsonable(self)
