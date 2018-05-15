import os
import subprocess

from redis import StrictRedis


class RedisServer:
    def __init__(self, path2config='server/config/redis.conf',
                       redis_server='/usr/bin/env redis-server',
                       start_it=True):
        if not os.path.isfile(path2config):
            raise RuntimeError("No Redis configuration file found")
        self._path2config = path2config
        with open(path2config, 'r') as conff:
            lines = conff.read().split('\n')
            lines = [line for line in lines
                          if line and not line.startswith('#')]
            config = [line.split(' ') for line in lines]
            config = [(p[0], ' '.join(p[1:])) for p in config]
            _config = {k: [] for k,_ in config}
            for k, v in config:
                _config[k].append(v)
            self._config = {k: v if len(v) > 1 else v[0]
                            for k,v in _config.items()}
        self._redis_server = None
        if start_it:
            self._redis_server = self.init_redis(path2config,
                                                 redis_server)

    @classmethod
    def init_redis(cls, path2config, redis_server):
        redis_call = redis_server.split(' ') + [path2config]
        return subprocess.Popen(redis_call)

    def __del__(self):
        self.kill_if_this_started_it()

    def kill_if_this_started_it(self):
        self._redis_server.kill()

    @property
    def host(self):
        return self._config.get('host', 'localhost')

    @property
    def port(self):
        return self._config['port']

    @property
    def passwd(self):
        return self._config['requirepass']


class RedisSetDict:
    def __init__(self, name, redis_server):
        self.redis = StrictRedis(redis_server.port,
                                 redis_server.host,
                                 redis_server.passwd)
        self._name = name

    @property
    def name(self):
        return self._name

    def add(self, key, *items):
        self[key] = set(items)

    def __getitem__(self, key):
        return self.redis.smembers(self.keyprfx+key)

    def __setitem__(self, key, items):
        items = set(items)
        redis.sadd(self.keypfrx+key, *items)
        redis.sadd(self.keyset_name, key)

    def __delitem__(self, key):
        self.redis.delete(self.keyprfx+key)

    def delete_keys(self, *keys):
        self.delete(*[self.keyprfx+key for key in keys])

    def delete(self):
        self.delete_keys(*self.keys)
        self.redis.delete(self.keyset_name)

    def __len__(self):
        return len(self.keys)

    def len(self, key):
        return self.redis.scard(self.keyprfx+key)

    def contains(self, key, item):
        return self.redis.sismember(self.keyprfx+key, item)

    def is_empty(self, key):
        return self.len(key) == 0

    @property
    def keys(self):
        return redis.smembers(self.keyset_name)

    @property
    def keyset_name(self):
        return self._name+'_setdict_keys'

    @property
    def keyprfx(self, key):
        return self._name+'_'


def get_redis(config):
    return RedisServer(path2config=config.redis_config,
                       redis_server=config.redis,
                       start_it=config.start_redis)
