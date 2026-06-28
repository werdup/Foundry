from __future__ import annotations

from .agent import Agent
from .decision import Decision
from .event import Event


class Observer:
    """Read-only simulation observer."""

    def on_event(self, event: Event) -> None:
        pass

    def on_decisions(self, event: Event, decisions: list[Decision]) -> None:
        pass

    def on_finish(self, agents: list[Agent]) -> None:
        pass
