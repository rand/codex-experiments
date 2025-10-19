# Add CI for Python and TypeScript

## Acceptance
- Create .github/workflows/ci.yml that runs:
  - uv run pytest -q
  - pnpm test
  - pyright and tsc
- Fail on type or test failures
- Commit message must include: "ci: add py+ts tests"
