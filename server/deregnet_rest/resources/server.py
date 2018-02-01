import os
import yaml

from deregnet_rest.resources.redis import get_redis
from deregnet_rest.resources.mongodb import get_mongod
from deregnet_rest.resources.database import (DatabaseServer,
                                              get_database_server,
                                              mongo_auth)
from deregnet_rest.controllers.runners import Runner

class Config:

    def __init__(self, config_file=None):
        self._file_config = None
        if config_file:
            with open(config_file, 'r') as yamlfp:
                self._file_config = yaml.load(yamlfp)

    def file_config(self, ATTR):
        if self._file_config:
            return self._file_config.get(ATTR)
        return None

    def __call__(self, ATTR):
        file_value = self.file_config(ATTR)
        if file_value is not None:
            return file_value
        return os.environ.get(ATTR)

    @property
    def mongod_config(self):
        return str(self('MONGOD_CONFIG'))

    @property
    def mongod(self):
        return str(self('MONGOD'))

    @property
    def start_mongod(self):
        if self('START_MONGOD') == 'false':
            return False
        return True

    @property
    def redis_config(self):
        return str(self('REDIS_CONFIG'))

    @property
    def redis(self):
        return str(self('REDIS'))

    @property
    def start_redis(self):
        if self('START_REDIS') == 'false':
            return False
        return True

    @property
    def host(self):
        return str(self('HOST'))

    @property
    def port(self):
        return int(self('PORT'))

    @property
    def debug(self):
        if self('DEBUG') == 'false':
            return False
        return True

    @property
    def server_backend(self):
        return self('SERVER_BACKEND')

    @property
    def start_runners(self):
        if self('START_RUNNERS') == 'false':
            return False
        return True


class Server(DatabaseServer):
    def __init__(self, num_runners=2, **kwargs):
        super().__init__(**kwargs)
        self._runners = []
        for runner_id in range(num_runners):
            log_file = 'data/runners/runner'+str(runner_id)+'.log'
            self._runners.append(
                                  Runner(self.config,
                                         self.mongod,
                                         self.redis,
                                         runner_id,
                                         20,
                                         log_file)
                                 )

    def runner(self, i):
        return self._runners[i]

    @property
    def runners(self):
        self._runners


def get_server(config):
    user, passwd = mongo_auth()
    mongod = get_mongod(config)
    redis = get_redis(config)
    return Server(user=user,
                  passwd=passwd,
                  mongod=mongod,
                  redis=redis)


def init_server(config):
    if config.start_runners:
        return get_server(config)
    return get_database_server(config)
