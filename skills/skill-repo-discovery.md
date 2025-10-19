# Repository Discovery
## Problem Framing
Codex needs a structured approach to understand unfamiliar repositories, identify active components, and surface risks before editing or running code.

## Steps
1. Read `README.md`, `AGENTS.md`, and `_INDEX` documents to capture stated goals and constraints.
2. Generate a lightweight repo map with `ls`, `tree`, or language-aware tooling to list key directories.
3. Inspect configuration files (`package.json`, `pyproject.toml`, CI workflows) to infer tooling expectations.
4. Summarize findings, explicitly noting unknowns, risky scripts, and required approvals.

## Inputs and Outputs
- Inputs: repository path, permission level, existing documentation.
- Outputs: short summary of architecture, list of tooling commands, flagged risk areas.

## Acceptance Checklist
- [ ] Summary references primary documentation locations.
- [ ] Tooling expectations list includes install, lint, type, and test commands.
- [ ] Risks call out destructive scripts or missing approvals.
- [ ] Follow-up questions capture unknown configuration areas.

## Safety Notes
- Avoid executing scripts beyond read-only commands without explicit approval.
- Note any environment variables or secrets referenced by configs and confirm they are not present locally.
