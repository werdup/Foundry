from __future__ import annotations

from abc import ABC, abstractmethod

from .decision import Decision
from .event import Event


class Environment(ABC):
    """Base interface for a world agents operate in."""

    @abstractmethod
    def reset(self, seed: int | None = None) -> Event:
        raise NotImplementedError

    @abstractmethod
    def step(self) -> Event:
        raise NotImplementedError

    @abstractmethod
    def apply(self, decisions: list[Decision]) -> list[Event]:
        raise NotImplementedError

    @abstractmethod
    def is_finished(self) -> bool:
        raise NotImplementedError
