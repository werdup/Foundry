# Architecture

This document describes the current conceptual architecture of Foundry.

It intentionally focuses on relationships rather than implementation.

---

# Core Loop

```text
            World
               │
      observe(observer)
               │
               ▼
         Observation
               │
               ▼
            Agent
               │
         decide(...)
               │
               ▼
           Decision
```

The World owns objective reality.

An Observation represents the information available to one observer.

An Agent transforms an Observation into one or more Decisions.

---

# Responsibilities

## World

Owns objective reality.

Provides observations.

Never exposes reality directly.

---

## Observation

Represents permitted perception.

Immutable.

Independent of World, Agent, and Memory.

---

## Agent

Consumes Observations.

Produces Decisions.

Maintains its own internal state.

---

## Decision

Represents an intended action.

Does not modify the World directly.

---

## Episode

Represents one bounded execution.

Episodes organize histories.

They do not define reality.

---

# Ownership

```text
Application
──────────────────────────

PowerballWorld
PokerWorld
RobotWorld

──────────────────────────

Foundry

World
Observation
Agent
Decision
Episode
```

Applications define reality.

Foundry defines contracts.

---

# Current Scope

Implemented:

- World
- Observation
- Agent
- Decision
- Episode

Intentionally Deferred:

- Simulation
- Memory
- Processes
- Replay
- Experiment
- Runner

These concepts remain deferred until their responsibilities become clear.

---

# Design Rule

Every abstraction should answer three questions.

1. What is it?
2. What is it not?
3. Who owns it?

If those questions cannot be answered clearly, the abstraction is probably premature.


---

# Future Architecture

This document intentionally reflects only the current architecture.

Future concepts should be added only after they have been validated through implementation and documented through an ADR.