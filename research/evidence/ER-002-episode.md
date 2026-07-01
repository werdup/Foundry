# ER-002 — Episode

## Purpose

Collect independent evidence relating to the Episode abstraction.

This review intentionally contains evidence only.

Interpretation belongs in Theory Reviews.

Architectural changes belong in ADRs.

---

## Inputs

- DOMAIN-004 — Manufacturing

## Outputs

- TR-002 — Episode

---

# Current Definition

Episode defines the execution boundary within which work occurs.

(Reference the current Episode ADR.)

---

# Evidence

## DOMAIN-004 — Manufacturing

### Evidence 1

A manufacturing objective remained intact despite pauses in execution.

Lunch breaks, shift changes, and temporary interruptions did not necessarily terminate the Episode.

---

### Evidence 2

Changing participating Agents did not necessarily change the Episode.

Work continued under the same governing objective.

---

### Evidence 3

Objective completion appeared to determine Episode completion more strongly than elapsed time.

---

### Evidence 4

Interruption and termination behaved differently.

Execution could pause without ending the Episode.

---

### Evidence 5

Completion and termination appeared to be distinct concepts.

Successful completion, cancellation, abandonment, and failure all represented possible terminal outcomes.

---

# Patterns

Across reviewed evidence:

- Episode boundaries were not determined solely by elapsed time.
- Interruptions did not necessarily terminate Episodes.
- Agent changes did not necessarily create new Episodes.
- Objective continuity consistently preserved Episode identity.
- Terminal outcomes appeared more significant than execution duration.

---

# Unresolved Pressure

The following questions remain unresolved.

- When does an Episode begin?
- Does commitment begin an Episode, or only execution?
- Are completion and termination fundamentally different?
- Are lifecycle states intrinsic to Episode?
- Can an Episode exist without an active Agent?

No conclusions are drawn within this document.