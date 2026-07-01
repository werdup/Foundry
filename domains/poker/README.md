# DOMAIN-002 — Poker

## Purpose

This domain study evaluates whether Foundry's current architecture can explain a domain containing:

- hidden information
- imperfect observations
- competing agents
- strategic decision-making

This is not a poker simulation.

It is an architectural validation exercise.

---

# Architectural Question

Can the existing Foundry architecture explain poker without introducing new foundational abstractions?

---

# Walkthrough 001

## Scenario

A poker table is prepared.

The deck is shuffled.

Players are seated.

Cards are dealt.

Players observe their own hands and make betting decisions.

---

## Domain Observation 1

The World may contain objective state that no Agent has ever observed.

Examples include:

- unseen cards
- burn cards
- future community cards

Objective state exists independently of observation.

---

### Interpretation

The World is larger than every Agent's knowledge.

---

### Open Questions

- Can objective state influence outcomes without ever becoming an Observation?
- Does every World necessarily contain unknowable state?

---

## Domain Observation 2

Different Agents receive different Observations while remaining in the same World.

Each player observes only their own cards.

No player directly observes the complete objective state.

---

### Interpretation

Observation partitions information rather than creating separate Worlds.

---

### Open Questions

- Can multiple Observations collectively reconstruct the World?
- Is every Observation intentionally incomplete?

---

## Domain Observation 3

Card values belong to the Observation.

Hand strength belongs to the Agent.

Two players may construct different assessments from identical observations.

---

### Interpretation

Agents appear to update internal models rather than directly reacting to observations.

---

### Open Questions

- Is hand strength part of an Agent's internal model?
- Where does probability belong?

---

## Domain Observation 4

Identical Observations do not require identical Decisions.

Different players routinely make different decisions from the same cards.

---

### Interpretation

Observations provide information.

Agent state determines decisions.

---

### Open Questions

- Which Agent properties most strongly influence decisions?
- Can identical Agents ever produce different decisions?

---

# Walkthrough Summary

## What Poker Strengthened

- World
- Observation
- Agent
- Authority Lens

---

## What Poker Challenged

- Relationship between hidden objective state and Observation
- Internal responsibilities of Agent

---

## No New Foundational Abstractions Emerged

Poker introduced significant architectural pressure without requiring additional foundational concepts.

Instead, it deepened the understanding of existing concepts.