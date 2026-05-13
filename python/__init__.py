import os
import secrets

from flask import Flask, jsonify, render_template
from jinja2 import TemplateNotFound
from werkzeug.exceptions import HTTPException

from python.config import DevelopmentConfig


def create_app(test_config=None):
    """Cria e configura a instância do aplicativo Flask."""
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../Static",
    )

    app.config.from_object(DevelopmentConfig)
    app.config["SECRET_KEY"] = (
        os.environ.get("SECRET_KEY")
        or app.config.get("SECRET_KEY")
        or secrets.token_hex(32)
    )
    app.config["SESSION_COOKIE_SECURE"] = (
        os.environ.get("SESSION_COOKIE_SECURE", "0") == "1"
    )

    if test_config is not None:
        app.config.from_mapping(test_config)

    # Registrar Blueprint de rotas
    from python.routes import bp

    app.register_blueprint(bp)

    @app.errorhandler(HTTPException)
    def handle_http_errors(error):
        """Retorna erros HTTP de forma consistente para API e templates."""
        if app.config.get("TESTING"):
            return jsonify(error=error.name, message=error.description), error.code

        template = f"errors/{error.code}.html"
        try:
            return render_template(template, error=error), error.code
        except TemplateNotFound:
            return render_template("errors/default.html", error=error), error.code

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        if app.config.get("TESTING"):
            raise error
        app.logger.exception("Erro interno não tratado: %s", error)
        safe_error = {
            "code": 500,
            "description": "Erro interno inesperado. Tente novamente mais tarde.",
        }
        return render_template("errors/500.html", error=safe_error), 500

    @app.after_request
    def apply_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self'; "
            "img-src 'self' data:; "
            "object-src 'none'; "
            "frame-ancestors 'none'"
        )
        return response

    return app
