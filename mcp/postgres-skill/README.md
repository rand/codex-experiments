# MCP Postgres Skill Server

## Overview
This hypothetical MCP server wraps a PostgreSQL schema with two safe capabilities for Codex-driven automation.

## Capabilities
- `get_schema()` — returns introspected tables, columns, and constraints for the connected database.
- `execute_sql(sql: string)` — runs read-only or migration statements after guardrail checks.

## Configuration
1. Provide connection strings via environment variables (e.g., `PGHOST`, `PGUSER`, `PGDATABASE`) managed outside this repository.
2. Implement guardrails to validate migrations before execution (use `scripts/apply_sql_migration.sh` as a local stub).
3. Register the MCP server name in your Codex agent manifest so tools become available alongside skills context.

## Safety Notes
- Never embed credentials or production URIs in code; rely on injected secrets.
- Gate destructive operations (DROP/ALTER) behind explicit approvals.
- Log migrations and surface summaries back to the agent for auditing.
