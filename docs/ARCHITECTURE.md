# Architecture

Foundry is organized around four core concepts:

```text
           Environment
                │
                ▼
            Simulation
                │
     ┌──────────┼──────────┐
     ▼          ▼          ▼
  Agents     Observers   Reports
     │
     ▼
  Memories
     │
     ▼
  Decisions
```

## Core objects

### Agent

An adaptive decision-maker.

Agents have:

- Identity
- Goals
- Strategy
- State
- Memories
- History

### Environment

The world the agent operates in.

An environment produces events and outcomes. The engine should not know whether the environment is Powerball, fantasy football, finance, or something else.

### Strategy

A strategy decides what an agent does next.

Strategies should be pluggable.

### Observer

Observers watch simulations and write outputs.

Observers must not mutate simulation state.

### Report

A report turns raw simulation output into something readable.

## Guiding architecture rule

The engine should remain environment-agnostic.

Powerball-specific logic belongs in:

```text
experiments/powerball/
```

Not in:

```text
foundry/engine/
```
