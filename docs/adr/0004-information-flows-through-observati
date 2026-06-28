# ADR-0004

## Title

Information Flows Through Observations

## Status

Accepted

## Context

Foundry models worlds that evolve over time.

A central architectural question is how decision makers acquire information about the world.

Allowing decision makers to inspect the World directly tightly couples behavior to implementation and prevents modeling hidden information, imperfect information, or observer-specific knowledge.

## Decision

Decision makers never inspect the World directly.

Instead, the World derives an Observation for a particular observer.

An Observation represents the information available to one observer at one moment in time.

Observations are immutable.

Decision makers produce Decisions using only:

- the current Observation
- their own internal state
- their own memory

The World remains the sole authority on objective reality.

## Consequences

Reality and perception become separate concepts.

This enables Foundry to naturally model:

- hidden information
- imperfect information
- asymmetric information
- sensor noise
- deception

without changing the decision-making architecture.

Observations are intentionally independent of:

- World
- Agent
- Event
- Memory

They represent only permitted perception.

## Alternatives Considered

### Agents inspect the World directly

Rejected.

This tightly couples decision makers to world state and prevents observer-specific perspectives.

### Events drive decisions

Rejected.

Events describe transitions.

Observations describe current knowledge.

These are separate concepts.