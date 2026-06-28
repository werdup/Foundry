from __future__ import annotations

from abc import ABC, abstractmethod

from .agent import Agent
from .observation import Observation


class World(ABC):
    """The authoritative representation of objective reality.

    A World never exposes its internal state directly.

    Instead, it derives an Observation for a particular observer.
    """

    @abstractmethod
    def observe(
        self,
        observer: Agent,
    ) -> Observation:
        """Derive an Observation for an observer."""
        raise NotImplementedError