#!/usr/bin/env bash
set -euo pipefail

SQL_INPUT="${1:-}"

if [[ -z "${SQL_INPUT}" ]]; then
  readarray -t STDIN_LINES || true
  SQL_INPUT="$(printf "%s\n" "${STDIN_LINES[@]}")"
fi

echo "[apply_sql_migration] Received SQL migration payload:"
echo "${SQL_INPUT}"
echo "[apply_sql_migration] No-op stub complete. Wire to MCP-managed database connection before enabling writes."
