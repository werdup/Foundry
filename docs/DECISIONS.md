# Decisions

This file records architectural decisions so future work has context.

## Decision 001 — Foundry is environment agnostic

The engine will never contain Powerball-specific code.

Powerball is the first experiment, not the identity of the framework.

## Decision 002 — Agents own memories

Memories belong to agents because memories influence future decisions.

## Decision 003 — Observers are read-only

Observers may inspect simulation state and write reports, but they must never mutate the simulation.

## Decision 004 — Reproducibility matters

Simulations should be reproducible from a seed whenever possible.

## Decision 005 — Prediction claims are out of scope

Foundry can compare strategies and simulated outcomes. It should not claim predictive power unless a future environment explicitly supports and validates prediction.
