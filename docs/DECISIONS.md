# Decisions

## Decision 001 — Foundry is domain-agnostic

Foundry is not a lottery simulator. Powerball is a domain, not the framework.

## Decision 002 — Core contains contracts, not domain behavior

`foundry/core` defines reusable concepts only.

## Decision 003 — Decisions must include reasons

Every decision should be explainable.

## Decision 004 — Memories are selective

Agents should not remember everything. They should remember meaningful events.

## Decision 005 — Objects should be JSON-serializable

This supports replay, debugging, reports, and future visualization.

## Decision 006 — Observers are read-only

Observers may inspect and record. Observers must not mutate simulation state.
