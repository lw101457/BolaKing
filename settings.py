from decouple import config

# app
APP_HOST = config("APP_HOST", "", cast=str)
APP_PORT = config("APP_PORT", "", cast=int)

SESSION_REDIS = config("SESSION_REDIS", "", cast=str)
USER_REDIS = config("USER_REDIS", "", cast=str)
CONFIG_REDIS = config("CONFIG_REDIS", "", cast=str)

# mysql
MYSQL_DB = config("MYSQL_DB", "", cast=str)

SQLALCHEMY_ENGINE_CONFIG = {
    'pool_size': config('SQLALCHEMY_POOL_SIZE', 10, cast=int),
    'max_overflow': config('SQLALCHEMY_MAX_OVERFLOW', 10, cast=int),
    'pool_timeout': config('SQLALCHEMY_POOL_TIMEOUT', 10, cast=int),
    'pool_pre_ping': config('SQLALCHEMY_POOL_PRE_PING', False, cast=bool),
    'echo': config('SQLALCHEMY_POOL_ECHO', False, cast=bool),
}

# user
TOKEN_SECRET_KEY = config("TOKEN_SECRET_KEY", "", cast=str)
