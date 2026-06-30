# Foundry Development Process

Foundry is not designed through intuition.

It is discovered through evidence.

The purpose of this document is to describe how architectural decisions are made and how the framework evolves over time.

---

# First Principle

Protect uncertainty.

When the correct architecture is unknown, document the uncertainty rather than prematurely resolving it.

Questions are preserved until experiments provide sufficient evidence for an architectural decision.

---

# Development Philosophy

Don't invent.

Discover.

Architectural concepts earn their place by repeatedly explaining evidence gathered through experiments.

Useful ideas are not sufficient.

Necessary ideas survive repeated attempts to disprove them.

---

# Development Loop

Every architectural change follows the same progression.

```text
Pressure

↓

Question

↓

Prediction

↓

Experiment

↓

Evidence

↓

Architecture

↓

Implementation Guide

↓

Implementation

↓

Validation

↓

New Pressure
```

The goal of each cycle is not implementation.

The goal is improved understanding.

---

# Repository Knowledge Flow

Knowledge moves through the repository in a specific order.

```text
QUESTIONS.md

↓

PREDICTIONS.md

↓

experiments/

↓

ADR/

↓

Implementation Guides

↓

Source Code
```

Questions come before architecture.

Architecture comes before implementation.

---

# Questions

Questions identify uncertainty.

Questions should remain open until evidence supports an architectural decision.

Questions are expected.

Premature answers are discouraged.

---

# Predictions

Predictions make the current architectural theory testable.

Predictions must be falsifiable.

If experiments contradict a prediction, the prediction should be updated or removed.

---

# Experiments

Experiments exist to gather evidence.

They are intentionally small.

They are not prototypes.

They are not framework code.

Their primary output is architectural observations.

---

# ADRs

Architectural Decision Records capture conclusions supported by evidence.

An ADR should never introduce an idea that has not already emerged through experiments.

---

# Implementation Guides

Implementation Guides are the primary collaboration artifact.

Every guide contains:

- Title
- Objective
- Files
- Repository Walkthrough
- Validation
- Commit
- Architectural Impact
- Next Question

Each guide should represent exactly one idea.

---

# Working Agreement

The repository is the source of truth.

Conversation history provides context but is never authoritative.

Before significant work begins:

- Synchronize with the latest repository.
- Review recent architectural discussions.
- Resolve any drift before continuing.

When architectural drift is detected, stop implementation and resynchronize before proceeding.

---

# Architectural Humility

When uncertainty exists:

- Record the question.
- Make a prediction.
- Design an experiment.
- Gather evidence.

Do not introduce new architectural concepts solely because they appear useful.

Concepts earn their place through repeated explanatory power.

---

# Signs of Drift

Development should pause whenever one or more of the following occur:

- New abstractions are proposed without experimental evidence.
- Multiple architectural questions are addressed in a single change.
- Behavior is used to justify an abstraction instead of architectural responsibility.
- Reusable framework code is written before the underlying problem is understood.
- Predictions begin to be treated as facts.
- The repository and the shared architectural understanding are no longer aligned.

When drift occurs, synchronization takes priority over implementation.

---

# Success Criteria

The framework should become simpler over time.

Experiments should produce better questions.

Architecture should emerge from evidence.

Implementation should become increasingly obvious.

If implementation becomes easier while the architecture becomes smaller, the process is working.