from foundry.core.agent import (
    AgentIdentity,
    PassiveAgent,
)
from foundry.core.event import Event


def test_agent_identity():
    agent = PassiveAgent(
        AgentIdentity(
            id="agent_001",
            name="Alice",
        )
    )

    assert agent.identity.name == "Alice"


def test_passive_agent_returns_no_decisions():
    agent = PassiveAgent(
        AgentIdentity(
            id="agent_001",
            name="Alice",
        )
    )

    decisions = agent.decide(Event(type="tick"))

    assert decisions == []


def test_agent_starts_with_empty_goals():
    agent = PassiveAgent(
        AgentIdentity(
            id="agent_001",
            name="Alice",
        )
    )

    assert agent.goals == []


def test_agent_starts_with_empty_memories():
    agent = PassiveAgent(
        AgentIdentity(
            id="agent_001",
            name="Alice",
        )
    )

    assert agent.memories == []