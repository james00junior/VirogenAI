# Contributing to VirogenAI

## Development workflow

1. Start from the latest `main`.
2. Create a phase or feature branch.
3. Implement the smallest production-quality change.
4. Add or update tests.
5. Run the applicable local checks.
6. Update documentation when behaviour or interfaces change.
7. Open a pull request when the branch is ready.
8. Merge only after required checks pass.

## Branch naming

```text
phase/<phase-name>
feature/<short-name>
fix/<short-name>
```

## Commit messages

Use clear prefixes such as:

```text
feat:
fix:
docs:
test:
refactor:
ci:
```

## Scientific changes

Changes to equations, assumptions, parameters, outputs, or scientific interpretation require explicit tests and documentation.

## Secrets

Do not commit credentials, tokens, passwords, private keys, or production configuration.

## Research notebooks

Notebooks are for research and exploration. Production functionality should be implemented in tested modules under the appropriate package.
