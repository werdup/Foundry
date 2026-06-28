# ADR 0003

## Title

Introduce Agent as the behavioral boundary of Foundry.

## Context

Foundry already models events and decisions, but nothing owns behavior.

## Decision

Introduce an abstract Agent class.

Agents:

- receive Events
- produce Decisions

Agents do not execute simulations.

They only determine behavior.

## Consequences

Simulation becomes responsible for orchestration.

Behavior becomes replaceable.