from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import UUID, uuid4

from .jsonable import to_jsonable


@dataclass
class Memory:
    """A meaningful remembered experience."""

    agent_id: str
    event_type: str
    summary: str
    importance: float = 0.5
    emotion: str | None = None
    tags: list[str] = field(default_factory=list)
    payload: dict[str, Any] = field(default_factory=dict)
    event_id: UUID | None = None
    id: UUID = field(default_factory=uuid4)

    def to_dict(self) -> dict[str, Any]:
        return to_jsonable(self)
