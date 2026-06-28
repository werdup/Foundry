from foundry.core import Agent, AgentIdentity, Decision, Environment, Event, Observer, Simulation, SimulationConfig


class CountingEnvironment(Environment):
    def __init__(self, limit: int = 3) -> None:
        self.limit = limit
        self.count = 0

    def reset(self, seed: int | None = None) -> Event:
        self.count = 0
        return Event(type="environment_reset", payload={"count": self.count})

    def step(self) -> Event:
        self.count += 1
        return Event(type="count_changed", payload={"count": self.count})

    def apply(self, decisions: list[Decision]) -> list[Event]:
        return [
            Event(type="decision_applied", payload={"actor_id": decision.actor_id, "action": decision.action})
            for decision in decisions
        ]

    def is_finished(self) -> bool:
        return self.count >= self.limit


class CountingAgent(Agent):
    def decide(self, event: Event) -> list[Decision]:
        if event.type == "count_changed":
            return [
                Decision(
                    actor_id=self.identity.id,
                    action="acknowledge_count",
                    parameters={"count": event.payload["count"]},
                    reason="The agent reacts to count changes.",
                    confidence=1.0,
                )
            ]
        return []


class PrintObserver(Observer):
    def on_event(self, event: Event) -> None:
        print(f"EVENT: {event.type} {event.payload}")

    def on_decisions(self, event: Event, decisions: list[Decision]) -> None:
        for decision in decisions:
            print(f"DECISION: {decision.action} because {decision.reason}")


if __name__ == "__main__":
    env = CountingEnvironment(limit=3)
    agent = CountingAgent(identity=AgentIdentity(id="agent_001", name="Counter"))
    sim = Simulation(
        environment=env,
        agents=[agent],
        config=SimulationConfig(max_steps=10, seed=1),
        observers=[PrintObserver()],
    )
    sim.run()
