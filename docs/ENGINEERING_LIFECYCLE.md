# VirogenAI — Engineering Lifecycle

## Principle

Every phase follows a controlled engineering lifecycle. A phase is complete only when implementation, tests, documentation, validation, and release controls are complete.

## Lifecycle

```text
Issue
  ↓
Design
  ↓
Implementation
  ↓
Unit Tests
  ↓
Integration Tests
  ↓
Scientific / AI Validation
  ↓
Review
  ↓
Merge
  ↓
Release Tag
  ↓
Freeze
  ↓
Next Phase
```

## Phase workflow

1. Define phase objectives and acceptance criteria.
2. Create or update technical design documentation.
3. Implement the smallest production-quality increment.
4. Add tests with the implementation.
5. Run targeted tests.
6. Fix failures before progressing.
7. Run the full applicable test suite.
8. Update documentation and changelog.
9. Merge into `main` only after required checks pass.
10. Create the phase release tag.
11. Mark the phase frozen.
12. Start the next phase from the stable baseline.

## Branching

Use phase or feature branches for material changes. `main` represents the latest stable baseline.

Suggested naming:

```text
phase/1-foundation
phase/2-data-platform
feature/<short-name>
fix/<short-name>
```

## Definition of Done

A change is done when:

- implementation is complete
- tests are present
- tests pass
- documentation is updated
- interfaces are stable enough for the current phase
- no secrets are committed
- relevant validation passes

## Phase freeze

A frozen phase should not be casually modified. Changes after freeze require a documented reason and should be represented as a subsequent change or release where appropriate.

## Scientific changes

Changes affecting model equations, parameters, assumptions, outputs, or scientific interpretation require explicit documentation and scientific tests. They must not be hidden inside unrelated refactoring.
