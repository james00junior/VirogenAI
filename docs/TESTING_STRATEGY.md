# VirogenAI — Testing Strategy

## Purpose

Testing protects both software correctness and scientific integrity.

## Test layers

### Unit tests

Test individual functions, classes, validators, parsers, and model components.

### Integration tests

Test interactions between modules and infrastructure components.

### API tests

Test HTTP routes, request validation, response schemas, error handling, and service behaviour.

### Simulation tests

Test:

- deterministic execution
- parameter validation
- initial and boundary conditions
- numerical stability
- reproducibility
- expected qualitative behaviour
- output schema

### Data tests

Future data-platform phases will test:

- schema validity
- required metadata
- duplicate detection
- provenance
- source integrity
- transformation correctness

### AI evaluation

Future AI phases will evaluate:

- retrieval quality
- citation grounding
- extraction accuracy
- hallucination rate
- structured-output validity
- tool selection
- simulation parameter correctness

### Scientific validation

Scientific validation is separate from ordinary software testing and includes model assumptions, parameter plausibility, literature consistency, sensitivity, uncertainty, and reproducibility.

## CI quality gate

The baseline CI pipeline should execute formatting/lint checks, type checks where configured, unit tests, integration tests, and simulation tests.

Additional gates will be introduced as the relevant phases become available.

## Test philosophy

Tests should verify both normal behaviour and scientifically important failure modes. Deterministic tests are preferred where stochasticity is not part of the model.
