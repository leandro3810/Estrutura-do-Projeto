from flask import Blueprint, current_app, jsonify, render_template

from python.services.enterprise_automation import (
    get_enterprise_automation_payload,
    get_operational_report_payload,
)
from python.services.project_overview import get_project_overview
from python.services.project_structure import get_project_structure_payload

bp = Blueprint("main", __name__)


def _has_enterprise_access() -> bool:
    allowed_roles = {
        role.lower() for role in current_app.config.get("AUTOMATION_ALLOWED_ROLES", ())
    }
    runtime_role = current_app.config.get("AUTOMATION_RUNTIME_ROLE", "").strip().lower()
    return bool(runtime_role) and runtime_role in allowed_roles


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


@bp.route("/api/enterprise/automation")
def enterprise_automation():
    if not _has_enterprise_access():
        return (
            jsonify(
                error="Forbidden",
                message="Perfil sem permissão para acessar automação empresarial.",
            ),
            403,
        )
    active_environment = current_app.config.get("AUTOMATION_ACTIVE_ENV", "production")
    return jsonify(get_enterprise_automation_payload(active_environment))


@bp.route("/api/enterprise/report")
def enterprise_report():
    if not _has_enterprise_access():
        return (
            jsonify(
                error="Forbidden",
                message="Perfil sem permissão para acessar relatório operacional.",
            ),
            403,
        )
    return jsonify(get_operational_report_payload())
