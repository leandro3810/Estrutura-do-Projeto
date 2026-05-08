from flask import Flask
import os

def create_app(test_config=None):
    # Cria e configura a instância do app
    app = Flask(__name__, 
                instance_relative_config=True,
                template_folder='../../templates',
                static_folder='../../Static')

    if test_config is None:
        # Carrega a configuração de instância, se existir, quando não estiver testando
        app.config.from_mapping(
            SECRET_KEY='dev',
        )
    else:
        # Carrega a configuração de teste se passada
        app.config.from_mapping(test_config)

    # Comando CLI de saudação
    @app.cli.command("saudacao")
    def saudacao():
        """Exibe uma mensagem de saudação personalizada."""
        print("Olá! Bem-vindo ao Estrutura-do-Projeto 🎉 (Modo Teste)")

    # Importante: O registro de rotas deve apontar para o local correto
    # Para testes, podemos usar as rotas principais ou mocks
    try:
        from python import routes
        app.register_blueprint(routes.app) # Se usar Blueprint, ajuste para .bp
    except ImportError:
        @app.route('/')
        def index():
            return "App de Teste Ativo"

    return app
