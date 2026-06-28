# Lab Notebook

## 2026-06-28 — Core Rewrite

### Question

What is the smallest useful language for Foundry?

### Result

Foundry now has a clean core that does not know about any specific domain.

### Next Question

What is the smallest working environment that proves the engine loop?

---

## 2026-06-28 — Episode Runtime Model

### Question

Where should simulation history live?

### Setup

Added a runtime Episode object that records events, decisions, seed, environment name, timing, and metadata.

### Result

Episodes can now be started, recorded into, finished, summarized, and serialized.

### Observation

Recorder and replay now have a stable object to write to and read from.

### Next Question

What is the smallest observer that records event and decision streams into an Episode?
