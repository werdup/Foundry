# Architecture

Foundry has three layers.

## 1. Core

Core defines the environment-agnostic language of the framework:

- Event
- Decision
- Memory
- Agent
- Environment
- Simulation

Core should not contain domain-specific ideas.

## 2. Engine

The engine runs the loop:

```text
environment.next_event()
agents react
agents decide
environment.apply_decisions()
observers record
repeat
```

## 3. Domains

Domains implement concrete worlds.

Examples:

```text
foundry/domains/powerball/
foundry/domains/fantasy_football/
foundry/domains/market/
```

## Rule

If code only makes sense for one domain, it does not belong in `foundry/core`.
