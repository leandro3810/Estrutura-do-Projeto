from datetime import UTC, datetime
from pathlib import Path

from flask import Blueprint, jsonify, render_template

from python.services.project_overview import get_project_overview

bp = Blueprint("main", __name__)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
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


@bp.route("/")
def home():
    overview = get_project_overview()
    return render_template("index.html", overview=overview)


@bp.route("/about")
def about():
    overview = get_project_overview()
    return render_template("about.html", overview=overview)


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


@bp.route("/api/project-structure")
def project_structure():
    return jsonify(
        {
            "root": PROJECT_ROOT.name,
            "generated_at": datetime.now(UTC).isoformat(),
            "structure": _build_tree(PROJECT_ROOT),
        }
    )


@bp.route("/health")
def health():
    return jsonify(status="ok", service="estrutura-do-projeto"), 200
