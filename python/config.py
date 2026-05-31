class BaseConfig:
    SECRET_KEY = None
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = True
    PREFERRED_URL_SCHEME = "https"
    AUTOMATION_ACTIVE_ENV = "production"
    AUTOMATION_ALLOWED_ROLES = ("operacoes", "gestao", "auditoria")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    AUTOMATION_ACTIVE_ENV = "development"
