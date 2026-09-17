# VirogenAI — Phase 1 Engineering Foundation

## 1. Purpose

Phase 1 establishes the production-ready engineering foundation for VirogenAI.

The objective is not to build the complete tumour simulation system. The objective is to create a stable software foundation on which the scientific data platform, research agents, RAG system, simulation engine, analytics layer, and user interface can be developed independently and integrated safely.

## 2. Objectives

- Establish the repository and module structure.
- Define architectural boundaries between AI, evidence, simulation, analytics, data, and applications.
- Establish reproducible local development.
- Establish automated quality gates.
- Separate scientific computation from LLM reasoning and orchestration.
- Establish configuration and secret-management conventions.
- Establish versioning and release management.
- Establish the initial API, simulation, AI, and data interfaces.

## 3. Repository structure

```text
virogenAI/
├── apps/
│   ├── api/
│   ├── web/
│   └── worker/
├── simulation/
│   ├── core/
│   ├── models/
│   ├── solvers/
│   ├── scenarios/
│   └── validation/
├── ai/
│   ├── agents/
│   ├── rag/
│   ├── prompts/
│   ├── models/
│   └── evaluation/
├── data/
│   ├── ingestion/
│   ├── processing/
│   ├── schemas/
│   └── validation/
├── analytics/
│   ├── statistics/
│   ├── visualization/
│   └── comparisons/
├── infrastructure/
│   ├── docker/
│   ├── terraform/
│   └── deployment/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── simulation/
│   ├── api/
│   └── evaluation/
├── docs/
├── notebooks/
│   └── research/
├── configs/
├── pyproject.toml
├── docker-compose.yml
├── Makefile
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── .env.example
└── .github/
    └── workflows/
```

Production code must not depend on research notebooks.

## 4. Technology foundation

- Backend: Python and FastAPI
- Scientific computing: NumPy, SciPy, Pandas
- ML: PyTorch where required
- AI: provider-independent interfaces, with local inference support through Ollama
- Orchestration: LangGraph interfaces introduced without coupling core simulation logic to agents
- Database: PostgreSQL
- Vector search: pgvector in the RAG phase
- Frontend: Next.js / React
- Analytics visualisation: Plotly
- 3D visualisation: Three.js in Phase 12
- Containers: Docker
- Testing: Pytest
- CI: GitHub Actions
- Observability: OpenTelemetry in production engineering
- IaC: Terraform during production engineering

## 5. Architectural principle

The LLM is not the scientific simulator.

```text
LLM
  ↓
reasoning / interpretation / orchestration
  ↓
validated parameters
  ↓
simulation engine
  ↓
deterministic numerical computation
  ↓
analytics
  ↓
LLM explanation
```

AI-generated simulation parameters must pass validation before entering the simulation engine.

## 6. API foundation

Initial endpoints:

```text
GET /health
GET /version
```

Future endpoints include simulation, research, and analysis APIs. Phase 1 establishes the service structure rather than the complete application workflow.

## 7. Simulation foundation

Establish the interface:

```text
SimulationConfig
        ↓
SimulationEngine
        ↓
SimulationResult
```

A simulation configuration must contain sufficient information to reproduce a run, including model version, parameters, initial conditions, duration, timestep, treatment configuration where applicable, and random seed where stochastic behaviour is introduced.

## 8. AI foundation

Phase 1 defines interfaces for future components such as:

- ResearchAgent
- EvidenceRetriever
- SimulationAgent
- AnalysisAgent
- SynthesisAgent

No agent may directly modify simulation internals.

## 9. Testing

Phase 1 establishes:

- unit tests
- integration tests
- API tests
- simulation tests
- reproducibility tests
- parameter validation tests
- CI execution

Future phases add RAG, LLM, scientific validation, security, and performance evaluation.

## 10. Configuration

Configuration must not be hard-coded. Environment variables and configuration files are used for environment-specific settings.

Real credentials and secrets must never be committed. `.env.example` documents required variables without containing real secrets.

## 11. Acceptance criteria

Phase 1 is complete when:

- repository structure exists
- Python environment is reproducible
- API starts successfully
- `/health` works
- `/version` works
- simulation interface exists
- simulation tests pass
- configuration management works
- secrets are excluded
- Docker development environment works
- CI executes successfully
- unit tests pass
- integration tests pass
- documentation is complete
- README explains local execution
- release is tagged

## 12. Release

Target release:

```text
v0.1.0
```

After release, Phase 1 is frozen. Structural changes require an explicit engineering decision and should be documented before implementation in later phases.
