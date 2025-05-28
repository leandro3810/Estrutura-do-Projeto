from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.cli.command("saudacao")
    def saudacao():
        """Exibe uma mensagem de saudação personalizada."""
        print("Olá! Bem-vindo ao Estrutura-do-Projeto 🎉")

    from . import routes
    app.register_blueprint(routes.bp)

    return app
