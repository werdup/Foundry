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

---

# Walkthrough 001 Summary

---

## What the Domain Taught Us

### Domain Observation 1

Survey branching does not create multiple Worlds.

It creates multiple Observations.

Different respondents receive different information while remaining consistent with the same objective state.

---

### Domain Observation 2

The World exists before any Agent interacts with it.

Agents participate in an existing World rather than creating one.

---

### Domain Observation 3

A respondent's decision and the resulting objective state are distinct.

Intent and recorded state should not be treated as the same thing.

---

### Domain Observation 4

Survey logic produces different Observations from the same World according to objective rules.

---

### Domain Observation 5

A completed survey contains objective data but not objective conclusions.

Narratives emerge after observation rather than existing within the World.

---

### Domain Observation 6

Consultants reason over Observations rather than directly over the World.

Dashboards, reports, and exports remain representations.

---

### Domain Observation 7

Observations provide information.

Meaning is constructed by the Agent.

Different Agents may construct different understandings from identical Observations.

---

## Emerging Interpretations

The following ideas are becoming stronger but remain hypotheses.

- Observation appears to define the information available for decision-making.
- Survey branching reinforces Observation rather than requiring a new abstraction.
- The authority lens continues to explain why new concepts have not been required.
- Agents appear to construct internal models rather than simply reacting to observations.
- Decisions appear to emerge from an Agent's internal model of the World.

## Open Questions

- Can an Agent participate in a World while simultaneously reasoning about it?
- What applies a Decision to the World?
- Can a perfect Observation exist?
- Where does shared knowledge reside?
- Can meaning ever be transferred, or is it always reconstructed?
- Is meaning best understood as an Agent's internal model of the World?

---

## Pressure Summary

Strengthened

- World
- Observation
- Agent
- Authority Lens

Challenged

- Relationship between Decision and World
- Responsibility of Agent

No new foundational abstractions emerged.