# VirogenAI — Deployment Strategy

## Development

Local development is the first deployment target. Docker is used to make service dependencies reproducible.

## Service direction

As the system grows, production may separate:

```text
Frontend
API
Worker
Simulation workloads
PostgreSQL
Object storage
Vector retrieval
Model serving
```

Services should be separated according to actual workload and scaling requirements rather than prematurely splitting the application.

## CI/CD

The intended pipeline is:

```text
lint
  ↓
tests
  ↓
simulation validation
  ↓
AI/RAG evaluation
  ↓
security checks
  ↓
container build
  ↓
deployment
```

Not every gate exists in Phase 1. Gates are introduced with the relevant phase.

## Infrastructure as code

Terraform will be introduced when cloud infrastructure becomes necessary. Infrastructure definitions should be version controlled and reviewed like application code.

## Releases

Production deployments should reference immutable version tags rather than an arbitrary working branch state.
