# VirogenAI — Security

## Principles

Security is part of the engineering lifecycle and should be introduced without blocking early scientific development unnecessarily.

## Secrets

Never commit:

- API keys
- passwords
- tokens
- private certificates
- production credentials

Use environment variables or an appropriate secret-management system.

## Configuration

`.env.example` may document required variables but must contain placeholders only.

## Data

Scientific source material and future datasets must be handled according to their licensing, access, privacy, and usage requirements.

Patient or otherwise sensitive data must not be introduced without an explicit data-governance design.

## AI security

AI-generated tool calls and parameters should be validated before execution. External content must not be allowed to bypass application-level validation or security controls.

## Production security

Production hardening will be expanded during Phase 13 and should include appropriate identity, access control, network security, secret management, dependency scanning, container scanning, logging, and audit controls.
