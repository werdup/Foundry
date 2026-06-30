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