import os
import secrets

from flask import Flask, jsonify, render_template
from jinja2 import TemplateNotFound
from werkzeug.exceptions import HTTPException

from python.config import BaseConfig, DevelopmentConfig


def create_app(test_config=None):
    """Cria e configura a instância do aplicativo Flask."""
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../Static",
    )

    flask_env = os.environ.get("FLASK_ENV", "development").lower()
    config_class = DevelopmentConfig if flask_env == "development" else BaseConfig
    app.config.from_object(config_class)

    if test_config is not None:
        app.config.from_mapping(test_config)

    env_secret = os.environ.get("SECRET_KEY")
    config_secret = app.config.get("SECRET_KEY")
    if env_secret:
        app.config["SECRET_KEY"] = env_secret
    elif config_secret:
        app.config["SECRET_KEY"] = config_secret
    elif app.config.get("DEBUG") or app.config.get("TESTING"):
        app.config["SECRET_KEY"] = secrets.token_hex(32)
    else:
        raise RuntimeError("SECRET_KEY obrigatório fora de desenvolvimento/teste.")

    if "SESSION_COOKIE_SECURE" in os.environ:
        app.config["SESSION_COOKIE_SECURE"] = (
            os.environ.get("SESSION_COOKIE_SECURE") == "1"
        )

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
        app.logger.exception("Erro interno não tratado.")
        safe_error = {
            "code": 500,
            "description": "Erro interno inesperado. Tente novamente mais tarde.",
        }
        return render_template("errors/500.html", error=safe_error), 500

    @app.after_request
    def apply_security_headers(response):
        csp_directives = [
            "default-src 'self'",
            "script-src 'self'",
            "style-src 'self'",
            "img-src 'self' data:",
            "object-src 'none'",
            "base-uri 'self'",
            "frame-ancestors 'none'",
        ]
        if not app.config.get("DEBUG"):
            csp_directives.append("upgrade-insecure-requests")

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Content-Security-Policy"] = "; ".join(csp_directives)
        return response

    return app
