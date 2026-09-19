# Scientific Data Platform

Phase 2 establishes canonical, validated data contracts before external research ingestion.

## Contracts

- `schemas/scenario.py` — simulation scenario and parameter validation
- `schemas/evidence.py` — normalized scientific evidence metadata
- `schemas/results.py` — reproducible simulation result envelope

These contracts are deliberately independent of databases, RAG providers, LLMs, and numerical solvers. They form the stable boundary between scientific data and downstream services.

## Principles

1. Validate data at boundaries.
2. Preserve provenance for evidence.
3. Version simulation models separately from application releases.
4. Keep raw source material separate from normalized records.
5. Never allow an LLM to bypass scientific parameter validation.
