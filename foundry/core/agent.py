from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from .decision import Decision
from .event import Event


@dataclass
class AgentIdentity:
    """Stable identity for an agent."""

    id: str
    name: str
    description: str | None = None


@dataclass
class AgentState:
    """Mutable state owned by an agent."""

    values: dict[str, Any] = field(default_factory=dict)


class Agent(ABC):
    """Base class for all Foundry agents."""

    def __init__(
        self,
        identity: AgentIdentity,
        goals: list[str] | None = None,
    ) -> None:
        self.identity = identity
        self.goals = goals or []
        self.memories: list[Any] = []
        self.state = AgentState()

    @abstractmethod
    def decide(self, event: Event) -> list[Decision]:
        """React to an event."""
        raise NotImplementedError


class PassiveAgent(Agent):
    """Agent that never reacts.

    Useful for tests.
    """

    def decide(self, event: Event) -> list[Decision]:
        return []