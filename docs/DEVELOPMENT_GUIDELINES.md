# VirogenAI — Development Guidelines

## General principles

- Prefer simple, explicit implementations over unnecessary abstraction.
- Keep scientific logic independently testable.
- Keep AI orchestration separate from numerical computation.
- Do not hard-code secrets or environment-specific configuration.
- Add tests with new functionality.
- Update documentation when interfaces or behaviour change.

## Production code vs research

Production code belongs in `apps/`, `simulation/`, `ai/`, `data/`, `analytics/`, or `infrastructure/` according to responsibility.

`notebooks/research/` is for exploration, experiments, visual inspection, and scientific prototyping. Important production logic must be transferred into tested modules.

## Interfaces

Public internal interfaces should be explicit and typed where practical. Provider-specific implementations should remain behind replaceable interfaces when multiple providers are expected.

## Errors

Errors should be explicit and actionable. Silent failure is discouraged, especially for scientific calculations, data ingestion, and AI tool execution.

## Reproducibility

Simulation and analytical workflows should record the configuration and relevant software/model versions required to reproduce results.

## Dependencies

Add dependencies only when they provide clear value. Prefer established libraries and avoid unnecessary framework proliferation.

## Commits

Use concise, meaningful commit messages. Suggested prefixes:

```text
feat: add simulation configuration
fix: validate timestep bounds
docs: update scientific specification
test: add reproducibility coverage
refactor: simplify evidence interface
ci: add Python test workflow
```

## Reviews

Review changes for:

- correctness
- tests
- scientific implications
- security
- maintainability
- interface compatibility
- documentation

## Research integrity

Do not present simulated results as experimental observations. Distinguish evidence, assumptions, hypotheses, model outputs, and interpretations.
