from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.cli.command('hello')
    def hello_command():
        """Exibe uma mensagem de saudação."""
        print("Olá! Este é um comando customizado para o estrutura-do-projeto.")

    from . import routes
    app.register_blueprint(routes.bp)

    return app
