# Decisions

Architectural decisions are recorded here so future work has context.

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

## Decision 007 — Episodes live in runtime, not core

Core contains timeless simulation concepts such as Event, Decision, Memory, Agent, and Environment.

Episode is different: it is a runtime artifact produced by an actual simulation run.

An Episode records history. It does not define the universal language of Foundry.
