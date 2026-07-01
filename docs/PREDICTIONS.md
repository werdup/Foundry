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
