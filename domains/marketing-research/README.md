# DOMAIN-001 — Marketing Research

## Purpose

This domain study evaluates whether Foundry's current architectural concepts are sufficient to explain a real marketing research workflow.

This is not a simulation.

It is an architectural validation exercise.

The objective is to explain the domain using only concepts that have already been earned.

---

# Architectural Question

Can the existing Foundry architecture explain marketing research without introducing new foundational abstractions?

---

# The World

The World contains objective facts.

Examples include:

- Respondents
- Surveys
- Questions
- Responses
- Timing
- Sample composition
- Metadata

These facts exist independently of any observer.

---

# Objective State

Examples of objective state include:

- A respondent selected Brand A.
- A survey contains 250 completed responses.
- A respondent is 34 years old.
- The interview lasted 11 minutes.

Objective state exists regardless of interpretation.

---

# Observations

Different participants receive different information.

Examples:

Research Consultant

- Survey results
- Crosstabs
- Metadata

Client

- Dashboards
- Narratives
- Charts

Designer

- Workflow
- Survey structure
- User interactions

Executive

- KPIs
- Trends
- Recommendations

Each participant receives an Observation rather than direct access to objective state.

---

# Agents

Potential Agents include:

- Research Consultant
- Client
- Product Manager
- Designer
- Executive

Each Agent interprets observations using different goals, experience, and incentives.

---

# Decisions

Examples include:

- Publish a narrative.
- Recommend a product change.
- Weight the sample.
- Launch another survey.
- Ignore statistically insignificant findings.

Decisions express intent.

They do not directly modify objective state.

---

# Episode

Possible Episode boundaries include:

- One survey
- One wave
- One reporting period
- One client engagement

The correct boundary remains an open question.

---

# Authority Audit

## Objective State

Currently appears to belong to:

World

---

## Information

Currently appears to belong to:

Observation

---

## Intent

Currently appears to belong to:

Decision

---

## Execution Boundary

Currently appears to belong to:

Episode

---

# Pressure Points

Questions this study should answer:

- Does every concept fit naturally?
- Are any responsibilities ambiguous?
- Does a new foundational abstraction become necessary?
- Does the authority lens continue to explain the architecture?

---

# Success Criteria

The study succeeds if it either:

- strengthens confidence in the existing architecture, or
- reveals where the architecture is incomplete.

Either outcome is valuable.