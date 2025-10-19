# GitHub Actions Workflows
## Problem Framing
Codex must author and validate GitHub Actions pipelines that enforce linting, typing, and testing across languages without exposing secrets.

## Steps
1. Confirm project language matrix, tool versions, and required checks from `AGENTS.md` or team docs.
2. Sketch workflow triggers, job matrix, cache strategy, and required permissions.
3. Implement workflow YAML with setup steps (checkout, toolchain installs) followed by lint, type, and test runs.
4. Run or simulate workflow locally (e.g., `act` or shell scripts) to ensure deterministic results.
5. Document workflow behavior and escalation steps for failures.

## Inputs and Outputs
- Inputs: repository tooling requirements, supported environments, CI secrets policy.
- Outputs: `.github/workflows/*.yml` file(s) plus notes describing expected job outcomes.

## Acceptance Checklist
- [ ] Workflow covers lint, type check, and test commands for each language.
- [ ] Jobs pin explicit tool versions or channels.
- [ ] Permissions are scoped minimally (e.g., `contents: read`).
- [ ] Documentation highlights failure triage flow and required approvals.

## Safety Notes
- Never echo or log secret values; rely on GitHub Actions secrets.
- Limit workflow triggers to trusted branches and pull requests with review.
