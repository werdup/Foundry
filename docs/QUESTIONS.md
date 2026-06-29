# Architectural Questions

This document captures important architectural questions that remain intentionally unresolved.

These are not implementation tasks.

They are research questions.

A question should only leave this document when there is sufficient evidence to make a permanent architectural decision.

---

# Active Questions

## Q-001

### What transforms one World into another?

Current thinking:

A World represents objective reality.

Observations are derived from a World.

What remains unresolved is how reality itself changes.

Possible directions:

- Decisions
- Processes
- Time
- External inputs
- A combination of the above

Status:

Open.

---

## Q-002

### Should Observer become its own abstraction?

Today:

```python
world.observe(agent)
```

works well.

However, cameras, sensors, referees, and spectators may also observe a World without making decisions.

Question:

Should "Observer" eventually become independent from "Agent"?

Status:

Deferred until multiple concrete use cases exist.

---

## Q-003

### What should Memory preserve?

Possible options:

- Observations
- Derived knowledge
- Events
- Decisions
- A combination

The answer affects replay, learning, and reasoning.

Status:

Open.

---

## Q-004

### Are Processes first-class?

Not every change in a World is caused by a decision.

Examples:

- Gravity
- Weather
- Lottery drawings
- Disease progression

Question:

Should these become first-class architectural concepts?

Status:

Open.

---

## Q-005

### What is the correct simulation loop?

Today we intentionally avoid defining the simulation engine.

Current understanding suggests something similar to:

World

↓

Observation

↓

Decision

↓

World

However, this remains intentionally unimplemented.

Status:

Open.

---

## Q-006

### What is the responsibility of an Episode?

Current thinking:

An Episode represents one bounded execution.

However, it remains unclear whether an Episode should own the history of that execution or merely define its boundaries.

Possible directions:

- Episode owns recorded history.
- Episode provides boundaries while another abstraction (for example, a Recorder) owns history.
- Episode owns only metadata while applications choose how history is preserved.

Question:

What is the minimum responsibility that every Episode must have?

Status:

Open.

Evidence needed:

Build the first evolving world and observe whether Episode naturally accumulates additional responsibilities.

---

# Principles

Questions are valuable.

They prevent premature certainty.

A good architectural decision is based on evidence rather than intuition.

Foundry intentionally preserves important unanswered questions until experience provides enough information to resolve them.