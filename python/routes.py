from flask import Blueprint, jsonify, render_template

from python.services.project_overview import get_project_overview
from python.services.project_structure import get_project_structure_payload

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    overview = get_project_overview()
    return render_template("index.html", overview=overview)


@bp.route("/about")
def about():
    overview = get_project_overview()
    return render_template("about.html", overview=overview)

@bp.route("/api/project-structure")
def project_structure():
    return jsonify(get_project_structure_payload())


@bp.route("/health")
def health():
    return jsonify(status="ok", service="estrutura-do-projeto"), 200
