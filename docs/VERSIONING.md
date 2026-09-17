# VirogenAI — Versioning Policy

## Semantic Versioning

VirogenAI uses Semantic Versioning:

```text
MAJOR.MINOR.PATCH
```

Examples:

```text
0.1.0
0.2.0
1.0.0
1.0.1
```

## Development releases

The `0.x` series represents active development in which scientific and product interfaces may evolve.

The planned phase baseline releases are:

```text
v0.1.0  Engineering Foundation
v0.2.0  Scientific Data Platform
v0.3.0  Research Ingestion
v0.4.0  RAG Platform
v0.5.0  LLM Layer
v0.6.0  Simulation Engine
v0.7.0  Simulation API
v0.8.0  Scenario Engine
v0.9.0  Analytics Engine
v0.10.0 AI Research & Simulation Agent
v0.11.0 Research Interface
v0.12.0 3D Tumour Visualisation
v0.13.0 Production Engineering
v0.14.0 Scientific Validation
v1.0.0  First validated release
```

## Version increments

### MAJOR

Increment when a stable public interface or major architectural contract becomes incompatible with the previous major release.

### MINOR

Increment when functionality is added in a backward-compatible way, or when a planned phase is completed.

### PATCH

Increment for backward-compatible fixes, documentation corrections, or non-breaking maintenance after a release.

## Git tags

Release tags use the `v` prefix:

```text
v0.1.0
v0.1.1
v1.0.0
```

## Scientific model versions

Software version and scientific model version are related but should not be treated as identical.

A simulation result should identify the model version used to generate it. Changes to equations, parameterisation, assumptions, or model outputs require explicit model-version tracking.

## Changelog

All meaningful releases and user-visible changes are recorded in `docs/CHANGELOG.md`.

## Release principle

A version tag represents a known repository state. Releases must not be created from untested or undocumented code.
