class Config:
    """Configuração base do projeto."""

    SECRET_KEY = "sua-chave-secreta-aqui"
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    """Configuração específica para execução de testes."""

    TESTING = True
    DEBUG = True
    # Você pode adicionar um banco de dados temporário aqui no futuro
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(Config):
    """Configuração para ambiente de desenvolvimento."""

    DEBUG = True
