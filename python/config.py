class BaseConfig:
    SECRET_KEY = "dev"
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
