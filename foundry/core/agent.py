from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from .decision import Decision
from .event import Event
from .jsonable import to_jsonable
from .memory import Memory


@dataclass
class AgentState:
    values: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return to_jsonable(self.values)


@dataclass
class AgentIdentity:
    id: str
    name: str
    archetype: str | None = None
    description: str | None = None


class Agent(ABC):
    """Base interface for adaptive decision-makers."""

    def __init__(
        self,
        identity: AgentIdentity,
        goals: list[str] | None = None,
        state: AgentState | None = None,
        memories: list[Memory] | None = None,
    ) -> None:
        self.identity = identity
        self.goals = goals or []
        self.state = state or AgentState()
        self.memories = memories or []

    @abstractmethod
    def decide(self, event: Event) -> list[Decision]:
        raise NotImplementedError

    def remember(self, memory: Memory) -> None:
        self.memories.append(memory)

    def to_dict(self) -> dict[str, Any]:
        return {
            "identity": to_jsonable(self.identity),
            "goals": to_jsonable(self.goals),
            "state": self.state.to_dict(),
            "memories": [memory.to_dict() for memory in self.memories],
        }
