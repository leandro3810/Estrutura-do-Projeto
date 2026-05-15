from datetime import UTC, datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
EXCLUDED_DIRS = {
    ".git",
    ".venv",
    ".pytest_cache",
    ".mypy_cache",
    ".tox",
    "__pypackages__",
    "venv",
    "env",
    "build",
    "dist",
    "node_modules",
    "__pycache__",
}
# Limita profundidade para evitar payloads muito grandes
# e manter a árvore legível no frontend.
MAX_DEPTH = 4


def _build_tree(path: Path, depth: int = 0) -> list[dict[str, object]]:
    if depth >= MAX_DEPTH:
        return []

    items: list[dict[str, object]] = []
    try:
        entries = sorted(
            path.iterdir(),
            key=lambda entry: (entry.is_file(), entry.name.lower()),
        )
    except OSError:
        return items

    for entry in entries:
        if entry.name in EXCLUDED_DIRS:
            continue
        # Mantém ocultos fora da árvore por padrão,
        # mesmo se não listados em EXCLUDED_DIRS.
        if entry.name.startswith("."):
            continue

        if entry.is_dir():
            items.append(
                {
                    "name": entry.name,
                    "type": "directory",
                    "children": _build_tree(entry, depth + 1),
                }
            )
        else:
            items.append({"name": entry.name, "type": "file"})

    return items


def get_project_structure_payload() -> dict[str, object]:
    return {
        "root": PROJECT_ROOT.name,
        "generated_at": datetime.now(UTC).isoformat(),
        "structure": _build_tree(PROJECT_ROOT),
    }
