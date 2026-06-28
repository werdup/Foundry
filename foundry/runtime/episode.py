from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum
from typing import Any
from uuid import UUID, uuid4

from foundry.core.decision import Decision
from foundry.core.event import Event
from foundry.core.jsonable import to_jsonable


class EpisodeState(StrEnum):
    CREATED = "created"
    STARTED = "started"
    FINISHED = "finished"


@dataclass
class Episode:
    """A permanent record of one simulation run.

    Episodes collect the factual history of a run: events, decisions,
    seed, environment name, timing, and metadata. They do not know how
    the simulation works, and they do not compute domain-specific meaning.
    """

    environment_name: str
    seed: int | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    id: UUID = field(default_factory=uuid4)
    state: EpisodeState = EpisodeState.CREATED
    started_at: datetime | None = None
    finished_at: datetime | None = None
    events: list[Event] = field(default_factory=list)
    decisions: list[Decision] = field(default_factory=list)

    def start(self) -> None:
        """Mark the episode as started."""
        if self.state == EpisodeState.FINISHED:
            raise RuntimeError("Cannot restart a finished episode.")

        if self.started_at is None:
            self.started_at = datetime.now(timezone.utc)

        self.state = EpisodeState.STARTED

    def record_event(self, event: Event) -> None:
        """Record an event in the episode history."""
        self._ensure_recording_allowed()
        self.events.append(event)

    def record_decision(self, decision: Decision) -> None:
        """Record a decision in the episode history."""
        self._ensure_recording_allowed()
        self.decisions.append(decision)

    def finish(self) -> None:
        """Seal the episode.

        Once finished, the episode should be treated as permanent history.
        Additional events or decisions cannot be recorded.
        """
        if self.state == EpisodeState.CREATED:
            self.start()

        if self.finished_at is None:
            self.finished_at = datetime.now(timezone.utc)

        self.state = EpisodeState.FINISHED

    @property
    def is_finished(self) -> bool:
        return self.state == EpisodeState.FINISHED

    def summary(self) -> dict[str, Any]:
        """Return a small derived summary of the episode."""
        return {
            "id": str(self.id),
            "environment_name": self.environment_name,
            "seed": self.seed,
            "state": self.state.value,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "finished_at": self.finished_at.isoformat() if self.finished_at else None,
            "event_count": len(self.events),
            "decision_count": len(self.decisions),
            "metadata": to_jsonable(self.metadata),
        }

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the episode."""
        return {
            **self.summary(),
            "events": [event.to_dict() for event in self.events],
            "decisions": [decision.to_dict() for decision in self.decisions],
        }

    def _ensure_recording_allowed(self) -> None:
        if self.state == EpisodeState.FINISHED:
            raise RuntimeError("Cannot record to a finished episode.")

        if self.state == EpisodeState.CREATED:
            self.start()
