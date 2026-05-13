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
