---

# Experiment 001A — CounterWorld

## Goal

Construct the smallest possible world containing objective state.

No agents.

No observations.

No simulation.

No framework.

Only state.

---

## Result

```python
world.counter = 0

world.counter += 1
```

The experiment successfully demonstrated that objective state can exist
independently of the rest of the framework.

---

## Authority Audit

### Objective State

```
counter
```

---

### Authority to Observe

The experiment.

---

### Authority to Modify

The experiment.

---

### Architectural Observations

#### Observation #5

The experiment exists outside the modeled world.

Unlike an Agent, the experiment may inspect objective state directly.

This is acceptable because experiments are external observers rather than
participants in the modeled system.

---

#### Observation #6

Objective state changed because external code exercised authority over it.

No Agent participated.

No Observation was created.

No Decision was made.

This suggests that objective state can change independently of the
decision-making architecture.

---

## Open Questions

- Should a World expose mutable objective state?
- Should objective state ever be directly modified?
- If not, who has authority to modify it?
- Is authority enforced by the framework or expressed by convention?