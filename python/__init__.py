import os

from flask import Flask


def create_app(test_config=None):
    """Cria e configura a instância do aplicativo Flask."""
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../Static",
    )

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        DEBUG=True,
    )

    if test_config is not None:
        app.config.from_mapping(test_config)

    # Registrar Blueprint de rotas
    from python.routes import bp

    app.register_blueprint(bp)

    return app
