# AGENTS.md
## Purpose
Document the GPT-5 Codex oriented workflow for developing, running, and validating reusable agent skills within this repository.

## Setup
- pnpm 9.x for Node tooling (`corepack enable pnpm && pnpm install`)
- uv 0.2+ for Python environments (`uv venv`, `uv pip install -r requirements.txt`)
- ruff 0.5+ for linting (`uv tool install ruff` or via `pyproject.toml`)
- pyright 1.1+ for static typing (`pnpm dlx pyright` or global install)

## Run
- Install dependencies: `pnpm install` and `uv venv && uv pip install -r requirements.txt`
- Type checks: `pnpm run typecheck` for TypeScript, `pnpm dlx pyright` for Python
- Tests: `pnpm test` for Node suites, `uv run pytest` for Python suites
- Development servers: `pnpm dev` when interactive experiences are added

## Code Style
- TypeScript runs with `tsconfig.json` strict mode enabled
- Python follows `ruff` formatting and lint rules plus `pyright` static typing
- Pre-submit: `pnpm run lint:ts`, `pnpm dlx ruff check`, `pnpm dlx pyright`

## Repo Map
- `/skills` Markdown-based skills grouped by domain
- `/tests/tasks` Manual smoke and parity checks for Codex agents
- `/mcp` MCP server documentation and examples
- `/agent` GPT-5 Codex Agents SDK experiments
- `/scripts` Shell utilities invoked by tools
- `/.github/workflows` Continuous integration pipelines

## Skills Index
- [`skills/skill-repo-discovery.md`](skills/skill-repo-discovery.md)
- [`skills/skill-prompt-discovery.md`](skills/skill-prompt-discovery.md)
- [`skills/api/rest-api-design.md`](skills/api/rest-api-design.md)
- [`skills/cicd/github-actions-workflows.md`](skills/cicd/github-actions-workflows.md)

## Guardrails
- Never commit secrets or credentials; keep environment-specific settings external
- Operate within the checked-out workspace; request approval before network operations
- Validate new executable skills with smoke tests before enabling automation

## CI Expectations
- CI must run `ruff`, `pyright`, `tsc`, `uv run pytest`, and `pnpm test`
- Pipelines fail on any lint, type, or test regression
- Pull requests require a passing CI run before review

## Tooling Notes for Codex
- Codex ingests `AGENTS.md` and `/skills` files as primary context when executing tasks
- Executable skills are exposed via MCP servers under `/mcp` or Agents SDK tools under `/agent`
- External connection details (databases, APIs) live outside the repo and are injected at runtime
