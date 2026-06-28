# ADR-0005

## Title

The World Is the Authority on Reality

## Status

Accepted

## Context

Foundry distinguishes between objective reality and perceived information.

To preserve this distinction, objective reality must have a single authoritative owner.

## Decision

Every domain defines its own World implementation.

The World owns objective reality.

The World never exposes reality directly.

Instead, it derives an Observation for a particular observer.

## Consequences

Agents cannot inspect objective reality.

Different observers may receive different observations from the same world.

World implementations remain entirely domain-specific.

Foundry provides only the contract.