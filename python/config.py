class BaseConfig:
    SECRET_KEY = None
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
