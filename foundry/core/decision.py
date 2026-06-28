from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import UUID, uuid4

from .jsonable import to_jsonable


@dataclass(frozen=True)
class Decision:
    """A decision made by an agent."""

    actor_id: str
    action: str
    parameters: dict[str, Any] = field(default_factory=dict)
    reason: str = ""
    confidence: float = 1.0
    id: UUID = field(default_factory=uuid4)

    def to_dict(self) -> dict[str, Any]:
        return to_jsonable(self)
