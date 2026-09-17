# VirogenAI — Project Roadmap

## Vision

VirogenAI is an AI-assisted scientific simulation and research platform for investigating solid tumour biology, treatment response, tumour evolution, and related biological mechanisms.

The platform combines scientific literature, structured biological evidence, retrieval-augmented generation, research agents, mechanistic simulation, statistical analysis, uncertainty analysis, and interactive visualisation.

Core principle:

> AI assists scientific reasoning; validated computational models perform the scientific simulation.

## Roadmap

### Phase 0 — Product & Scientific Specification

Define the initial biological scope, simulation objectives, assumptions, terminology, and validation strategy.

### Phase 1 — Engineering Foundation

Establish repository architecture, API and simulation interfaces, AI interfaces, configuration, testing, Docker, CI, documentation, and release management.

Release: `v0.1.0`

### Phase 2 — Scientific Data Platform

Create the scientific evidence platform, metadata schemas, source management, ingestion interfaces, validation, and PostgreSQL foundation.

Release: `v0.2.0`

### Phase 3 — Research Ingestion

Build controlled literature search, evidence extraction, mechanism extraction, metadata extraction, validation, and synthesis workflows.

Release: `v0.3.0`

### Phase 4 — RAG Platform

Implement hybrid scientific retrieval using keyword, vector, metadata, and evidence ranking approaches. Ground scientific answers in retrievable evidence.

Release: `v0.4.0`

### Phase 5 — LLM Layer

Benchmark local and other supported models for scientific reasoning, extraction, summarisation, structured output, citation grounding, tool calling, and context handling.

Local inference can initially use Ollama.

Release: `v0.5.0`

### Phase 6 — Simulation Engine

Implement the first controlled tumour simulation covering tumour growth, treatment effect, resistance, and parameter uncertainty. Candidate modelling approaches include ODE, PDE, agent-based, and hybrid models.

Release: `v0.6.0`

### Phase 7 — Simulation API

Expose simulation execution and results through a production API.

Release: `v0.7.0`

### Phase 8 — Scenario Engine

Support controlled comparison of treatment, resistance, oxygen, and other biological scenarios.

Release: `v0.8.0`

### Phase 9 — Analytics Engine

Implement growth curves, response curves, sensitivity analysis, parameter importance, uncertainty intervals, simulation ensembles, and scenario comparison independently of the LLM.

Release: `v0.9.0`

### Phase 10 — AI Research & Simulation Agent

Connect user questions to evidence retrieval, parameter construction, validation, simulation, analytics, and evidence-grounded explanation through controlled orchestration.

Release: `v0.10.0`

### Phase 11 — Research Interface

Build the interactive research workspace combining conversation, simulation, analytics, parameters, assumptions, and evidence.

Release: `v0.11.0`

### Phase 12 — 3D Tumour Visualisation

Introduce spatial visualisation of tumour cells, populations, resistant regions, necrosis, oxygen gradients, drug concentration, blood vessels, and related structures as supported by the scientific models.

Release: `v0.12.0`

### Phase 13 — Production Engineering

Implement production deployment, CI/CD, container builds, security scanning, observability, logging, metrics, tracing, failure handling, infrastructure as code, and operational controls.

Release: `v0.13.0`

### Phase 14 — Scientific Validation & Release

Validate software correctness, numerical behaviour, scientific assumptions, parameterisation, literature consistency, reproducibility, AI grounding, and simulation parameter correctness.

Release: `v0.14.0`

## VirogenAI 1.0

`v1.0.0` is reserved for the first release that has passed the required software, scientific, AI, reproducibility, and production-readiness gates.

## Post-1.0 research directions

Potential future research includes multi-scale tumour models, spatial tumour evolution, vascular modelling, immune interactions, multi-drug treatment simulations, treatment scheduling, patient-specific modelling, digital-twin research, GPU-accelerated simulation, distributed simulation ensembles, Bayesian parameter inference, uncertainty quantification, pathology integration, genomics integration, and clinical research interfaces.

These capabilities are intentionally outside the initial release scope.
