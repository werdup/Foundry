# Foundry

Foundry is a framework for simulating adaptive agents operating in uncertain environments.

Agents make decisions.  
Environments produce outcomes.  
Experience creates memories.  
Memories influence future decisions.

Foundry is designed for experimentation, simulation, and research — not prediction.

## Project principle

Foundry exists to explore adaptive decision-making under uncertainty. Every new feature should make simulations more explainable, more reproducible, or more interesting — not simply more complex.

## Current status

This repository currently contains the project skeleton and documentation scaffolding.

## Structure

```text
foundry/
  engine/          Core simulation loop and orchestration
  agents/          Adaptive decision-makers
  environments/    Worlds agents operate in
  strategies/      Decision strategies and plugins
  observers/       Read-only simulation observers
  reports/         Report generation
  models/          Shared domain models
  utils/           Utilities

experiments/
  powerball/       First experimental environment

docs/
  Architecture, roadmap, decisions, philosophy, and lab notebook
```
