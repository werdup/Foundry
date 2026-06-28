from foundry.core import Agent, AgentIdentity, Decision, Environment, Event, Simulation, SimulationConfig


class TinyEnvironment(Environment):
    def __init__(self):
        self.count = 0

    def reset(self, seed=None):
        self.count = 0
        return Event(type="reset")

    def step(self):
        self.count += 1
        return Event(type="tick", payload={"count": self.count})

    def apply(self, decisions):
        return [Event(type="applied", payload={"count": len(decisions)})]

    def is_finished(self):
        return self.count >= 2


class TinyAgent(Agent):
    def decide(self, event):
        if event.type == "tick":
            return [Decision(actor_id=self.identity.id, action="respond", reason="Testing.")]
        return []


def test_event_is_json_serializable():
    event = Event(type="test", payload={"value": 1})
    data = event.to_dict()
    assert data["type"] == "test"
    assert data["payload"]["value"] == 1
    assert isinstance(data["id"], str)


def test_decision_has_reason():
    decision = Decision(actor_id="a1", action="act", reason="Because this is a test.")
    assert decision.reason


def test_simulation_runs():
    env = TinyEnvironment()
    agent = TinyAgent(identity=AgentIdentity(id="a1", name="Tiny"))
    sim = Simulation(environment=env, agents=[agent], config=SimulationConfig(max_steps=5, seed=123))
    sim.run()
    assert sim.steps_run == 2
    assert agent.identity.name == "Tiny"
