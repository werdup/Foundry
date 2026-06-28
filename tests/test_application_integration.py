from foundry.core import (
    AgentIdentity,
    Observation,
    PassiveAgent,
    World,
)


class CounterWorld(World):
    """A minimal application-defined World.

    This class intentionally lives outside of Foundry's production code
    to demonstrate that applications own reality.
    """

    def observe(self, observer: PassiveAgent) -> Observation:
        return Observation(
            attributes={
                "counter": 5,
            }
        )


def test_application_world_integrates_with_foundry():

    world = CounterWorld()

    agent = PassiveAgent(
        AgentIdentity(
            id="agent_001",
            name="Alice",
        )
    )

    observation = world.observe(agent)

    decisions = agent.decide(observation)

    assert observation.attributes["counter"] == 5

    assert decisions == []