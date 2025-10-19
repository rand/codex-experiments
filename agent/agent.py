"""Example GPT-5 Codex agent wiring with a single SQL migration tool."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any, Callable, ParamSpec, Protocol, TypeVar, cast

P = ParamSpec("P")
R = TypeVar("R")


class ToolProtocol(Protocol):
    def __call__(
        self, *, name: str, schema: dict[str, Any]
    ) -> Callable[[Callable[P, R]], Callable[P, R]]:
        ...


try:
    from openai import tool as _codex_tool  # pyright: ignore[reportMissingImports, reportUnknownVariableType]  # noqa: I001

    codex_tool: ToolProtocol = cast(ToolProtocol, _codex_tool)
except ImportError:

    def _fallback_tool(
        *, name: str, schema: dict[str, Any]
    ) -> Callable[[Callable[P, R]], Callable[P, R]]:
        """Fallback decorator when OpenAI Agents SDK is unavailable."""

        def decorator(func: Callable[P, R]) -> Callable[P, R]:
            return func

        return decorator

    codex_tool = _fallback_tool


REPO_ROOT = Path(__file__).resolve().parent.parent


@codex_tool(name="apply_sql_migration", schema={"sql": {"type": "string"}})
def apply_sql_migration(*, sql: str) -> str:
    """Forward the provided SQL migration to the repository script."""
    script_path = REPO_ROOT / "scripts" / "apply_sql_migration.sh"
    result = subprocess.run(
        [str(script_path)],
        input=sql,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def run() -> None:
    """Demonstrate invoking tests before applying a SQL migration."""
    print("[agent] Running pre-migration smoke checks...")
    for command in (
        ["pnpm", "test"],
        ["uv", "run", "pytest", "-q"],
    ):
        try:
            subprocess.run(command, check=True)
        except FileNotFoundError:
            print(f"[agent] Skipping command (not installed): {' '.join(command)}")
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(f"Pre-check failed: {' '.join(command)}") from exc

    response = apply_sql_migration(
        sql="/* sample */ CREATE TABLE example(id INT PRIMARY KEY);"
    )
    print("[agent] apply_sql_migration response:")
    print(response)


if __name__ == "__main__":
    run()
