# Architectural Predictions

Foundry is being developed through questions, experiments, and evidence.

This document records predictions made before architectural decisions are finalized.

Predictions are intentionally falsifiable.

If future experiments contradict these predictions, the architecture should evolve accordingly.

---

## P-001

### Every architectural concept owns a distinct authority.

Current hypothesis:

Core abstractions are better explained by the authority they own than by the behaviors they perform.

Evidence against:

A necessary abstraction cannot be described through a single authority.

Status:

Active.

---

## P-002

### Ambiguous authority identifies architectural seams.

Current hypothesis:

Whenever responsibility for authority becomes unclear, the architecture is signaling that a concept has not yet been discovered or responsibilities are incorrectly assigned.

Evidence against:

Authority becomes ambiguous while the architecture remains clear and cohesive.

Status:

Active.

---

## P-003

### Experiments produce better questions before they produce better abstractions.

Current hypothesis:

The primary outcome of an experiment is improved understanding, not reusable code.

Evidence against:

Experiments consistently lead directly to implementation without refining the underlying questions.

Status:

Active.

---

## P-004

### Simulation is orchestration rather than a foundational concept.

Current hypothesis:

Simulation coordinates interactions between architectural concepts but does not own unique authority.

Evidence against:

Simulation eventually requires responsibility that cannot naturally belong to any existing concept.

Status:

Active.

---

## P-005

### The same architectural concepts should explain multiple domains.

Current hypothesis:

Powerball, traffic systems, healthcare, marketing research, robotics, and other domains should all be explainable using the same core concepts.

Evidence against:

A domain requires introducing domain-specific foundational abstractions.

Status:

Active.

---

## P-006

### Architectural concepts are best evaluated by the unique authority they own.

Current hypothesis:

Authority provides a stronger basis for evaluating architectural concepts than behavior.

Behavior explains what a concept does.

Authority explains why it deserves to exist.

Evidence against:

A necessary architectural concept cannot be justified through unique authority, yet is clearly justified through behavior alone.

Status:

Active.

---

## P-007

### Agents maintain internal models of the World.

### Current Hypothesis

Agents do not react directly to Observations.

Instead, Observations are used to update an Agent's internal model of the World.

Decisions emerge from the Agent's current internal model rather than directly from incoming information.

This internal model may include:

- objective state
- expectations
- goals
- previous observations
- models of other Agents

These are considered internal properties of an Agent rather than separate architectural abstractions.

---

### Predicted Evidence

If this hypothesis is correct, independent domains should consistently demonstrate that:

- identical Observations can produce different Decisions.
- Agent behavior changes when internal models change without requiring new Observations.
- communication transfers information that allows another Agent to reconstruct an updated internal model.
- no additional foundational abstraction is required to explain reasoning.

---

### Evidence Against

This prediction should be weakened if a domain demonstrates any of the following:

- Decisions emerge directly from Observations without an intermediate internal model.
- A necessary architectural abstraction exists outside the Agent to explain reasoning.
- Internal models can be transferred directly between Agents rather than reconstructed.
- Two identical Agents receiving identical Observations consistently produce different Decisions without any difference in internal state.

---

### Current Evidence

Supporting:

- CounterWorld
- DOMAIN-001 — Marketing Research
- DOMAIN-002 — Poker (preliminary)

Contradicting:

None currently identified.

---

### Status

Active

---

---

## P-008

### Episodes define completion boundaries rather than temporal boundaries.

### Current Hypothesis

An Episode represents a bounded unit of execution organized around the completion of a coherent objective.

Episodes are not primarily defined by elapsed time.

Instead, an Episode begins when execution becomes committed toward a specific objective and concludes when that objective reaches a terminal outcome.

Terminal outcomes may include:

- successful completion
- cancellation
- abandonment
- failure

Interruptions such as pauses, shift changes, or delays do not necessarily create new Episodes.

### Predicted Evidence

If this hypothesis is correct, independent domains should consistently demonstrate that:

- Episodes remain intact across interruptions in execution.
- Agent changes do not necessarily create new Episodes.
- World changes may occur without changing Episode boundaries.
- Episode boundaries are determined by objective continuity rather than elapsed time.

### Evidence Against

This prediction should be weakened if a domain demonstrates any of the following:

- elapsed time alone determines Episode boundaries.
- temporary interruptions necessarily create new Episodes.
- changing Agents always creates a new Episode.
- Episode completion cannot be explained through objective completion criteria.

### Current Evidence

Supporting

- DOMAIN-004 — Manufacturing (preliminary)

Contradicting

None currently identified.

### Status

Active.
