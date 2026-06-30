# Foundry Development

This document describes how Foundry evolves.

It does not describe Python conventions or coding standards.

It describes how architectural knowledge enters the framework.

---

# First Principle

Protect uncertainty.

When the correct architecture is unknown, preserve the uncertainty rather than prematurely resolving it.

Questions exist to be explored.

Predictions exist to be challenged.

Architecture exists to explain evidence.

---

# Guiding Principle

Don't invent.

Discover.

Architectural concepts earn their place through repeated explanatory power.

Useful concepts are insufficient.

Necessary concepts survive repeated attempts to disprove them.

---

# Knowledge Lifecycle

Every architectural idea progresses through the same stages.

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

Architecture Decision

↓

Implementation Guide

↓

Implementation

↓

Validation

↓

New Pressure
```

No stage should be skipped.

---

# Repository Knowledge Hierarchy

Knowledge moves through the repository in the following order.

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

The repository intentionally separates uncertainty from conclusions.

---

# Architectural Humility

When uncertainty exists:

- Record the question.
- Make the prediction.
- Design the smallest useful experiment.
- Gather evidence.

Do not resolve uncertainty through intuition alone.

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

Every guide should represent exactly one architectural idea.

---

# Repository Synchronization

The repository is the authoritative source of architectural truth.

Conversation provides context.

The repository records decisions.

Before beginning significant work:

- Synchronize with the latest repository.
- Review recent architectural discussions.
- Resolve drift before implementation.

Whenever repository state and shared understanding disagree, synchronize first.

---

# Signs of Drift

Pause development whenever:

- New abstractions are proposed without evidence.
- Multiple architectural questions are addressed simultaneously.
- Behavior is used to justify abstractions instead of architectural responsibility.
- Framework code is written before understanding the problem.
- Predictions begin to be treated as facts.
- Repository state and shared understanding diverge.

Drift should be corrected before implementation continues.

---

# Success

Foundry succeeds when:

- Questions become more precise.
- Experiments become smaller.
- Architecture becomes simpler.
- Implementation becomes increasingly obvious.

The framework should become easier to explain as it grows.