# Foundry

Foundry is a framework for simulating adaptive agents operating in uncertain environments.

Agents react to events.  
Agents make decisions.  
Environments apply decisions.  
Experience creates memories.  
Memories influence future behavior.

Foundry is designed for experimentation, simulation, and research — not prediction.

## First principle

Foundry exists to explore adaptive decision-making under uncertainty.

Every new feature should make simulations more explainable, reproducible, inspectable, or interesting — not simply more complex.

## Architecture

```text
                Event
                  │
                  ▼
             Agent reacts
                  │
                  ▼
             Decision made
                  │
                  ▼
        Environment changes
                  │
                  ▼
             New Event
```

## Current status

This is the Foundry core rewrite. It intentionally contains almost no domain logic.

The goal of this first commit is to establish the language:

- `Event`
- `Decision`
- `Memory`
- `Agent`
- `Environment`
- `Simulation`
