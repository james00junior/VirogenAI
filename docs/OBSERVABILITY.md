# VirogenAI — Observability

## Objective

Observability should make it possible to understand application behaviour, simulation execution, AI workflows, and system failures.

## Initial direction

Production observability will use structured logs, metrics, and distributed tracing where appropriate.

OpenTelemetry is the intended instrumentation direction.

## Important metrics

Application:

- API latency
- request volume
- error rate

Simulation:

- simulation duration
- queue time
- solver failures
- failed runs
- resource usage

AI:

- LLM latency
- token usage where available
- tool failures
- agent workflow failures

RAG:

- retrieval latency
- retrieval quality
- evidence coverage
- citation grounding

## Scientific traceability

Simulation executions should retain sufficient identifiers to connect a result to its configuration, model version, and relevant evidence or parameter provenance.

## Development scope

Detailed production observability is implemented during Phase 13. Phase 1 establishes the architectural requirement and interfaces needed to introduce it later.
