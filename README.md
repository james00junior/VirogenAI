# VirogenAI

AI-assisted scientific research and simulation platform for solid-tumour biology.

## Vision

VirogenAI combines scientific evidence, retrieval-augmented generation, controlled research agents, mechanistic simulation, statistical analysis, uncertainty analysis, and interactive visualisation.

The platform is designed around a clear separation between AI reasoning and scientific computation:

```text
Research question
      ↓
AI / research orchestration
      ↓
Scientific evidence
      ↓
Validated simulation parameters
      ↓
Simulation engine
      ↓
Analytics
      ↓
Evidence-grounded explanation
```

The LLM assists with reasoning, retrieval, orchestration, and explanation. It is not the numerical scientific simulator.

## Project status

Current phase: **Phase 1 — Engineering Foundation**

Target release: `v0.1.0`

See [`docs/PROJECT_ROADMAP.md`](docs/PROJECT_ROADMAP.md) and [`docs/PHASE_1_PLAN.md`](docs/PHASE_1_PLAN.md).

## Documentation

- [Project Roadmap](docs/PROJECT_ROADMAP.md)
- [Phase 1 Plan](docs/PHASE_1_PLAN.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Scientific Specification](docs/SCIENTIFIC_SPECIFICATION.md)
- [Engineering Lifecycle](docs/ENGINEERING_LIFECYCLE.md)
- [Versioning](docs/VERSIONING.md)
- [Development Guidelines](docs/DEVELOPMENT_GUIDELINES.md)
- [Testing Strategy](docs/TESTING_STRATEGY.md)
- [AI, RAG & Agent Strategy](docs/AI_RAG_AGENT_STRATEGY.md)
- [Simulation Strategy](docs/SIMULATION_STRATEGY.md)
- [Data Strategy](docs/DATA_STRATEGY.md)
- [Security](docs/SECURITY.md)
- [Deployment](docs/DEPLOYMENT.md)
- [Observability](docs/OBSERVABILITY.md)
- [Changelog](docs/CHANGELOG.md)

## Development philosophy

VirogenAI is developed phase by phase. Each phase has explicit acceptance criteria, tests, documentation, a release version, and a freeze point before the next phase begins.

Research notebooks are used for exploration. Production functionality belongs in tested application, simulation, AI, data, analytics, or infrastructure modules.

## Scientific scope

The initial scientific scope focuses on controlled solid-tumour simulation, including tumour growth, treatment effect, resistance, viability, and selected tumour-microenvironment variables. More complex spatial and multi-scale models are introduced only when they can be scientifically justified and validated.

## Important distinction

VirogenAI is initially a research and simulation platform. Simulation results must not be represented as clinical diagnoses, treatment recommendations, or validated patient-specific clinical predictions without appropriate evidence, validation, governance, and regulatory frameworks.
