# Foundry

> This document defines the principles that guide Foundry's design.
>
> Architectural decisions should be evaluated against these principles before implementation details.

---

# Purpose

Foundry is a framework for modeling how decisions emerge from information.

It is intentionally domain-agnostic.

Foundry does not model lotteries, poker games, robots, markets, or hospitals.

Instead, it provides the abstractions needed to model any system where observers make decisions based on incomplete knowledge of an evolving world.

Applications own reality.

Foundry owns the language used to describe it.

---

# First Principles

## Reality is objective.

Every world has an objective state.

The World is the sole authority on that reality.

Reality exists whether or not it is observed.

---

## Perception is subjective.

Observers never inspect reality directly.

Instead, a World derives an Observation representing what a particular observer is permitted to perceive.

Different observers may perceive the same reality differently.

---

## Knowledge is incomplete.

Observations are not reality.

They are representations of perceived information.

An Observation may be incomplete, noisy, delayed, or even incorrect.

This is a feature of the architecture, not a limitation.

---

## Decisions are local.

Agents never make decisions from objective reality.

Every decision is based on:

- the current Observation
- the agent's own memory
- the agent's internal state

Nothing else.

---

## History emerges.

Reality evolves over time.

Observers acquire new information.

Agents make new decisions.

History is the result of those interactions.

Foundry models that process rather than any particular domain.

---

# Design Principles

## Foundry owns abstractions.

Applications own implementations.

Foundry provides contracts such as World, Observation, Agent, and Decision.

Applications provide concrete implementations such as PowerballWorld or PokerWorld.

---

## One responsibility per abstraction.

Every core concept should have one clear responsibility.

Complex behavior should emerge from simple concepts working together.

---

## Public APIs should read like conversations.

Examples:

```python
observation = world.observe(agent)

decision = agent.decide(observation)
```

The API should describe relationships between concepts rather than implementation details.

---

## Delay abstraction until it is earned.

Do not introduce a new abstraction until there are at least two concrete use cases that require it.

Simple code is preferred over speculative flexibility.

---

# What Foundry Is Not

Foundry is not:

- an AI framework
- a game engine
- a reinforcement learning library
- a robotics toolkit
- a lottery simulator

Those are domains that can be modeled using Foundry.

Foundry itself is a framework for reasoning about information, decisions, and evolving worlds.

---

# A Guiding Question

When evaluating a new abstraction, ask:

> Does this make the flow of information through the system clearer?

If the answer is no, reconsider the design.
