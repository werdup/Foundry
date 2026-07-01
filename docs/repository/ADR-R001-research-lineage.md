# ADR-R001 — Research Lineage

## Status

Accepted

---

# Context

Foundry has evolved beyond a collection of architectural documents.

The repository now contains a structured research process:

- Questions
- Predictions
- Experiments
- Domain Studies
- Evidence Reviews
- Theory Reviews
- ADRs
- FOUNDRY.md

Each artifact exists for a different purpose.

Together they describe how architectural knowledge evolves.

Without explicit relationships between these artifacts, future contributors can understand individual documents but may struggle to reconstruct the reasoning that produced them.

The repository requires a consistent way to preserve the lineage of architectural decisions.

---

# Decision

Research artifacts SHALL participate in an explicit lineage of reasoning.

Each artifact should make clear:

- what informed it
- what it informs

The repository therefore treats architectural knowledge as an evolving graph rather than a collection of isolated documents.

Research lineage exists to preserve reasoning rather than chronology.

---

# Research Pipeline

Architectural knowledge progresses through distinct stages.

Question

↓

Prediction

↓

Experiment / Domain Study

↓

Evidence Review

↓

Theory Review

↓

Architectural Decision Record

↓

FOUNDRY

Each stage answers a different research question.

---

# Responsibilities

| Artifact | Primary Question |
|----------|------------------|
| Questions | What uncertainty exists? |
| Predictions | What should happen if current theory is correct? |
| Experiments | Can the idea be isolated? |
| Domain Studies | Does the idea generalize? |
| Evidence Reviews | What evidence exists for this concept? |
| Theory Reviews | What conclusions survive accumulated evidence? |
| ADRs | What architectural decision has been earned? |
| FOUNDRY | What architectural language has survived repeated review? |

---

# Traceability Convention

Research Lineage is implemented through explicit relationships between artifacts.

The first repository convention is:

## Inputs

Artifacts that directly informed this document.

## Outputs

Artifacts expected to consume or build upon this document.

These relationships describe knowledge flow rather than implementation dependencies.

Additional conventions may be introduced in the future without changing this principle.

---

# Consequences

## Positive

- Architectural reasoning becomes reconstructable.
- Future contributors can follow decisions back to original uncertainty.
- Architectural decisions become auditable.
- Theory Reviews become explicit integration points.
- Repository evolution becomes easier to understand.

## Negative

- Long-lived artifacts require lightweight relationship maintenance.
- Historical artifacts will gradually adopt lineage as they are modified.

---

# Migration Strategy

Research Lineage will be adopted incrementally.

Existing artifacts should not be modified solely to satisfy this ADR.

Whenever an artifact is meaningfully updated, explicit lineage should be added if absent.

This allows the repository to converge naturally without large-scale refactoring.

---

# Alternatives Considered

## Central index of relationships

Rejected.

Relationships belong with the artifacts they describe.

---

## Automatic lineage generation

Rejected.

Repository conventions should precede automation.

Automation may be introduced after conventions become stable.

---

## No explicit lineage

Rejected.

The repository has reached sufficient complexity that implicit reasoning is no longer adequate.

---

# Architectural Principle

Architectural knowledge should be explainable by following its lineage back to uncertainty.

Research artifacts collectively preserve that lineage.