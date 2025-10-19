# MCP Integration Guide

## Registering MCP Servers with GPT-5 Codex
1. Define the MCP server metadata (name, entrypoint, transport) in your Codex agent configuration.
2. Place connection credentials (DSNs, API tokens) in your local secret store or environment manager — never in this repository.
3. Update the Codex session manifest to reference the MCP server name so `AGENTS.md` and skill context are loaded alongside executable tools.

## Directory Layout
- `mcp/postgres-skill/` — example server contract for a PostgreSQL-focused skill bundle.
- Additional servers should live under `mcp/<domain>-skill/`.

## Development Notes
- Use uv-managed virtual environments when prototyping MCP servers (`uv venv && uv pip install ...`).
- Document server capabilities and safety constraints in the directory `README.md`.
- Run smoke tests from `/tests/tasks` before enabling a new server for Codex.
