# ER-001 — Observation

## Purpose

Collect independent evidence relating to the Observation abstraction.

This review intentionally contains evidence only.

Interpretation belongs in Theory Reviews.

Architectural changes belong in ADRs.

---

# Current Definition

Observation represents the information available from the World to an Agent.

(Reference ADR-0004.)

---

# Evidence

## CounterWorld

### Evidence

CounterWorld established that World and Observation must remain separate authorities.

Observation exists because Agents cannot directly access authoritative state.

---

## DOMAIN-001 — Marketing Research

### Evidence 1

Survey branching produced multiple Observations while remaining within a single World.

### Evidence 2

Consultants reasoned over Observations rather than directly over survey data.

### Evidence 3

Observation provided information.

Interpretation remained internal to the Agent.

---

## DOMAIN-002 — Poker

### Evidence 1

Different players received different Observations while sharing the same World.

### Evidence 2

Hidden cards demonstrated that objective state may never become an Observation.

### Evidence 3

Identical Observations did not require identical Decisions.

---

## DOMAIN-003 — Navigation

### Evidence 1

Maps contained more information than Agents incorporated into their internal understanding.

### Evidence 2

Communication enabled another Agent to reconstruct understanding without transferring it directly.

### Evidence 3

Observation appeared to involve selective acquisition rather than automatic availability.

---

# Patterns

Across all reviewed domains:

- Observation remained distinct from World.
- Observation supplied information rather than interpretation.
- Observation did not determine Decisions.
- Observation consistently preceded Agent reasoning.
- Observation experienced increasing pressure regarding selective acquisition.

---

# Unresolved Pressure

The following questions remain unresolved.

- Is Observation defined by available information or acquired information?
- Does selective attention belong to Observation or Agent?
- Can an Observation ever be complete?
- Is every Observation necessarily partial?

No conclusions are drawn within this document.