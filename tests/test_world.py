from foundry.core import AgentIdentity
from foundry.core import Observation
from foundry.core import PassiveAgent
from foundry.core import World


class CounterWorld(World):

    def observe(self, observer):

        return Observation(
            attributes={
                "counter": 5,
            }
        )


def test_world_produces_observation():

    world = CounterWorld()

    agent = PassiveAgent(
        AgentIdentity(
            id="agent_001",
            name="Alice",
        )
    )

    observation = world.observe(agent)

    assert observation.attributes["counter"] == 5