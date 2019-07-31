from cached_property import threaded_cached_property as lazy_property

import settings


class Clients:

    @lazy_property
    def mysql_db(self):
        from sqlalchemy import create_engine
        return create_engine(settings.MYSQL_DB, **settings.SQLALCHEMY_ENGINE_CONFIG)

    @lazy_property
    def session_redis(self):
        import redis
        return redis.Redis(connection_pool=redis.BlockingConnectionPool.from_url(settings.SESSION_REDIS))

    @lazy_property
    def user_redis(self):
        import redis
        return redis.Redis(connection_pool=redis.BlockingConnectionPool.from_url(settings.USER_REDIS))

    @lazy_property
    def config_redis(self):
        import redis
        return redis.Redis(connection_pool=redis.BlockingConnectionPool.from_url(settings.CONFIG_REDIS))


clients = Clients()
