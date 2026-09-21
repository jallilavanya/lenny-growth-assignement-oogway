# PRD — The Lenny Growth Assistant

## Discovery Brief

### User
Product managers, growth leaders, founders, and product/growth teams who want practical insights from Lenny's Podcast without manually searching a large transcript corpus.

### Problem
Useful product and growth knowledge is distributed across a large transcript corpus. Users must search, read, synthesize, and rewrite insights manually.

### Job To Be Done
“When I have a product or growth problem, I want to ask a natural-language question and receive an evidence-grounded synthesis from Lenny's Podcast that I can immediately use or turn into reusable content.”

### Success metrics
- ≥90% citation coverage for answers where retrieval returns evidence.
- ≥80% top-K retrieval relevance on a curated evaluation set.
- ≥95% successful session persistence/reload checks.
- ≥90% artifact generation success on supported prompts.
- P95 local model response under 60 seconds on evaluation hardware.
- Zero execution of tested malicious HTML payloads in the Artifact Viewer.

### Assumptions
- The supplied transcript archive is the authoritative knowledge corpus for this application.
- Local Ollama is the default demonstration model.
- A single local user is sufficient for the take-home; user authentication is out of scope.

### Scope
In scope: conversational RAG, ingestion, sessions, Ollama, cloud abstraction, Ship30 skill, artifacts, viewer, security, tests, Docker, operational docs.

Out of scope: enterprise authentication, arbitrary web search, unrestricted code execution, arbitrary local file editing, and distributed production infrastructure.

### Risks
Hallucination, incomplete transcript coverage, retrieval errors, local-model quality/latency, cloud cost, DB failure, Ollama failure, unsafe HTML, cross-session leakage, and prompt injection through retrieved text.

### Trade-offs
A local Ollama embedding path avoids mandatory paid embedding APIs. A deterministic hash embedder exists for tests only. The agent layer is intentionally a small internal routing abstraction rather than coupling the core workflow to a provider-specific agent SDK, because the required local Ollama path must remain first-class.

## Sources and references

- Transcript archive: https://github.com/ChatPRD/lennys-podcast-transcripts
- Ship 30 for 30 guide: https://www.ship30for30.com/post/how-to-start-writing-online-the-ship-30-for-30-ultimate-guide
