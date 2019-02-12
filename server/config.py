import os

class Config:

    @classmethod
    def get(cls, envvar):
        return os.environ.get(envvar)

    @classmethod
    def mongo_host(cls):
        return str(cls.get('MONGO_HOST'))

    @classmethod
    def mongo_port(cls):
        return int(cls.get('MONGO_PORT'))

    @classmethod
    def redis_host(cls):
        return str(cls.get('REDIS_HOST'))

    @classmethod
    def redis_port(cls):
        return str(cls.get('REDIS_PORT'))

    @classmethod
    def host(cls):
        return str(cls.get('HOST'))

    @classmethod
    def port(cls):
        return int(cls.get('PORT'))

    @classmethod
    def debug(cls):
        if cls.get('DEBUG') == 'false':
            return False
        return True

    @classmethod
    def server_backend(cls):
        return cls.get('SERVER_BACKEND')
