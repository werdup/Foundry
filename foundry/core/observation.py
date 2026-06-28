from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class Observation:
    """An immutable representation of what an observer is
    permitted to perceive at one moment in time.

    An Observation intentionally contains no knowledge of:

    - the World
    - the Agent
    - Memory
    - Decisions

    It is simply a representation of perceived information.
    """

    attributes: Mapping[str, Any]

    metadata: Mapping[str, Any] = field(default_factory=dict)