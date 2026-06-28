from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .agent import Agent
from .environment import Environment
from .observer import Observer


@dataclass
class SimulationConfig:
    max_steps: int = 100
    seed: int | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class Simulation:
    """Environment-agnostic simulation loop."""

    def __init__(
        self,
        environment: Environment,
        agents: list[Agent],
        config: SimulationConfig | None = None,
        observers: list[Observer] | None = None,
    ) -> None:
        self.environment = environment
        self.agents = agents
        self.config = config or SimulationConfig()
        self.observers = observers or []
        self.steps_run = 0

    def run(self) -> None:
        event = self.environment.reset(seed=self.config.seed)
        self._notify_event(event)

        while not self.environment.is_finished() and self.steps_run < self.config.max_steps:
            decisions = []
            for agent in self.agents:
                decisions.extend(agent.decide(event))

            self._notify_decisions(event, decisions)

            resulting_events = self.environment.apply(decisions)
            for resulting_event in resulting_events:
                self._notify_event(resulting_event)

            if self.environment.is_finished():
                break

            event = self.environment.step()
            self._notify_event(event)
            self.steps_run += 1

        for observer in self.observers:
            observer.on_finish(self.agents)

    def _notify_event(self, event):
        for observer in self.observers:
            observer.on_event(event)

    def _notify_decisions(self, event, decisions):
        for observer in self.observers:
            observer.on_decisions(event, decisions)
